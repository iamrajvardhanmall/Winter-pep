from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def LPU():
    return {"Hello World"}
print(LPU())