import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file
with open("q-vercel-python.json", "r") as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    """API endpoint to fetch marks of students by name."""
    marks = []
    for student in name:
        record = next((item for item in students_data if item["name"] == student), None)
        marks.append(record["marks"] if record else None)

    return {"marks": marks}
