    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('.learn-more').forEach(function (button) {
            button.addEventListener('click', function () {
                var clientId = this.getAttribute('data-client-id');
                var modal = document.getElementById('myModal-' + clientId);
                modal.style.display = 'block';
            });
        });

        document.querySelectorAll('.close').forEach(function (closeBtn) {
            closeBtn.addEventListener('click', function () {
                var clientId = this.getAttribute('data-client-id');
                var modal = document.getElementById('myModal-' + clientId);
                modal.style.display = 'none';
            });
        });

        window.onclick = function (event) {
            document.querySelectorAll('.modal').forEach(function (modal) {
                if (event.target == modal) {
                    modal.style.display = 'none';
                           }
            });
        };

        document.querySelectorAll('.submitButton').forEach(function (submitButton) {
            submitButton.addEventListener('click', function () {
                var clientId = this.getAttribute('data-client-id');
                alert('Delete action for client id: ' + clientId);
            });
        });
    });
    function redirectToViber(phoneNumber) {
        var viberUrl = 'viber://chat?number=' + phoneNumber ;
        window.location.href = viberUrl;
    }
