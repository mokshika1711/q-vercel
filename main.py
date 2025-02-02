from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Load the dataset (Assuming CSV format with columns "name" and "marks")
df = pd.read_csv("students_marks.csv")  

app = FastAPI()

# Enable CORS (Allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    """API endpoint to fetch marks of students by name."""
    marks = []
    for student in name:
        row = df[df["name"] == student]
        marks.append(int(row["marks"].values[0]) if not row.empty else None)
    
    return {"marks": marks}
