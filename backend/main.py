from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_CONFIG = {
    "dbname": "hellodb",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": 5432
}

@app.get("/")
def hello():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 'Hello from PostgreSQL'")
            message = cur.fetchone()[0]
    return {"message": message}
