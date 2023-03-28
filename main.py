class Client:
    def __init__(self, name, last_name, phone_number, age):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

franta = Client("Franta", "Vomáčka", "222 222 222", 29)
pepa = Client("Pepa", "Zdepa", "321 987 654", 30)
class Database:
    def __init__(self):
        self.clients = [franta, pepa]


    def create_client(self, name, last_name, phone_number, age):
        client = Client(name, last_name, phone_number, age)
        self.clients.append(client)
        print(f"Vytvořen klient {name} {last_name}, Telefonní číslo: {phone_number} ve věku {age} let")


    def add_client(self):
        name = input("Zadejte prosím křestní jméno klienta:\n")
        last_name = input("Zadejte prosím příjmení klienta:\n")
        phone_number = input("Zadejte telefonní číslo klienta:\n")
        age = input("Vložte věk klienta")
        self.create_client(name, last_name, phone_number, age)

    def show_all_clients(self):
        if not self.clients:
            print("Nejsou uloženy žadní klienti.")
        else:
            for client in self.clients:
                print(f"{client.name} {client.last_name}, {client.phone_number}, {client.age} let ")



    def find_by_name(self, name, last_name):
        found_clients = []
        for client in self.clients:
            if client.name == name:
                if client.last_name == last_name:
                    found_clients.append(client)


        if found_clients:
            print(f"Nalezeno {len(found_clients)} se jménem {name} {last_name}:")
            for client in found_clients:
                print(f"{client.name} {client.last_name}, {client.phone_number}, {client.age}")

        else:
            print(f"Nenalezen klient se jménem {name} {last_name}.")

    def delete_client(self):
        name = input("Zadejte jméno, které si přejete odstranit.")
        last_name = input("Zadejte příjmení, které si přejete odstanit")
        found_client = False
        for client in self.clients:
            if client.name == name:
                if client.last_name == last_name:
                    self.clients.remove(client)
                    print(f"Klient {client.name} {client.last_name} byl odstraněn")
                    found_client = True


        if not found_client:
            print(f"Klient jménem {name} {last_name} nebyl nalezen")



