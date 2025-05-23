from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Placeholder for future database connection
# Example:
# import psycopg2
# conn = psycopg2.connect(os.getenv('DATABASE_URL'))
# (Database connection logic will be added here)

@app.get("/")
def read_root():
    return {"message": "Vocalize Backend - Alive!"}

@app.get("/api/gemini-test")
def gemini_test():
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        # Placeholder for Gemini API integration
        return {"message": "AI processing initiated with Gemini key..."}
    else:
        return JSONResponse(status_code=500, content={"error": "GEMINI_API_KEY not found in environment variables."})

# Future features:
# - Add database models and connection logic
# - Integrate Google Gemini Generative API
# - Implement expense tracking endpoints 