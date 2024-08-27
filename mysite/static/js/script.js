document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach(pre => {
      // Создаем кнопку "Скопировать"
      const button = document.createElement('button');
      button.innerHTML = '<i class="bi bi-clipboard"></i> cкопировать';
      button.classList.add('copy-btn');
      button.classList.add('btn-sm');
      button.classList.add('btn');
      button.classList.add('d-flex');
      button.classList.add('float-right');


      
      // Добавляем кнопку перед содержимым блока <pre>
      pre.style.position = 'relative';
      pre.prepend(button);

      // Обработчик клика для копирования текста
      button.addEventListener('click', () => {
          const code = pre.querySelector('code').innerText;
          navigator.clipboard.writeText(code).then(() => {
              button.innerHTML = '<i class="bi bi-clipboard-check"></i> скопированно';
              setTimeout(() => {
                  button.innerHTML = '<i class="bi bi-clipboard"></i>';
              }, 2000);
          }).catch(err => {
              console.error('Ошибка копирования: ', err);
          });
      });
  });
});