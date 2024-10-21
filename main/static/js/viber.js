document.addEventListener("DOMContentLoaded", function() {
    const chatButton = document.getElementById('chat-button');
    const chatBox = document.getElementById('chat-box');
    const closeChatButton = document.getElementById('close-chat-button');
    const viberButton = document.getElementById('viber-button');

    const phoneNumber = '380972515114';

    chatButton.addEventListener('click', function() {
        chatBox.classList.toggle('hidden');
    });

    closeChatButton.addEventListener('click', function() {
        chatBox.classList.add('hidden');
    });

    viberButton.addEventListener('click', function(e) {
        e.preventDefault();
        const viberUrl = `viber://chat?number=${phoneNumber}`;
        window.location.href = viberUrl;
    });
});
