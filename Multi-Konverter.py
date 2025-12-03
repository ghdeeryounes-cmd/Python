def unit_converter():
    while True:
        print("\n Multi-Konverter")
        print("1. Temperatur" )
        print("2. Währung (EUR to USD)")
        print("3. Gewicht")
        print("4. Beenden")
        
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            print("\n Temperatur-Konverter")
            temp = float(input("Temperatur: "))
            einheit = input("Von (C/F ): ").upper()
            
            if einheit == "C":
                fahrenheit = (temp * 9/5) + 32
                print(f" {temp}C = {fahrenheit:.1f}F")
            elif einheit == "F":
                celsius = (temp - 32) * 5/9
                print(f" {temp}F = {celsius:.1f}C")
                
        elif choice == "2":
            print("\n Währungs-Konverter")
            euro = float(input("Euro Betrag: "))
            usd = euro * 1.07  
            print(f" {euro}€ = {usd:.2f}$")
            
        elif choice == "3":
            print("\n Gewichts-Konverter")
            kg = float( input ("Kilogramm: "))
            pound = kg * 2.20462
            print(f" {kg} kg = {pound:.2f} lb")
            
        elif choice == "4":
            break

if __name__ == "__main__":
    unit_converter()