Think of it like this:

```text
Router -> Service -> Repository -> Database
```

A request should flow through these layers.

---

# Root Folder

```text
backend/
```

Entire backend application lives here.

---

# app/

```text
app/
```

Actual source code of your backend.

Everything important is inside this folder.

---

# main.py

```text
app/main.py
```

Entry point of FastAPI.

Starts the application.

Example:

```python
app = FastAPI()
```

All routers eventually get attached here.

---

# core/

```text
app/core/
```

Global application settings and configurations.

Stuff used by entire application.

---

## config.py

```text
app/core/config.py
```

Loads environment variables.

Example:

```env
DATABASE_URL=
JWT_SECRET=
```

Accessed anywhere in project.

---

## security.py

```text
app/core/security.py
```

Authentication and security logic.

Examples:

* JWT creation
* JWT validation
* Password hashing
* Password verification

---

## dependencies.py

```text
app/core/dependencies.py
```

Reusable FastAPI dependencies.

Examples:

```python
get_current_user()
get_db()
require_admin()
```

---

# db/

```text
app/db/
```

Database-related code.

---

## session.py

```text
app/db/session.py
```

Creates database connection.

Example:

```python
SessionLocal()
```

Every query uses this.

---

## base.py

```text
app/db/base.py
```

Imports all SQLAlchemy models.

Used by Alembic migrations.

Without this migrations may not detect tables.

---

## migrations/

```text
app/db/migrations/
```

Optional place for migration helpers.

Most migration files actually go in:

```text
alembic/versions/
```

---

# modules/

```text
app/modules/
```

Business features.

Every major feature gets its own module.

This is where most development happens.

---

# Example: auth/

```text
auth/
```

Everything related to login/signup.

---

## router.py

```text
auth/router.py
```

Defines API endpoints.

Example:

```python
POST /login
POST /register
```

Only handles request/response.

No business logic.

---

## service.py

```text
auth/service.py
```

Business logic.

Example:

```python
validate password
create token
send email
```

Brain of the module.

---

## repository.py

```text
auth/repository.py
```

Database queries.

Example:

```python
create user
find user
update user
```

Only database work.

---

## schemas.py

```text
auth/schemas.py
```

Pydantic models.

Request and response validation.

Example:

```python
LoginRequest
UserResponse
```

---

## models.py

```text
auth/models.py
```

SQLAlchemy database tables.

Example:

```python
class User(Base):
```

Creates actual database structure.

---

# users/

```text
modules/users/
```

User profile management.

Examples:

* update profile
* upload avatar
* account settings

---

# maps/

```text
modules/maps/
```

Map-related functionality.

Examples:

* draw AOI
* save map projects
* layer management

---

# datasets/

```text
modules/datasets/
```

Geospatial datasets.

Examples:

* SAR
* NDWI
* DEM
* Sentinel

Dataset upload and management.

---

# models/

```text
modules/models/
```

AI model marketplace.

Examples:

* publish model
* version model
* search models
* model metadata

---

# jobs/

```text
modules/jobs/
```

Background tasks.

Example:

User clicks:

```text
Run Flood Detection
```

Creates job.

Worker processes it later.

---

# publishers/

```text
modules/publishers/
```

People publishing geospatial models.

Examples:

* publisher profile
* ratings
* model ownership

---

# wallet/

```text
modules/wallet/
```

Future payments.

Examples:

* credits
* subscriptions
* transactions

---

# services/

```text
app/services/
```

Shared services used by multiple modules.

Not tied to one feature.

---

## storage/

```text
services/storage/
```

File storage.

Examples:

* MinIO
* S3
* Cloudflare R2

Uploads:

```text
GeoTIFF
Raster
Images
Results
```

---

## email/

```text
services/email/
```

Email sending.

Examples:

```text
OTP
Verification
Password reset
```

---

## queue/

```text
services/queue/
```

Background task system.

Examples:

```text
Celery
RabbitMQ
Redis Queue
```

---

# utils/

```text
app/utils/
```

Small helper functions.

Examples:

```python
date formatter
file validator
common helpers
```

Avoid putting business logic here.

---

# tests/

```text
app/tests/
```

Unit tests.

Examples:

```python
test_auth.py
test_users.py
```

Used by CI/CD.

---

# alembic/

```text
alembic/
```

Database migration system.

Tracks schema changes.

Example:

```bash
alembic revision
alembic upgrade head
```

---

# docker/

```text
docker/
```

Docker-related files.

Examples:

```text
postgres config
nginx config
worker config
```

Keeps root folder clean.

---

# scripts/

```text
scripts/
```

Automation scripts.

Examples:

```bash
seed database
create admin
load datasets
```

Useful for development.

---

# .env

```text
.env
```

Secrets and configuration.

Example:

```env
DATABASE_URL=
JWT_SECRET=
REDIS_URL=
```

Never commit to GitHub.

---

# pyproject.toml

```text
pyproject.toml
```

Backend package manager configuration.

Contains:

```text
dependencies
ruff
pytest
project metadata
```

Python equivalent of package.json.

---

# Dockerfile

```text
Dockerfile
```

Instructions to build backend container.

Example:

```docker
FROM python:3.13
```

---

# docker-compose.yml

```text
docker-compose.yml
```

Starts entire local stack.

Example:

```text
FastAPI
Postgres
Redis
MinIO
```

Single command:

```bash
docker compose up
```

---

# One Rule For Your Team

When someone asks:

> "Where should this code go?"

Use this checklist:

| Type                    | Location      |
| ----------------------- | ------------- |
| API Endpoint            | router.py     |
| Business Logic          | service.py    |
| Database Query          | repository.py |
| Request/Response Models | schemas.py    |
| Database Tables         | models.py     |
| Shared External Service | services/     |
| Helper Function         | utils/        |

If your team follows just this rule consistently, your codebase will remain understandable even when it reaches tens of thousands of lines.
