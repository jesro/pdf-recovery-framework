def build_plan(profile, file_path):
    letters = profile["letters"]
    digits = profile["digits"]
    tool = profile["tool"]
    attack = profile["attack"]
    
    plan = {
        "tool": tool,
        "attack": attack,
        "letters": letters,
        "digits": digits,
        "file": file_path,
        "command_preview": f"{tool} -a {attack} -1 ?l?d -i {file_path} ?1"  # Example
    }
    return plan