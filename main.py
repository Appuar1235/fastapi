from fastapi import FastAPI

app = FastAPI()


@app.put("/predict")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def root():
    return {"message": "Hello World"}