from fastapi import FastAPI
from routes.routes import router
from dotenv import load_dotenv
from os import getenv

load_dotenv()
port = getenv("PORT")

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=port)

