# FastAPI User Management Service

Микросервис для управления пользователями с поддержкой различных хранилищ данных

## Особенности

- 🚀 Реализация на FastAPI с асинхронной обработкой запросов
- 💾 Поддержка разных типов хранилищ (in-memory, PostgreSQL, MySQL)
- ⚙️ Конфигурация через YAML-файл
- 🐳 Готовый Docker-образ
- 📝 Автоматическая документация Swagger/Redoc
- ✅ Валидация данных через Pydantic v2

## Требования

- Python 3.9+
- Docker (опционально)
- Поддерживаемые СУБД (опционально):
  - PostgreSQL (рекомендуется)
  - MySQL
  - SQLite
- Хранение в оперативной памяти (опционально)

## Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/sergey-brovko/test_for_iqtek.git
cd test_for_iqtek
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Отредактировать `config.yaml`:
```yaml
repository:
  type: "sql"  # или "memory"
  database:
    driver: "postgresql+asyncpg"
    host: "localhost"
    port: 5432
    user: "your_user"
    password: "your_password"
    name: "your_db"
```

## Запуск

Для работы с SQL-репозиторием:
```bash
uvicorn src.main:app --reload
```

Для in-memory репозитория:
```bash
uvicorn src.main:app --reload
```

Документация API будет доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## Примеры запросов

Создать пользователя:
```bash
curl -X POST "http://localhost:8000/user/" \
-H "Content-Type: application/json" \
-d '{"full_name": "John Doe"}'
```

Получить пользователя:
```bash
curl "http://localhost:8000/user/1"
```

Обновить пользователя:
```bash
curl -X PUT "http://localhost:8000/user/1" \
-H "Content-Type: application/json" \
-d '{"full_name": "John Doe"}'
```

Удалить пользователя:
```bash
curl -X DELETE "http://localhost:8000/user/1"
```

## Конфигурация

Основные параметры `config.yaml`:
```yaml
repository:
  type: "sql"       # Тип хранилища (sql/memory)
  database:
    driver: "postgresql+asyncpg"  # Доступные драйверы:
                                  # - postgresql+asyncpg
                                  # - mysql+asyncmy
                                  # - sqlite+aiosqlite
    host: "db_host"
    port: 5432
    user: "db_user"
    password: "db_password"
    name: "db_name"
```

## Docker

Собрать образ и запустить контейнер с приложением:
```bash
docker-compose up app --build
```

Собрать образ и запустить контейнер с postgresql:
```bash
docker-compose up postgres_db --build
```

## Разработка

Структура проекта:
```
test_for_iqtek/
├── src/                 # Основной код приложения
├── config.yaml          # Конфигурация
├── Dockerfile           # Конфигурация Docker
├── docker-compose.yaml 
└── requirements.txt     # Зависимости
```

## Лицензия

MIT License
