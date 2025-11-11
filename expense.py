from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    title:str
    amount:float
    category:str

expenses:List[Expense]=[]

@app.post("/expenses", response_model=Expense)
async def add_expense(expense:Expense):
    expenses.append(expense)
    return expense

@app.get("/expenses", response_model=List[Expense])
async def get_all_expenses():
    return expenses

@app.get("/expenses/highest", response_model=Expense)
async def get_highest_expense():
    if not expenses:
        raise HTTPException(status_code=404, detail="No expense found")
    highest=max(expenses, key = lambda x: x.amount)
    return highest
