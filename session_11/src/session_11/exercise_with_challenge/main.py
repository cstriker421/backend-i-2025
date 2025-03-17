from fastapi import FastAPI, HTTPException
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

items = {} # Mock database for storing items

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: dict):
    logger.info(f"Item received: {item}")
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    
    item_id = len(items) + 1
    item["id"] = item_id
    items[item_id] = item
    logger.info(f"Item created with ID: {item_id}")
    return {"item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    logger.info(f"Updating item with ID: {item_id}")
    if item_id not in items:
        logger.error("Item not found for update")
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_item = items[item_id]
    updated_item.update(item)
    items[item_id] = updated_item
    logger.info(f"Item with ID {item_id} updated")
    return {"updated_item": {"item_id": item_id, **updated_item}}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Deleting item with ID: {item_id}")
    if item_id not in items:
        logger.error("Item not found for deletion")
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items[item_id]
    logger.info(f"Item with ID {item_id} deleted")
    return {"message": f"Item with ID {item_id} has been deleted"}


@app.get("/items/{item_id}") # GET endpoint for retrieving an item by its ID
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
