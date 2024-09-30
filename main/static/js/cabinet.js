const chatButton = document.getElementById('chat-button');
        const chatBox = document.getElementById('chat-box');

        chatButton.addEventListener('click', () => {
            chatBox.classList.remove('hidden');
        });

        //  (Optional) Додати функціональність для закриття вікна чату

        chatBox.addEventListener('click', (event) => {
            if (event.target === chatBox) {
                chatBox.classList.add('hidden');
            }
        });

        const closeChatButton = document.getElementById('close-chat-button');

        closeChatButton.addEventListener('click', () => {
            chatBox.classList.add('hidden');
        });
          var openModalBtn = document.getElementById("openModalBtn");
                            var modal = document.getElementById("myModal");
                            var closeBtn1 = modal.getElementsByClassName("close")[0];

                            openModalBtn.onclick = function() {
                                modal.style.display = "block";
                            }

                            closeBtn1.onclick = function() {
                                modal1.style.display = "none";
                            }

                            window.onclick = function(event) {
                                if (event.target == modal1) {
                                    modal1.style.display = "none";
                                }
                            }

                            var submitButton = document.getElementById("submitButton");
                            submitButton.onclick = function() {
                                var checkboxes = modal1.querySelectorAll('input[type="checkbox"]');
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

                            var checkboxes = modal1.querySelectorAll('input[type="checkbox"]');
                            checkboxes.forEach(function(checkbox) {
                                checkbox.addEventListener('change', function() {
                                    checkboxes.forEach(function(otherCheckbox) {
                                        if (otherCheckbox !== checkbox) {
                                            otherCheckbox.checked = false;
                                        }
                                    });
                                });
                            });

                            // Second modal handling
                            var btn = document.getElementById("openModalButton");
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