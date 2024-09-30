document.addEventListener("DOMContentLoaded", function() {
    // Отримуємо всі елементи вкладок та всі контейнери контенту
    const tabButtons = document.querySelectorAll(".nav ul li");
    const tabContents = document.querySelectorAll(".tab");

    // Функція для зміни активної вкладки
    function showTab(index) {
        // Спочатку ховаємо весь контент та знімаємо клас 'active' з усіх вкладок
        tabContents.forEach(content => content.style.display = "none");
        tabButtons.forEach(button => button.classList.remove("active"));

        // Показуємо відповідний контент та додаємо клас 'active' до натиснутої вкладки
        tabContents[index].style.display = "block";
        tabButtons[index].classList.add("active");
    }

    // Додаємо обробники подій до кожної вкладки
    tabButtons.forEach((button, index) => {
        button.addEventListener("click", () => showTab(index));
    });

    // За замовчуванням показуємо першу вкладку
    showTab(0);
});


