const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const sidebarTextElements = document.querySelectorAll('.sidebar-text');
const sidebarTitle = document.getElementById('sidebar-title');
const menuIcon = document.getElementById('menu-icon');

function toggleSidebar() {
    if (sidebar.classList.contains('open')) {
        // Collapse Sidebar
        sidebar.classList.remove('open');
        sidebar.classList.add('w-10');
        sidebarTextElements.forEach(el => el.classList.add('hidden'));
        sidebarTitle.classList.add('hidden');
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    } else {
        // Expand Sidebar
        sidebar.classList.add('open');
        sidebar.classList.remove('w-10');
        sidebarTextElements.forEach(el => el.classList.remove('hidden'));
        sidebarTitle.classList.remove('hidden');
        menuIcon.classList.remove('fa-bars');
        menuIcon.classList.add('fa-times');
    }
}

menuToggle.addEventListener('click', toggleSidebar);


document.addEventListener('htmx:afterSwap', function(event) {
    if (event.detail.target.id === 'editBox') {
        event.detail.target.classList.remove('hidden');
    }
});





document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search");
    const categoryFilter = document.getElementById("categoryFilter");
    const tableRows = document.querySelectorAll("#productTable tr");

    function filterProducts() {
        const searchText = searchInput.value.toLowerCase();
        const selectedCategory = categoryFilter.value.toLowerCase();

        tableRows.forEach(row => {
            const productName = row.children[1].textContent.toLowerCase();
            const productCategory = row.children[2].textContent.toLowerCase();

            // Check if row matches search text
            const matchesSearch = searchText === "" || productName.includes(searchText);
            const matchesCategory = selectedCategory === "" || productCategory === selectedCategory;

            // Only show row if both conditions are met
            row.style.display = (matchesSearch && matchesCategory) ? "" : "none";
        });
    }

    // Event listener for search input
    searchInput.addEventListener("input", function () {
        categoryFilter.value = ""; // Reset category filter
        filterProducts(); // Apply filtering
    });

    // Event listener for category dropdown
    categoryFilter.addEventListener("change", filterProducts);
});
