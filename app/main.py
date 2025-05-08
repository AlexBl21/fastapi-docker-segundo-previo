from fastapi import FastAPI, Request
import json
import os

import sqlite3
DB_PATH = "data/db.sqlite3"
os.makedirs("data", exist_ok=True)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
""")
conn.commit()
conn.close()

app = FastAPI()
@app.get("/")
async def root():
    return {
        "message": "Welcome to the FastAPI application! "
        "You can use this API to manage your notes."
    }


@app.get("/notes")
async def get_notes():

    # TODO: Implementar
    return {"notes": []}


@app.post("/notes")
async def create_note(request: Request):
    # TODO: Implementar
    return {"message": "Note created successfully!"}
