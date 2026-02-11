import json

with open("config/profiles.json") as f:
    profiles = json.load(f)

def get_profile(name):
    return profiles.get(name)

def list_profiles():
    return list(profiles.keys())