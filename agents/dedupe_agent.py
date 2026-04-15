from tools.db import Session, Shipment

def save_if_not_exists(data):
    session = Session()

    if not data or data.get("shipment_id") == "UNKNOWN":
        print("Skipping invalid record")
        return False

    exists = session.query(Shipment).filter_by(
        shipment_id=data["shipment_id"]
    ).first()

    if exists:
        print("Duplicate:", data["shipment_id"])
        return False

    shipment = Shipment(**data)
    session.add(shipment)
    session.commit()
    return True