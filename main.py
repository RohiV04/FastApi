import uvicorn
from fastapi import FastAPI
from router.note import note
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(note)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
