import os
import time
import random
import hashlib
import requests
from time import sleep
from bs4 import BeautifulSoup

# Definisanje tema
themes = {
    'light': {
        'background': '\033[47m',  # Bela pozadina
        'text': '\033[30m',         # Crni tekst
    },
    'dark': {
        'background': '\033[40m',  # Crna pozadina
        'text': '\033[37m',         # Beli tekst
    },
    'blue': {
        'background': '\033[44m',  # Plava pozadina
        'text': '\033[37m',         # Beli tekst
    },
    'green': {
        'background': '\033[42m',  # Zelena pozadina
        'text': '\033[30m',         # Crni tekst
    },
    'red': {
        'background': '\033[41m',  # Crvena pozadina
        'text': '\033[37m',         # Beli tekst
    },
    'yellow': {
        'background': '\033[43m',  # Žuta pozadina
        'text': '\033[30m',         # Crni tekst
    },
    'magenta': {
        'background': '\033[45m',  # Magenta pozadina
        'text': '\033[37m',         # Beli tekst
    },
    'cyan': {
        'background': '\033[46m',  # Cijan pozadina
        'text': '\033[30m',         # Crni tekst
    },
    'orange': {
        'background': '\033[48;5;214m',  # Narandžasta pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'pink': {
        'background': '\033[48;5;213m',  # Roze pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'purple': {
        'background': '\033[48;5;55m',   # Ljubičasta pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'brown': {
        'background': '\033[48;5;94m',   # Braon pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'light blue': {
        'background': '\033[48;5;117m',  # Svetlo plava pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'dark green': {
        'background': '\033[48;5;22m',   # Tamno zelena pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'light green': {
        'background': '\033[48;5;118m',  # Svetlo zelena pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'dark blue': {
        'background': '\033[48;5;24m',   # Tamno plava pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'light gray': {
        'background': '\033[48;5;250m',  # Svetlo siva pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'dark gray': {
        'background': '\033[48;5;236m',  # Tamno siva pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'gold': {
        'background': '\033[48;5;220m',  # Zlatna pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'silver': {
        'background': '\033[48;5;7m',    # Srebrna pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'navy': {
        'background': '\033[48;5;17m',   # Mornarska plava pozadina
        'text': '\033[37m',               # Beli tekst
    },
    ' teal': {
        'background': '\033[48;5;30m',   # Teal pozadina
        'text': '\033[37m',               # Beli tekst
    },
    'lavender': {
        'background': '\033[48;5;189m',  # Lavanda pozadina
        'text': '\033[30m',               # Crni tekst
    },
    'peach': {
        'background': '\033[48;5;214m',  # Breskva pozadina
        'text': '\033[30m',               # Crni tekst
    },
}

tasks = []
INSTALLATION_FILE = "installation_complete.txt"
USERS_FILE = "users.txt"




# Globalna lista za čuvanje naziva programa
saved_files = []

def programiranje():
    program_code = ""
    print("\n--- Dobrodošli u mod za programiranje ---")
    while True:
        print("\n1. Napiši novi program")
        print("2. Sačuvaj program")
        print("3. Prikaži dostupne programe")
        print("4. Pokreni program")
        print("5. Izmeni postojeći program")
        print("6. Izlaz iz programiranja")

        izbor = input("Izaberite opciju: ")

        if izbor == "1":
            program_code = write_code()
        elif izbor == "2":
            file_name = save_program(program_code)
            if file_name:
                saved_files.append(file_name)
        elif izbor == "3":
            show_files()
        elif izbor == "4":
            run_selected_program()
        elif izbor == "5":
            program_code = edit_selected_program()
        elif izbor == "6":
            print("Izlaz iz modula za programiranje...")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo!")

def write_code():
    print("\n--- Napišite svoj program (unesite 'KRAJ' da završite) ---")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "KRAJ":
            break
        code_lines.append(line)
    print("Program je napisan.")
    return "\n".join(code_lines)

