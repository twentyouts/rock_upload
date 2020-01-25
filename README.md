# rock_upload

- [x] Загрузить файл на сервак
- [ ] Обработчик который мониторит загрузили или нет файл
- [ ] Загрузка файла в базу
- [ ] Понять как во фронте забрать файл


link на подсказку как сделать на фронте забор файла - https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/


## Для запуска 
1. docker build . -t aiohttp
2. docker run -d -it -v $PWD/uploads:/app/uploads -p 8000:8080 aiohttp
3. docker exec -it {contatiner id}  python ./uploader/aio_http.py

## Создал новое приложение в рокстате 
и по ссылке https://twenty.dg02.ru/rock_upload/main/ где main это метод под декоратором @expose пробую отправлять запросы

## Тестовые отправки файла из терминала
Для отправки файла из терминала  curl -F "data=@/home/twentyouts/Documents/new.txt" https://twenty.dg02.ru/rock_upload/main/

## Curl команды для отправки запросов
https://gist.github.com/subfuzion/08c5d85437d5d4f00e58


