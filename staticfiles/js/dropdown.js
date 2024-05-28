// dropdown.js

  const menuButton = document.getElementById('menu-button');
  const menu = document.querySelector('.absolute');

  menuButton.addEventListener('click', () => {
    const isVisible = menu.classList.contains('hidden');
    if (isVisible) {
      menu.classList.remove('hidden');
      menu.setAttribute('aria-expanded', 'true');
    } else {
      menu.classList.add('hidden');
      menu.setAttribute('aria-expanded', 'false');
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (event) => {
    if (!menuButton.contains(event.target) && !menu.contains(event.target)) {
      menu.classList.add('hidden');
      menu.setAttribute('aria-expanded', 'false');
    }
  });