def save_program(program_code):
    if not program_code:
        print("Nema koda za čuvanje!")
        return None
    file_name = input("Unesite ime fajla (bez ekstenzije): ") + ".py"
    with open(file_name, "w") as f:
        f.write(program_code)
    print(f"Program je uspešno sačuvan kao {file_name}")
    return file_name

def show_files():
    if not saved_files:
        print("\nNema sačuvanih programa.")
        return
    print("\n--- Lista sačuvanih programa ---")
    for idx, file_name in enumerate(saved_files, start=1):
        print(f"{idx}. {file_name}")

def run_selected_program():
    if not saved_files:
        print("\nNema programa za pokretanje.")
        return
    show_files()
    izbor = input("Izaberite broj programa koji želite da pokrenete: ")
    try:
        izbor_idx = int(izbor) - 1
        if 0 <= izbor_idx < len(saved_files):
            file_name = saved_files[izbor_idx]
            if os.path.exists(file_name):
                print(f"\n--- Pokretanje programa {file_name} ---")
                os.system(f"python {file_name}")
                print("--- Izvršavanje završeno ---")
            else:
                print("Fajl ne postoji!")
        else:
            print("Pogrešan broj!")
    except ValueError:
        print("Morate uneti broj!")

def edit_selected_program():
    if not saved_files:
        print("\nNema programa za izmenu.")
        return ""
    show_files()
    izbor = input("Izaberite broj programa koji želite da izmenite: ")
    try:
        izbor_idx = int(izbor) - 1
        if 0 <= izbor_idx < len(saved_files):
            file_name = saved_files[izbor_idx]
            if os.path.exists(file_name):
                print(f"\n--- Trenutni sadržaj fajla {file_name} ---")
                with open(file_name, "r") as f:
                    existing_code = f.read()
                print(existing_code)
                print("\n--- Unesite novi kod za fajl (unesite 'KRAJ' da završite) ---")
                code_lines = []
                while True:
                    line = input()
                    if line.strip().upper() == "KRAJ":
                        break
                    code_lines.append(line)
                new_code = "\n".join(code_lines)
                with open(file_name, "w") as f:
                    f.write(new_code)
                print(f"Program {file_name} je uspešno izmenjen.")
                return new_code
            else:
                print("Fajl ne postoji!")
        else:
            print("Pogrešan broj!")
    except ValueError:
        print("Morate uneti broj!")
    return ""

        
def šta_je_novo():
        clear_screen()
        print("Šta je novo u RUBY os X edition")
        print("1.dodat je ruby DOS i morate da pokrenete poseban fajld(boot.sys) da bi ste ušli u sistem")
        print("2.Optimizovali smo sistem maximalno")
        print("3.Popravljeni su dosta bagova")
        print("4.dodata je opcija informacije sistema")
        print("5.svaki put kada pokrenete sistem dobićete BIOS ekran sa informacijama")
        print("6.dodata je aplikacija za programiranje")
        
def sys_info():
        clear_screen()
        print("OS = RUBY OS")
        print("MEMORY = 128GB")
        print("user = localhost$079")
        print("sys boot = boot.sys")
        print("sys asm = run.asm")
        print("BIOS file = bios.dll")
        print("creator = Ognjen Đokić")
        
def bios_loading():
        clear_screen()
        print("==============")
        print("      BAD BIOS       ")
        print("==============")
        time.sleep(6)
        clear_screen()
        print("BAD BIOS")
        print("ver:1.7")
        print("mem:123MB")
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_installation():
    if not os.path.exists(INSTALLATION_FILE):
        print("Sistem nije instaliran. Pokrećem instalaciju...")
        install_system()
    else:
        print("Sistem proverava instalaciju.")
        time.sleep(6)
        print("Sistem je pronašao instalaciju na /storage/emulate/0/RUBY os/BOOT")
        time.sleep(2)
        clear_screen()

    # Dodajemo logiku za nastavak posle instalacije
    print("Pokretanje sistema...")
    bios_loading()

def splash_screen(theme):
    clear_screen()
    print(f"{theme['background']}{theme['text']}Dobro došli u RUBY OS!")
    print("======================")
    print("Učitavanje...")
    print("1.1.2")
    print("X edition")
    time.sleep(4)
    clear_screen()

