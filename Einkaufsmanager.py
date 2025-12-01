import json

def load_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_products(products):
    with open("products.json", "w") as f:
        json.dump(products, f, indent=2)

def shopping_manager():
    produkte = load_products()
    
    while True:
        print("\n Einkaufsmanager")
        print("1. Produkt hinzufügen")
        print("2. Produkte anzeigen")
        print("3. Gesamtpreis berechnen")
        print("4. Beenden")
        
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            name = input("Produktname: ")
            preis = float(input("Preis: "))
            menge = int(input("Menge: "))
            
            produkte.append({
                "name": name,
                "preis": preis,
                "menge": menge
            })
            save_products(produkte)
            print(" Produkt hinzugefügt!")
            
        elif choice == "2":
            if not produkte:
                print(" Keine Produkte vorhanden!")
            else:
                print("\n Deine Produkte:")
                for i, produkt in enumerate(produkte, 1):
                    gesamt = produkt['preis'] * produkt['menge']
                    print(f"{i}. {produkt['name']} - {produkt['preis']}€ x {produkt['menge']} = {gesamt}€")
                    
        elif choice == "3":
            total = sum(p['preis'] * p['menge'] for p in produkte)
            print(f" Gesamtpreis: {total}€")
            
        elif choice == "4":
            break

if __name__ == "__main__":
    shopping_manager()