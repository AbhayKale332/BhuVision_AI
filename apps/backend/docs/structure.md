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