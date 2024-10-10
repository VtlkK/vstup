// Знаходимо всі елементи з класом 'info-button'
    var infoButtons = document.querySelectorAll('.info-button');

    // Додаємо обробник кліку для кожного елемента
    infoButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        // Знаходимо відповідний info-box (він повинен бути сусідом info-button)
        var infoBox = button.nextElementSibling;

        // Перемикаємо видимість info-box
        if (infoBox.style.display === 'block') {
          infoBox.style.display = 'none';
        } else {
          infoBox.style.display = 'block';
        }

        // Зупиняємо подію, щоб не закривати вікно при кліці на сам спан
        event.stopPropagation();
      });
    });

    // Закриваємо модальне вікно при кліку поза ним
    document.addEventListener('click', function(event) {
      infoButtons.forEach(function(button) {
        var infoBox = button.nextElementSibling;

        // Якщо клік не на info-box і не на info-button, закриваємо info-box
        if (!infoBox.contains(event.target) && event.target !== button) {
          infoBox.style.display = 'none';
        }
      });
    });
