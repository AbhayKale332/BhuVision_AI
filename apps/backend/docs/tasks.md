For a project of this size, don't start with a random FastAPI tutorial structure.

Start with a structure that can survive 2+ years of development.

```text
backend/

├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── migrations/
│   │
│   ├── modules/
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── schemas.py
│   │   │   └── models.py
│   │   │
│   │   ├── users/
│   │   ├── maps/
│   │   ├── datasets/
│   │   ├── models/
│   │   ├── jobs/
│   │   ├── publishers/
│   │   └── wallet/
│   │
│   ├── services/
│   │   ├── storage/
│   │   ├── email/
│   │   └── queue/
│   │
│   ├── utils/
│   │
│   └── tests/
│
├── alembic/
├── docker/
├── scripts/
│
├── .env
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

### Tech Stack

```text
FastAPI
PostgreSQL
PostGIS
SQLAlchemy 2.0
Alembic
Pydantic Settings
JWT Auth
Redis
Celery
RabbitMQ
MinIO
Pytest
Ruff
Docker
```

### First files

**main.py**

```python
from fastapi import FastAPI

app = FastAPI(
    title="PrithviLens API",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}
```

**config.py**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
```

**session.py**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

### Day-1 Rules

Never:

```python
# bad
router -> directly talks to database
```

Always:

```text
Router
 ↓
Service
 ↓
Repository
 ↓
Database
```

Example:

```text
POST /users

router
 ↓
user_service
 ↓
user_repository
 ↓
postgres
```

### Create these modules immediately

```text
auth
users
publishers
datasets
maps
jobs
```

Even if they are empty.

Future-you will thank present-you.

### Before writing any feature

Setup:

```bash
ruff
pytest
alembic
docker
pre-commit
```

first.

A clean foundation saves hundreds of hours later. For your project, I would spend the first **3–5 days building infrastructure and architecture before writing a single geospatial feature**. That is what senior teams do.
