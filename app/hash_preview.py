def preview(file_path):
    # For demo: show first 4 bytes of PDF as hash-like string
    with open(file_path, "rb") as f:
        content = f.read(16)
    return content.hex()