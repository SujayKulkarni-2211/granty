/**
 * Template functionality for Grant Writing Assistant
 * This handles template loading, parsing and application
 */

/**
 * Load a template by ID
 * @param {string} templateId - ID of the template to load
 * @returns {Promise<Object>} - Template data
 */
async function loadTemplate(templateId) {
    try {
        const response = await fetch(`/api/templates/${templateId}`);
        const result = await response.json();
        
        if (result.success) {
            return result.template;
        } else {
            throw new Error('Error loading template');
        }
    } catch (error) {
        console.error('Error loading template:', error);
        throw error;
    }
}

/**
 * Apply a template to create a new draft
 * @param {string} templateId - ID of the template to apply
 * @returns {Promise<string>} - ID of the new draft
 */
async function applyTemplate(templateId) {
    try {
        showLoading('Creating new draft from template...');
        
        const response = await fetch('/editor', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            params: {
                template_id: templateId
            }
        });
        
        // Redirect to the new draft
        window.location.href = response.url;
    } catch (error) {
        console.error('Error applying template:', error);
        hideLoading();
        throw error;
    }
}

/**
 * Parse custom uploaded template file
 * @param {File} file - Uploaded file
 * @returns {Promise<string>} - ID of the newly created template
 */
async function parseCustomTemplate(file) {
    try {
        showLoading('Analyzing custom template...');
        
        const formData = new FormData();
        formData.append('file', file);
        
        const response = await fetch('/custom-template', {
            method: 'POST',
            body: formData
        });
        
        // Redirect to the new template
        window.location.href = response.url;
    } catch (error) {
        console.error('Error parsing custom template:', error);
        hideLoading();
        throw error;
    }
}

/**
 * Get all available templates
 * @returns {Promise<Array>} - Array of template objects
 */
async function getAllTemplates() {
    try {
        const response = await fetch('/api/templates');
        const result = await response.json();
        
        if (result.success) {
            return result.templates;
        } else {
            throw new Error('Error loading templates');
        }
    } catch (error) {
        console.error('Error loading templates:', error);
        return [];
    }
}

/**
 * Generate form fields from template structure
 * @param {Object} template - Template object
 * @param {HTMLElement} container - Container to append fields to
 */
function generateFormFields(template, container) {
    // Clear container
    container.innerHTML = '';
    
    // Create sections
    template.sections.forEach((section, sectionIndex) => {
        // Create section container
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'section-container mb-4';
        
        // Create section header
        const sectionHeader = document.createElement('h3');
        sectionHeader.textContent = section.name;
        sectionDiv.appendChild(sectionHeader);
        
        // Create questions
        section.questions.forEach((question, questionIndex) => {
            // Create question container
            const questionDiv = document.createElement('div');
            questionDiv.className = 'mb-3';
            
            // Create label
            const label = document.createElement('label');
            label.className = 'form-label';
            label.textContent = question;
            label.setAttribute('for', `question-${sectionIndex}-${questionIndex}`);
            questionDiv.appendChild(label);
            
            // Create textarea
            const textarea = document.createElement('textarea');
            textarea.className = 'form-control question-input';
            textarea.id = `question-${sectionIndex}-${questionIndex}`;
            textarea.setAttribute('rows', '3');
            textarea.setAttribute('data-section', section.name);
            textarea.setAttribute('data-question', question);
            questionDiv.appendChild(textarea);
            
            // Add to section
            sectionDiv.appendChild(questionDiv);
        });
        
        // Add apply button
        const applyBtn = document.createElement('button');
        applyBtn.type = 'button';
        applyBtn.className = 'btn btn-sm btn-outline-primary apply-answers';
        applyBtn.setAttribute('data-section', section.name);
        applyBtn.innerHTML = '<i class="fas fa-check me-2"></i>Apply to Section';
        sectionDiv.appendChild(applyBtn);
        
        // Add to container
        container.appendChild(sectionDiv);
    });
}

/**
 * Calculate template completion percentage based on answered questions
 * @param {Object} template - Template object
 * @param {Object} answers - User's answers
 * @returns {number} - Completion percentage (0-100)
 */
function calculateTemplateCompletion(template, answers) {
    let totalQuestions = 0;
    let answeredQuestions = 0;
    
    // Count total and answered questions
    template.sections.forEach(section => {
        totalQuestions += section.questions.length;
        
        section.questions.forEach(question => {
            const key = `${section.name}-${question}`;
            if (answers[key] && answers[key].trim().length > 0) {
                answeredQuestions++;
            }
        });
    });
    
    // Calculate percentage
    return Math.round((answeredQuestions / totalQuestions) * 100);
}

/**
 * Create a new template
 * @param {Object} templateData - Template data
 * @returns {Promise<string>} - ID of the newly created template
 */
async function createTemplate(templateData) {
    try {
        showLoading('Creating new template...');
        
        const response = await fetch('/api/templates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(templateData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            return result.template_id;
        } else {
            throw new Error('Error creating template');
        }
    } catch (error) {
        console.error('Error creating template:', error);
        throw error;
    } finally {
        hideLoading();
    }
}