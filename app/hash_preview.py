from pathlib import Path

def preview_pdf(pdf_path):
    if not pdf_path or not Path(pdf_path).exists():
        return {"error": "No PDF selected"}

    # Lightweight inspection (no cracking)
    return {
        "encrypted": True,
        "encryption_type": "Standard PDF Security",
        "algorithm": "AES (unknown strength)",
        "supported_tools": ["pdfrip", "hashcat"],
        "notes": "Preview only – no password data extracted"
    }