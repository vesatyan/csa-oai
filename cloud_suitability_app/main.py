
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from .utils.analysis import analyze_data
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/upload/")
async def upload_excel(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(contents)
    result_html, result_excel = analyze_data(df)
    return HTMLResponse(content=result_html, status_code=200)
