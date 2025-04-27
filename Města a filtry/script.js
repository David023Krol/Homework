document.addEventListener('DOMContentLoaded', () => {
    // --- Tabulka - Filtrování podle města ---
    const filterInputTable = document.getElementById('filter-by-city');
    const tableBody = document.getElementById('data-table-body');
    const tableRows = Array.from(tableBody.querySelectorAll('tr')); // Převod NodeList na Array pro snadnější manipulaci

    filterInputTable.addEventListener('input', function() {
        const filterText = this.value.toLowerCase();
        tableRows.forEach(row => {
            const cityCell = row.cells[1];
            const cityText = cityCell.textContent.toLowerCase();
            row.style.display = cityText.includes(filterText) ? '' : 'none';
        });
    });

    // --- Formulář - Filtrování výběrového menu ---
    const filterInputSelect = document.getElementById('filter-city-select');
    const selectElement = document.getElementById('mesto');
    const originalOptions = Array.from(selectElement.options).map(option => ({ value: option.value, text: option.text }));

    filterInputSelect.addEventListener('input', function() {
        const filterText = this.value.toLowerCase();
        selectElement.innerHTML = '<option value="">Všechna města</option>';
        originalOptions.forEach(option => {
            if (option.text.toLowerCase().includes(filterText)) {
                const newOption = document.createElement('option');
                newOption.value = option.value;
                newOption.text = option.text;
                selectElement.appendChild(newOption);
            }
        });
    });

    // --- Formulář - Zpracování odeslání ---
    const submitButton = document.getElementById('submit-form');
    const nameInput = document.getElementById('jmeno');
    const emailInput = document.getElementById('email');
    const citySelect = document.getElementById('mesto');
    const formMessage = document.getElementById('form-message');

    submitButton.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedCity = citySelect.value;
        const name = nameInput.value;
        const email = emailInput.value;

        console.log('Odesláno:', { město: selectedCity, jméno: name, email: email });

        // Simulace úspěšného odeslání
        formMessage.textContent = 'Odesláno!';
        formMessage.className = 'form-message success';
        setTimeout(() => {
            formMessage.textContent = '';
            formMessage.className = 'form-message';
            nameInput.value = '';
            emailInput.value = '';
            citySelect.value = '';
            filterInputSelect.value = ''; // Vymaže i filtr u selectu
            selectElement.innerHTML = '<option value="">Všechna města</option>';
            originalOptions.forEach(option => {
                const newOption = document.createElement('option');
                newOption.value = option.value;
                newOption.text = option.text;
                selectElement.appendChild(newOption);
            });
        }, 3000);
    });

    // --- Navigace v rámci stránky (smooth scroll) ---
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});