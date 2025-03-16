import random

kahoot = [
    {
        "question": "Welche Faustregel gilt für Schrift?",
        "options": ["Serifenschriften für Print, Sans-Serif für Bildschirm", "Serifenschriften für Bildschirm, Sans-Serif für Print", "Serifenschriften für Print, Sans-Serif für Bildschirm", "Serifenschriften für Bildschirm, Sans-Serif für Bildschirm"],
        "correct_answer": "Serifenschriften für Print, Sans-Serif für Bildschirm"
    },
    {
        "question": "Wie oft sollte die ID 'bild' auf einer Website verwendet werden?",
        "options": ["so oft wie es Bilder gibt", "beliebig oft", "id ist ungültig", "einmal"],
        "correct_answer": "einmal"
    },
    {
        "question": "Was muss die Vagrantbox auf jeden Fall haben, damit eine PHP-Seite im Browser angezeigt werden kann?",
        "options": ["eine Datenbank", "ein Bash-Script", "Ajax", "einen Webserver"],
        "correct_answer": "einen Webserver"
    },
    {
        "question": "Wie viele Adressen hat IPv6?",
        "options": ["16 Millionen", "4 Milliarden", "340 Sextillionen", "1 Trillion"],
        "correct_answer": "340 Sextillionen"
    },
    {
        "question": "Wofür steht die Abkürzung LEMP?",
        "options": ["Für die Lampen...", "Für Linux, Nginx, MySQL, PHP", "Für Linux, Engine, Netjano, Python", "Für Linux, Epsche, MySQL, PHP"],
        "correct_answer": "Für Linux, Nginx, MySQL, PHP"
    },
    {
        "question": "Warum gibt es kein Feld 'Fragment Offset' im IPv6-Base-Header?",
        "options": ["Bei IPv6 dürfen nur die Router die Pakete fragmentieren", "Bei IPv6 wird direkt übertragen, Punkt zu Punkt", "Bei IPv6 wird die Datagramm-Länge gleich der Pfad-MTU gesetzt, Ende zu Ende", "Bei IPv6 ist alles anders"],
        "correct_answer": "Bei IPv6 dürfen nur die Router die Pakete fragmentieren"
    },
    {
        "question": "Was ist ein gültiger IPv6 Scope?",
        "options": ["Global scope", "Link-local scope"],
        "correct_answer": "Global scope"
    },
    {
        "question": "Auf welcher Schicht liegt nach dem TCP/IP-Modell das IP-Protokoll?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "3"
    },
    {
        "question": "Was wird auf der Website bei Ausführung des folgenden Codes angezeigt?",
        "code": """
        var eingabe1 = 10;
        var eingabe2 = 14;
        var ergabe1a = eingabe1 + eingabe2;
        document.write(ergabe1a);
        """,
        "options": ["Es wird ein Error auf der Webseite angezeigt.", "Es kommt zum Laufzeitfehler und es wird nichts auf der Website angezeigt.", "Der JavaScript-Code kann erst gar nicht kompiliert werden.", "24"],
        "correct_answer": "24"
    },
    {
        "question": "Wofür steht die Abkürzung SQL?",
        "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language"],
        "correct_answer": "Structured Query Language"
    },
    {
        "question": "Wie wird eine Datenbankverbindung in PHP hergestellt?",
        "options": ["Mit der 'pdo_connect' Funktion", "Mit der 'sqlite3_connect' Funktion", "Mit der 'mysqli_connect' Funktion", "Mit der 'mysql_connect' Funktion"],
        "correct_answer": "Mit der 'mysqli_connect' Funktion"
    },
    {
        "question": "Wie wird 'php Datenbankzugriff' richtig übersetzt?",
        "options": ["PHP database connection", "PHP database access", "PHP database management", "PHP database manipulation"],
        "correct_answer": "PHP database access"
    },
    {
        "question": "Was ist die korrekte Syntax für eine Schleife in PHP?",
        "options": ["for($i=0;$i<10;$i++)", "for(i=0;i<10)"],
        "correct_answer": "for($i=0;$i<10;$i++)"
    },
    {
        "question": "Mit welcher Funktion löscht man ein Element aus einem Array in PHP?",
        "options": ["erase()", "remove()", "delete()", "unset()"],
        "correct_answer": "unset()"
    },
    {
        "question": "Wie erzeugt man ein leeres Array in PHP?",
        "options": ["new Array()", "array()"],
        "correct_answer": "array()"
    },
    {
        "question": "Wie greift man auf das erste Element eines Arrays in PHP zu?",
        "options": ["$array[0]", "$array(0)"],
        "correct_answer": "$array[0]"
    },
    {
        "question": "Was bedeutet die Abkürzung MXT und auf welcher OSI-Schicht wird diese eingesetzt?",
        "options": ["Natural Address Transformation (OSI 2)", "Natural Address Translation (OSI 3)", "Natural Address Transpiration (OSI 4)", "Natural Address Turbo (OSI 1)"],
        "correct_answer": "Natural Address Translation (OSI 3)"
    },
    {
        "question": "Was bedeutet 'Ambient Intelligenze'?",
        "options": ["die ambitionierte Umgebung", "die Intelligenz der Ameisen", "die implizite Intelligenz", "die Intelligenz der Umgebung"],
        "correct_answer": "die Intelligenz der Umgebung"
    },
    {
        "question": "Um was für ein (php)-Array handelt es sich?",
        "options": ["associations", "Miscrillives", "preemptives", "incidences"],
        "correct_answer": "Miscrillives"
    },
    {
        "question": "Wie kann das DIV-Element <div class='willl'></div> in CSS angesprochen werden?",
        "options": [".willl", "#willl", '"willl"'],
        "correct_answer": ".willl"
    },
    {
        "question": "Wie oft sollte die ID 'hild' auf einer Website verwendet werden?",
        "options": ["so oft wie es Bilder gibt", "beliebig oft", "ist ungültig", "einmal"],
        "correct_answer": "einmal"
    },
    {
        "question": "Wie viele Bits können bei 192.168.2.2/TS theoretisch zur Bildung von Subnetzen verwendet werden?",
        "options": ["16", "8", "17", "19"],
        "correct_answer": "16"
    }
]


def abfragen(quiz_data):
    score = 0
    random.shuffle(quiz_data)  
    for i, question_data in enumerate(quiz_data):
        print(f"\nFrage {i + 1}: {question_data['question']}")
        if "code" in question_data:
            print(f"Code:\n{question_data['code']}")
        for j, option in enumerate(question_data['options']):
            print(f"{j + 1}. {option}")
        
        user_answer = input("Deine Antwort (Nummer): ")
        if question_data['options'][int(user_answer) - 1] == question_data['correct_answer']:
            print("Richtig! Yippiii!!")
            score += 1
        else:
            print(f"Falsch! =( - Die richtige Antwort ist: {question_data['correct_answer']}")
    
    print(f"\nQuiz beendet! Deine Punktzahl: {score}/{len(quiz_data)}")


if __name__ == "__main__":
    abfragen(kahoot)