import hashlib
from datetime import datetime

from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from Clases.Employee import Employee

uri = "mongodb+srv://boghtml:1234567890HTML@cluster0.prceocq.mongodb.net/auto_service?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['auto_service']

client.admin.command('ping')
print("Pinged your deployment. You successfully connected to MongoDB!")

from bson import ObjectId


def get_client_by_id(client_id):
    try:
        client = db.appointments.find_one({'_id': ObjectId(client_id)})
        return client
    except Exception as e:
        print(f"Error retrieving client: {e}")
        return None


def update_client_status(client_id, new_status):
    # Оновлення статусу клієнта в базі даних
    db.appointments.update_one(
        {"_id": ObjectId(client_id)},
        {"$set": {"status": new_status}}
    )


def update_client_viewed_status(client_id, viewed):
    result = db.appointments.update_one({'_id': ObjectId(client_id)}, {'$set': {'viewed': viewed}})
    # print(f"Updated {result.modified_count} records in the database.")


def get_unviewed_clients_count():
    count = db.appointments.count_documents({'viewed': False})
    return count


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
    clients_collection = db['appointments']
    all_clients = clients_collection.find()

    # Конвертація сьогоднішньої дати до формату dd-mm-yyyy для подальшого порівняння
    today = datetime.now()

    filtered_clients = []
    for client in all_clients:
        client_date_str = client.get('date', '01-01-1970')  # Значення за замовчуванням на випадок відсутності дати
        client_date = datetime.strptime(client_date_str, '%d-%m-%Y')

        if filter_option == "Майбутні" and client_date >= today:
            filtered_clients.append({
                '_id': client.get("_id", ''),
                'name': client.get('name', ''),
                'surname': client.get('surname', ''),
                'phone': client.get('phone', ''),
                'brand': client.get('brand', ''),
                'model': client.get('model', ''),
                'year': client.get('year', ''),
                'date': client_date_str,
                'comment': client.get('comment', ''),
                'viewed': client.get('viewed', False),
                'status': client.get('status', '')
            })
        elif filter_option == "Минулі" and client_date < today:
            filtered_clients.append({
                '_id': client.get("_id", ''),
                'name': client.get('name', ''),
                'surname': client.get('surname', ''),
                'phone': client.get('phone', ''),
                'brand': client.get('brand', ''),
                'model': client.get('model', ''),
                'year': client.get('year', ''),
                'date': client_date_str,
                'comment': client.get('comment', ''),
                'viewed': client.get('viewed', False),
                'status': client.get('status', '')
            })
        elif filter_option == "Усі":
            filtered_clients.append({
                '_id': client.get("_id", ''),
                'name': client.get('name', ''),
                'surname': client.get('surname', ''),
                'phone': client.get('phone', ''),
                'brand': client.get('brand', ''),
                'model': client.get('model', ''),
                'year': client.get('year', ''),
                'date': client_date_str,
                'comment': client.get('comment', ''),
                'viewed': client.get('viewed', False),
                'status': client.get('status', '')
            })

    return filtered_clients


def get_clients_by_phone(phone_number):
    try:
        # Використання регулярного виразу для пошуку всіх клієнтів, номер телефону яких містить заданий рядок
        regex_pattern = f".*{phone_number}.*"  # Не сувора відповідність, шукає будь-який текст, що містить 'phone_number'
        clients = list(db.appointments.find({"phone": {"$regex": regex_pattern}}))
        return clients
    except Exception as e:
        print(e)


def update_car_base(updated_car):
    try:
        filter_query = {'_id': updated_car._id}
        update_query = {
            '$set': {
                'brand': updated_car.brand,
                'model': updated_car.model,
                'year': updated_car.year
            }
        }
        db.cars.update_one(filter_query, update_query)
    except Exception as e:
        raise Exception(f"Error updating car in the database: {e}")


def update_employee_base(updated_employee):
    print("update_employee_base")
    try:
        filter_query = {'_id': updated_employee._id}
        update_query = {
            '$set': {
                'name': updated_employee.name,
                'position': updated_employee.position,
                'salary': updated_employee.salary
            }
        }
        db.employees.update_one(filter_query, update_query)
    except Exception as e:
        print(f"Error updating employee in the database: {e}")


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
            'date': client.get('date', ''),
            'comment': client.get('comment', ''),
            'viewed': client.get('viewed', False),
            'status': client.get('status', '')
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


def update_service_base(updated_service):
    try:
        filter_query = {'_id': updated_service._id}
        update_query = {
            '$set': {
                'name': updated_service.name,
                'price': updated_service.price
            }
        }
        db.services.update_one(filter_query, update_query)
    except Exception as e:
        print(f"Error updating service in the database: {e}")


def add_employee_status(employee_id, status):
    result = db.employee_status.insert_one({"employee_id": employee_id, "status": status})
    return result.inserted_id


def get_employee_id_by_name(name):
    employee = db.employees.find_one({"name": name})
    if employee:
        return employee["_id"]  # Повертаємо ID працівника
    return None


def get_employee_by_id(employee_id):
    employee_data = db.employees.find_one({"_id": employee_id})
    if employee_data:
        return Employee(employee_data['name'], employee_data['position'], employee_data['_id'])
    else:
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


def remove_car_base_event(car_id):
    try:
        db.cars.delete_one({'_id': ObjectId(car_id)})
        return True
    except Exception as e:
        print(f"Error deleting car: {e}")
        return False


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
