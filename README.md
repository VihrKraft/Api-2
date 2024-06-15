# Обрезка ссылок с помощью Битли

Благодаря этому проекту можно сокращать ссылки и следить за количеством нажатий по ним.

### Как установить

Bitly не даст вам данные, пока вы не получите сервисный ключ – “токен”. Для этого не нужно писать код, достаточно сгенерировать токен на [сайте]('https://app.bitly.com/settings/api').

Вы получите сервисный токен приложения на подобии такого: `82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72`.

После создаете `.env` файл и записываете в нем ваш сервисный ключ в таком виде:
```
BITLY_TOKEN=82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Для запуска программы нужно указать специальный аргумент. Это может быть длинная или короткая ссылка. 

Для получения короткой ссылки нужно ввести длинную, например:
```
python main.py https://dvmn.org/
```
Для того, чтобы узнать колличество переходов по ней, нужно ввести полученную короткую ссылку, например:
```
python main.py https://bit.ly/3tkvUyq
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).