## Graduation Project (Дипломный проект)

### Запуск проекта
1. Клонируйте репозиторий

https://github.com/tolyan-yalta/graduation_project.git

2. Перейдите в папку с проектом
```Bash
cd graduation_project
```

3. Создайте виртуальное окружение и активируйте его
```Bash
python -m venv venv
source venv/bin/activate
```

4. Установите зависимости
```Bash
pip install -r requirements.txt
```

5. Применяем миграции к базе данных
```Bash
python manage.py migrate
```

6. Создаём администратора сайта
```Bash
python manage.py createsuperuser
```

7. Запускаем сервер
```Bash
python manage.py runserver
```

Открываем браузер и переходим по адресу:   
http://127.0.0.1:8000/   
Для входа в административную панель сайта переходим по адресу:   
http://127.0.0.1:8000/admin/   
Вводим имя пользователя и пароль администратора, чтобы войти в панель управления сайта.
