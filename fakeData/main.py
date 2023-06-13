from faker import Faker
import pandas as pd

fake = Faker(["pl_PL"])

name = []
surname= []
username = []
email = []
phone = []
job = []
indexList = []

for i in range(1,31):
    indexList.append(i)
    name.append(fake.first_name())
    surname.append(fake.last_name())
    username.append(fake.user_name())
    email.append(fake.email())
    phone.append(fake.phone_number())
    job.append(fake.job())


person = {
            "Index": indexList,
            'Imię': name,
            'Nazwisko': surname,
            'Nazwa Użytkownika': username,
            'Email': email,
            'Numer telefonu': phone,
            'Zawód': job
          }

df = pd.DataFrame(person)
df.to_csv('C:/Users/karol/PycharmProjects/finalWSB/fakeData/pracownicy.csv', encoding='UTF-8', index= False)
print (df)
