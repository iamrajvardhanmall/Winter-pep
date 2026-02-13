from fastapi import FastAPI, status

app = FastAPI(title="LPU")

# @app.get("/", tags=['main'], status_code=status.HTTP_404_NOT_FOUND)
# def LPU():
#     return ("Hello World")


@app.get("/", tags=['main'], status_code=status.HTTP_404_NOT_FOUND)
def LPU():
    return {
            "msg": "Hello World"
    }



# @app.get("/about")
# def about():
#     return ("LPU is good place to live")
