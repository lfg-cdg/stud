from fastapi import APIRouter, HTTPException

from app.schemas import BookmarkCreate, BookmarkUpdate

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])

bookmarks = []
bookmark_id_counter = 0


@router.post("/", status_code=201)
def create_bookmark(bookmark: BookmarkCreate):
    global bookmark_id_counter
    bookmark_id_counter += 1

    created_bookmark = {"id": bookmark_id_counter, **bookmark.model_dump()}
    bookmarks.append(created_bookmark)
    return {"message": "Bookmark created", "bookmark": created_bookmark}


@router.get("/")
def check_bookmarks():
    return bookmarks


@router.get("/favourite")
def check_favourite_bookmarks():
    favourite = []

    for bookmark in bookmarks:
        if bookmark["is_favourite"]:
            favourite.append(bookmark)

    return favourite


@router.get("/{bookmark_id}")
def check_bookmark_by_id(bookmark_id: int):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            return bookmark

    raise HTTPException(status_code=404, detail="Bookmark not found")


@router.put("/{bookmark_id}")
def update_bookmark(bookmark_id: int, updated_bookmark: BookmarkUpdate):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            bookmark.update(updated_bookmark.model_dump())
            return bookmark

    raise HTTPException(status_code=404, detail="Bookmark not found")


@router.delete("/{bookmark_id}")
def delete_bookmark(bookmark_id: int):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            bookmarks.remove(bookmark)
            return {"message": "Bookmark deleted"}

    raise HTTPException(status_code=404, detail="Bookmark not found")
