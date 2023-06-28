from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def holamundo():
    return "Hola mundo"