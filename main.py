from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def first_func():
    return ("Hello Bushra you finally started writing code, just keep trying you will make it one day inshallah")