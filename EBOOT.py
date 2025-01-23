import os
from datetime import timedelta
import time
import random
import hashlib
import requests
import sys
import platform
import webbrowser
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

tasks = [
"kernel"
"network"
"system"
"servers"
"installation"
]
ROOT_FILE = "root/root.dat"
root_status = False
INSTALLATION_FILE = "installation_complete.sys"
USERS_FILE = "users.dat"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Trenutni direktorijum gde se nalazi skripta
sysfiles = os.path.join(BASE_DIR, "kernel", "hal.dll")

def neofetch():
    # Ispravan ASCII logo za RUBYOS
    ascii_logo = """
____  _   _ ______   _____  ____
|  _ \| | | | __ ) \ / / _ \/ ___|
| |_) | | | |  _ \ V / | | \___ \ 
|  _ <| |_| | |_) || || |_| |___) |
|_| \_\\___/|____/ |_| \___/|____/
    """

    # Sistem informacije
    os_name = platform.system() + " " + platform.release()
    kernel = platform.version()
    try:
        uptime_seconds = int(os.times().elapsed)
        uptime = str(timedelta(seconds=uptime_seconds))
    except Exception:
        uptime = "N/A"
    memory_usage = "N/A (Not Supported)"
    cpu = platform.processor() or "Unknown CPU"
    user = os.environ.get("USER", "Unknown User")
    shell = os.environ.get("SHELL", "Unknown Shell")

    # Prikaz informacija
    print(ascii_logo)
    print(f"User:          {user}")
    print(f"OS:            {os_name}")
    print(f"Kernel:        {kernel}")
    print(f"Uptime:        {uptime}")
    print(f"Memory Usage:  {memory_usage}")
    print(f"CPU:           {cpu}")
    print(f"Shell:         {shell}")

