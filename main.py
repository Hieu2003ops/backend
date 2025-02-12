from fastapi import FastAPI, Request
import uvicorn
from ai_agents.main import run_crewai_pipeline  # Giữ nguyên main.py
from dotenv import load_dotenv
import os

# Load environment variables từ file .env
load_dotenv()

# Khởi động FastAPI
app = FastAPI()

# 🔥 API GET để kiểm tra Backend đang chạy
@app.get("/")
def root():
    return {"message": "🚀 CrewAI Backend is running!"}

# 🔥 API GET để test API
@app.get("/test")
def test_api():
    return {"message": "✅ API is active!", "status": "success"}

# 🔥 API POST để nhận topic và chạy CrewAI
@app.post("/generate")
async def generate_content(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    if not topic:
        return {"error": "Topic is required"}
    
    # Call the CrewAI pipeline function and return the result
    result, file_path = run_crewai_pipeline(topic)
    return {"content": result, "markdown_file": file_path}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
