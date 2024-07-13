from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.comments import NewComment, UpdateComment
from database.schema import Comments
from utils.jwt_utils import decode_jwt_token

def create_comment(comment: NewComment, db: Session, req: Request):
    token = req.cookies.get("token")
    token_data = decode_jwt_token(token)

    new_comment = Comments (
        id=str(uuid4()),
        content=comment.content,
        owner_id=str(token_data["user_id"]),
        post_id=comment.post_id,
        created_at=str(datetime.utcnow()),
        updated_at=str(datetime.utcnow())
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return { "message": "Comment created successfully", "comment": new_comment }

def get_post_comments(db: Session):
    all_comments = db.query(Comments).all()
    if not all_comments:
        raise HTTPException(status_code=404, detail="No comments found")
    
    if all_comments == []:
        return JSONResponse(content={"message": "No comments found"}, status_code=404)

    return { "comments": all_comments }
    

def update_comment(comment_id: str, comment: UpdateComment, db: Session):
    find_comment = db.query(Comments).filter(Comments.id == comment_id).first()
    if not find_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if not comment.content:
        raise HTTPException(status_code=400, detail="Content is required")

    find_comment.content = comment.content
    find_comment.updated_at = str(datetime.utcnow())

    db.commit()
    db.refresh(find_comment)

    return { "message": "Comment updated successfully", "comment": find_comment }

def delete_comment(comment_id: str, db: Session):
    find_comment = db.query(Comments).filter(Comments.id == comment_id).first()
    if not find_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    db.delete(find_comment)
    db.commit()

    return { "message": "Comment deleted successfully" }