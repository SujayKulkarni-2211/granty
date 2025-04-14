/**
 * Editor functionality for Grant Writing Assistant
 */

/**
 * Initialize the editor
 * @param {Object} draftData - Initial draft data
 */
function initEditor(draftData) {
    // Store draft data globally for access
    window.currentDraft = draftData;
    
    // Setup event listeners
    setupTitleEditing();
    setupSaveButton();
    setupGenerateButton();
    setupFormatButtons();
    setupQuestionInputs();
    setupApplySectionButtons();
    setupPolishButtons();
    setupFigureInsertion();
    
    // Enable preview and export buttons if draft has an ID
    if (draftData.id) {
        document.getElementById('previewBtn').classList.remove('disabled');
        document.getElementById('exportBtn').classList.remove('disabled');
        
        // Update href attributes
        document.getElementById('previewBtn').href = `/preview/${draftData.id}`;
        document.getElementById('exportBtn').href = `/export/${draftData.id}`;
        document.getElementById('diagramBtn').href = `/diagrams?draft_id=${draftData.id}`;
    } else {
        document.getElementById('previewBtn').classList.add('disabled');
        document.getElementById('exportBtn').classList.add('disabled');
    }
}

/**
 * Set up title editing functionality
 */
function setupTitleEditing() {
    const editTitleBtn = document.getElementById('editTitleBtn');
    const titleEditModal = document.getElementById('titleEditModal');
    const draftTitleInput = document.getElementById('draftTitleInput');
    const saveTitleBtn = document.getElementById('saveTitleBtn');
    const draftTitleElement = document.getElementById('draftTitle');
    
    // Open edit modal
    editTitleBtn.addEventListener('click', function() {
        const titleModal = new bootstrap.Modal(titleEditModal);
        draftTitleInput.value = window.currentDraft.title;
        titleModal.show();
    });
    
    // Save title
    saveTitleBtn.addEventListener('click', function() {
        const newTitle = draftTitleInput.value.trim();
        if (newTitle) {
            // Update displayed title
            draftTitleElement.textContent = newTitle;
            // Update draft data
            window.currentDraft.title = newTitle;
            // Close modal
            bootstrap.Modal.getInstance(titleEditModal).hide();
        }
    });
}

/**
 * Set up save button functionality
 */
function setupSaveButton() {
    const saveBtn = document.getElementById('saveBtn');
    
    saveBtn.addEventListener('click', function() {
        saveCurrentDraft();
    });
}

/**
 * Save the current draft
 */
async function saveCurrentDraft() {
    // Get content from all editor sections
    const contentElements = document.querySelectorAll('.editor-content');
    
    // Create a consolidated content object with section names as keys
    const content = {};
    contentElements.forEach(element => {
        const sectionName = element.getAttribute('data-section');
        content[sectionName] = element.innerHTML;
    });
    
    // Get answers from input fields
    const answers = {};
    document.querySelectorAll('.question-input').forEach(input => {
        const section = input.getAttribute('data-section');
        const question = input.getAttribute('data-question');
        const key = `${section}-${question}`;
        answers[key] = input.value;
    });
    
    // Create draft object
    const draft = {
        id: window.currentDraft.id,
        title: window.currentDraft.title,
        template_id: window.currentDraft.template_id,
        sections: window.currentDraft.sections,
        answers: answers,
        content: consolidateContent(content),
        figures: window.currentDraft.figures
    };
    
    // Show loading indicator
    showLoading('Saving draft...');
    
    try {
        // Send to server
        const response = await fetch('/editor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(draft)
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Update draft ID if new draft
            if (!window.currentDraft.id) {
                window.currentDraft.id = result.draft_id;
                // Update buttons that need draft_id
                document.getElementById('previewBtn').href = `/preview/${result.draft_id}`;
                document.getElementById('previewBtn').classList.remove('disabled');
                document.getElementById('exportBtn').href = `/export/${result.draft_id}`;
                document.getElementById('exportBtn').classList.remove('disabled');
                document.getElementById('diagramBtn').href = `/diagrams?draft_id=${result.draft_id}`;
            }
            
            // Show success message
            showNotification('Draft saved successfully', 'success');
        } else {
            showNotification('Error saving draft', 'danger');
        }
    } catch (error) {
        console.error('Error saving draft:', error);
        showNotification('Error saving draft', 'danger');
    } finally {
        hideLoading();
    }
}

/**
 * Consolidate individual section content into a single HTML string
 * @param {Object} sectionContent - Object with section names as keys and content as values
 * @returns {string} - Combined HTML content
 */
