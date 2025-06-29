/**
 * Diagrams functionality for Grant Writing Assistant
 */

/**
 * Initialize the diagram editor
 * @param {Object} diagramData - Initial diagram data
 * @param {string} draftId - ID of the associated draft
 */
function initDiagramEditor(diagramData, draftId) {
    // Store diagram data globally for access
    window.currentDiagram = diagramData;
    window.draftId = draftId;
    
    // Initialize mermaid
    mermaid.initialize({
        startOnLoad: false, // We'll manually trigger
        theme: 'neutral',
        securityLevel: 'loose',
        fontFamily: 'Arial, sans-serif'
    });
    
    // Setup event listeners
    setupTitleEditing();
    setupSaveDiagramButton();
    setupInsertIntoGrantButton();
    setupDiagramTypeSelector();
    setupRenderButton();
    
    // Set initial diagram type
    const diagramType = diagramData.type || 'flowchart';
    document.querySelector(`.diagram-types [data-diagram-type="${diagramType}"]`).classList.add('active');
    updateCurrentDiagramType(diagramType);
    
    // Set example content if no code is provided
    const diagramCode = document.getElementById('diagramCode');
    if (!diagramCode.value.trim()) {
        diagramCode.value = getExampleCode(diagramType);
    }
    
    // Initial render
    renderDiagram();
}

/**
 * Set up title editing functionality
 */
function setupTitleEditing() {
    const editTitleBtn = document.getElementById('editTitleBtn');
    const titleEditModal = document.getElementById('titleEditModal');
    const diagramTitleInput = document.getElementById('diagramTitleInput');
    const saveTitleBtn = document.getElementById('saveTitleBtn');
    const diagramTitleElement = document.getElementById('diagramTitle');
    
    // Open edit modal
    editTitleBtn.addEventListener('click', function() {
        const titleModal = new bootstrap.Modal(titleEditModal);
        diagramTitleInput.value = window.currentDiagram.title;
        titleModal.show();
    });
    
    // Save title
    saveTitleBtn.addEventListener('click', function() {
        const newTitle = diagramTitleInput.value.trim();
        if (newTitle) {
            // Update displayed title
            diagramTitleElement.textContent = newTitle;
            // Update diagram data
            window.currentDiagram.title = newTitle;
            // Close modal
            bootstrap.Modal.getInstance(titleEditModal).hide();
        }
    });
}

/**
 * Set up save diagram button functionality
 */
function setupSaveDiagramButton() {
    const saveDiagramBtn = document.getElementById('saveDiagramBtn');
    
    saveDiagramBtn.addEventListener('click', function() {
        saveCurrentDiagram();
    });
}

/**
 * Save the current diagram
 */
async function saveCurrentDiagram() {
    // Get values from inputs
    const title = document.getElementById('diagramTitle').textContent;
    const caption = document.getElementById('diagramCaption').value;
    const description = document.getElementById('diagramDescription').value;
    const code = document.getElementById('diagramCode').value;
    const diagramType = document.querySelector('.diagram-types .list-group-item.active').getAttribute('data-diagram-type');
    
    // Create diagram object
    const diagram = {
        id: window.currentDiagram.id || generateUUID(),
        title: title,
        type: diagramType,
        caption: caption,
        description: description,
        code: code
    };
    
    // Show loading indicator
    showLoading('Saving diagram...');
    
    try {
        // Send to server
        const response = await fetch('/save-diagram', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(diagram)
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Update diagram ID if new diagram
            if (!window.currentDiagram.id) {
                window.currentDiagram.id = result.diagram_id;
                
                // Enable insert button if draft ID exists
                if (window.draftId) {
                    document.getElementById('insertIntoGrantBtn').disabled = false;
                }
            }
            
            // Update current diagram data
            window.currentDiagram = diagram;
            
            // Show success message
            showNotification('Diagram saved successfully', 'success');
        } else {
            showNotification('Error saving diagram', 'danger');
        }
    } catch (error) {
        console.error('Error saving diagram:', error);
        showNotification('Error saving diagram', 'danger');
    } finally {
        hideLoading();
    }
}

/**
 * Set up insert into grant button functionality
 */