def install_system():
    print("Započinjem instalaciju sistema...")
    # Simulacija koraka instalacije
    time.sleep(1)
    print("1. Priprema diska...")
    time.sleep(3)
    print("2. Kreiranje particija...")
    time.sleep(1)
    print("3. Formatiranje particija...")
    time.sleep(1)
    print("4. Instalacija osnovnog sistema...")
    time.sleep(12)
    print("5. Konfiguracija sistema...")
    time.sleep(1)
    print("6. Postavljanje korisnika...")
    time.sleep(1)
    print("7. Instalacija bootloader-a...")
    time.sleep(5)
    print("Povezivanje sa BIOSOM...")
    time.sleep(7)
    print("učitavanje kernela...")
    time.sleep(7)
    clear_screen()
    print("SETUP se pokreće")
    time.sleep(5)
    print("setup instalira fajldove")
    time.sleep(8)
    print("instaling SYS.dll")
    time.sleep(9)
    print("instaling EBOOT.py")
    time.sleep(3)
    print("instaling logs")
    time.sleep(7)
    print("instaling error logs")
    time.sleep(5)
    clear_screen()
    time.sleep(7)
    print("loading...")
    time.sleep(6)
    clear_screen()
    
    # Oznaka da je instalacija završena
    with open(INSTALLATION_FILE, 'w') as f:
        f.write("logs loding.")

    print("Instalacija je uspešno završena!")
    time.sleep(3)
    clear_screen()

