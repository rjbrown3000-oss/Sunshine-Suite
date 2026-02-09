def update_build_log(version, change):
    log_entry = {"id": version, "time": "2026-02-09", "desc": change}
    build_history.append(log_entry)
    return "Build History Updated Successfully."
