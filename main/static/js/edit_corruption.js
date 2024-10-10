  function validateInput(input) {
        // Регулярний вираз для українських літер, цифр, пробілів, знаків (тире, апострофи, крапка, кома, /, !, ?, _, =, +, *, (, ), #)
        const regex = /^[А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]*$/;
        // Зберігаємо значення до і після очищення
        const originalValue = input.value;
        // Очищаємо значення до тих, що відповідають регулярному виразу
        input.value = originalValue.replace(/[^А-ЩЬЮЯа-щьюя0-9 \-\'’.,\/!?_=\+\*\(\)#]/g, '');
    }





    // Отримати модальне вікно
    var modal = document.getElementById("myModal");

    // Отримати кнопку, яка відкриває модальне вікно
    var btn = document.querySelector(".info-icon");

    // Отримати елемент <span> з елементом закриття
    var span = document.getElementsByClassName("close")[0];

    // Коли користувач натискає кнопку, відкрити модальне вікно
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Коли користувач натискає на <span> (x), закрити модальне вікно
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Коли користувач натискає будь-де поза модальним вікном, закрити його
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }