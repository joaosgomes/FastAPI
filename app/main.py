from enum import Enum
import time
from typing import Union,List
from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.websockets import WebSocket
import random 
from fastapi.responses import JSONResponse
import httpx
# from models import Model


description = """
FastAPI Description

## FastAPI
"""

app = FastAPI(
    title="FastAPI",
    description=description,
    version="0.0.1",
    terms_of_service="https://opensource.org/licenses/MIT",
    contact={
        "name": "FastAPI",
        "url": "https://opensource.org/licenses/MIT",
        "email": "joao.s.gomes@outlook.pt",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },)


class Tags(Enum):
    root = "/"
    websocket = "Websocket"


#db:List[Model]=[
#Model(
#    Id = 1, 
#    Value = 'Value 1'
#    )
#]

#Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Some-Info"] = "Some Info..."
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/",
         tags=[Tags.root],
         summary="Root /",
         description="Description of Root Endpoint")
def read_root(request: Request):
    client_host = request.client.host

    return {"client_host": client_host, "response": "Response Root", "Request": request.state}





async def streamer():
    for i in range(100000):
        yield "."


@app.get("/stream")
async def main():
    return StreamingResponse(streamer())




@app.get("/fastapi", response_class=RedirectResponse)
async def redirect_fastapi():
    return "https://fastapi.tiangolo.com"


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    '''
    returns a JSON response in the form of:
    {
      'healtcheck': 'Everything OK!'
    }
    '''
    return {'healthcheck': 'Everything OK!'}




# @app.websocket_route("/ws")
# async def websocket(websocket: WebSocket):
#      await websocket.accept()
#      await websocket.send_json({"msg": "Hello WebSocket From FastAPI"})
#      await websocket.close()

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#      print('Accepting client connection...')
#      await websocket.accept()
#      while True:
#          try:
#              # Wait for any message from the client
#              await websocket.receive_text()
#              # Send message to the client
#              resp = {'value': random.uniform(0, 1)}
#              await websocket.send_json(resp)
#          except Exception as e:
#              print('error:', e)
#              break
#      print('Bye..')


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
