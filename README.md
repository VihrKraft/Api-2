# Обрезка ссылок с помощью Битли

Благодаря этому проекту можно сокращать ссылки и следить за количеством нажатий по ним.

### Как установить

Нужно зарегистрироваться в VK. VK не даст вам данные, пока вы не получите сервисный ключ – “токен”. Он нужен для взаимодействия с API VK. Его нужно сгенерировать. Что можно сделать в [сервисном токене приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token).

Вы получите сервисный токен приложения на подобии такого: `82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72`.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).