/**
 * Gemini AI integration functionality for Grant Writing Assistant
 * This handles frontend interactions with the Gemini API
 */

/**
 * Generate content for a specific section using Gemini AI
 * @param {string} sectionName - Name of the section
 * @param {Object} answers - User's answers to questions
 * @returns {Promise<string>} - Generated content
 */
async function generateSectionContent(sectionName, answers) {
    try {
        showLoading(`Generating ${sectionName} content...`);
        
        const response = await fetch('/polish-section', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                section_name: sectionName,
                content: formatPromptFromAnswers(sectionName, answers)
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            return result.content;
        } else {
            throw new Error('Error generating section content');
        }
    } catch (error) {
        console.error('Error generating section content:', error);
        throw error;
    } finally {
        hideLoading();
    }
}

/**
 * Format a prompt from user answers for Gemini
 * @param {string} sectionName - Name of the section
 * @param {Object} answers - User's answers to questions
 * @returns {string} - Formatted prompt
 */
function formatPromptFromAnswers(sectionName, answers) {
    let prompt = `Write a professional, detailed section for "${sectionName}" in a grant proposal based on the following information:\n\n`;
    
    for (const key in answers) {
        if (key.startsWith(`${sectionName}-`)) {
            const question = key.substring(sectionName.length + 1);
            prompt += `Question: ${question}\nAnswer: ${answers[key]}\n\n`;
        }
    }
    
    prompt += `Please format the content professionally and ensure all key points from the answers are included. 
Use appropriate headings, paragraphs, and emphasis.
The content should be suitable for inclusion in a formal grant proposal for "${sectionName}".`;
    
    return prompt;
}

/**
 * Generate a complete draft using Gemini AI
 * @param {string} templateId - ID of the template
 * @param {Object} answers - User's answers to all questions
 * @returns {Promise<string>} - Complete generated draft
 */
async function generateCompleteDraft(templateId, answers) {
    try {
        showLoading('Generating complete draft. This may take a minute...');
        
        const response = await fetch('/generate-draft', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                template_id: templateId,
                answers: answers
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            return result.content;
        } else {
            throw new Error('Error generating draft');
        }
    } catch (error) {
        console.error('Error generating draft:', error);
        throw error;
    } finally {
        hideLoading();
    }
}

/**
 * Polish existing content using Gemini AI
 * @param {string} sectionName - Name of the section
 * @param {string} content - Current content to polish
 * @returns {Promise<string>} - Polished content
 */
async function polishContent(sectionName, content) {
    try {
        showLoading(`Polishing ${sectionName} content...`);
        
        const response = await fetch('/polish-section', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                section_name: sectionName,
                content: content
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            return result.content;
        } else {
            throw new Error('Error polishing content');
        }
    } catch (error) {
        console.error('Error polishing content:', error);
        throw error;
    } finally {
        hideLoading();
    }
}

/**
 * Format AI-generated text for display in the editor
 * @param {string} text - Raw text from AI
 * @returns {string} - Formatted HTML
 */
function formatAIGeneratedText(text) {
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