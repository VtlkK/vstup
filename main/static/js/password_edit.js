 document.getElementById('togglePass').addEventListener('click', function () {
            const passwordField = document.getElementById('pass');
            const toggleIcon = document.getElementById('toggleIconPass');

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                toggleIcon.textContent = '👁️'; // Іконка для показу пароля
            } else {
                passwordField.type = 'password';
                toggleIcon.textContent = '🙈'; // Іконка для приховування пароля
            }
        });