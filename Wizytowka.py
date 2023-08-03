from faker import Faker

fake = Faker()

class VisitCard:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.email}"
    
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname}, {self.position}, e-mail: {self.email}")

    @property
    def full_name_length(self):
        return len(self.name) + len(self.surname) + 1  # +1 for the space between names


name1, surname1 = fake.first_name(), fake.last_name()
name2, surname2 = fake.first_name(), fake.last_name()
name3, surname3 = fake.first_name(), fake.last_name()

Karina = VisitCard(name=name1, surname=surname1, company=fake.company(), position=fake.job(), email=fake.email())
Mariusz = VisitCard(name=name2, surname=surname2, company=fake.company(), position=fake.job(), email=fake.email())
Kasia = VisitCard(name=name3, surname=surname3, company=fake.company(), position=fake.job(), email=fake.email())

visit_cards = [Karina, Mariusz, Kasia]

for card in visit_cards:
    card.contact()

by_name = sorted(visit_cards, key=lambda card: card.name)
by_surname = sorted(visit_cards, key=lambda card: card.surname)
by_email = sorted(visit_cards, key=lambda card: card.email)

print("Sortowanie według imienia:")
print(by_name)

print("Sortowanie według nazwiska:")
print(by_surname)

print("Sortowanie według adresu e-mail:")
print(by_email)
