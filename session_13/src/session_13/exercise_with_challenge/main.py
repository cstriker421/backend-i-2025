import logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from contextlib import asynccontextmanager

# Logging Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Database Setup
DATABASE_URL = "postgresql://postgres:password@db:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# Model
class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

# Lifespan Handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created")
    yield

# App
app = FastAPI(lifespan=lifespan)

# Logic Layer
def create_item_logic(session: Session, item: Item) -> Item:
    logger.info(f"Creating item: {item.name}")
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def update_item_logic(session: Session, item_id: int, new_item: Item) -> Item:
    logger.info(f"Updating item ID: {item_id}")
    statement = select(Item).where(Item.id == item_id)
    existing_item = session.exec(statement).one_or_none()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    existing_item.name = new_item.name
    existing_item.description = new_item.description
    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item

def delete_item_logic(session: Session, item_id: int) -> dict:
    logger.info(f"Deleting item ID: {item_id}")
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return {"message": f"Item {item_id} deleted successfully"}

def search_items_logic(session: Session, query: str):
    logger.info(f"Searching for items containing: {query}")
    statement = select(Item).where(Item.name.ilike(f"%{query}%"))
    items = session.exec(statement).all()
    return items

def delete_by_keyword_logic(session: Session, keyword: str) -> dict:
    logger.info(f"Deleting items with keyword in description: {keyword}")
    statement = select(Item).where(Item.description.ilike(f"%{keyword}%"))
    items = session.exec(statement).all()
    deleted_count = 0
    for item in items:
        logger.info(f"Deleting item ID: {item.id}")
        session.delete(item)
        deleted_count += 1
    session.commit()
    return {"deleted": deleted_count}

# API Endpoints
@app.post("/items/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    return create_item_logic(session, item)

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, session: Session = Depends(get_session)):
    statement = select(Item).where(Item.id == item_id)
    result = session.exec(statement)
    item = result.one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, session: Session = Depends(get_session)):
    return update_item_logic(session, item_id, item)

@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    return delete_item_logic(session, item_id)

@app.get("/items/search/", response_model=list[Item])
def search_items(query: str, session: Session = Depends(get_session)):
    return search_items_logic(session, query)

@app.delete("/items/delete-by-keyword/")
def delete_items_by_keyword(keyword: str, session: Session = Depends(get_session)):
    return delete_by_keyword_logic(session, keyword)
