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