document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.codehilite').forEach(container => {
        // Найти блок <pre> внутри контейнера
        const pre = container.querySelector('pre');
        if (!pre) return; // Пропустить, если нет <pre>

        // Создаем кнопку "Скопировать"
        const button = document.createElement('button');
        button.innerHTML = '<i class="bi bi-clipboard"></i> Скопировать';
        button.classList.add('copy-btn');
        button.classList.add('btn-sm');
        button.classList.add('btn');

        // Создаем элемент <p> для кнопки и добавляем его перед блоком <pre>
        const buttonContainer = document.createElement('p');
        buttonContainer.classList.add('button-container');
        buttonContainer.appendChild(button);

        // Вставляем <p> с кнопкой перед блоком <pre> внутри контейнера
        container.insertBefore(buttonContainer, pre);


        // Обработчик клика для копирования текста
        button.addEventListener('click', () => {
            const code = pre.querySelector('code').innerText;
            navigator.clipboard.writeText(code).then(() => {
                button.innerHTML = '<i class="bi bi-clipboard-check"></i> Скопировано';
                setTimeout(() => {
                    button.innerHTML = '<i class="bi bi-clipboard"></i> Скопировать';
                }, 2000);
            }).catch(err => {
                console.error('Ошибка копирования: ', err);
            });
        });
    });
});