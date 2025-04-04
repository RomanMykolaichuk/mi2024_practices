from fastapi import FastAPI

app = FastAPI()

@app.get("/f1")
def my_function():
    return {"message":"Привіт від FastAPI"}

@app.get("/")
def my_next_function():
    return {"message":"Повідомлення від FastAPI", 
            "text":"Текст повідомлення"}

