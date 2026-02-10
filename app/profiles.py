import json
from pathlib import Path

PROFILE_PATH = Path("/app/config/profiles.json")

def load_profiles():
    with PROFILE_PATH.open() as f:
        return json.load(f)

def save_profiles(data):
    with PROFILE_PATH.open("w") as f:
        json.dump(data, f, indent=2)