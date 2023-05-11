import csv
import uuid
from datetime import datetime, time

from faker import Faker

fake = Faker("pt_BR")

products = [
    {"product": "shampoo para carros", "unit_price": 29.90},
    {"product": "limpa-vidros automotivo", "unit_price": 19.90},
    {"product": "cera automotiva", "unit_price": 39.90},
    {"product": "limpa-rodas", "unit_price": 24.90},
    {"product": "condicionador de couro automotivo", "unit_price": 49.90},
    {"product": "desodorizador de ar automotivo", "unit_price": 14.90},
    {"product": "removedor de insetos", "unit_price": 19.90},
    {"product": "limpa-tapetes automotivo", "unit_price": 34.90},
    {"product": "polidor de metais automotivo", "unit_price": 39.90},
    {"product": "limpa-estofados automotivo", "unit_price": 49.90},
]

states = ["paraná", "santa catarina", "rio grande do sul"]


class Row:
    def __init__(self):
        product = self.get_product()

        self.id = str(uuid.uuid4())
        self.date_time = self.get_date()
        self.state = self.get_state()
        self.quantity = fake.random_int(min=1, max=100)
        self.product = product["product"]
        self.unit_price = product["unit_price"]
        self.total_price = self.quantity * self.unit_price

    def get_date(self):
        date_start = datetime(2023, 1, 1)
        date_end = datetime(2023, 4, 30)

        date_time = fake.date_between_dates(date_start=date_start, date_end=date_end)
        # Gerando um horário aleatório
        random_time = time(
            hour=fake.random_int(min=0, max=23),
            minute=fake.random_int(min=0, max=59),
            second=fake.random_int(min=0, max=59),
        )

        # Combinando a data e hora aleatórias
        date_time = datetime.combine(date_time, random_time)

        # Formatando a data e hora no formato desejado
        formatted_date = date_time.strftime("%m/%d/%Y %H:%M:%S")

        return formatted_date

    def get_product(self):
        index = fake.random_int(min=0, max=9)
        return products[index]

    def get_state(self):
        index = fake.random_int(min=0, max=2)
        return states[index]


rows = [Row() for i in range(1000)]


with open("./data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["id", "date_time", "state", "quantity", "product", "unit_price", "total_price"]
    )
    for row in rows:
        writer.writerow(
            [
                row.id,
                row.date_time,
                row.state,
                row.quantity,
                row.product,
                round(row.unit_price, 2),
                round(row.total_price, 2),
            ]
        )
