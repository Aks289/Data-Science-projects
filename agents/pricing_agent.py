from tools.db import Session, Shipment

def compute_avg_cost():
    session = Session()
    data = session.query(Shipment).all()

    if not data:
        return 0

    return sum(d.cost for d in data) / len(data)