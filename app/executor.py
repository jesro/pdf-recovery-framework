def execute(plan, enabled):
    if not enabled:
        return "Execution disabled (safe mode)."
    return "Execution would happen here."