from pathlib import Path

def load_config():
    config = {}
    path = Path("/app/config/defaults.conf")
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            k, v = line.split("=", 1)
            config[k] = v
    return config