# Demo FastStream

Пример взаимодействия микросерисов (FastAPI и AIOgram) через RabbitMQ с использованием FastStream

---

## О проекте

Этот небольшой проект демонстрирует, как два микросервиса — API на FastAPI и телеграм-бот на AIOgram — могут
обмениваться сообщениями через RabbitMQ при помощи библиотеки FastStream

Основная цель — научиться использовать FastStream и интегрировать его в более сложные
проекты: [Личный телеграм бот](https://github.com/mksmin/tasker-bot)

### Сервисы

- **API-сервис** (demo-fastapi) — принимает HTTP-запросы и посылает сообщение через RabbitMQ
- **Телеграм-бот** (demo-aiogram) — слушает очередь, выполняет логику и возвращает ответ

--- 

## Запуск

1. Клонировать репозиторий

```bash
git clone https://github.com/mksmin/demo-faststream.git
cd demo-faststream
```

2. Настроить .env для каждого сервиса

#### demo-aiogram

```bash
cd demo-aiogram
cp .env.template .env
sudo nano .env
# подставить свои значения
ctrl + O
Enter
ctrl + X
```

#### demo-fastapi

```bash
cd demo-fastapi
cd demo-aiogram
cp .env.template .env
sudo nano .env
# подставить свои значения
ctrl + O
Enter
ctrl + X
```

3. Запустить проекты через docker

```bash
docker compose up --build -d 
```

4. Проверить доступность сервисов:

| Сервис          | Адрес                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------|
| 📘 FastAPI      | [http://localhost:8000/docs](http://localhost:8000/docs)                                |
| 📬 RabbitMQ UI  | [http://localhost:15672](http://localhost:15672) (логин/пароль из `docker-compose.yml`) |
| 🤖 Telegram-бот | отправьте `/start` в Telegram-боте                                                      |
