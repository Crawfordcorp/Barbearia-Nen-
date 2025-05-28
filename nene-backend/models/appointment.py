
from db import appointments_collection

def create_appointment(user_id, barber, service, date, price):
    appointment = {
        "user_id": user_id,
        "barber": barber,
        "service": service,
        "date": date,
        "price": price
    }
    appointments_collection.insert_one(appointment)
    return {"message": "Agendamento confirmado"}

def list_appointments():
    return list(appointments_collection.find({}, {"_id": 0}))
