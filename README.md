#Placeholder App

Сборка докер образа приложения<br>
``docker-compose build``<br>
Запуск контейнера 
`docker-compose up`
При запуске контейнера автоматически применятся все миграции связанные с базой данных
В приложении существует возможность поддержки версионирования
Все изображения связанные с работой приложения находятся в папке `images`

Конфигурирование: poetry buildpack
``heroku buildpacks:clear``
``heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
``
``heroku buildpacks:add heroku/python``

Версия Python
``heroku config:set PYTHON_RUNTIME_VERSION=3.8.0``
Установка Poetry
``heroku config:set POETRY_VERSION=1.1.13``
``heroku config:set DISABLE_POETRY_CREATE_RUNTIME_FILE=1``