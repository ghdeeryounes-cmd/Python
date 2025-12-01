import json

def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)

def banking_system():
    accounts = load_accounts()
    
    while True:
        print("\n Banking System")
        print("1. Konto erstellen")
        print("2. Einzahlen")
        print("3. Abheben")
        print("4. Kontostand")
        print("5. Beenden")
        
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            konto_nr = input("Kontonummer: ")
            if konto_nr not in accounts:
                accounts[konto_nr] = {"balance": 0, "transactions": []}
                save_accounts(accounts)
                print(" Konto erstellt!")
            else:
                print(" Konto existiert bereits!")
                
        elif choice == "2":
            konto_nr = input("Kontonummer: ")
            if konto_nr in accounts:
                betrag = float(input("Betrag: "))
                accounts[konto_nr]["balance"] += betrag
                accounts[konto_nr]["transactions"].append(f"Einzahlung: +{betrag}€")
                save_accounts(accounts)
                print(" Einzahlung erfolgreich!")
            else:
                print(" Konto nicht gefunden!")
                
        elif choice == "3":
            konto_nr = input("Kontonummer: ")
            if konto_nr in accounts:
                betrag = float(input("Betrag: "))
                if betrag <= accounts[konto_nr]["balance"]:
                    accounts[konto_nr]["balance"] -= betrag
                    accounts[konto_nr]["transactions"].append(f"Auszahlung: -{betrag}€")
                    save_accounts(accounts)
                    print(" Auszahlung erfolgreich!")
                else:
                    print(" Nicht genug Geld!")
            else:
                print(" Konto nicht gefunden!")
                
        elif choice == "4":
            konto_nr = input("Kontonummer: ")
            if konto_nr in accounts:
                print(f" Kontostand: {accounts[konto_nr]['balance']}€")
                print(" Letzte Transaktionen:")
                for trans in accounts[konto_nr]["transactions"][-5:]:
                    print(f"  {trans}")
            else:
                print(" Konto nicht gefunden!")
                
        elif choice == "5":
            break

if __name__ == "__main__":
    banking_system()