from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api import routes


app = FastAPI(title="Sentinel")
app.include_router(routes.router)


@app.get("/")
def root():
    return HTMLResponse("<h2> Hello from Uvicorn on behalf of Sentinel. </h2>")
