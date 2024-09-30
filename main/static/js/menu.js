
  function handleDropdownChange() {
        const selectedValue = document.getElementById('input').value;

        // Зберігаємо вибір у localStorage
        localStorage.setItem('selectedDropdownValue', selectedValue);

        const modalClasses = {
            'main': 'modal01',
            'ver': 'modal02',
            'ank': 'modal03',
            'docs': 'modal04',
            'med': 'modal05',
            'red': 'modal06',
            'reds': 'modal07',
            'napravlen': 'modal08',
            'vid_napr': 'modal09',
            'end': 'modal10',
        };

        Object.values(modalClasses).forEach(modalClass => {
            document.querySelectorAll(`.${modalClass}`).forEach(modal => {
                modal.style.display = 'none';
            });
        });

        const modalClassToShow = modalClasses[selectedValue];
        if (modalClassToShow) {
            document.querySelectorAll(`.${modalClassToShow}`).forEach(modal => {
                modal.style.display = 'block';
            });
        }
    }

    // Відновлення вибору після завантаження сторінки
    window.addEventListener('load', () => {
        const savedValue = localStorage.getItem('selectedDropdownValue');
        if (savedValue) {
            document.getElementById('input').value = savedValue;
        }
        handleDropdownChange();
    });

    document.getElementById('input').addEventListener('change', handleDropdownChange);