def register_user():
    username = input("Unesite korisničko ime: ")
    password = input("Unesite lozinku: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open(USERS_FILE, 'a') as f:
        f.write(f"{username},{hashed_password}\n")
    
    print("Registracija je uspešna!")

def login_user():
    username = input("Unesite korisničko ime: ")
    password = input("Unesite lozinku: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        with open(USERS_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(',')
                if username == stored_username and hashed_password == stored_password:
                    print("Prijava je uspešna!")
                    return True
            print("Nevažeće korisničko ime ili lozinka.")
            return False
    except FileNotFoundError:
        print("Nema registrovanih korisnika.")
        return False

def login_or_register():
    while True:
        choice = input("Da li želite da se prijavite (p) ili registrujete (r)?: ").lower()
        if choice == 'r':
            register_user()
            break
        elif choice == 'p':
            if login_user():
                break
            else:
                print("Pokušajte ponovo.")
        else:
            print("Nevažeća opcija. Molimo unesite 'p' za prijavu ili 'r' za registraciju.")

def show_menu(theme):
    print(f"{theme['background']}{theme['text']}Izaberite opciju:")
    print("1. Prikaži datum i vreme")
    print("2. Prikaži fajlove u trenutnom direktorijumu")
    print("3. Kreiraj novi fajl")
    print("4. Pročitaj fajl")
    print("5. Kreiraj novu fasciklu")
    print("6. Prikaži fajlove u specifičnoj fascikli")
    print("7. Izbriši fajl ili fasciklu")
    print("8. Promeni temu")
    print("9. Očisti ekran")
    print("10. Igra: Pogodi broj")
    print("11. Kalkulator")
    print("12. Upravljanje zadacima")
    print("13. Web pretraživač")
    print("14.Informacije o sistemu")
    print("15.Šta je novo?")
    print("16.code mod")
    print("17. Izlaz")

def select_theme():
    clear_screen()  # Čisti ekran pre prikaza tema
    print("Izaberite temu:")
    for idx, theme_name in enumerate(themes.keys(), start=1):
        print(f"{idx}. {theme_name.capitalize()} tema")
    
    choice = input("Unesite vaš izbor (1-{}): ".format(len(themes)))
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(themes):
            return list(themes.values())[choice_index]
        else:
            print("Nevažeći izbor, podrazumevana tema je svetla.")
            return themes['light']
    except ValueError:
        print("Nevažeći unos, podrazumevana tema je svetla.")
        return themes['light']

def display_datetime():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Trenutni datum i vreme: {current_time}")

def list_files():
    files = os.listdir('.')
    print("Fajlovi u trenutnom direktorijumu:")
    for file in files:
        print(file)

def create_file():
    filename = input("Unesite ime novog fajla: ")
    with open(filename, 'w') as f:
        content = input("Unesite sadržaj fajla: ")
        f.write(content)
    print(f"Fajl '{filename}' je kreiran.")

def read_file():
    filename = input("Unesite ime fajla za čitanje: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Sadržaj fajla '{filename}':")
            print(content)
    except FileNotFoundError:
        print("Fajl nije pronađen.")

def create_directory():
    dirname = input("Unesite ime nove fascikle: ")
    try:
        os.makedirs(dirname)
        print(f"Fascikla '{dirname}' je kreirana.")
    except FileExistsError:
        print("Fascikla već postoji.")

def list_specific_directory():
    dirname = input("Unesite ime fascikle: ")
    try:
        files = os.listdir(dirname)
        print(f"Fajlovi u fascikli '{dirname}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Fascikla nije pronađena.")

def delete_file_or_directory():
    name = input("Unesite ime fajla ili fascikle za brisanje: ")
    try:
        if os.path.isfile(name):
            os.remove(name)
            print(f"Fajl '{name}' je obrisan.")
        elif os.path.isdir(name):
            os.rmdir(name)
            print(f"Fascikla '{name}' je obrisana.")
        else:
            print("Fajl ili fascikla ne postoji.")
    except Exception as e:
        print(f"Greška prilikom brisanja: {e}")

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Pogodi broj između 1 i 100!")
    while True:
        guess = int(input("Unesite vaš pogodak: "))
        attempts += 1
        if guess < number_to_guess:
            print("Previše malo!")
        elif guess > number_to_guess:
            print("Previše veliko!")
        else:
            print(f"Čestitam! Pogodili ste broj {number_to_guess} u {attempts} pokušaja.")
            break

def calculator():
    print("Kalkulator")
    num1 = float(input("Unesite prvi broj: "))
    operator = input("Unesite operator (+, -, *, /): ")
    num2 = float(input("Unesite drugi broj: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Nevažeći operator.")
        return
    
    print(f"Rezultat: {result}")

def manage_tasks():
    while True:
        print("Upravljanje zadacima:")
        print("1. Dodaj zadatak")
        print("2. Prikaži zadatke")
        print("3. Izbriši zadatak")
        print("4. Izlaz")
        choice = input("Izaberite opciju: ")
        
        if choice == '1':
            task = input("Unesite zadatak: ")
            tasks.append(task)
            print("Zadatak je dodat.")
        elif choice == '2':
            print("Zadaci:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '3':
            task_index = int(input("Unesite broj zadatka za brisanje: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Zadatak je obrisan.")
            else:
                print("Nevažeći broj zadatka.")
        elif choice == '4':
            break
        else:
            print("Nevažeća opcija.")

def web_browser():
    url = input("Unesite URL: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    except requests.exceptions.RequestException as e:
        print(f"Greška prilikom pristupa URL-u: {e}")
        

def main():
    bios_loading()
    check_installation()
    theme = select_theme()
    splash_screen(theme)
    login_or_register() 

    while True:
        show_menu(theme)
        choice = input("Izaberite opciju (1-17): ")
        
        if choice == '1':
            display_datetime()
        elif choice == '2':
            list_files()
        elif choice == '3':
            create_file()
        elif choice == '4':
            read_file()
        elif choice == '5':
            create_directory()
        elif choice == '6':
            list_specific_directory()
        elif choice == '7':
            delete_file_or_directory()
        elif choice == '8':
            theme = select_theme()
        elif choice == '9':
            clear_screen()
        elif choice == '10':
            guess_number_game()
        elif choice == '11':
            calculator()
        elif choice == '12':
            manage_tasks()
        elif choice == '13':
            web_browser()
        elif choice == '14':
             sys_info()
        elif choice == '15':
            šta_je_novo()
        elif choice == '16':
            programiranje()
        elif choice == '17':
            clear_screen()
            command_promt()
        else:
            print("Nevažeća opcija, pokušajte ponovo.")

if __name__ == "__main__":
    main()