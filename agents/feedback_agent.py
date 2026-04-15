def feedback(report):
    if report["anomaly"]:
        return {
            "status": "ALERT",
            "message": "Costs above market → review pricing or extraction"
        }

    return {
        "status": "OK",
        "message": "System operating normally"
    }