def terminal():
    global root_status
    print("RUBY terminal")
    print("Type 'help' for a list of commands.")
    
    while True:
        choice = input(">> ").strip().lower()
        
        if choice == "help":
            print("""
Available commands:
- help       : Display this help message.
- exit       : Exit the terminal.
- clear      : Clear the screen.
- date       : Show the current date and time.
- echo [msg] : Repeat the entered message.
- calc       : Simple calculator.
- ls         : List files in the current directory.
- about      : Information about Ruby OS.
-web      :explore the web!
- mkdir [name]: Create a new directory.
- rmdir [name]: Remove an existing directory.
- touch [name]: Create a new file.
- rm [name]  : Remove a file.
- read [name]: Read and display a file's content.
- write [name]: Write content to a file.
- sysinfo    : Display system information.
- reboot     : Simulate a system reboot.
""")
        
        elif choice == "exit":
            print("Exiting RUBY terminal...")
            break
            
        elif choice == "ruby update":
            print("Reading database...")
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Ostanite na istoj liniji
                time.sleep(1)
                print()
                
            
        elif choice == "apt install pac":
            main_menu()
            
        elif choice == 'sudo root':
            root_system()          
        
        elif choice == "clear":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif choice == "date":
            from datetime import datetime
            print("Current date and time:", datetime.now())
        
        elif choice.startswith("echo "):
            print(choice[5:])
            
        elif choice == 'neofetch':
            neofetch()
        
        elif choice == "calc":
            try:
                expression = input("Enter calculation: ")
                result = eval(expression)
                print("Result:", result)
            except Exception as e:
                print("Error in calculation:", e)
                
        elif choice == 'web':
            web()
        
        elif choice == "ls":
            import os
            files = os.listdir(".")
            print("Files in current directory:")
            for f in files:
                print(f)
        
        elif choice.startswith("mkdir "):
            import os
            dir_name = choice[6:]
            try:
                os.mkdir(dir_name)
                print(f"Directory '{dir_name}' created.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("rmdir "):
            import os
            dir_name = choice[6:]
            try:
                os.rmdir(dir_name)
                print(f"Directory '{dir_name}' removed.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("touch "):
            file_name = choice[6:]
            try:
                with open(file_name, "w") as f:
                    pass
                print(f"File '{file_name}' created.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("rm "):
            import os
            file_name = choice[3:]
            try:
                os.remove(file_name)
                print(f"File '{file_name}' removed.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("read "):
            file_name = choice[5:]
            try:
                with open(file_name, "r") as f:
                    print(f.read())
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("write "):
            file_name = choice[6:]
            try:
                content = input("Enter content to write: ")
                with open(file_name, "w") as f:
                    f.write(content)
                print(f"Content written to '{file_name}'.")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == "konami":
            konami_easter_egg()
        
        elif choice == "about":
            print("Ruby OS - A custom operating system project made with love.")
        
        elif choice == "sysinfo":
            import platform
            print(f"System: {platform.system()}")
            print(f"Version: {platform.version()}")
            print(f"Release: {platform.release()}")
            print(f"Machine: {platform.machine()}")
        
        elif choice == "reboot":
            print("Rebooting system...")
            loading_kernel()
            
        elif choice == "sudo -root -h":
            if root_status:
                print("""
Root-specific commands:
- sudo config [key] [value]: Modify root configurations.
- sudo users: List all users with root access.
- sudo shutdown: shutting down the system.
- sudo reboot: rebooting with root permissions.
- sudo logs: Display system logs.
""")
            else:
                print("Access denied. You are not a root user.")

        elif choice.startswith("sudo "):
            if not root_status:
                print("Access denied. You are not a root user.")
            else:
                command = choice[5:]
                if command.startswith("config "):
                    parts = command.split(" ", 2)
                    if len(parts) == 3:
                        key, value = parts[1], parts[2]
                        print(f"Configuration '{key}' updated to '{value}'.")
                    else:
                        print("Usage: root config [key] [value]")
                elif command == "users":
                    print("Listing root users: [admin, root_user]")  # Primer
                elif command == "shutdown":
                    print("System is shutting down...")
                    break
                elif command == "reboot":
                    print("System is rebooting with root permissions...")
                    loading_kernel()
                elif command == "logs":
                    print("script start:/start /hf /ruby /ebby64 /ruby os is starting echo {command}")
                else:
                    print("Unknown root command. Type '--root -help' for a list of commands.")
        
        else:
            print("Unknown command. Type 'help' for a list of commands.")
            
 # Na početku programa definišite:
  # Početno stanje: korisnik nije root

# Definišite putanju do fajla za čuvanje statusa
ROOT_STATUS_FILE = "root_status.txt"

def save_root_status(status):
    with open(ROOT_STATUS_FILE, 'w') as f:
        f.write(str(status))  # Sačuvaj True ili False u fajl

def load_root_status():
    try:
        with open(ROOT_STATUS_FILE, 'r') as f:
            return f.read().strip() == 'True'  # Učitaj True/False iz fajla
    except FileNotFoundError:
        return False  # Ako fajl ne postoji, podrazumevamo da korisnik nije root

# Na početku programa učitajte root status
root_status = load_root_status()

def root_system():
    global root_status  # Koristimo globalnu promenljivu za root_status
    
    # Unos korisničkog imena i lozinke
    username = input("[SUDO] Unesite korisničko ime: ")
    password = input("[SUDO] Unesite lozinku: ")

    # Hashiranje lozinke za poređenje
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Otvorimo datoteku sa korisnicima i proveravamo da li postoji uneseni korisnik
        with open(USERS_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(',')
                
                # Ako su korisničko ime i lozinka tačni, korisnik dobija root pristup
                if username == stored_username and hashed_password == stored_password:
                    print("Uspešno ste dobili root pristup!")
                    root_status = True  # Korisnik je sada root
                    save_root_status(True)  # Sačuvaj root status
                    print("type sudo -root -h to see root commands")
                    return  # Prekida funkciju nakon uspešnog prijavljivanja

        print("Pogrešno korisničko ime ili lozinka.")  # Ako se ne nađe korisnik u datoteci

    except FileNotFoundError:
        print(f"Greška: Datoteka {USERS_FILE} ne postoji.")  # Ako datoteka sa korisnicima ne postoji
    except Exception as e:
        print(f"Došlo je do greške: {e}")  # Za sve druge greške


tools = [
    {
        "id": "tool1",
        "name": "File Manager",
        "description": "A tool to manage your files easily.",
        "version": "1.2",
        "category": "Utilities",
        "function": lambda: print("\nOpening File Manager... Files organized!\n")
    },
    {
        "id": "tool2",
        "name": "Text Editor",
        "description": "A lightweight text editor for coding.",
        "version": "2.5",
        "category": "Development",
        "function": lambda: print("\nOpening Text Editor... Ready to code!\n")
    },
    {
        "id": "tool3",
        "name": "Media Player",
        "description": "Play audio and video files.",
        "version": "3.1",
        "category": "Multimedia",
        "function": lambda: print("\nLaunching Media Player... Enjoy your media!\n")
    },
    {
        "id": "tool4",
        "name": "XHack",
        "description": "A tool that helps to do hacking activities easy as possible no knowlige for coding by @OgnjenDev #ABCstudio.",
        "version": "1.0",
        "category": "Entertainment",
        "function": lambda: main2hack()
    },
    {
         "id": "tool5",
         "name": "Rock,paper,scissors",
         "description": "A rock paper scissors game made by @thisdev",
         "version": "a.1",
         "category": "Games",
         "function": lambda: rock_paper_scissors()
    }
]

import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors or 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        print()  # Blank line for clarity


# Lista instaliranih alata
installed_tools = []

# Funkcija za simulaciju "hakovanja"
import time
import random

def display_menu():
    print("=== XHack ===")
    print("1. Prikazivanje podataka")
    print("2. Skeniranje mreže")
    print("3. Preuzimanje fajlova")
    print("4. Kreiranje backdoor-a")
    print("5. Šifrovanje podataka")
    print("6. Izvršavanje skripte")
    print("7. Hakovanje WiFi-a")
    print("8. Hakovanje Bluetooth-a")
    print("9. Generisanje lozinke")
    print("10. Napad na server")
    print("11. Bluetooth spam")
    print("12. Emulacija RFID kartice")
    print("13. Skeniranje infracrvenih signala")
    print("14. Imitacija IR daljinskog upravljača")
    print("15. Skeniranje i emulacija NFC-a")
    print("16. Isključivanje kamera u blizini")
    print("17. Skeniranje portova")
    print("18. slanje phishing email-a")
    print("19. Prikupljanje informacija o domenima")
    print("20. Simulacija napada socijalnog inženjeringa")
    print("21. Skeniranje USB uređaja")
    print("22. Emulacija GPS lokacije")
    print("23. Skeniranje WiMAX mreže")
    print("24. hakovanje Facebook profila")
    print("25. Generisanje virusa")
    print("0. Izlaz")
    print("=============================")

def fake_hacking(action, details):
    print(f"\nIzvršavam: {action}...")
    time.sleep(2)
    print(details)
    time.sleep(random.uniform(1, 3))  
    print(f"Operacija '{action}' završena!\n")

def generate_fake_password():
    length = random.randint(8, 12)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generisana lažna lozinka: {password}\n")

def simulate_server_attack():
    print("Simuliram napad na server...")
    time.sleep(2)
    print("Prikupljam informacije o serveru...")
    time.sleep(2)
    print("Izvršavam DDoS napad...")
    time.sleep(2)
    print("Napad uspešan! Server je pod kontrolom!\n")

def bluetooth_spam():
    print("Pokrećem Bluetooth spam...")
    time.sleep(2)
    print("Skeniram dostupne Bluetooth uređaje...")
    time.sleep(2)
    devices = ["Samsung A54", "oppo XC", "lenovo 4th gen", "ASUS;"]
    for device in devices:
        print(f"Slanje spam poruka na {device}...")
        time.sleep(1)
        print(f"Spam poruka uspešno poslata na {device}!")
    print("Bluetooth spam završeno!\n")

def emulate_rfid():
    print("Emuliram RFID karticu...")
    time.sleep(2)
    print("Pretražujem dostupne RFID čitače...")
    time.sleep(2)
    print("Emulacija uspešna! RFID kartica je aktivna i spremna za korišćenje!\n")

def scan_ir_signals():
    print("Skeniram infracrvene signale...")
    time.sleep(2)
    print("Prikupljam informacije o dostupnim IR uređajima...")
    time.sleep(2)
    print("Skeniranje završeno! Pronađeni IR uređaji su: TV, Klimatizacija, DVD plejer.\n")

def imitate_ir_remote():
    print("Imitiram IR daljinski upravljač...")
    time.sleep(2)
    devices = ["TV", "Klimatizacija", "DVD plejer"]
    for device in devices:
        print(f"Slanje komande za uključivanje na {device}...")
        time.sleep(1)
        print(f"Uključivanje {device} uspešno!")
    print("\nIzaberite uređaj za kontrolu:")
    print("1. TV")
    print("2. Klimatizacija")
    choice = input("Izaberite opciju (1-2): ")
    if choice == '1':
        control_tv()
    elif choice == '2':
        print("Kontrolisanje klimatizacije... Uključivanje/isključivanje uspešno!")
    else:
        print("Nepoznata opcija.")

def control_tv():
    print("Kontrolisanje TV-a...")
    time.sleep(1)
    print("Izaberite opciju:")
    print("1. Uključi TV")
    print("2. Isključi TV")
    choice = input("Izaberite opciju (1-2): ")
    if choice == '1':
        print("Uključivanje TV-a... Uspešno!")
    elif choice == '2':
        print("Isključivanje TV-a... Uspešno!")
    else:
        print("Nepoznata opcija.")

def scan_usb_devices():
    print("Skeniram USB uređaje...")
    time.sleep(2)
    print("Pronađeni USB uređaji: USB flash disk, USB tastatura, USB miš...")
    time.sleep(2)
    print("Skeniranje završeno!\n")

def emulate_gps_location():
    print("Emuliram GPS lokaciju...")
    time.sleep(2)
    print("Pretražujem dostupne GPS lokacije...")
    time.sleep(2)
    print("Emulacija uspešna! GPS lokacija je aktivna i spremna za korišćenje!\n")

def scan_wimax_network():
    print("Skeniram WiMAX mrežu...")
    time.sleep(2)
    print("Prikupljam informacije o WiMAX mreži...")
    time.sleep(2)
    print("Skeniranje završeno! Pronađene informacije o WiMAX mreži...\n")

def fake_facebook_hack():
    print("Lažno hakovanje Facebook profila...")
    time.sleep(2)
    print("Prikupljam informacije o Facebook profilu...")
    time.sleep(2)
    print("Lažno hakovanje uspešno! Facebook profil je pod kontrolom!\n")

def generate_fake_virus():
    print("Generisanje lažnog virusa...")
    time.sleep(2)
    print("Kreiram lažni virus...")
    time.sleep(2)
    print("Lažni virus je kreiran! Spreman za upotrebu...\n")

def main2hack():
    while True:
        display_menu()
        choice = input("Izaberite opciju (0-25): ")

        if choice == '1':
            fake_hacking("Prikazivanje podataka", "Prikazujem korisničke podatke i osetljive informacije... Pristupam bazi podataka i pretražujem korisničke profile...")
        elif choice == '2':
            fake_hacking("Skeniranje mreže", "Skeniram dostupne IP adrese i otvorene portove... Prikupljam informacije o mrežnoj topologiji i aktivnim uređajima...")
        elif choice == '3':
            fake_hacking("Preuzimanje fajlova", "Preuzimam tajne fajlove sa udaljenog servera... Potvrđujem integritet fajlova pre nego što ih preuzmem...")
        elif choice == '4':
            fake_hacking("Kreiranje backdoor-a", "Kreiram tajni ulaz za buduće napade... Uspostavljam trajnu vezu sa serverom za dalju kontrolu...")
        elif choice == '5':
            fake_hacking("Šifrovanje podataka", "Šifrujem osetljive podatke kako bih ih zaštitio... Koristim AES algoritam za šifrovanje i čuvanje podataka u sigurnom formatu...")
        elif choice == '6':
            fake_hacking("Izvršavanje skripte", "Izvršavam skriptu za automatizaciju napada... Skripta se pokreće sa privilegijama administratora, omogućavajući brže izvršavanje...")
        elif choice == '7':
            fake_hacking("Hakovanje WiFi-a", "Prikupio sam informacije o WiFi mrežama u okolini... Pokušavam da se povežem na najjaču mrežu koristeći brute-force napad...")
        elif choice == '8':
            fake_hacking("Hakovanje Bluetooth-a", "Skeniram dostupne Bluetooth uređaje... Pronalazim ranjive uređaje u blizini i pokušavam da uspostavim vezu...")
        elif choice == '9':
            generate_fake_password()
        elif choice == '10':
            simulate_server_attack()
        elif choice == '11':
            bluetooth_spam()
        elif choice == '12':
            emulate_rfid()
        elif choice == '13':
            scan_ir_signals()
        elif choice == '14':
            imitate_ir_remote()
        elif choice == '15':
            scan_usb_devices()
        elif choice == '16':
            emulate_gps_location()
        elif choice == ' 17':
            scan_wimax_network()
        elif choice == '18':
            fake_facebook_hack()
        elif choice == '19':
            generate_fake_virus()
        elif choice == '20':
            print("Simulacija napada socijalnog inženjeringa...")
            time.sleep(2)
            print("Prikupljam informacije o žrtvi...")
            time.sleep(2)
            print("Simulacija uspešna! Žrtva je pod kontrolom!\n")
        elif choice == '21':
            scan_usb_devices()
        elif choice == '22':
            emulate_gps_location()
        elif choice == '23':
            scan_wimax_network()
        elif choice == '24':
            fake_facebook_hack()
        elif choice == '25':
            generate_fake_virus()
        elif choice == '0':
            print("Izlazim iz programa...")
            break
        else:
            print("Nepoznata opcija, pokušajte ponovo.")



# Prikaz dostupnih alata
def list_tools():
    print("\n=== Available Tools ===")
    for idx, tool in enumerate(tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
        print(f"   Description: {tool['description']}")
        print(f"   Category: {tool['category']}\n")

# Instalacija alata
import time


installed_tools = []


def install_tool(choice):
    try:
        tool = tools[choice - 1]  # Izbor alata na osnovu korisničkog unosa
        if tool in installed_tools:
            print(f"\n'{tool['name']}' is already installed.\n")
        else:
            clear_screen()
            print("""
The following packages will be installed:
 gi
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 4.5MB of archives.
After this operation, 19.2MB of additional disk space will be used.
Get:1 https://packages.termux.org/apt/termux-main stable/main aarch64 git aarch64 2.34.1-1 [4.5MB]
Fetched 4.5MB in 3s (1,313kB/s)
Selecting previously unselected package git.
(Reading database ... 113 files and directories currently installed.)
Preparing to unpack .../git_2.34.1-1_aarch64.deb ...
""")
            print(f"Unpacking '{tool['name']}'")
            time.sleep(4)
            print(f"Setting up '{tool['name']}'")
            time.sleep(3)
            print("Processing triggers for man-db (2.9.4-2) ...")
            print("Reading database...")
            
            # Simulacija progres bar-a
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Ostanite na istoj liniji
                time.sleep(1)
            print()
            print(f"\nInstalling '{tool['name']}'...")
            time.sleep(2)
            print("Please wait...")
            installed_tools.append(tool)  # Dodavanje alata u instalirane alate
            print(f"'{tool['name']}' installed successfully!\n")
    except IndexError:
        print("\nInvalid choice. Please try again.\n")

# Testiranje komande

# Prikaz instaliranih alata
def list_installed_tools():
    if not installed_tools:
        print("\nNo tools installed yet.\n")
        return

    print("\n=== Installed Tools ===")
    for idx, tool in enumerate(installed_tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
    print()

# Pokretanje instaliranog alata
def run_installed_tool(choice):
    try:
        tool = installed_tools[choice - 1]
        print(f"\nRunning '{tool['name']}'...\n")
        tool["function"]()
    except IndexError:
        print("\nInvalid choice. Please try again.\n")

# Glavni meni
def main_menu():
    while True:
        print("=== Ruby OS Tools Menu ===")
        print("1. List available tools")
        print("2. Install a tool")
        print("3. View installed tools")
        print("4. Run an installed tool")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            list_tools()
        elif choice == "2":
            try:
                list_tools()
                tool_choice = int(input("Enter the number of the tool to install: "))
                install_tool(tool_choice)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        elif choice == "3":
            clear_screen()
            list_installed_tools()
        elif choice == "4":
            try:
                list_installed_tools()
                if installed_tools:
                    tool_choice = int(input("Enter the number of the tool to run: "))
                    run_installed_tool(tool_choice)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        elif choice == "5":
            print("\nExiting Ruby OS Tools. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.\n")

            
def sys_info():
                print(f"System: {platform.system()}")
                print(f"Version: {platform.version()}")
                print(f"Release: {platform.release()}")
                print(f"Machine: {platform.machine()}")

def loading_kernel():
    print("Loading kernel.py")
    time.sleep(3)
    print("Starting kernel.py")
    
    # Provera da li fajl postoji
    if not os.path.exists(sysfiles):
        clear_screen()
        print("File 'hal.dll' is missing or corrupted")
        kernelres()
    
    print("kernel.py loaded successfully.")
    check_installation()
    
def kernelres():
    print("Dobrodošli u kernel fixer")
    print("1.popravi sistem")
    print("2.izađi")
    while True:
        choice = input(">> ")
        
        if choice == '1':
                with open(sysfiles, 'w') as f:
                    f.write("01101000 01100001 01101100 00101110 01100100 01101100 01101100 00100000 01101001 01110011 00100000 01100110 01101001 01111000 01100101 01100100 ")

            
def ene():
    # Dimenzije okvira
    width = 60
    height = 10
    
    # Opcije
    options = ["1. Instaliraj sistem", "2. popravi sistem/instalaciju", "3. izlaz"]
    selected = 0  # Početno selektovana opcija
    
    while True:
        # Kreiramo okvir
        print("#" * width)
        for _ in range(height - 2):
            print("#" + " " * (width - 2) + "#")
        
        # Ispisujemo opcije sa strelicom unutar okvira
        for i, option in enumerate(options):
            line = "# " + option.ljust(width - 3) + "#"
            if i == selected:
                line = "# > " + option.ljust(width - 5) + "#"
            print(line)
        
        print("#" * width)

        # Čekanje na pritisak tastera
        key = input("\nPritisnite 'w' za gore, 's' za dole i Enter za izbor: ")

        if key == 'w' and selected > 0:
            clear_screen()
            selected -= 1  # Pomeri selekciju gore
        elif key == 's' and selected < len(options) - 1:
            clear_screen()
            selected += 1  # Pomeri selekciju dole
        elif key == '':
            if selected == 0:
                install_sys()
            elif selected == 1:
                res()
            elif selected == 2:
                 sys.exit()
                 
    
            
def res():
    clear_screen()
    print("Welcome to Ruby os reset")
    print("1.reset instalation")
    print("2.reset system")
    while True:
        choice = input(">> ")
        
        if choice == '1':
            reins()
        elif choice == '2':
             resys()
             
def resys():
    clear_screen()
    print("Welcome to system reset")
    print("Do you want to fix/scan system?")
    
    while True:
        choice = input("y/n: ").lower()  # Normalize input
        
        if choice == 'y':
            for i in range(11):  # 10 steps + 1 (range is inclusive-exclusive)
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Stay on the same line
                time.sleep(1)
            print()  # Move to the next line after progress bar finishes
            print("system is fixed.")
            ene()  # Call the next function
            break  # Exit the loop after fixing
        elif choice == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 'y' or 'n'.")


def reins():
    clear_screen()
    print("Welcome to installation reset")
    print("Do you want to fix/scan installation?")
    
    while True:
        choice = input("y/n: ").lower()  # Normalize input
        
        if choice == 'y':
            for i in range(11):  # 10 steps + 1 (range is inclusive-exclusive)
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Stay on the same line
                time.sleep(1)
            print()  # Move to the next line after progress bar finishes
            print("instalation is fixed.")
            ene()  # Call the next function
            break  # Exit the loop after fixing
        elif choice == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 'y' or 'n'.")
            
            

def show_progress(steps, delay=0.2):
    for i in range(steps + 1):
        bar = "█" * i + "-" * (steps - i)
        print(f"\r[{bar}] {i * 100 // steps}%", end="")
        time.sleep(delay)
    print()  # Novi red nakon završetka

def install_sys():
    package_name = "python"
    print(f"Instalacija paketa '{package_name}' je u toku...\n")

    # Simulacija komandi
    commands = [
        "apt update",
        "apt upgrade -y",
        "pkg install python -y",
        "pip install --upgrade pip",
        "pip install requests",
        "apt autoremove -y",
        "apt clean",
        "lsb_release -a",
        "mkdir -p /home/user/test",
        "chmod 755 /home/user/test",
        "chown user:user /home/user/test",
        "cat /etc/os-release",
        "wget https://github.com/OgnjenDev/Ruby os/drivers.py",
        "tar -xzvf package.tar.gz",
        "nano /etc/hosts",
        "vi /etc/hostname",
        "ps aux",
        "top",
        "free -h",
        "uptime",
        "whoami",
        "hostname",
        "date",
        "df -h",
        "du -sh /home/user",
        "lsof",
        "ip a",
        "ifconfig",
        "ping -c 4 google.com",
        "curl -I https://github.com/OgnjenDev",
        "netstat -tuln",
        "iptables -L",
        "service apache2 status",
        "systemctl status apache2",
        "systemctl start apache2",
        "systemctl stop apache2",
        "systemctl restart apache2"
    ]

    outputs = [
        "Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease\nHit:2 http://archive.ubuntu.com/ubuntu focal-updates InRelease\nHit:3 http://archive.ubuntu.com/ubuntu focal-security InRelease\nReading package lists... Done\n",
        "Reading package lists... Done\nBuilding dependency tree\nReading state information... Done\nCalculating upgrade... Done\nThe following packages will be upgraded: libc-bin libc-dev-bin libc6 libc6-dev\n4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.\nNeed to get 17.2 MB of archives.\nAfter this operation, 1,024 B of additional disk space will be used.\nDo you want to continue? [Y/n] Y\nFetched 17.2 MB in 2s (8,422 kB/s)\n",
        "Updating package lists... Done\nChecking for packages... Done\nInstalling python...\n[##########] 100% | Installed python version 3.8.10.\n",
        "Requirement already up-to-date: pip in /usr/local/lib/python3.8/dist-packages (21.2.4)\n",
        "Requirement already satisfied: requests in /usr/local/lib/python3.8/dist-packages (2.26.0)\nRequirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests) (1.26.6)\nRequirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests) (3.2)\nRequirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests) (2021.5.30)\nRequirement already satisfied: chardet<5,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests) (4.0.0)\n",
        "Reading package lists... Done\nBuilding dependency tree\nReading state information... Done\nThe following packages will be REMOVED: python3-pip\n0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.\nNeed to get 3.1 MB of archives.\nAfter this operation, 8.1 MB disk space will be freed.\nDo you want to continue? [Y/n] Y\nFetched 3.1 MB in 1s (2,157 kB/s)\n",
        "Cleaning up package cache...\nAll cached packages cleaned.\n",
        "Distributor ID: Ubuntu\nDescription:    Ubuntu 20.04 LTS\nRelease:        20.04\nCodename:       focal\n",
        "Directory '/home/user/test' created.\n",
        "Permissions for '/home/user/test' set to 755.\n",
        "Ownership of '/home/user/test' set to user:user.\n",
        "NAME=\"Ubuntu\"\nVERSION=\"20.04 LTS (Focal Fossa)\"\nID=ubuntu\nID_LIKE=debian\nVERSION_ID=\"20.04\"\nVERSION_CODENAME=focal\nUBUNTU_CODENAME=focal\n",
        "--2025-01-03 12:34:56--  https://example.com/package.tar.gz\nResolving example.com (example.com)... 93.184.216.34\nConnecting to example.com (example.com)|93.184.216.34|:443... connected.\nHTTP request sent, awaiting response... 200 OK\nLength: 123456 (121K) [application/gzip]\nSaving to: ‘package.tar.gz’\n\npackage.tar.gz          100%[====================================>] 120.56K  268KB/s    in 0.4s\n",
        "package/\npackage/file1.txt\npackage/file2.txt\npackage/file3.txt\n",
        "[Opened nano editor, displaying /etc/hosts content]\n",
        "[Opened vi editor, displaying /etc/hostname content]\n",
        "USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\nroot         1  0.0  0.1 169236  4568 ?        Ss   Jan01   0:09 /sbin/init\nuser      1557  0.0  0.1 162432  4868 ?        S    Jan02   0:03 /usr/bin/python3\n",
        "top - 12:45:12 up 10 days,  3:14,  2 users,  load average: 0.10, 0.12, 0.15\nTasks: 151 total,   1 running, 150 sleeping,   0 stopped,   0 zombie\n%Cpu(s):  3.1 us,  2.5 sy,  0.0 ni, 94.1 id,  0.3 wa,  0.0 hi,  0.0 si,  0.0 st\nMiB Mem :   3844.9 total,    295.7 free,   1873.7 used,   1675.5 buff/cache\nMiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   2282.1 avail Mem\n",
        "              total        used        free      shared  buff/cache   available\nMem:           3.8Gi       1.8Gi       295Mi       128Mi       1.7Gi       2.5Gi\nSwap:          2.0Gi          0B       2.0Gi\n",
        " 12:45:12 up 10 days,  3:14,  2 users,  load average: 0.10, 0.12, 0.15\n",
        "user",
        "hostname",
        "Thu Jan  3 12:45:12 UTC 2025",
        "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1        50G   10G   40G  20% /\ntmpfs           16G  1.5G   14G  10% /dev/shm\n",
        "du: cannot read directory '/home/user': Permission denied\n",
        "COMMAND     PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME\npython3    1557 user   12u  IPv4  123456      0t0  TCP *:http (LISTEN)\n",
        "inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0\n",
        "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\ninet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255\n",
        "PING google.com (8.8.8.8) 56(84) bytes of data.\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=13.2 ms\n",
        "HTTP/1.1 200 OK\nDate: Thu, 03 Jan 2025 12:45:12 GMT\nContent-Type: text/html; charset=UTF-8\n",
        "Active Internet connections (only servers)\nProto Recv-Q Send-Q Local Address           Foreign Address         State\ntcp        0      0 *:80                    *:*                     LISTEN",
        "Chain INPUT (policy ACCEPT)\ntarget     prot opt source               destination         \nACCEPT     all  --  anywhere             anywhere             \n",
        "● apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: active (running) since Tue 2025-01-01 15:30:00 UTC; 2 days ago",
        "● apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: inactive (dead) since Tue 2025-01-01 15:30:00 UTC; 2 days ago",
        "apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: active (running)",
        "apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: active (running) since Tue 2025-01-01 15:30:00 UTC; 2 days ago",
        "● apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: inactive (dead) since Tue 2025-01-01 15:30:00 UTC; 2 days ago",
        "apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: active (running)",
        "apache2.service - The Apache HTTP Server\n   Loaded: loaded (/etc/systemd/system/apache2.service; enabled; vendor preset: enabled)\n   Active: active (running) since Tue 2025-01-01 15:30:00 UTC; 2 days ago",
        "The Apache HTTP Server is now active and running.",
        "systemd[1]: Stopping Apache HTTP Server...",
        "systemctl[1]: apache2.service stopped successfully.",
        "systemctl restart apache2",
        "The Apache HTTP Server has been successfully restarted."
    ]

    for i, command in enumerate(commands):
        print(f"~$ {command}")
        time.sleep(4)
        print(outputs[i])
        print("\nInstalling  INSTALLATION:")
        show_progress(20)

    print("\nInstalacija završena!")
        # Oznaka da je instalacija završena
    with open(INSTALLATION_FILE, 'w') as f:
        f.write("00000000  4e 54 4f 53 4b 52 4e 4c  53 59 53 00 00 00 00 00  |NTOSKRNL SYS.......|00000010  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|00000020  30 30 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |00............|00000030  00 00 00 00 00 00 00 00  30 00 00 00 00 00 00 00  |........0.......|00000040  04 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|...")

    print("Instalacija je uspešno završena!")
    time.sleep(3)
    clear_screen()
    print("Pokretanje sistema...")
    term()
    
def term():
    print("Welcome to ruby term")
    print("Start the commands to start the system")
    while True:
        command = input("~$ ")
        
        if command == 'pip install wget':
            print("Wget installed")
            print("100% [############]")
        elif command == 'wget https://github.com/OgnjenDev/ruby os':
            print("Copying ruby to sys64")
            time.sleep(5)
            print(".")
            time.sleep(2)
            print("..")
            time.sleep(2)
            print("...")
        elif command == 'mv ruby/sys/boot.asm ruby/sys/start/':
            print("Moving...")
            time.sleep(4)
        elif command == 'cd sys64':
            print("Dir: sys64")
        elif command == 'ruby':
            print("steps:{ 0000 7289 0864")
            time.sleep(2)
            print("Loading boot/kernel.py...")
            time.sleep(3)
            print("Loading boot/kernel/loading.asm")
            time.sleep(4)
            print("Setting setup.py...")
            time.sleep(3)
            clear_screen()
            print("=====Linux kernel=====")
            print("Connecting to localhost:6060")
            print("=" * 10)
            print(".")
            time.sleep(4)
            print("..")
            time.sleep(3)
            print("...")
            time.sleep(3)
            print("localhost is loading files")
            time.sleep(4)
            loading_kernel()
        else:
            print("Unknown command")

def dodaci():
    print("Dobrodošli u dodatke!")
    print("1. podešavanja")
    print("2. backup")
    print("3. izlaz")
    while True:
        user_input = input("Unesite opciju: ")
        if user_input == '1':
            podešavanja()
        elif user_input == '2':
            if os.path.exists(INSTALLATION_FILE):
                os.remove(INSTALLATION_FILE)
                print("Fajl INSTALLATION_FILE je uspešno obrisan. Molimo vas da resetujete Vertex sistem!")
            else:
                print("Greška se desila tokom backup-a.")
        elif user_input == '3':
            print("izlaženje...")
            break
        else:
            print("Nepoznata opcija. Pokušajte ponovo.")
            
def podešavanja():
            print("Dobrodošli u podešavanja")
            print("1.User")
            print("2.Rezolucija")
            while True:
                choice = input("Unesite opciju:")
                
                if choice == 1:
                    print(f"{username}")
                    print(f"{hashed_password}")
                elif choice == '2':
                    print("1024 * 1024")
                    
            
def konami_easter_egg():
    print("Otkrili ste tajnu! Aktiviranje Easter egg-a...")
    time.sleep(2)
    print(r"""
       ______
    .-        -.
   /            \
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    | \IIIIII/ |
    \          /
     `--------`
    """)
    print("Čestitamo! Otkrili ste skriveni deo sistema!")
    time.sleep(2)
    print("Nastavite sa istraživanjem...")

import os
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
    print("\n--- Napišite svoj program u Pythonu (unesite 'KRAJ' da završite) ---")
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

    file_name = input(f"Unesite ime fajla (bez ekstenzije): ") + ".py"
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
        print("Šta je novo u VERTEX X edition")
        print("1.Optimizovali smo sistem maximalno")
        print("2.Popravljeni su dosta bagova")
        print("3.dodata je opcija informacije sistema")
        print("4.svaki put kada pokrenete sistem dobićete BIOS ekran sa informacijama")
        print("5.dodata je aplikacija za programiranje") 
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_installation():
    if not os.path.exists(INSTALLATION_FILE):
        print("Sistem nije instaliran. Pokrećem instalaciju...")
        ene()
    else:
        print("Sistem proverava instalaciju.")
        time.sleep(6)
        print("Sistem je pronašao instalaciju na /storage/emulated/0/RUBY os/BOOT")
        time.sleep(2)
        clear_screen()

    # Dodajemo logiku za nastavak posle instalacije
    print("Pokretanje sistema...")

def splash_screen(theme):
    clear_screen()
    print(f"{theme['background']}{theme['text']}Dobro došli u Ruby os!")
    print("======================")
    print("Učitavanje...")
    print("1.2.1")
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
    print("14. Informacije o sistemu")
    print("15. Šta je novo?")
    print("16. Terminal")
    print("17. code mod")
    print("18. dodaci")
    print("19. Izlaz")

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

# Predefinisani važni zadaci
def manage_tasks():
    while True:
        print("\nUpravljanje zadacima:")
        print("1. Dodaj zadatak")
        print("2. Prikaži sve zadatke")
        print("3. Izbriši zadatak")
        print("4. Izlaz")
        choice = input("Izaberite opciju: ")

        if choice == '1':
            task = input("Unesite zadatak: ")
            tasks.append(task)
            print("Zadatak je dodat.")

        elif choice == '2':
            if not tasks:
                print("Nema zadataka za prikaz.")
            else:
                print("\nSvi zadaci:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif choice == '3':
            if not tasks:
                print("Nema zadataka za brisanje.")
            else:
                print("\nSvi zadaci:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                task_index = int(input("Unesite broj zadatka za brisanje: ")) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print("Zadatak je obrisan.")

                    # Proveravamo da li su svi "važni" zadaci obrisani
                    if "[VAŽNO]" not in " ".join(tasks):
                        show_bsod()
                else:
                    print("Nevažeći broj zadatka.")

        elif choice == '4':
            print("Izlaz iz upravljanja zadacima...")
            break

        else:
            print("Nevažeća opcija. Pokušajte ponovo.")


def show_bsod():
    """Simulira Blue Screen of Death (BSOD)."""
    clear_screen()
    print("\033[44m\033[37m")  # Plava pozadina i beli tekst
    print("=" * 60)
    print("A problem has been detected and the system has been shut down to prevent damage.")
    print("\nIMPORTANT_TASKS_NOT_FOUND")
    print("\nIf this is the first time you've seen this stop error screen,")
    print("restart your system. If this screen appears again, contact your")
    print("system administrator or technical support.")
    print("=" * 60)
    print("\033[0m")  # Resetovanje boja
    sys.exit()  # Izlazak iz programa

import time

def bootloader():
    clear_screen()
    # Svi koraci učitavanja
    steps = [
        "Loading Linux kernel...",
        "Initializing hardware drivers...",
        "Detecting file systems...",
        "[ OK ] Mounting root filesystem...",
        "[ OK ] Starting udev Kernel Device Manager...",
        "[ OK ] Detecting network hardware...",
        "[ OK ] Configuring network interfaces...",
        "[ OK ] Starting system logging service...",
        "[ OK ] Starting D-Bus System Message Bus...",
        "[ OK ] Starting Avahi mDNS/DNS-SD Stack...",
        "[ OK ] Initializing swap space...",
        "[ OK ] Mounting additional filesystems...",
        "[ OK ] Starting Light Display Manager...",
        "[ OK ] Preparing graphical interface...",
        "[ OK ] Loading kernel modules...",
        "[ OK ] Initializing Random Number Generator (RNG)...",
        "[ OK ] Checking disk partitions...",
        "[ OK ] Starting Cryptographic Setup...",
        "[ OK ] Activating LVM and RAID volumes...",
        "[ OK ] Loading device mapper...",
        "[ OK ] Starting systemd-udevd...",
        "[ OK ] Starting network time synchronization...",
        "[ OK ] Applying system security policies...",
        "[ OK ] Enabling AppArmor security profiles...",
        "[ OK ] Starting kernel log daemon...",
        "[ OK ] Initializing process scheduler...",
        "[ OK ] Setting hostname to 'ruby-os'...",
        "[ OK ] Loading virtualization modules...",
        "[ OK ] Starting storage manager...",
        "[ OK ] Starting power management daemon...",
        "[ OK ] Enabling swap partition...",
        "[ OK ] Checking battery status...",
        "[ OK ] Starting keyboard configuration service...",
        "[ OK ] Initializing USB controllers...",
        "[ OK ] Starting PCI bus enumeration...",
        "[ OK ] Enabling thermal management...",
        "[ OK ] Loading ACPI modules...",
        "[ OK ] Configuring system clock...",
        "[ OK ] Starting hardware abstraction layer...",
        "[ OK ] Starting input/output subsystems...",
        "[ OK ] Mounting EFI system partition...",
        "[ OK ] Starting network configuration daemon...",
        "[ OK ] Applying network settings...",
        "[ OK ] Starting SSH server...",
        "[ OK ] Enabling firewall rules...",
        "[ OK ] Starting DNS resolver service...",
        "[ OK ] Activating IP forwarding...",
        "[ OK ] Initializing systemd timers...",
        "[ OK ] Mounting user data partition...",
        "[ OK ] Starting Bluetooth services...",
        "[ OK ] Configuring audio devices...",
        "[ OK ] Loading ALSA sound modules...",
        "[ OK ] Setting up PulseAudio...",
        "[ OK ] Initializing GPU drivers...",
        "[ OK ] Starting OpenGL renderer...",
        "[ OK ] Configuring display resolution...",
        "[ OK ] Starting graphical desktop services...",
        "[ OK ] Loading desktop environment components...",
        "[ OK ] Initializing clipboard manager...",
        "[ OK ] Starting desktop notification system...",
        "[ OK ] Loading system theme...",
        "[ OK ] Starting file indexing service...",
        "[ OK ] Initializing search indexing...",
        "[ OK ] Starting update manager...",
        "[ OK ] Checking for software updates...",
        "[ OK ] Applying critical updates...",
        "[ OK ] Verifying update integrity...",
        "[ OK ] Configuring package manager...",
        "[ OK ] Checking disk health...",
        "[ OK ] Enabling journaling...",
        "[ OK ] Starting data backup services...",
        "[ OK ] Configuring default applications...",
        "[ OK ] Initializing user preferences...",
        "[ OK ] Preparing user directories...",
        "[ OK ] Starting session manager...",
        "[ OK ] Verifying user permissions...",
        "[ OK ] Configuring input devices...",
        "[ OK ] Loading desktop icons...",
        "[ OK ] Starting system tray...",
        "[ OK ] Initializing window manager...",
        "[ OK ] Preparing taskbar...",
        "[ OK ] Loading wallpaper...",
        "[ OK ] Setting up desktop shortcuts...",
        "[ OK ] Starting process monitor...",
        "[ OK ] Starting system monitoring tools...",
        "[ OK ] Initializing disk usage monitor...",
        "[ OK ] Configuring file manager...",
        "[ OK ] Setting up clipboard history...",
        "[ OK ] Initializing cloud services...",
        "[ OK ] Syncing cloud data...",
        "[ OK ] Preparing email client...",
        "[ OK ] Checking mail server settings...",
        "[ OK ] Starting web browser integration...",
        "[ OK ] Initializing system notifications...",
        "[ OK ] Configuring power saving settings...",
        "[ OK ] Enabling screen locking...",
        "[ OK ] Setting up login screen...",
        "[ OK ] Initializing GPU acceleration...",
        "[ OK ] Loading system fonts...",
        "[ OK ] Verifying font cache...",
        "[ OK ] Configuring system logs...",
        "[ OK ] Loading background services...",
        "[ OK ] Starting accessibility features...",
        "[ OK ] Verifying installed packages...",
        "[ OK ] Loading Python environment...",
        "[ OK ] Initializing virtual environments...",
        "[ OK ] Starting Ruby OS services...",
        "[ OK ] Starting backup and restore services...",
        "[ OK ] Initializing AI assistant...",
        "[ OK ] Starting local server...",
        "[ OK ] Initializing Ruby OS firewall...",
        "[ OK ] Checking disk encryption...",
        "[ OK ] Configuring GPU pipelines...",
        "[ OK ] Initializing advanced security modules...",
        "[ OK ] Checking thermal sensors...",
        "[ OK ] Verifying secure boot...",
        "[ OK ] Checking BIOS settings...",
        "[ OK ] Finalizing user session...",
        "[ OK ] Preparing audio pipelines...",
        "[ OK ] Initializing multitasking...",
        "[ OK ] Loading secure shell keys...",
        "[ OK ] Setting up virtual desktops...",
        "[ OK ] Finalizing boot sequence...",
        "[ OK ] Applying finishing touches...",
        "[ OK ] Starting user applications...",
        "[ OK ] Finalizing desktop environment setup..."
        "[ INFO ] System is booted"
    ]

    print("Booting Ruby OS...\n")
    for step in steps:
        print(step)
        time.sleep(0.1)  # Pauza između koraka

    

def web():
        print("Dobrodošli na web")
        print("1.google")
        print("2.duckduck go")
        print("3.exit")
        while True:
            choice = input("Izaberite opciju:")
            
            if choice == '1':
                webbrowser.open ("https://google.com")
            elif choice == '2':
                webbrowser.open ("https://duckduckgo.com")
            elif choice == '3':
                 break
        

def main():
    loading_kernel()
    bootloader()
    check_installation()
    theme = select_theme()
    splash_screen(theme)
    login_or_register() 

    while True:
        show_menu(theme)
        choice = input("Izaberite opciju (1-18): ")
        
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
            web()
        elif choice == '14':
             sys_info()
        elif choice == '15':
            šta_je_novo()
        elif choice == '16':
            terminal()
        elif choice == '17':
            programiranje()  
        elif choice == '18':
            dodaci()
        elif choice == '19':
            clear_screen()
            print("Isključivanje...")
            time.sleep(2)
            break
        elif choice == 'konami':
            konami_easter_egg()
        else:
            print("Nevažeća opcija, pokušajte ponovo.")

if __name__ == "__main__":
    main()