function consolidateContent(sectionContent) {
    let fullContent = '';
    
    // Get sections in the right order from the draft data
    window.currentDraft.sections.forEach(section => {
        const sectionName = section.name;
        if (sectionContent[sectionName]) {
            fullContent += `<h2>${sectionName}</h2>`;
            fullContent += sectionContent[sectionName];
        }
    });
    
    return fullContent;
}

/**
 * Set up generate button functionality
 */
function setupGenerateButton() {
    const generateBtn = document.getElementById('generateBtn');
    
    generateBtn.addEventListener('click', async function() {
        // Get answers from input fields
        const answers = {};
        document.querySelectorAll('.question-input').forEach(input => {
            const section = input.getAttribute('data-section');
            const question = input.getAttribute('data-question');
            const key = `${section}-${question}`;
            answers[key] = input.value;
        });
        
        // Check if we have enough answers (at least 30% of questions)
        const totalQuestions = document.querySelectorAll('.question-input').length;
        const answeredQuestions = Object.values(answers).filter(answer => answer.trim().length > 0).length;
        
        if (answeredQuestions < totalQuestions * 0.3) {
            showNotification('Please answer more questions before generating the draft', 'warning');
            return;
        }
        
        // Confirm with user
        if (!confirm('This will generate a complete draft based on your answers. Existing content may be replaced. Continue?')) {
            return;
        }
        
        // Show loading indicator
        showLoading('Generating draft. This may take a minute...');
        
        try {
            // Send to server
            const response = await fetch('/generate-draft', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    template_id: window.currentDraft.template_id,
                    answers: answers
                })
            });
            
            const result = await response.json();
            
            if (result.success) {
                // Parse the generated content
                const generatedContent = parseGeneratedContent(result.content);
                
                // Update the editor sections with the generated content
                window.currentDraft.sections.forEach(section => {
                    const sectionName = section.name;
                    const editorElement = document.getElementById(`editor-${slugify(sectionName)}`);
                    
                    if (editorElement && generatedContent[sectionName]) {
                        editorElement.innerHTML = generatedContent[sectionName];
                    }
                });
                
                // Save the draft
                await saveCurrentDraft();
                
                showNotification('Draft generated successfully', 'success');
            } else {
                showNotification('Error generating draft', 'danger');
            }
        } catch (error) {
            console.error('Error generating draft:', error);
            showNotification('Error generating draft', 'danger');
        } finally {
            hideLoading();
        }
    });
}

/**
 * Parse generated content from AI and split into sections
 * @param {string} content - Raw content from AI
 * @returns {Object} - Object with section names as keys and HTML content as values
 */
