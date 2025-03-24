const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarTextElements = document.querySelectorAll('.sidebar-text');
    const sidebarTitle = document.getElementById('sidebar-title');
    const menuIcon = document.getElementById('menu-icon');

    function toggleSidebar() {
        if (sidebar.classList.contains('w-20')) {
            // Expand Sidebar
            sidebar.classList.remove('w-20');
            sidebar.classList.add('w-64');
            sidebarTextElements.forEach(el => el.classList.remove('hidden'));
            sidebarTitle.classList.remove('hidden');
            menuIcon.classList.remove('fa-bars');
            menuIcon.classList.add('fa-times'); // Change to "X"
        } else {
            // Collapse Sidebar
            sidebar.classList.remove('w-64');
            sidebar.classList.add('w-20');
            sidebarTextElements.forEach(el => el.classList.add('hidden'));
            sidebarTitle.classList.add('hidden');
            menuIcon.classList.remove('fa-times');
            menuIcon.classList.add('fa-bars'); // Change back to "≡"
        }
    }

    menuToggle.addEventListener('click', toggleSidebar);
