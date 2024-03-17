import hashlib
from datetime import datetime

from bson import ObjectId
from pymongo import collection

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://boghtml:1234567890HTML@cluster0.prceocq.mongodb.net/auto_service?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['auto_service']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def delete_client(client_id):
    try:
        result = db.appointments.delete_one({"_id": ObjectId(client_id)})
        if result.deleted_count > 0:
            print(f"Client with _id {client_id} has been deleted.")
            return True
        else:
            print(f"No client found with _id {client_id}.")
            return False
    except Exception as e:
        print(f"Error deleting client: {e}")
        return False


def get_clients1(filter_option):
    today = datetime.now().strftime('%Y-%m-%d')  # Сьогоднішня дата в строковому форматі
    query = {}
    if filter_option == "Майбутні":
        query = {"date": {"$gte": today}}
    elif filter_option == "Минулі":
        query = {"date": {"$lt": today}}

    clients_collection = db['appointments']
    clients_list = []
    for client in clients_collection.find(query):
        clients_list.append({
            '_id': client.get("_id", ''),
            'name': client.get('name', ''),
            'surname': client.get('surname', ''),
            'phone': client.get('phone', ''),
            'brand': client.get('brand', ''),
            'model': client.get('model', ''),
            'year': client.get('year', ''),
            'date': client.get('date', '')
        })
    return clients_list


def get_clients():
    clients_collection = db['appointments']
    clients_list = []
    for client in clients_collection.find():  # Тепер коректно викликаємо find на колекції
        clients_list.append({
            '_id': client.get("_id", ''),
            'name': client.get('name', ''),
            'surname': client.get('surname', ''),
            'phone': client.get('phone', ''),
            'brand': client.get('brand', ''),
            'model': client.get('model', ''),
            'year': client.get('year', ''),
            'date': client.get('date', '')
        })
    return clients_list


def add_car_base(car):
    result = db.cars.insert_one(car.__dict__)
    return result  # Повертаємо результат вставки


# Додавання працівника
def add_employee_base(employee):
    result = db.employees.insert_one(employee.__dict__)
    return result


# Додавання послуги
def add_service_base(service):
    result = db.services.insert_one(service.__dict__)
    return result


def add_employee_status(employee_id, status):
    result = db.employee_status.insert_one({"employee_id": employee_id, "status": status})
    return result.inserted_id


def get_employee_id_by_name(name):
    employee = db.employees.find_one({"name": name})
    if employee:
        return employee["_id"]  # Повертаємо ID працівника
    return None


def get_busy_employees_ids():
    busy_workers = db.employee_status.find({"status": "зайнятий"})
    return [worker["employee_id"] for worker in busy_workers]


def update_employee_status(employee_id, new_status):
    db.employee_status.update_one({"employee_id": employee_id}, {"$set": {"status": new_status}})


def add_order_base(order_dict):
    result = db.orders.insert_one(order_dict)
    return result.inserted_id


def add_user_base(username, password):
    # Хешування пароля перед збереженням
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    user_data = {
        "username": username,
        "password": hashed_password
    }
    result = db.users.insert_one(user_data)
    return result.inserted_id


def remove_service_base(service_id):
    db.services.delete_one({'_id': service_id})


def remove_car_base(car_id):
    print(car_id)
    db.cars.delete_one({'_id': ObjectId(car_id)})


def remove_order_base(order_id):
    db.orders.delete_one({'_id': ObjectId(order_id)})


def remove_employees_base(employee_id):
    print(employee_id)
    db.employees.delete_one({'_id': ObjectId(employee_id)})


def get_services_base():
    return list(db.services.find())


def get_orders_base():
    return list(db.orders.find())


# Отримання всіх автомобілів
def get_cars_base():
    return list(db.cars.find())


# Отримання всіх працівників
def get_employees_base():
    return list(db.employees.find())


def update_car_base(car_id, updated_car):
    db.cars.update_one({'_id': car_id}, {'$set': updated_car.__dict__})


def get_free_employees():
    # Отримуємо ідентифікатори зайнятих працівників
    busy_ids = get_busy_employees_ids()
    # Знаходимо тільки тих працівників, які не знаходяться в списку зайнятих
    free_employees = db.employees.find({"_id": {"$nin": busy_ids}})
    return list(free_employees)


def get_busy_employees():
    # Використовуємо функцію get_busy_employees_ids() для отримання ідентифікаторів зайнятих працівників
    busy_ids = get_busy_employees_ids()
    # Знаходимо працівників за цими ідентифікаторами
    busy_employees = db.employees.find({"_id": {"$in": busy_ids}})
    return list(busy_employees)


def set_worker_free(employee_id):
    # Встановлюємо статус працівника на "вільний", видаляючи його запис із таблиці статусів
    db.employee_status.delete_one({"employee_id": employee_id})


def is_username_available(username):
    users_collection = db['users']
    return users_collection.find_one({"username": username}) is None


def check_user_credentials(username, hashed_password):
    # Пошук користувача з заданим ім'ям користувача в базі даних
    user = db.users.find_one({'username': username})
    if user and 'password' in user:
        # Порівняння збереженого хешу пароля з хешем введеного пароля
        return user['password'] == hashed_password
    return False
