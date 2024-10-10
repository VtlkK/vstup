   function validatePhoneNumber(input) {
        // Регулярний вираз для 10 цифр
        const regex = /^\d{0,10}$/;
        // Зберігаємо значення до і після очищення
        const originalValue = input.value;
        // Очищаємо значення до тих, що відповідають регулярному виразу
        input.value = originalValue.replace(/[^0-9]/g, '').substring(0, 10);
    }


    function validateInput(input) {
        // Регулярний вираз для українських літер, цифр, пробілів, знаків (тире, апострофи, крапка, кома, /, !, ?, _, =, +, *, (, ), #)
        const regex = /^[А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]*$/;
        // Зберігаємо значення до і після очищення
        const originalValue = input.value;
        // Очищаємо значення до тих, що відповідають регулярному виразу
        input.value = originalValue.replace(/[^А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]/g, '');
    }