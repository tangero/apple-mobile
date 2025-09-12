// Custom navigation behavior for Apple Mobile site
document.addEventListener('DOMContentLoaded', function() {
    
    // Enhanced collapsible navigation for parent items
    function initializeCollapsibleNav() {
        const parentItems = document.querySelectorAll('.navigation-list-item');
        
        parentItems.forEach(item => {
            const link = item.querySelector('.navigation-list-link');
            const childList = item.querySelector('.navigation-list-child-list');
            
            if (childList && link) {
                item.classList.add('has-children');
                
                // Check if current page is within this section
                const currentPageInSection = childList.querySelector('.navigation-list-item.active') ||
                                           childList.querySelector('.navigation-list-link[aria-current="page"]');
                
                // Set initial state - expanded if current page is in section, collapsed otherwise
                if (currentPageInSection) {
                    item.classList.remove('collapsed');
                } else {
                    item.classList.add('collapsed');
                }
                
                // Add click handler to parent link
                link.addEventListener('click', function(e) {
                    // Only prevent default if this is a parent item (has children)
                    if (childList) {
                        e.preventDefault();
                        
                        // Toggle collapsed state
                        item.classList.toggle('collapsed');
                        
                        // Update aria-expanded for accessibility
                        const isExpanded = !item.classList.contains('collapsed');
                        link.setAttribute('aria-expanded', isExpanded.toString());
                    }
                });
                
                // Set initial aria-expanded value
                const isExpanded = !item.classList.contains('collapsed');
                link.setAttribute('aria-expanded', isExpanded.toString());
            }
        });
    }
    
    // Mobile menu toggle enhancement
    function initializeMobileMenu() {
        const menuButton = document.getElementById('menu-button');
        const siteNav = document.querySelector('.site-nav');
        
        if (menuButton && siteNav) {
            menuButton.addEventListener('click', function() {
                siteNav.classList.toggle('nav-open');
                const isOpen = siteNav.classList.contains('nav-open');
                menuButton.setAttribute('aria-pressed', isOpen.toString());
            });
        }
    }
    
    // Auto-collapse other sections when one is expanded (accordion behavior)
    function initializeAccordionBehavior() {
        const parentItems = document.querySelectorAll('.navigation-list-item.has-children');
        
        parentItems.forEach(item => {
            const link = item.querySelector('.navigation-list-link');
            
            if (link) {
                link.addEventListener('click', function() {
                    // If this item is being expanded, collapse others
                    if (item.classList.contains('collapsed')) {
                        parentItems.forEach(otherItem => {
                            if (otherItem !== item && !otherItem.classList.contains('collapsed')) {
                                // Don't collapse if it contains the current page
                                const currentPageInSection = otherItem.querySelector('.navigation-list-child-list .navigation-list-item.active') ||
                                                           otherItem.querySelector('.navigation-list-child-list .navigation-list-link[aria-current="page"]');
                                
                                if (!currentPageInSection) {
                                    otherItem.classList.add('collapsed');
                                    const otherLink = otherItem.querySelector('.navigation-list-link');
                                    if (otherLink) {
                                        otherLink.setAttribute('aria-expanded', 'false');
                                    }
                                }
                            }
                        });
                    }
                });
            }
        });
    }
    
    // Generate Table of Contents for articles
    function generateTableOfContents() {
        const tocContainer = document.getElementById('toc-container');
        if (!tocContainer) return;
        
        // Find all headings in the content area
        const content = document.querySelector('.content');
        if (!content) return;
        
        const headings = content.querySelectorAll('h2, h3, h4, h5, h6');
        if (headings.length === 0) {
            tocContainer.style.display = 'none';
            return;
        }
        
        // Create TOC list
        const tocList = document.createElement('ul');
        tocList.className = 'toc-list';
        
        let currentLevel = 2;
        let currentList = tocList;
        const listStack = [tocList];
        
        headings.forEach((heading, index) => {
            const level = parseInt(heading.tagName.substring(1));
            const headingId = heading.id || `heading-${index}`;
            
            // Set ID if not present
            if (!heading.id) {
                heading.id = headingId;
            }
            
            // Create list item
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = `#${headingId}`;
            link.textContent = heading.textContent;
            link.className = `toc-link toc-level-${level}`;
            
            // Smooth scroll behavior
            link.addEventListener('click', function(e) {
                e.preventDefault();
                heading.scrollIntoView({ behavior: 'smooth', block: 'start' });
                
                // Update URL hash
                if (history.pushState) {
                    history.pushState(null, null, `#${headingId}`);
                }
            });
            
            listItem.appendChild(link);
            
            // Handle nesting
            if (level > currentLevel) {
                // Create nested list
                const nestedList = document.createElement('ul');
                nestedList.className = 'toc-nested';
                
                // Add to previous item or current list
                const lastItem = currentList.lastElementChild;
                if (lastItem) {
                    lastItem.appendChild(nestedList);
                } else {
                    currentList.appendChild(nestedList);
                }
                
                listStack.push(nestedList);
                currentList = nestedList;
                currentLevel = level;
            } else if (level < currentLevel) {
                // Go back to appropriate level
                while (listStack.length > 1 && level < currentLevel) {
                    listStack.pop();
                    currentLevel--;
                }
                currentList = listStack[listStack.length - 1];
            }
            
            currentList.appendChild(listItem);
            currentLevel = level;
        });
        
        tocContainer.appendChild(tocList);
    }
    
    // Initialize all navigation enhancements
    initializeCollapsibleNav();
    initializeMobileMenu();
    initializeAccordionBehavior();
    generateTableOfContents();
    
    // Re-initialize on page load (for SPA-like behavior)
    window.addEventListener('load', function() {
        initializeCollapsibleNav();
        generateTableOfContents();
    });
});