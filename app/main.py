from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()
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

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to the FastAPI application! "
                   "You can use this API to manage your notes."
    }

@app.get("/notes")
async def get_notes():
    return {"notes": []}
@app.post("/notes")
async def create_note(note: Note):
    if not note.title.strip() or not note.content.strip():
        raise HTTPException(status_code=400, detail="Title and content cannot be empty.")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (note.title, note.content))
        conn.commit()
        conn.close()
        return {"message": "Note created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
