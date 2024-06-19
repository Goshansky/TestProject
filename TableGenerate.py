from faker import Faker
import random
from UserModule import User
from ClientModule import Client

fake = Faker('ru_RU')
client_manager = Client()
user_manager = User()


# Функция для генерации случайного пароля
def generate_password():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))


# Создаем 10 пользователей
a = []
for _ in range(10):
    full_name = fake.name()
    login = fake.user_name()
    password = generate_password()
    a.append(full_name)
    new_user = user_manager.create(full_name, login, password)

# Создаем 100 клиентов
for _ in range(100):
    number = random.randint(1000000, 9999999)
    if _ % 2:
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        middle_name = fake.middle_name_male()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        middle_name = fake.middle_name_female()

    birthday = fake.date_of_birth().strftime('%Y-%m-%d')
    client_inn = fake.ssn()[:10]
    responsible_full_name = random.choice(a)

    new_client = client_manager.create(number, last_name, first_name, middle_name, birthday, client_inn,
                                       responsible_full_name, 'Не в работе')