function parseGeneratedContent(content) {
    const sections = {};
    let currentSection = null;
    let currentContent = '';
    
    // Split content by lines
    const lines = content.split('\n');
    
    // Process each line
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        
        // Check if line is a section header (starts with # or ## )
        if (line.match(/^#{1,2}\s+(.+)$/)) {
            // Extract section name from header
            const match = line.match(/^#{1,2}\s+(.+)$/);
            const sectionName = match[1].trim();
            
            // If we already have a section, save its content
            if (currentSection) {
                sections[currentSection] = currentContent.trim();
                currentContent = '';
            }
            
            // Set current section to new section
            currentSection = sectionName;
        } else if (currentSection) {
            // Process formatting for this line
            let formattedLine = line;
            
            // Bold: **text** -> <strong>text</strong>
            formattedLine = formattedLine.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
            
            // Italic: *text* -> <em>text</em> (but avoid cases where * is used in lists)
            formattedLine = formattedLine.replace(/(?<!\*)\*([^\*]+)\*(?!\*)/g, '<em>$1</em>');
            
            // Add paragraphs for non-empty lines that aren't lists or headings
            if (formattedLine.trim() && !formattedLine.match(/^[#*\-\d]/) && !formattedLine.match(/<h\d>/)) {
                formattedLine = `<p>${formattedLine}</p>`;
            }
            
            // Add line to current section content
            currentContent += formattedLine + '\n';
        }
    }
    
    // Save the last section
    if (currentSection && currentContent) {
        sections[currentSection] = currentContent.trim();
    }
    
    return sections;
}

/**
 * Set up formatting buttons
 */
function setupFormatButtons() {
    document.querySelectorAll('.format-btn').forEach(button => {
        button.addEventListener('click', function() {
            const format = this.getAttribute('data-format');
            formatSelectedText(format);
        });
    });
}

/**
 * Format selected text in the active editor
 * @param {string} format - Format to apply (bold, italic, etc.)
 */
function formatSelectedText(format) {
    // Get the active editor (the one that's currently visible)
    const activeTab = document.querySelector('.tab-pane.active');
    if (!activeTab) return;
    
    const editor = activeTab.querySelector('.editor-content');
    if (!editor) return;
    
    // Get selection
    const selection = window.getSelection();
    const range = selection.getRangeAt(0);
    
    // If selection is not in the editor, return
    if (!editor.contains(range.commonAncestorContainer)) return;
    
    // Apply formatting based on format type
    switch (format) {
        case 'bold':
            document.execCommand('bold', false, null);
            break;
        case 'italic':
            document.execCommand('italic', false, null);
            break;
        case 'underline':
            document.execCommand('underline', false, null);
            break;
        case 'h1':
            document.execCommand('formatBlock', false, '<h1>');
            break;
        case 'h2':
            document.execCommand('formatBlock', false, '<h2>');
            break;
        case 'h3':
            document.execCommand('formatBlock', false, '<h3>');
            break;
        case 'ul':
            document.execCommand('insertUnorderedList', false, null);
            break;
        case 'ol':
            document.execCommand('insertOrderedList', false, null);
            break;
    }
}

/**
 * Set up question input event handlers
 */
function setupQuestionInputs() {
    document.querySelectorAll('.question-input').forEach(input => {
        input.addEventListener('input', function() {
            const section = this.getAttribute('data-section');
            const question = this.getAttribute('data-question');
            const key = `${section}-${question}`;
            
            // Update the answers object in the current draft
            if (!window.currentDraft.answers) {
                window.currentDraft.answers = {};
            }
            window.currentDraft.answers[key] = this.value;
        });
    });
}

/**
 * Set up apply section buttons
 */
function setupApplySectionButtons() {
    document.querySelectorAll('.apply-answers').forEach(button => {
        button.addEventListener('click', async function() {
            const sectionName = this.getAttribute('data-section');
            
            // Get all question inputs for this section
            const sectionQuestions = Array.from(document.querySelectorAll(`.question-input[data-section="${sectionName}"]`));
            
            // Check if we have answers
            const hasAnswers = sectionQuestions.some(input => input.value.trim().length > 0);
            if (!hasAnswers) {
                showNotification('Please answer at least one question first', 'warning');
                return;
            }
            
            // Create a prompt for the AI
            let prompt = `Based on the following information, write a detailed section for "${sectionName}" in a grant proposal:\n\n`;
            
            sectionQuestions.forEach(input => {
                const question = input.getAttribute('data-question');
                const answer = input.value.trim();
                
                if (answer) {
                    prompt += `Question: ${question}\nAnswer: ${answer}\n\n`;
                }
            });
            
            // Show loading indicator
            showLoading(`Generating ${sectionName} section...`);
            
            try {
                // Send to server to generate section content
                const response = await fetch('/polish-section', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        section_name: sectionName,
                        content: prompt
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    // Find the editor for this section
                    const editorElement = document.getElementById(`editor-${slugify(sectionName)}`);
                    
                    if (editorElement) {
                        // Update the editor content with the generated text
                        const formattedContent = formatGeneratedText(result.content);
                        editorElement.innerHTML = formattedContent;
                        
                        // Activate the tab for this section
                        const tabId = `tab-${slugify(sectionName)}`;
                        const tab = document.getElementById(tabId);
                        if (tab) {
                            bootstrap.Tab.getOrCreateInstance(tab).show();
                        }
                        
                        showNotification(`${sectionName} section updated`, 'success');
                    }
                } else {
                    showNotification('Error generating section content', 'danger');
                }
            } catch (error) {
                console.error('Error generating section content:', error);
                showNotification('Error generating section content', 'danger');
            } finally {
                hideLoading();
            }
        });
    });
}

/**
 * Format generated text with proper HTML
 * @param {string} text - Raw text from AI
 * @returns {string} - Formatted HTML
 */
function formatGeneratedText(text) {
    // Split into lines
    const lines = text.split('\n');
    let formatted = '';
    let inList = false;
    let listType = '';
    
    // Process each line
    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim();
        
        if (!line) {
            // Empty line, close any open list
            if (inList) {
                formatted += `</${listType}>`;
                inList = false;
            }
            continue;
        }
        
        // Format headers (# Title, ## Subtitle)
        if (line.startsWith('# ')) {
            if (inList) {
                formatted += `</${listType}>`;
                inList = false;
            }
            const title = line.substring(2);
            formatted += `<h1>${title}</h1>`;
            continue;
        }
        
        if (line.startsWith('## ')) {
            if (inList) {
                formatted += `</${listType}>`;
                inList = false;
            }
            const subtitle = line.substring(3);
            formatted += `<h2>${subtitle}</h2>`;
            continue;
        }
        
        if (line.startsWith('### ')) {
            if (inList) {
                formatted += `</${listType}>`;
                inList = false;
            }
            const subsubtitle = line.substring(4);
            formatted += `<h3>${subsubtitle}</h3>`;
            continue;
        }
        
        // Format lists
        const bulletListMatch = line.match(/^[\*\-]\s(.+)$/);
        if (bulletListMatch) {
            if (!inList || listType !== 'ul') {
                if (inList) formatted += `</${listType}>`;
                formatted += '<ul>';
                listType = 'ul';
                inList = true;
            }
            formatted += `<li>${bulletListMatch[1]}</li>`;
            continue;
        }
        
        const numberedListMatch = line.match(/^\d+\.\s(.+)$/);
        if (numberedListMatch) {
            if (!inList || listType !== 'ol') {
                if (inList) formatted += `</${listType}>`;
                formatted += '<ol>';
                listType = 'ol';
                inList = true;
            }
            formatted += `<li>${numberedListMatch[1]}</li>`;
            continue;
        }
        
        // Close any open list if we're not adding to it
        if (inList) {
            formatted += `</${listType}>`;
            inList = false;
        }
        
        // Format bold and italic
        line = line.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        line = line.replace(/\*(.+?)\*/g, '<em>$1</em>');
        
        // Add as paragraph
        formatted += `<p>${line}</p>`;
    }
    
    // Close any open list at the end
    if (inList) {
        formatted += `</${listType}>`;
    }
    
    return formatted;
}

/**
 * Set up polish buttons
 */
function setupPolishButtons() {
    document.querySelectorAll('.polish-section').forEach(button => {
        button.addEventListener('click', async function() {
            const sectionName = this.getAttribute('data-section');
            
            // Find the editor for this section
            const editorElement = document.getElementById(`editor-${slugify(sectionName)}`);
            if (!editorElement) return;
            
            // Get current content
            const currentContent = editorElement.innerHTML;
            
            // Check if there is content to polish
            if (!currentContent.trim()) {
                showNotification('No content to polish', 'warning');
                return;
            }
            
            // Show loading indicator
            showLoading(`Polishing ${sectionName} section...`);
            
            try {
                // Send to server to polish content
                const response = await fetch('/polish-section', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        section_name: sectionName,
                        content: currentContent
                    })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    // Update the editor content with the polished text
                    const formattedContent = formatGeneratedText(result.content);
                    editorElement.innerHTML = formattedContent;
                    
                    showNotification(`${sectionName} section polished`, 'success');
                } else {
                    showNotification('Error polishing section content', 'danger');
                }
            } catch (error) {
                console.error('Error polishing section content:', error);
                showNotification('Error polishing section content', 'danger');
            } finally {
                hideLoading();
            }
        });
    });
}

