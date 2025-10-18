from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET for /me
    allow_headers=["*"],
)

# Constants with fallback values
CAT_FACT_URL = os.getenv("CAT_FACT_URL", "https://catfact.ninja/fact")
USER_EMAIL = os.getenv("EMAIL", "default.email@example.com")
USER_NAME = os.getenv("FULL_NAME", "Default Name")
USER_STACK = os.getenv("STACK", "Python/FastAPI")

@app.get("/me")
def get_profile():
    # Get current UTC timestamp in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    # Fetch cat fact with timeout and error handling
    try:
        response = requests.get(CAT_FACT_URL, timeout=5) # 5-second timeout to prevent hanging
        response.raise_for_status() # Raise exception for 4xx/5xx errors
        cat_fact = response.json().get("fact", "No fact available")
    except requests.RequestException as e:
        # Fallback message on failure
        cat_fact = "Unable to fetch cat fact at this time."
        # Log the error
        print(f"Error fetching cat fact: {str(e)}")
    
    # Construct response
    return {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }