from main import *

db = Database()
while True:
    print("Vítejte v informačním systému pojišťovny\n=========================================")
    choose = input("=========  Co potřebujete udělat? =======\n"
                   " 1) Pro přidání klienta zadejte 'add'\n"
                   " 2) Pro zobrazení všech klientů zadejte 'show'\n"
                   " 3) Pro vyhledávání vložte 'search'\n"
                   " 4) Pro odstranění klienta zadejte 'delete'\n"
                   " 5) Pro ukončení aplikace zadejte 'konec'\n=========================================\n")

    if choose == "add":
        db.add_client()
    elif choose == "show":
        db.show_all_clients()
    elif choose == "search":
        name = input("Zadejte křestní jméno\n")
        last_name = input("Zadejte příjmení:\n")
        db.find_by_name(name, last_name)
    elif choose == "delete":
        db.delete_client()
    elif choose == "konec":
        print("Ukončuje se aplikace")
        
        break
    else:
        print("Špatně zadaný příkaz. Zkuste to znovu prosím")
