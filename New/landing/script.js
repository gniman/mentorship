document.addEventListener("DOMContentLoaded", function() {

    const openModelButtons = document.querySelectorAll('[data-model-target]');
    const closeModelButtons = document.querySelectorAll('[data-close-button]');
    const overlay = document.getElementById('overlay');
    
    
    function openModal(targetModal) {
        if (targetModal) {
            targetModal.classList.add('active');
            overlay.classList.add('active');
        }
    }
    
    function closeModal(targetModal) {
        if (targetModal) {
            targetModal.classList.remove('active');
            overlay.classList.remove('active');
        }
    }
    
    openModelButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modalId = button.getAttribute('data-model-target');
            const modal = document.querySelector(modalId);
            openModal(modal);
        });
    });
    
    closeModelButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            closeModal(modal);
        });
    });
    });
    