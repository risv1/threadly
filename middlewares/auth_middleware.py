from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import RedirectResponse

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next: RequestResponseEndpoint):

        if req.url.path == "/auth/register":
            response = await call_next(req)
            return response

        if req.url.path == "/auth/login":
            response = await call_next(req)
            return response
        
        if req.url.path == "/threads/all":
            response = await call_next(req)
            return response
    
        if req.url.path == "/posts/thread/{thread_id}":
            response = await call_next(req)
            return response
        
        if req.url.path == "/comments/post/{post_id}":
            response = await call_next(req)
            return response

        token = req.cookies.get("token")
        if not token:
            raise HTTPException(status_code=401, detail="Unauthorized")

        response = await call_next(req)
        return response