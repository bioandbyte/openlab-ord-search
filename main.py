
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OpenLab ORD Search API",
    description="External reaction database service for OpenLab"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "service": "OpenLab ORD Search",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "success": True,
        "service": "ORD search backend",
        "status": "ready"
    }

@app.post("/search")
def search_reactions(payload: dict):
    reactants = payload.get("reactants", [])

    if not isinstance(reactants, list) or not reactants:
        return {
            "success": False,
            "error": "Please provide reactants."
        }

    return {
        "success": True,
        "external_results": [],
        "external_status": "ORD search index not configured yet",
        "message": "Backend is running; ORD index setup is still required."
    }
