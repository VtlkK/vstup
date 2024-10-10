var openModalBtn = document.getElementById("openModalBtn");
var modal = document.getElementById("myModal");
var closeBtn1 = modal.getElementsByClassName("close")[0];

openModalBtn.onclick = function() {
    modal.style.display = "block";
}

closeBtn1.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Обробка вибору чекбоксів і перенаправлення
var submitButton = document.getElementById("submitButton");
submitButton.onclick = function() {
    var checkboxes = modal.querySelectorAll('input[type="checkbox"]');
    var checkedUrl = "";
    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            checkedUrl = checkbox.getAttribute("data-url");
        }
    });
    if (checkedUrl) {
        window.location.href = checkedUrl;
    } else {
        alert("Будь ласка, виберіть опцію.");
    }
}

// Логіка вибору тільки одного чекбоксу
var checkboxes = modal.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        checkboxes.forEach(function(otherCheckbox) {
            if (otherCheckbox !== checkbox) {
                otherCheckbox.checked = false;
            }
        });
    });
});

// Обробка другого модального вікна
var btn = document.getElementById("openModalButton");  // Додай кнопку з правильним ID
var modal2 = document.getElementById("myModal2");
var closeBtn2 = modal2.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal2.style.display = "block";
}

closeBtn2.onclick = function() {
    modal2.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal2) {
        modal2.style.display = "none";
    }
}