function setupInsertIntoGrantButton() {
    const insertIntoGrantBtn = document.getElementById('insertIntoGrantBtn');
    
    if (!window.draftId) {
        insertIntoGrantBtn.disabled = true;
        return;
    }
    
    insertIntoGrantBtn.addEventListener('click', async function() {
        // Make sure diagram is saved first
        if (!window.currentDiagram.id) {
            showNotification('Please save the diagram first', 'warning');
            return;
        }
        
        // Show loading indicator
        showLoading('Inserting diagram into grant...');
        
        try {
            // Get the current draft
            const response = await fetch(`/get-draft/${window.draftId}`);
            const draft = await response.json();
            
            if (!draft.success) {
                showNotification('Error getting draft', 'danger');
                return;
            }
            
            // Add figure to draft if not already present
            if (!draft.figures) {
                draft.figures = [];
            }
            
            // Check if figure already exists
            const existingFigureIndex = draft.figures.findIndex(f => f.id === window.currentDiagram.id);
            
            if (existingFigureIndex >= 0) {
                // Update existing figure
                draft.figures[existingFigureIndex] = {
                    id: window.currentDiagram.id,
                    title: window.currentDiagram.title,
                    caption: window.currentDiagram.caption,
                    type: window.currentDiagram.type,
                    code: window.currentDiagram.code,
                    description: window.currentDiagram.description
                };
            } else {
                // Add new figure
                draft.figures.push({
                    id: window.currentDiagram.id,
                    title: window.currentDiagram.title,
                    caption: window.currentDiagram.caption,
                    type: window.currentDiagram.type,
                    code: window.currentDiagram.code,
                    description: window.currentDiagram.description
                });
            }
            
            // Save the updated draft
            const saveResponse = await fetch('/editor', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(draft)
            });
            
            const saveResult = await saveResponse.json();
            
            if (saveResult.success) {
                showNotification('Diagram inserted into grant successfully', 'success');
                
                // Redirect to editor
                window.location.href = `/editor?draft_id=${window.draftId}`;
            } else {
                showNotification('Error inserting diagram into grant', 'danger');
            }
        } catch (error) {
            console.error('Error inserting diagram into grant:', error);
            showNotification('Error inserting diagram into grant', 'danger');
        } finally {
            hideLoading();
        }
    });
}

/**
 * Set up diagram type selector
 */
function setupDiagramTypeSelector() {
    document.querySelectorAll('.diagram-types .list-group-item').forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all items
            document.querySelectorAll('.diagram-types .list-group-item').forEach(i => {
                i.classList.remove('active');
            });
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // Get selected diagram type
            const diagramType = this.getAttribute('data-diagram-type');
            
            // Update the current diagram type
            updateCurrentDiagramType(diagramType);
            
            // Provide example code if the current code is empty or for a different diagram type
            const diagramCode = document.getElementById('diagramCode');
            const currentCode = diagramCode.value.trim();
            
            // Check if current code matches the selected type
            const typeRegex = new RegExp(`^${diagramType}\\s+`, 'i');
            if (!currentCode || !typeRegex.test(currentCode)) {
                // Offer to replace with example
                if (currentCode && !confirm('Replace current diagram code with example for the new diagram type?')) {
                    return;
                }
                
                // Set example code
                diagramCode.value = getExampleCode(diagramType);
                
                // Render the new diagram
                renderDiagram();
            }
        });
    });
}

/**
 * Update the current diagram type display
 * @param {string} type - Diagram type
 */
function updateCurrentDiagramType(type) {
    const diagramTypeElement = document.getElementById('currentDiagramType');
    
    // Map type to display name
    const typeDisplayNames = {
        'flowchart': 'Flowchart',
        'sequence': 'Sequence Diagram',
        'class': 'Class Diagram',
        'mindmap': 'Mind Map',
        'gantt': 'Gantt Chart',
        'pie': 'Pie Chart'
    };
    
    diagramTypeElement.textContent = typeDisplayNames[type] || type;
}

/**
 * Set up render button
 */
function setupRenderButton() {
    const renderBtn = document.getElementById('renderBtn');
    const diagramCode = document.getElementById('diagramCode');
    
    renderBtn.addEventListener('click', function() {
        renderDiagram();
    });
    
    // Also render on code change after a delay
    let renderTimeout;
    diagramCode.addEventListener('input', function() {
        clearTimeout(renderTimeout);
        renderTimeout = setTimeout(() => {
            renderDiagram();
        }, 1000); // Debounce rendering for 1 second
    });
}

/**
 * Render the current diagram
 */
