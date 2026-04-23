from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Bookmark
from app.schemas import BookmarkCreate, BookmarkPatch, BookmarkResponse, BookmarkUpdate

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])


def get_bookmark_or_404(bookmark_id: int, db: Session = Depends(get_db)) -> Bookmark:
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()

    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found!")

    return bookmark


@router.post("/", status_code=201, response_model=BookmarkResponse)
def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    new_bookmark = Bookmark(**bookmark.model_dump())

    db.add(new_bookmark)
    db.commit()
    db.refresh(new_bookmark)

    return new_bookmark


@router.get("/", response_model=list[BookmarkResponse])
def get_bookmarks(db: Session = Depends(get_db)):
    return db.query(Bookmark).all()


@router.get("/favourite", response_model=list[BookmarkResponse])
def get_favourite_bookmarks(db: Session = Depends(get_db)):
    favourite_bookmarks = db.query(Bookmark).filter(Bookmark.is_favourite.is_(True)).all()

    return favourite_bookmarks


@router.get("/{bookmark_id}", response_model=BookmarkResponse)
def get_bookmark_by_id(bookmark_id: int, db: Session = Depends(get_db)):
    return get_bookmark_or_404(bookmark_id, db)


@router.put("/{bookmark_id}", response_model=BookmarkResponse)
def update_bookmark(bookmark_id: int, new_bookmark: BookmarkUpdate, db: Session = Depends(get_db)):
    bookmark = get_bookmark_or_404(bookmark_id, db)

    for key, value in new_bookmark.model_dump().items():
        setattr(bookmark, key, value)

    db.commit()
    db.refresh(bookmark)

    return bookmark


@router.delete("/{bookmark_id}", status_code=200)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = get_bookmark_or_404(bookmark_id, db)

    db.delete(bookmark)
    db.commit()

    return {"message": "Bookmark deleted!"}


@router.patch("/{bookmark_id}", response_model=BookmarkResponse)
def patch_bookmark(bookmark_id: int, patch: BookmarkPatch, db: Session = Depends(get_db)):
    bookmark = get_bookmark_or_404(bookmark_id, db)

    new_bookmark = patch.model_dump(exclude_unset=True)
    for key, value in new_bookmark.items():
        setattr(bookmark, key, value)

    db.commit()
    db.refresh(bookmark)

    return bookmark