/**
 * Set up figure insertion
 */
function setupFigureInsertion() {
    document.querySelectorAll('.insert-figure').forEach(button => {
        button.addEventListener('click', function() {
            const figureId = this.getAttribute('data-figure-id');
            
            // Find the figure in the draft
            const figure = window.currentDraft.figures.find(f => f.id === figureId);
            if (!figure) return;
            
            // Get the active editor
            const activeTab = document.querySelector('.tab-pane.active');
            if (!activeTab) return;
            
            const editor = activeTab.querySelector('.editor-content');
            if (!editor) return;
            
            // Create figure HTML
            const figureHtml = `
                <figure class="diagram-figure" data-figure-id="${figure.id}">
                    <div class="mermaid">${figure.code}</div>
                    <figcaption>${figure.caption}</figcaption>
                </figure>
            `;
            
            // Insert at cursor position or at end
            const selection = window.getSelection();
            if (selection.rangeCount) {
                const range = selection.getRangeAt(0);
                if (editor.contains(range.commonAncestorContainer)) {
                    range.deleteContents();
                    range.insertNode(range.createContextualFragment(figureHtml));
                } else {
                    editor.innerHTML += figureHtml;
                }
            } else {
                editor.innerHTML += figureHtml;
            }
            
            // Re-render mermaid diagrams
            if (typeof mermaid !== 'undefined') {
                mermaid.init(undefined, document.querySelectorAll('.mermaid'));
            }
            
            showNotification('Figure inserted successfully', 'success');
        });
    });
}

/**
 * Utility function to slugify a string
 * @param {string} text - Text to slugify
 * @returns {string} - Slugified text
 */
function slugify(text) {
    return text
        .toString()
        .toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w\-]+/g, '')
        .replace(/\-\-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
}