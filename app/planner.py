def build_plan(tool, attack, pdf_path, letters=0, digits=0):
    if tool == "hashcat" and attack == "mask":
        mask = "?l" * letters + "?d" * digits
        return {
            "tool": "hashcat",
            "command": f"hashcat -a 3 <hash> \"{mask}\"",
            "pdf": pdf_path
        }

    if tool == "pdfrip":
        return {
            "tool": "pdfrip",
            "command": f"pdfrip -f \"{pdf_path}\" --{attack}",
            "pdf": pdf_path
        }

    return {"error": "Invalid plan"}