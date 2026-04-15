def generate_report(avg_cost, market_data):
    anomaly = avg_cost > market_data["rate"]

    return {
        "avg_cost": avg_cost,
        "market_rate": market_data["rate"],
        "anomaly": anomaly
    }