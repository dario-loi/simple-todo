from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="templates")

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT, completed BOOLEAN)"""
)
conn.commit()


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return templates.TemplateResponse(
        "index.html", {"request": request, "todos": todos}
    )


@app.post("/")
async def create_todo(request: Request, task: str = Form(...)):
    cursor.execute("INSERT INTO todos (task, completed) VALUES (?, ?)", (task, False))
    conn.commit()
    return {"task": task}


@app.post("/complete/{todo_id}")
async def complete_todo(todo_id: int):
    cursor.execute("UPDATE todos SET completed = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    return {"message": "Task marked as completed"}


@app.post("/remove/{todo_id}")
async def remove_todo(todo_id: int):
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    return {"message": "Task removed"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
