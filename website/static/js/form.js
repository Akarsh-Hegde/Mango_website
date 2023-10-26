document.querySelector('#cart-form').addEventListener('submit', function (e) {
        e.preventDefault();

        const selectedWeek = document.querySelector('select[name="week"]').value;
        const selectedOption = document.querySelector('input[name="flexRadioDefault"]:checked').value;
        const selectedQuantity = document.querySelector('select[name="quantity"]').value;

        document.getElementById('selectedWeek').textContent = selectedWeek;
        document.getElementById('selectedOption').textContent = selectedOption;
        document.getElementById('selectedQuantity').textContent = selectedQuantity;

        const modal = new bootstrap.Modal(document.getElementById('exampleModal'));
        modal.show();
    });