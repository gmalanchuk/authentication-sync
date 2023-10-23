from datetime import datetime

from fastapi import FastAPI


app = FastAPI(title="AuthenticationSync API", version='1.0.0')


@app.get('/')
async def hella():
    return 'hella'


@app.on_event("startup")
async def startup() -> None:
    """Executed before the server starts"""

    start_time = datetime.now()

    end_time = datetime.now()
