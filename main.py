from fastapi import FastAPI
from models.models import chat_with_bots
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=['GET', 'POST'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Item(BaseModel):
    text: str
    model_name: str


@app.post("/text")
async def input_text(item: Item):
    bot_ans = chat_with_bots(item.text, model_name=item.model_name)
    return {
        "message": bot_ans
    }
