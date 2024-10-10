function validatePhoneNumber(input) {
        // Регулярний вираз для цифр та крапки
        const regex = /^[\d.]{0,11}$/;
        // Зберігаємо значення до і після очищення
        const originalValue = input.value;
        // Очищаємо значення до цифр та крапки і обмежуємо довжину до 11 символів (10 цифр і 1 крапка)
        input.value = originalValue.replace(/[^0-9.]/g, '').substring(0, 11);
    }



    function validateInput(input) {
        // Регулярний вираз для українських літер, цифр, пробілів, знаків (тире, апострофи, крапка, кома, /, !, ?, _, =, +, *, (, ), #)
        const regex = /^[А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]*$/;
        // Зберігаємо значення до і після очищення
        const originalValue = input.value;
        // Очищаємо значення до тих, що відповідають регулярному виразу
        input.value = originalValue.replace(/[^А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]/g, '');
    }





    function addInfoButton(containerId, infoText) {
        const container = document.getElementById(containerId);
        const infoButton = document.createElement("div");
        infoButton.className = "info-button";

        const button = document.createElement("button");
        button.type = "button";
        button.className = "info-icon";
        button.textContent = "i";

        const infoPopup = document.createElement("div");
        infoPopup.className = "info-popup";
        infoPopup.textContent = infoText;

        infoButton.appendChild(button);
        infoButton.appendChild(infoPopup);

        container.appendChild(infoButton);
    }