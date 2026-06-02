Ai use in database.py, models.py and in the docker compose, help to set the db, configs and all the other stufs, and help to decide between using vscode postgresql extension or pgadmin

AI give me this structure idea 

    project/
    │
    ├── core/
    │   └── database.py        ← engine, SessionLocal, Base
    │
    ├── models/
    │   └── user.py            ← SQLAlchemy ORM models
    │
    ├── schemas/
    │   └── user.py            ← Pydantic request/response models
    │
    ├── services/
    │   └── user_service.py    ← business logic (uses CRUD)
    │
    ├── services/
    │   └── user.py            ← actual SQL queries
    │
    └── routers/
        └── user.py            ← API endpoints

correct progression
    router → schema(validation) -> service(queries) → model(structure) → database