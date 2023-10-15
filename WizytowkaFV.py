from faker import Faker

fake = Faker()

class ContactCard:
    def __init__(self, first_name, last_name, company_name, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.position = position
        self.email = email

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}, {self.position}, {self.email}")

class BaseContact(ContactCard):
    def __init__(self, first_name, last_name, company_name, position, email, phone_number):
        super().__init__(first_name, last_name, company_name, position, email)
        self.phone_number = phone_number

    def contact(self):
        super().contact()
        print(f"Wybieram numer prywatny {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

class BusinessContact(ContactCard):
    def __init__(self, first_name, last_name, company_name, position, email, phone_number, business_phone):
        super().__init__(first_name, last_name, company_name, position, email)
        self.phone_number = phone_number
        self.business_phone = business_phone

    def contact(self):
        super().contact()
        print(f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        company_name = fake.company()
        position = fake.job()
        email = fake.email()

        if contact_type == "BaseContact":
            phone_number = fake.phone_number()
            contact = BaseContact(first_name, last_name, company_name, position, email, phone_number)
        elif contact_type == "BusinessContact":
            phone_number = fake.phone_number()
            business_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, company_name, position, email, phone_number, business_phone)

        contacts.append(contact)

    return contacts

# Tworzenie 5 losowych wizytówek prywatnych
private_contacts = create_contacts("BaseContact", 5)

# Tworzenie 5 losowych wizytówek biznesowych
business_contacts = create_contacts("BusinessContact", 5)

# Wyświetlenie danych wizytówek
for contact in private_contacts + business_contacts:
    print(f"{contact.first_name} {contact.last_name} - {contact.email}")

# Kontaktowanie się z osobą
private_contacts[0].contact()
business_contacts[0].contact()

# Wyświetlenie długości etykiety
print(private_contacts[0].label_length)
print(business_contacts[0].label_length)
