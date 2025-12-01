import json

def load_questions():
    return [
        {
            "frage": "Was ist die Hauptstadt von Deutschland?",
            "optionen": ["A: Berlin", "B: München", "C: Hamburg"],
            "antwort": "A"
        },
        {
            "frage": "Welche Sprache wird in Brasilien gesprochen?",
            "optionen": ["A: Spanisch", "B: Portugiesisch", "C: Englisch"],
            "antwort": "B"
        },
        {
            "frage": "Wie viele Bits hat ein Byte?",
            "optionen": ["A: 4", "B: 8", "C: 16"],
            "antwort": "B"
        }
    ]

def quiz_game():
    fragen = load_questions()
    punkte = 0
    
    print(" Willkommen beim Quiz-Spiel!")
    
    for i, frage in enumerate(fragen, 1):
        print(f"\n Frage {i}: {frage['frage']}")
        for option in frage['optionen']:
            print(option)
        
        antwort = input("Deine Antwort (A/B/C): ").upper()
        
        if antwort == frage['antwort']:
            print(" Richtig!")
            punkte += 1
        else:
            print(f" Falsch! Richtige Antwort: {frage['antwort']}")
    
    print(f"\n Quiz beendet! Punkte: {punkte}/{len(fragen)}")

if __name__ == "__main__":
    quiz_game()