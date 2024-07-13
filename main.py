from fastapi import FastAPI
import uvicorn
from routes import auth_routes, post_routes, thread_routes, user_routes, comment_routes
from dotenv import load_dotenv
from os import getenv

load_dotenv()
port = getenv("PORT")

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(thread_routes.router, prefix="/threads", tags=["threads"])
app.include_router(post_routes.router, prefix="/posts", tags=["posts"])
app.include_router(comment_routes.router, prefix="/comments", tags=["comments"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=port)

