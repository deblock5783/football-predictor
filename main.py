from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class MatchInput(BaseModel):
    home_goals: int
    away_goals: int

@app.post("/predict")
def predict_score(data: MatchInput):
    if data.home_goals > data.away_goals:
        result = "Home Win"
    elif data.home_goals < data.away_goals:
        result = "Away Win"
    else:
        result = "Draw"
    return {"prediction": result}

@app.get("/")
def root():
    return {"message": "Football Predictor API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
