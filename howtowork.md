If I joined your team as a senior engineer, I would **forbid anyone from writing actual features for the first few days**.

The goal is:

> Build the foundation once, build features many times.

---

# Week 0 — Planning (Before Writing Code)

### 1. Define Scope

Write exactly:

```text
Users
Publishers
Maps
Datasets
Models
Jobs
Wallet
```

Then write:

```text
Must Have
Nice To Have
Future
```

Most student projects fail because they keep adding features.

---

### 2. Draw Architecture

One diagram:

```text
Next.js
    ↓
FastAPI
    ↓
Postgres + PostGIS
    ↓
Redis
    ↓
Workers
    ↓
MinIO
```

Everyone should understand this.

---

### 3. Design Database

Before coding.

Create:

```text
users
publishers
datasets
models
model_versions
jobs
wallets
transactions
```

Even rough schemas are enough.

---

# Week 1 — Engineering Setup

### 4. Create Monorepo

```text
project/
├── frontend/
├── backend/
├── docs/
└── infra/
```

---

### 5. Git Setup

Create:

```bash
main
develop
```

Never commit directly to main.

---

### 6. .gitignore

Setup properly from day one.

---

### 7. README

Write:

```text
Project Vision
Architecture
Setup Steps
Folder Structure
```

Future teammates will thank you.

---

# Backend Setup

### 8. Setup Ruff

Python linting.

```bash
pip install ruff
```

Run:

```bash
ruff check .
```

Every commit.

---

### 9. Setup Formatting

```bash
ruff format .
```

Nobody should argue about formatting.

---

### 10. Setup Pytest

```bash
pip install pytest
```

Create:

```text
tests/
```

immediately.

---

### 11. Setup Alembic

Database migrations.

Never manually change production databases.

---

### 12. Setup Environment Variables

Create:

```text
.env.example
```

Commit this.

Never commit:

```text
.env
```

---

# Frontend Setup

### 13. Setup ESLint

Already comes with Next.js.

Must pass before merge.

---

### 14. Setup Prettier

Consistent formatting.

No discussions.

---

### 15. Setup React Query

Before first API call.

---

### 16. Setup Zustand

Before first global state.

---

# Infrastructure Setup

### 17. Dockerize Everything

Create:

```text
frontend
backend
postgres
redis
minio
```

containers.

Every teammate should run:

```bash
docker compose up
```

and get the project running.

---

### 18. Create Health Checks

Backend:

```text
GET /health
```

Frontend:

```text
Landing Page
```

First milestone:

System runs.

---

# Quality Setup

### 19. Pre-commit Hooks

Install:

```bash
pre-commit
```

Before commit:

```text
lint
format
```

runs automatically.

---

### 20. GitHub Actions

On every push:

```text
Lint
Test
Build
```

If tests fail:

```text
Merge blocked
```

---

# Documentation Setup

### 21. docs/

Create:

```text
architecture.md
database.md
api.md
roadmap.md
```

Do not rely on memory.

---

# First Feature

Only after all above:

Build:

```text
Authentication
```

Because it touches:

```text
Frontend
Backend
Database
JWT
Protected Routes
```

and validates architecture.

---

# Order I Would Follow

```text
1. Scope
2. Architecture
3. Database Design
4. Monorepo
5. Git
6. Docker
7. PostgreSQL + PostGIS
8. FastAPI Setup
9. Next.js Setup
10. Linting
11. Formatting
12. Tests
13. GitHub Actions
14. Authentication
15. Map Viewer
16. AOI Selection
17. Dataset Layers
18. Job System
19. Model Marketplace
20. Publisher Dashboard
21. Wallet
```

The key lesson is:

**Don't optimize for writing features fast. Optimize for making the 50th feature as easy to build as the 1st.** That's the difference between a project that survives growth and one that becomes unmaintainable after a month.
