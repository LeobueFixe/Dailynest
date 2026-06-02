Ai use in database.py, models.py and in the docker compose, help to set the db, configs and all the other stufs, and help to decide between using vscode postgresql extension or pgadmin

AI give me this idea for structure folders 
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
├── crud/
│   └── user.py            ← actual SQL queries
│
└── routers/
    └── user.py            ← API endpoints