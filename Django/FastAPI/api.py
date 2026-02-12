from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def LPU():
    return ("Hello World")
# print(LPU())

@app.get("/about")
def about():
    return ("LPU is good place to live")
print(about())