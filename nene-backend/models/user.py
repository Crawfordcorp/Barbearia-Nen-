
from werkzeug.security import generate_password_hash, check_password_hash
from db import users_collection

def create_user(name, email, password):
    if users_collection.find_one({"email": email}):
        return {"error": "Usuário já existe"}

    hashed_password = generate_password_hash(password)
    user = {"name": name, "email": email, "password": hashed_password}
    users_collection.insert_one(user)
    return {"message": "Usuário criado com sucesso"}

def login_user(email, password):
    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return {"error": "Credenciais inválidas"}
    return {"message": "Login realizado com sucesso", "user_id": str(user["_id"])}
