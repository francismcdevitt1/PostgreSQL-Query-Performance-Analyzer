
from fastapi import FastAPI
from query_analyzer import analyze_query
from query_analyzer import get_query_history

app = FastAPI()

@app.post("/analyze")
def analyze(sql_query: str):

    return analyze_query(sql_query)

@app.get("/history")
def history():
    return get_query_history()