function renderDiagram() {
    const diagramCode = document.getElementById('diagramCode').value;
    const diagramPreview = document.getElementById('diagramPreview');
    
    // Clear previous content
    diagramPreview.innerHTML = '';
    
    // Remove any previous error messages
    const existingError = document.querySelector('.diagram-error');
    if (existingError) {
        existingError.remove();
    }
    
    if (!diagramCode.trim()) {
        diagramPreview.innerHTML = '<div class="text-muted text-center">Enter diagram code to see preview</div>';
        return;
    }
    
    try {
        // Add loading indicator
        diagramPreview.innerHTML = `
            <div class="diagram-loading">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        `;
        
        // Render the diagram
        setTimeout(() => {
            try {
                mermaid.render('mermaid-diagram', diagramCode, (svgCode) => {
                    diagramPreview.innerHTML = svgCode;
                });
            } catch (error) {
                console.error('Error rendering diagram:', error);
                diagramPreview.innerHTML = '';
                
                // Show error message
                const errorDiv = document.createElement('div');
                errorDiv.className = 'diagram-error';
                errorDiv.textContent = `Error rendering diagram: ${error.message || 'Unknown error'}`;
                diagramPreview.parentNode.appendChild(errorDiv);
            }
        }, 100);
    } catch (error) {
        console.error('Error rendering diagram:', error);
        diagramPreview.innerHTML = '';
        
        // Show error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'diagram-error';
        errorDiv.textContent = `Error rendering diagram: ${error.message || 'Unknown error'}`;
        diagramPreview.parentNode.appendChild(errorDiv);
    }
}

/**
 * Get example code for a diagram type
 * @param {string} type - Diagram type
 * @returns {string} - Example code
 */
function getExampleCode(type) {
    const examples = {
        'flowchart': `flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Process 1]
    B -->|No| D[Process 2]
    C --> E[End]
    D --> E`,
        
        'sequence': `sequenceDiagram
    participant Researcher
    participant Committee
    participant Funder
    Researcher->>Committee: Submit grant proposal
    Committee->>Committee: Review proposal
    Committee-->>Researcher: Request revisions
    Researcher->>Committee: Submit revised proposal
    Committee->>Funder: Recommend funding
    Funder-->>Committee: Approve funding
    Committee->>Researcher: Notify of approval`,
        
        'class': `classDiagram
    class Project {
        +String title
        +Date startDate
        +Date endDate
        +Double budget
        +submitReport()
    }
    class Researcher {
        +String name
        +String institution
        +conductResearch()
    }
    class Deliverable {
        +String name
        +Date dueDate
        +Boolean completed
    }
    Project "1" *-- "many" Deliverable
    Project "1" o-- "1..*" Researcher`,
        
        'mindmap': `mindmap
    root((Grant Project))
        Research Objectives
            Primary Goal
            Secondary Goals
        Methodology
            Data Collection
            Analysis Techniques
            Validation Methods
        Expected Outcomes
            Publications
            Patents
            Community Impact
        Budget Allocation
            Personnel
            Equipment
            Operations`,
        
        'gantt': `gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Planning
    Project Definition    :a1, 2023-01-01, 30d
    Literature Review     :after a1, 45d
    section Implementation
    Data Collection       :2023-03-15, 90d
    Data Analysis         :2023-06-15, 60d
    section Reporting
    Draft Report          :2023-08-15, 30d
    Final Report          :2023-09-15, 15d`,
        
        'pie': `pie title Budget Allocation
    "Personnel" : 45
    "Equipment" : 30
    "Operations" : 15
    "Travel" : 10`
    };
    
    return examples[type] || examples['flowchart'];
}

/**
 * Generate a UUID
 * @returns {string} - A UUID v4 string
 */
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

/**
 * Show notification 
 * @param {string} message - Message to display
 * @param {string} type - Type of notification (success, danger, warning, info)
 */
function showNotification(message, type) {
    // If we don't have a notification container, create one
    let container = document.querySelector('.notification-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'notification-container position-fixed top-0 end-0 p-3';
        document.body.appendChild(container);
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `toast align-items-center text-white bg-${type} border-0`;
    notification.role = 'alert';
    notification.ariaLive = 'assertive';
    notification.ariaAtomic = 'true';
    
    notification.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    // Add to container
    container.appendChild(notification);
    
    // Initialize and show
    const toast = new bootstrap.Toast(notification, {
        autohide: true,
        delay: 5000
    });
    toast.show();
    
    // Remove from DOM after hidden
    notification.addEventListener('hidden.bs.toast', function() {
        notification.remove();
    });
}

/**
 * Show loading indicator
 * @param {string} message - Message to display
 */
function showLoading(message) {
    // Create loading overlay if it doesn't exist
    let overlay = document.querySelector('.loading-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'loading-overlay';
        
        overlay.innerHTML = `
            <div class="bg-white p-3 rounded shadow">
                <div class="d-flex align-items-center">
                    <div class="spinner-border text-primary me-3" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <div class="loading-message">${message}</div>
                </div>
            </div>
        `;
        
        document.body.appendChild(overlay);
    } else {
        // Update message
        overlay.querySelector('.loading-message').textContent = message;
        overlay.style.display = 'flex';
    }
}

/**
 * Hide loading indicator
 */
function hideLoading() {
    const overlay = document.querySelector('.loading-overlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}