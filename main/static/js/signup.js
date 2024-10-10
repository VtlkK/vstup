 function toggleMilitaryField() {
            var sex = document.getElementById('sex').value;
            var militaryField = document.getElementById('militaryField');

            if (sex === 'Жін.') {
                militaryField.style.display = 'none';  // Приховати для жінок
            } else {
                militaryField.style.display = 'block'; // Залишити видимим для інших
            }
        }


        function adjustInputWidth() {
                var addressInput = document.getElementById("address");
                if (window.innerWidth <= 768) {
                    addressInput.style.width = "100%";
                } else {
                    addressInput.style.width = "66%";
                }
            }

            // Викликаємо функцію при завантаженні сторінки і при зміні розміру екрану
            window.addEventListener('resize', adjustInputWidth);
            window.addEventListener('load', adjustInputWidth);




        document.getElementById('togglePassword').addEventListener('click', function () {
            const passwordField = document.getElementById('password');
            const toggleIcon = document.getElementById('toggleIcon');

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                toggleIcon.textContent = '👁️'; // Іконка для показу пароля
            } else {
                passwordField.type = 'password';
                toggleIcon.textContent = '🙈'; // Іконка для приховування пароля
            }
        });


        function validateAddress(input) {

            input.value = input.value.replace(/[^А-Яа-яІіЇїЄєҐґ0-9',. -]/g, '');
        }

        function validateDate(input) {
            input.value = input.value.replace(/[^0-9.]/g, '');
        }


        function validatePhoneNumber(input) {
            input.value = input.value.replace(/[^0-9-]/g, '');
        }


         function validateInput(input) {

            input.value = input.value.replace(/[^А-Яа-яІіЇїЄєҐґ' ]/g, '');


            if (input.value.length > 0) {
                input.value = input.value.charAt(0).toUpperCase() + input.value.slice(1);
            }
         }



