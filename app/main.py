from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import psycopg2

app = FastAPI(title="Самостійна робота 7")

DB_DSN = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB')}"

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<p>Самостійна робота 7</p>"

@app.get("/visits")
async def add_visit():
    conn = psycopg2.connect(DB_DSN)
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id, visited_at")
    visit = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Новий візит додано", "id": visit[0], "time": str(visit[1])}

@app.get("/visits/count")
async def count_visits():
    conn = psycopg2.connect(DB_DSN)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"total_visits": count}