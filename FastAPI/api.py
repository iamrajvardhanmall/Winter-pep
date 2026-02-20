from fastapi import FastAPI, status

app = FastAPI(title="LPU")

# @app.get("/", tags=['main'], status_code=status.HTTP_404_NOT_FOUND)
# def LPU():
#     return ("Hello World")



# @app.get("/about")
# def about():
#     return ("LPU is good place to live")


# @app.get("/", tags=['main'], status_code=status.HTTP_404_NOT_FOUND)
# def LPU():
#     return {
#             "msg": "Hello World"
#     }

# @app.get("/", tags=['main'], status_code=status.HTTP_404_NOT_FOUND)
# def indexPostViews(data:str):
#     return {
#             "msg": "Hello World"
#     }
    

@app.get("/post/{id}")
def indexView(id:int):
    return {
        'id': "id"
    }
