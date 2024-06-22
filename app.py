import json
import urllib

from fastapi import FastAPI, Request
from starlette.datastructures import FormData
from starlette.middleware.base import BaseHTTPMiddleware

from service.api import router


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
