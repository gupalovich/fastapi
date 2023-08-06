from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from ..db.session import SessionLocal
from ..models.item import Item

router = APIRouter()


@router.post("/items/")
def create_item(item: Item, db: Session = Depends(SessionLocal)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(SessionLocal)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
