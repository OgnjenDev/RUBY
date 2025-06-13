import os
from datetime import timedelta
import json
import time
import random
import hashlib
import requests
import curses
import sys
import psutil
import shutil
import socket
import subprocess
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
        "id": "tool4",  # Poboljšano sa jedinstvenim ID-jem
        "name": "XHack",
        "description": "A tool that helps to do hacking activities easy as possible, no knowledge for coding by @OgnjenDev #ABCstudio.",
        "version": "1.0",
        "category": "Entertainment",
        "function": lambda: main2hack()
    },
    {
        "id": "tool5",
        "name": "Rock, Paper, Scissors",
        "description": "A rock paper scissors game made by @thisdev.",
        "version": "a.1",
        "category": "Games",
        "function": lambda: rock_paper_scissors()
    },
    {
        "id": "tool6",  # Promenio sam ID na jedinstveni
        "name": "Wifi speed test",
        "description": "a program for measurming wifi speed.",
        "version": "1.0",
        "category": "Utilities",
        "function": lambda: measure_speed()
    },
    {
        "id": "tool7",
        "name": "A test game",
        "description": "A test game for ruby by @BitCrafter",
        "version": "1.0",
        "category": "Games",
        "function": lambda: main2testgame()
        
    },
    {
        "id": "tool8",
        "name": "Ruby Paint",
        "description": "You can now make drawings in Ruby!!",
        "version": "1.0",
        "category": "Utilities",
        "function": lambda: curses.wrapper(main4paint)
        
    },
    {
        "id": "tool9",
        "name": "Snake Game",
        "description": "A snake game in python",
        "version": "1.0",
        "category": "Games",
        "function": lambda: curses.wrapper(main4snake)
        
    },
    {
        "id": "tool10",
        "name": "PyControl",
        "description": "A python remote control app for ruby OS github: https://github.com/OgnjenDev/Pycontrol",
        "version": "1.0",
        "category": "Utilities",
        "function": lambda: pycontrol()
        
    },
        
]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
tasks = [
"kernel",
"network",
"system",
"servers",
"installation"
]
dir = os.getcwd()
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[40m'"
total_ram = psutil.virtual_memory().total / (1024 ** 2)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOTLOADER = os.path.join(BASE_DIR, "bootloader", "bootorder.dll")
ROOT_FILE = os.path.join(BASE_DIR, "root", "root.dat")
INSTALLATION_FILE = os.path.join(BASE_DIR, "installation_complete.sys")
USERS_FILE = os.path.join(BASE_DIR, "users.dat")
SYSFILES = os.path.join(BASE_DIR, "kernel", "hal.dll")
time = time.strftime("%Y-%m-%d %H:%M:%S")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def welcome():
    clear_screen()
    print(f"Welcome to{BLUE} Ruby OS")
    print("\033[0m")
    
    
def man():
    man_pages = {
        "help": "Prikazuje sve dostupne komande.",
        "clear": "Briše ekran.",
        "exit": "Zatvara terminal.",
        "man": "Prikazuje objašnjenje za komandu.",
        "echo": "Ispisuje tekst koji korisnik unese.",
        "date": "Pokazuje datum i vreme.",
        "cp": "Kopira fajld sa jdenog mesta na drugo.",
        "mv": "Pomera fajld sa jednog mesta na drugo.",
        "ls": "Polazuje fajldove u trenutnom direktorijumu.",
        "cd": "Menja direktorijum.",
        "web": "Otvara web browser.",
        "sudo su": "Daje vam root pristup.",
        "free": "Pokazuje koliko prostora ima na disku.",
        "rpm": "Otvara Ruby Packing Menager gde možede da instalirate razne alate.",
        "ruby update": "Updatuje sistem",
        "pwd": "Pokazuje trenutni direktorijum."
    }

    izbor = input("Koju komandu želiš? ").strip()
    if izbor in man_pages:
        print(man_pages[izbor])
    else:
        print("Još nismo dodali tu komandu!")

def game_manager():
    print("\n🎮 Dobrodošli u Ruby OS Game Manager! 🎮")
    games = {
        "1": ("Pogodi broj", igra_pogodi_broj),
        "2": ("Zmija (Snake)", igra_zmija),
        "3": ("Kamen, papir, makaze", igra_kpm),
        "4": ("Križić-kružić (Tic Tac Toe)", igra_ttt),
        "5": ("Brojevi na brzinu", igra_brojevi_na_brzinu)
    }
    
    while True:
        print("\nIzaberite igru ili 0 za izlaz:")
        for key, (name, _) in games.items():
            print(f"{key}. {name}")
        print("0. Izlaz iz Game Managera")
        
        izbor = input("Unesite opciju: ").strip()
        
        if izbor == '0':
            print("Izlaz iz Game Managera...")
            break
        elif izbor in games:
            print(f"\nPokrećem igru: {games[izbor][0]}\n")
            games[izbor][1]()
        else:
            print("Nepoznata opcija, pokušajte ponovo.")

def igra_pogodi_broj():
    broj = random.randint(1, 50)
    pokusaji = 0
    print("Pogodi broj između 1 i 50!")
    while True:
        try:
            guess = int(input("Unesi svoj broj: "))
            pokusaji += 1
            if guess == broj:
                print(f"Bravo! Pogodio si broj za {pokusaji} pokušaja.")
                break
            elif guess < broj:
                print("Broj je veći.")
            else:
                print("Broj je manji.")
        except ValueError:
            print("Unesi validan broj.")

def igra_zmija():
    print("Zmija igra je u razvoju. Za sada uživaj u ostalim igrama!")

def igra_kpm():
    opcije = ['kamen', 'papir', 'makaze']
    print("Igra Kamen, papir, makaze!")
    while True:
        korisnik = input("Izaberi (kamen/papir/makaze) ili 'izlaz' za kraj: ").lower()
        if korisnik == 'izlaz':
            print("Izlaz iz igre.")
            break
        if korisnik not in opcije:
            print("Nepoznata opcija.")
            continue
        
        komp = random.choice(opcije)
        print(f"Računar je izabrao: {komp}")
        
        if korisnik == komp:
            print("Nerešeno!")
        elif (korisnik == 'kamen' and komp == 'makaze') or \
             (korisnik == 'papir' and komp == 'kamen') or \
             (korisnik == 'makaze' and komp == 'papir'):
            print("Pobedili ste!")
        else:
            print("Izgubili ste!")

def igra_ttt():
    # Tic Tac Toe igra za dva igrača
    tabla = [' ' for _ in range(9)]
    
    def print_tabla():
        print()
        for i in range(3):
            print(" " + " | ".join(tabla[i*3:(i+1)*3]))
            if i < 2:
                print("---+---+---")
        print()

    def check_win(player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # horizontalno
            [0,3,6], [1,4,7], [2,5,8],  # vertikalno
            [0,4,8], [2,4,6]            # dijagonale
        ]
        for cond in win_conditions:
            if all(tabla[i] == player for i in cond):
                return True
        return False

    def check_draw():
        return all(s != ' ' for s in tabla)

    player_turn = 'X'
    while True:
        print_tabla()
        try:
            move = int(input(f"Igrač {player_turn}, izaberi polje (1-9): "))
            if move < 1 or move > 9:
                print("Unesi broj između 1 i 9.")
                continue
            if tabla[move-1] != ' ':
                print("Polje je zauzeto.")
                continue
            tabla[move-1] = player_turn
        except ValueError:
            print("Unesi validan broj.")
            continue
        
        if check_win(player_turn):
            print_tabla()
            print(f"Igrač {player_turn} je pobedio! 🎉")
            break
        if check_draw():
            print_tabla()
            print("Nerešeno!")
            break
        
        player_turn = 'O' if player_turn == 'X' else 'X'

def igra_brojevi_na_brzinu():
    print("Dobrodošli u igru 'Brojevi na brzinu'!")
    print("Unesite brojeve što brže možete. Imaš 10 sekundi.")
    start = time.time()
    score = 0
    while time.time() - start < 10:
        broj = random.randint(1, 100)
        print(f"Unesi broj: {broj}")
        try:
            odgovor = int(input("Vaš unos: "))
            if odgovor == broj:
                score += 1
                print("Tačno! +1 poen")
            else:
                print("Netačno!")
        except ValueError:
            print("Nevažeći unos.")
    print(f"Kraj igre! Osvojili ste {score} poena.")
    
import subprocess
import sys

import time
import os

def friday_the_13th_easter_egg():
    horror_ascii = """
    ███████╗██████╗ ██╗   ██╗██╗██████╗  █████╗ ██╗   ██╗
    ██╔════╝██╔══██╗██║   ██║██║██╔══██╗██╔══██╗╚██╗ ██╔╝
    ███████╗██████╔╝██║   ██║██║██████╔╝███████║ ╚████╔╝ 
    ╚════██║██╔═══╝ ╚██╗ ██╔╝██║██╔═══╝ ██╔══██║  ╚██╔╝  
    ███████║██║      ╚████╔╝ ██║██║     ██║  ██║   ██║   
    ╚══════╝╚═╝       ╚═══╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
         ░▒▓█ WELCOME TO FRIDAY THE 13TH █▓▒░
    """

    print(horror_ascii)
    time.sleep(1)

    glitch = "ERROR: RUBY OS CORE INTERRUPTED...\n"
    for i in range(3):
        print(glitch * 2)
        time.sleep(0.2)

    print("You feel a strange chill... ⚰️\n")

# Pozovi ovu funkciju gde želiš u Ruby OS-u

def pip():
    def run(cmd):
        result = subprocess.getoutput(cmd)
        print(result)

    while True:
        print("\n==== PIP CONTROL ====")
        print("[1] Install package")
        print("[2] Uninstall package")
        print("[3] Update package")
        print("[4] List installed packages")
        print("[5] Search package (pypi.org)")
        print("[6] Upgrade pip")
        print("[0] Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            pkg = input("Package to install: ").strip()
            if pkg:
                run(f"{sys.executable} -m pip install {pkg}")

        elif choice == "2":
            pkg = input("Package to uninstall: ").strip()
            if pkg:
                run(f"{sys.executable} -m pip uninstall -y {pkg}")

        elif choice == "3":
            pkg = input("Package to update: ").strip()
            if pkg:
                run(f"{sys.executable} -m pip install --upgrade {pkg}")

        elif choice == "4":
            run(f"{sys.executable} -m pip list")

        elif choice == "5":
            pkg = input("Search term: ").strip()
            if pkg:
                run(f"{sys.executable} -m pip search {pkg}")

        elif choice == "6":
            run(f"{sys.executable} -m pip install --upgrade pip")

        elif choice == "0":
            print("Exiting PIP control...")
            break

        else:
            print("Invalid choice!")

    

def pycontrol():
    blacklist = [
        'rm -rf', 'reboot', 'shutdown', 'poweroff', ':(){', 'mkfs', 'dd if=', '>:',
        'killall', 'kill -9', 'init 0', 'init 6', 'halt', 'chown /', 'chmod 777 /',
        '>', '<', 'wget http', 'curl http', 'scp ', 'nc -e', 'telnet'
    ]

    mode = input("Run as [server/client]: ").strip().lower()

    if mode == 'server':
        HOST = '0.0.0.0'
        PORT = 9999

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"[+] Waiting for connection on port {PORT}...")

        client_socket, addr = server.accept()
        ip = addr[0]
        print(f"[+] Incoming connection from {ip}")

        allow = input(f"Allow connection from {ip}? (Y/n): ").strip().lower()
        if allow != 'y' and allow != '':
            client_socket.send(b"[ACCESS DENIED]")
            client_socket.close()
            print("[!] Connection denied.")
            server.close()
            return
        else:
            client_socket.send(b"[ACCESS GRANTED]")
            time.sleep(0.5)
            print(f"[+] Connection accepted from {ip}")

        current_dir = os.getcwd()

        while True:
            try:
                command = client_socket.recv(1024).decode().strip()
                print(f"[Client] {command}")

                if command.lower() == 'exit':
                    break

                if any(bad in command for bad in blacklist):
                    client_socket.send(b"[!] Command blocked for security reasons.")
                    continue

                if command.startswith("cd "):
                    path = command[3:].strip()
                    try:
                        os.chdir(path)
                        current_dir = os.getcwd()
                        client_socket.send(f"[+] Changed directory to {current_dir}".encode())
                    except Exception as e:
                        client_socket.send(f"[Error] {str(e)}".encode())
                else:
                    output = subprocess.getoutput(command)
                    client_socket.send(output.encode() or b"[+] Command executed with no output.")
            except Exception as e:
                client_socket.send(f"[Error] {str(e)}".encode())

        client_socket.close()
        server.close()

    elif mode == 'client':
        HOST = input("Enter server IP: ").strip()
        PORT = 9999

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((HOST, PORT))
            response = client.recv(1024).decode()
            if "[ACCESS DENIED]" in response:
                print("[!] Access denied by server.")
                client.close()
                return
            elif "[ACCESS GRANTED]" in response:
                print(f"[+] Connected to {HOST}:{PORT}")
            else:
                print("[!] Unknown server response.")
                client.close()
                return
        except Exception as e:
            print(f"[!] Failed to connect: {str(e)}")
            return

        while True:
            command = input("Shell> ").strip()
            if not command:
                continue
            client.send(command.encode())
            if command.lower() == "exit":
                break
            response = client.recv(8192).decode()
            print(response)

        client.close()

    else:
        print("Invalid mode. Use 'server' or 'client'.")



def zip_manager():
    current_dir = os.getcwd()

    def list_dir():
        print(f"\n📁 Trenutni direktorijum: {current_dir}")
        for item in os.listdir(current_dir):
            print(" └──", item)
        print()

    def change_dir(new_path):
        nonlocal current_dir
        if os.path.isdir(new_path):
            current_dir = os.path.abspath(new_path)
            print(f"✅ Promenjen direktorijum na: {current_dir}")
        else:
            print("❌ Putanja ne postoji.")

    def extract_zip():
        zip_path = input("📦 Unesi ime ZIP fajla (ili punu putanju): ")
        full_zip_path = os.path.join(current_dir, zip_path) if not os.path.isabs(zip_path) else zip_path
        if not os.path.isfile(full_zip_path):
            print("❌ ZIP fajl ne postoji.")
            return
        extract_to = input("📁 Unesi direktorijum za ekstrakciju (ili Enter za podrazumevani): ") or os.path.splitext(full_zip_path)[0]
        os.makedirs(extract_to, exist_ok=True)
        os.system(f'unzip -o "{full_zip_path}" -d "{extract_to}"')
        print(f"✅ Ekstraktovano u '{extract_to}'\n")

    def create_zip():
        folder = input("📂 Unesi ime foldera za ZIP-ovanje: ")
        full_folder_path = os.path.join(current_dir, folder) if not os.path.isabs(folder) else folder
        if not os.path.isdir(full_folder_path):
            print("❌ Folder ne postoji.")
            return
        zip_name = input("📦 Unesi ime za ZIP fajl (ili Enter za podrazumevani): ") or (folder.rstrip("/").rstrip("\\") + ".zip")
        zip_name = os.path.join(current_dir, zip_name) if not os.path.isabs(zip_name) else zip_name
        os.system(f'zip -r "{zip_name}" "{full_folder_path}"')
        print(f"✅ Kreiran ZIP fajl: {zip_name}\n")

    while True:
        print("\n========== 📦 ZIP MENI 📦 ==========")
        print(f"📂 Trenutni dir: {current_dir}")
        print("1️⃣  Listaj fajlove")
        print("2️⃣  Promeni direktorijum")
        print("3️⃣  Ekstraktuj ZIP fajl")
        print("4️⃣  Kreiraj ZIP fajl")
        print("5️⃣  Izlaz")
        choice = input("👉 Izaberi opciju (1-5): ")

        if choice == "1":
            list_dir()
        elif choice == "2":
            new_path = input("📂 Unesi novu putanju: ")
            change_dir(new_path)
        elif choice == "3":
            extract_zip()
        elif choice == "4":
            create_zip()
        elif choice == "5":
            print("👋 Izlaz iz ZIP Menadžera.")
            break
        else:
            print("⚠️ Nevažeća opcija, pokušaj ponovo.")

    
def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Uspešno premešteno: {source} → {destination}")
    except Exception as e:
        print(f"Greška: {type(e).__name__} - {e}")

def cp(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Uspešno kopirano: {source} → {destination}")
    except Exception as e:
        print(f"Greška: {type(e).__name__} - {e}")

def cp_r(source, destination):
    try:
        shutil.copytree(source, destination)
        print(f"Uspešno kopiran direktorijum: {source} → {destination}")
    except Exception as e:
        print(f"Greška: {type(e).__name__} - {e}")
    
def bsod():
    random_numbers_left = [f"{random.randint(0, 999999999999999):04}" for _ in range(10)]
    random_numbers_right = [f"{random.randint(0, 99999999999999):04}" for _ in range(10)]

    bsod_text = "\n".join(
        f"{left}        {right}"
        for left, right in zip(random_numbers_left, random_numbers_right)
    )

    bsod_message = f"""
    
{RED} A fatal exception {random.randint(0, 99)} has occurred at {hex(random.randint(0x1000, 0xFFFF))}:{hex(random.randint(0x1000, 0xFFFF))}.
The current application will be terminated.

{bsod_text}

* Press any key to terminate the current application.
* Press CTRL+ALT+DEL again to restart your computer. You will
  lose any unsaved information in all applications.

"""
    print(bsod_message)
    usr = input("Press enter to continue ")
    sys.exit()
    
def ram4test():
    
    if total_ram < 64:
        print("Nedovoljno RAM-a za Ruby OS!")
        bsod()
    else:
        print("...")
        
ram4test()
    
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
    
import curses
import time
import random

MESSAGES = [
    "Testing memory blocks...",
    "Checking for bad sectors...",
    "Analyzing RAM speed...",
    "Verifying data integrity...",
    "Scanning for memory leaks..."
]

def ram_test(stdscr):
    curses.curs_set(0)  # Sakrij kursor
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    title = "RAM Test Utility"
    stdscr.addstr(1, (width - len(title)) // 2, title, curses.A_BOLD)

    for i in range(101):
        stdscr.addstr(3, 2, f"Progress: {i}%")
        stdscr.addstr(5, 2, f"Status: {random.choice(MESSAGES)}")
        
        bar = "[" + ("#" * (i // 2)) + (" " * (50 - i // 2)) + "]"
        stdscr.addstr(4, 2, bar)
        
        stdscr.refresh()
        time.sleep(0.05)

    # Simulacija neuspeha u 30% slučajeva
    if random.randint(1, 100) <= 30:
        stdscr.addstr(7, 2, "RAM Test FAILED!", curses.A_BOLD)
        stdscr.addstr(8, 2, "Starting RAM Recovery...", curses.A_BOLD)
        stdscr.refresh()
        time.sleep(2)
        ram_recovery(stdscr)
    else:
        stdscr.addstr(7, 2, "Test completed successfully!", curses.A_BOLD)
        stdscr.addstr(9, 2, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()

def ram_recovery(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "RAM Recovery in progress...", curses.A_BOLD)

    attempts = 0
    while True:
        attempts += 1
        stdscr.addstr(3, 2, f"Attempt {attempts} to fix RAM...")
        stdscr.refresh()
        time.sleep(2)

        # 50% šanse da uspe svaki put
        if random.randint(1, 100) <= 50:
            stdscr.addstr(5, 2, "RAM Recovery SUCCESSFUL!", curses.A_BOLD)
            break
        else:
            stdscr.addstr(5, 2, "RAM Recovery FAILED, retrying...", curses.A_BOLD)
        
        stdscr.refresh()
        time.sleep(2)

    stdscr.addstr(7, 2, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


# Lista opcija



import curses
import time

# Lista opcija (možeš dodati više opcija)
options = ["Ruby OS", "Ruby OS Recovery", "Ruby OS RAM Recovery", "Shutdown"]


def draw_menu(stdscr):
    curses.curs_set(0)  # Sakrij kursor
    stdscr.nodelay(0)
    stdscr.timeout(100)
    
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 5, "GRUB 2.0 Bootloader", curses.A_BOLD)
        stdscr.addstr(1, 5, "Use ↑ and ↓ to navigate, Enter to select", curses.A_DIM)

        # Crtanje opcija
        for idx, option in enumerate(options):
            x = 5
            y = idx + 3
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)  # Obeleži izabranu opciju
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord("\n"):  # Ako pritisne Enter
            stdscr.clear()
            stdscr.addstr(5, 5,"...", curses.A_BOLD)
            stdscr.refresh()
            time.sleep(2)
            
            if options[current_row] == "Ruby OS":
                welcome()
            elif options[current_row] == "Ruby OS Recovery":
                resys()
            elif options[current_row] == "Ruby OS RAM Recovery":
                curses.wrapper(ram_test)
            elif options[current_row] == "Shutdown":
                sys.exit()
            
            break  # Izađi iz petlje

curses.wrapper(draw_menu)                        
    
def web():
        print("Dobrodošli na web")
        print("1. google")
        print("2. duckduck go")
        print("3. firefox")
        print("4. Čitač HTML-a")
        print("5. exit")
        while True:
            choice = input("Izaberite opciju:")
            
            if choice == '1':
                webbrowser.open ("https://google.com")
            elif choice == '2':
                webbrowser.open ("https://duckduckgo.com")
            elif choice == '3':
                 webbrowser.open ("https://firefox.com")
            elif choice == '4':
                html()
            elif choice == '5':
                break
                

def html():
    url = input("Unesite URL: ").strip()

    # Ako korisnik ne unese http ili https, dodaj https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url)
        response.raise_for_status()  # Proverava HTTP greške
        
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    except requests.exceptions.RequestException as e:
        print(f"Greška prilikom prikaza URL-a: {e}")
            
           
import curses

def init_screen():
    curses.initscr()
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    curses.curs_set(0)  # Sakrij kursor
    win.keypad(1)
    win.nodelay(0)
    return win

def draw_pixel(win, x, y, char="█"):
    win.addch(y, x, char)

def main4paint(win):
    win.clear()
    curses.curs_set(0)
    
    h, w = win.getmaxyx()
    x, y = w // 2, h // 2  # Početna pozicija "miša"

    pixels = set()  # Set za čuvanje piksela (crtanje)
    
    while True:
        win.clear()
        
        # Iscrtavanje svih piksela
        for px, py in pixels:
            draw_pixel(win, px, py)
        
        # Prikazivanje kursora
        draw_pixel(win, x, y, "X")

        win.refresh()
        key = win.getch()

        if key == ord('q'):  # Izlazak iz programa
            break
        elif key == curses.KEY_UP:
            y = max(0, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(h - 1, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(w - 1, x + 1)
        elif key == 10:  # Enter - crta piksel
            pixels.add((x, y))
        elif key == 8 or key == 127:  # Backspace - briše piksel
            pixels.discard((x, y))
             
            
# Parametri igre
screen_width = 20
screen_height = 10
player_x = 1
player_y = 1
score = 0

# Mapa sveta sa ziduom, praznim prostorom i poenima
game_map = [
    "####################",
    "#..............*..#",
    "#...#..............#",
    "#...............#..#",
    "#..*...............#",
    "#........#.........#",
    "#.....*............#",
    "#..................#",
    "#.........*........#",
    "####################"
]

# Funkcija za crtanje mape
def draw_map():
    global player_x, player_y
    os.system('cls' if os.name == 'nt' else 'clear')  # Čisti ekran
    
    # Pretvorimo mapu u listu karaktera da bismo menjali poziciju igrača
    map_lines = [list(line) for line in game_map]
    
    # Postavi poziciju igrača na mapi
    map_lines[player_y][player_x] = '@'
    
    # Prolazimo kroz mapu i crtamo je
    for row in map_lines:
        print(''.join(row))
    
    # Prikazujemo broj poena
    print(f"Poeni: {score}")

# Funkcija za kretanje igrača
def move_player(direction):
    global player_x, player_y, score
    
    # U zavisnosti od pritisnutog ključa pomeramo igrača
    if direction == 'w' and game_map[player_y - 1][player_x] != '#':
        player_y -= 1
    elif direction == 's' and game_map[player_y + 1][player_x] != '#':
        player_y += 1
    elif direction == 'a' and game_map[player_y][player_x - 1] != '#':
        player_x -= 1
    elif direction == 'd' and game_map[player_y][player_x + 1] != '#':
        player_x += 1
    
    # Ako igrač pokupi poen, povecavamo poene
    if game_map[player_y][player_x] == '*':
        score += 1
        # Uklanjamo poen sa mape
        game_map[player_y] = game_map[player_y][:player_x] + '.' + game_map[player_y][player_x + 1:]

# Glavna funkcija
def main2testgame():
    global player_x, player_y, score
    
    while True:
        # Crtamo mapu i poziciju igrača
        draw_map()
        
        # Kontrola kretanja
        key = input("Pritisnite W/A/S/D za kretanje ili Q za izlaz: ")
        
        if key.lower() == 'q':  # Izlaz iz igre
            print(f"Igra je završena. Poeni: {score}")
            break
        elif key.lower() in ['w', 'a', 's', 'd']:
            move_player(key.lower())  # Kretanje u zavisnosti od tastature
        
        # Osveži ekran
        time.sleep(0.2)

# Pokretanje igre

import curses
import time
import sys
from random import randint

class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ',
            1: ' * ',
            2: ' # ',
            3: ' & ',
        }
        self.snake_coords = []
        self._generate_field()
        self.add_entity()

    def add_entity(self):
        
        while(True):
            i = randint(0, self.size-1)
            j = randint(0, self.size-1)
            entity = [i, j]
            
            if entity not in self.snake_coords:
                self.field[i][j] = 3
                break

    def _generate_field(self):
        self.field = [[0 for j in range(self.size)] for i in range(self.size)]

    def _clear_field(self):        
        self.field = [[j if j!= 1 and j!= 2 else 0 for j in i] for i in self.field]


    def render(self, screen):
        size = self.size
        self._clear_field()


        # Render snake on the field
        for i, j in self.snake_coords:
            self.field[i][j] = 1

        # Mark head
        head = self.snake_coords[-1]
        self.field[head[0]][head[1]] = 2

        for i in range(size):
            row = ''
            for j in range(size):
                row += self.icons[ self.field[i][j] ]

            screen.addstr(i, 0, row)

    def get_entity_pos(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 3:
                    return [i, j]

        return [-1, -1]


    def is_snake_eat_entity(self):
        entity = self.get_entity_pos()
        head = self.snake_coords[-1]
        return entity == head


class Snake:
    def __init__(self, name):
        self.name = name
        self.direction = curses.KEY_RIGHT

        # Init basic coords
        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]
        
    def set_direction(self, ch):

        # Check if wrong direction
        if ch == curses.KEY_LEFT and self.direction == curses.KEY_RIGHT:
            return
        if ch == curses.KEY_RIGHT and self.direction == curses.KEY_LEFT:
            return
        if ch == curses.KEY_UP and self.direction == curses.KEY_DOWN:
            return
        if ch == curses.KEY_DOWN and self.direction == curses.KEY_UP:
            return 

        self.direction = ch

    def level_up(self):
        # get last point direction
        a = self.coords[0]
        b = self.coords[1]

        tail = a[:]

        if a[0] < b[0]:
            tail[0]-=1
        elif a[1] < b[1]:
            tail[1]-=1
        elif a[0] > b[0]:
            tail[0]+=1
        elif a[1] > b[1]:
            tail[1]+=1

        tail = self._check_limit(tail)
        self.coords.insert(0, tail)

    def is_alive(self):
        head = self.coords[-1]
        snake_body = self.coords[:-1]
        return head not in snake_body

    def _check_limit(self, point):
        # Check field limit
        if point[0] > self.field.size-1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.field.size-1
        elif point[1] < 0:
            point[1] = self.field.size-1
        elif point[1] > self.field.size-1:
            point[1] = 0

        return point

    def move(self):
        # Determine head coords
        head = self.coords[-1][:]

        # Calc new head coords
        if self.direction == curses.KEY_UP:
            head[0]-=1
        elif self.direction == curses.KEY_DOWN:
            head[0]+=1
        elif self.direction == curses.KEY_RIGHT:
            head[1]+=1
        elif self.direction == curses.KEY_LEFT:
            head[1]-=1

        # Check field limit
        head = self._check_limit(head)

        del(self.coords[0])
        self.coords.append(head)
        self.field.snake_coords = self.coords

        if not self.is_alive():
            sys.exit()


        # check if snake eat an entity
        if self.field.is_snake_eat_entity():
            curses.beep()
            self.level_up()
            self.field.add_entity()




    def set_field(self, field):
        self.field = field


def main4snake(screen):
    clear_screen()
    # Configure screen
    screen.timeout(0)

    # Init snake & field
    field = Field(10)
    snake = Snake("Joe")
    snake.set_field(field)

    while(True):
        # Get last pressed key
        ch = screen.getch()
        if ch != -1:
            # If some arrows did pressed - change direction
            snake.set_direction(ch)

        # Move snake
        snake.move()
        
        # Render field
        field.render(screen)
        screen.refresh()
        
        time.sleep(.4)



def measure_speed():
    url = "https://www.google.com"  # Možeš koristiti bilo koji server
    start_time = time.time()
    
    response = requests.get(url)
    
    end_time = time.time()
    download_time = end_time - start_time
    print(f"Download time: {download_time:.2f} seconds")
    
    # Izračunaj brzinu na osnovu veličine odgovora
    speed = len(response.content) / download_time / 1_000_000  # Mbps
    print(f"Download speed: {speed:.2f} Mbps")


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
            
INSTALLED_TOOLS_FILE = "installed_tools.json"


# Lista instaliranih alata (biće učitana iz fajla)
installed_tools = []

# Funkcija za učitavanje instaliranih alata iz fajla
def load_installed_tools():
    global installed_tools
    if os.path.exists(INSTALLED_TOOLS_FILE):
        with open(INSTALLED_TOOLS_FILE, "r") as file:
            try:
                data = json.load(file)
                installed_tools = [tool for tool in tools if tool["id"] in data]
            except json.JSONDecodeError:
                installed_tools = []
    else:
        installed_tools = []

# Funkcija za čuvanje instaliranih alata u fajl
def save_installed_tools():
    with open(INSTALLED_TOOLS_FILE, "w") as file:
        json.dump([tool["id"] for tool in installed_tools], file)

# Funkcija za listanje dostupnih alata
def list_tools():
    print("\n=== Available Tools ===")
    for idx, tool in enumerate(tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
        print(f"   Description: {tool['description']}")
        print(f"   Category: {tool['category']}\n")

# Funkcija za instalaciju alata
def install_tool(choice):
    try:
        tool = tools[choice - 1]  
        if tool in installed_tools:
            print(f"\n'{tool['name']}' is already installed.\n")
        else:
            clear_screen()
            print("Reading package lists... Done")
            print("Building dependency tree       ")
            print("Reading state information... Done")
            print("The following additional packages will be installed:")
            print(f"' {tool['name']}'  -man liberror-perl")
            print("Suggested packages:")
            print(f"  '{tool['name']}'-daemon-run | '{tool['name']}'-daemon-sysvinit '{tool['name']}'-doc '{tool['name']}'-email '{tool['name']}'-gui gitk gitweb '{tool['name']}'-cvs '{tool['name']}'-mediawiki '{tool['name']}'-svn")
            print("The following NEW packages will be installed:")
            print(f" '{tool['name']}'-man liberror-perl")
            time.sleep(4)
            print("0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.")
            print("Need to get 9 MB of archives.")
            print("After this operation, 9MB of additional disk space will be used.")
            print("Do you want to continue? [Y/n] ")
            print("Fetching packages...")
            time.sleep(3)
            print(f"Downloading '{tool['name']}' (version-x.x.x)...")
            time.sleep(4)
            print(f"Downloading '{tool['name']}'-man (version-x.x.x)...")
            time.sleep(3)
            print("Downloading liberror-perl (version-x.x.x)...")
            time.sleep(3)
            print("Fetched  MB in 3s (3 MB/s)")
            print("Selecting previously unselected package liberror-perl.")
            print("Preparing to unpack .../liberror-perl_x.x.x.deb ...")
            time.sleep(5)
            print("Unpacking liberror-perl (x.x.x) ...")
            time.sleep(2)
            print("Selecting previously unselected package '{tool['name']}'-man.")
            print(f"Preparing to unpack .../'{tool['name']}'-man_x.x.x.deb ...")
            print(f"Unpacking '{tool['name']}'-man (x.x.x) ...")
            time.sleep(3)
            print(f"Selecting previously unselected package '{tool['name']}'.")
            print(f"Preparing to unpack .../'{tool['name']}'_x.x.x.deb ...")
            time.sleep(3)
            print(f"Unpacking '{tool['name']}' (x.x.x) ...")
            time.sleep(4)
            print("Setting up liberror-perl (x.x.x) ...")
            time.sleep(3)
            print(f"Setting up '{tool['name']}'-man (x.x.x) ...")
            time.sleep(4)
            print(f"Setting up '{tool['name']}' (x.x.x) ...")
            time.sleep(3)
            print("Processing triggers for man-db (x.x.x) ...")
            time.sleep(4)
            print("'{tool['name']}' successfully installed!")
            time.sleep(2)
            installed_tools.append(tool)
            save_installed_tools()  # Čuvanje promene
            print(f"'{tool['name']}' installed successfully!\n")
    except IndexError:
        print("\nInvalid choice. Please try again.\n")

# Funkcija za prikaz instaliranih alata
def list_installed_tools():
    if not installed_tools:
        print("\nNo tools installed yet.\n")
        return

    print("\n=== Installed Tools ===")
    for idx, tool in enumerate(installed_tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
    print()

# Funkcija za pokretanje instaliranog alata
def run_installed_tool(choice):
    try:
        tool = installed_tools[choice - 1]
        print(f"\nRunning '{tool['name']}'...\n")
        tool["function"]()
    except IndexError:
        print("\nInvalid choice. Please try again.\n")


# Glavni meni
def pac():
    load_installed_tools()  # Učitaj instalirane alate pri pokretanju
    
    while True:
        print("\n=== Ruby OS Tools Menu ===")
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
   
    
import random

    
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
    username = input("[ SUDO ] Unesite korisničko ime: ")
    password = input("[ SUDO ] Unesite lozinku: ")

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
      

DEV_FILE = os.path.join(BASE_DIR, "home", "usr", "dev_file.txt")
DEV_PASSWORD = "rubyisgood666"  # Postavi lozinku za dev mod
SERVER_FILE = os.path.join(BASE_DIR, "home", "usr", "server_file.txt")

def is_dev():
    """Proverava da li je uređaj podešen kao developerski."""
    if os.path.exists(DEV_FILE):
        with open(DEV_FILE, "r") as f:
            return f.read().strip() == "dev=True"
    return False

def set_dev_status(status):
    """Postavlja developerski status u fajl."""
    with open(DEV_FILE, "w") as f:
        f.write(f"dev={status}")
        
def is_server():
    """Proverava da li je uređaj podešen kao developerski."""
    if os.path.exists(SERVER_FILE):
        with open(SERVER_FILE, "r") as f:
            return f.read().strip() == "server=True"
    return False

def set_server_status(status):
    """Postavlja developerski status u fajl."""
    with open(SERVER_FILE, "w") as f:
        f.write(f"server={status}")

def opt():
    print("Koji uređaj koristite za instalaciju")
    print("1. Normalna instalacija (kompijuter)")
    print("2. Prenosna instalacija (laptop, telefon, tablet)")
    print("3. Server instalacija (za servere)")
    print("4. Developer instalacija (samo za developere)")

    while True:
        choice = input("Unesite setup opciju: ")

        if choice == '1':
            set_dev_status("False")
            print("Ponovo uključite računar")
            sys.exit()
        elif choice == '2':
            set_dev_status("False")
            print("Ponovo uključite računar")
            sys.exit()
        elif choice == '3':
            set_server_status("True")
            print("Ponovo uključite računar")
            sys.exit()
        elif choice == '4':
            password = input("Unesite lozinku za developer režim: ")
            if password == DEV_PASSWORD:
                print("Lozinka ispravna. Omogućavam developer režim.")
                set_dev_status("True")
                print("Ponovo uključite računar")
                sys.exit()
            else:
                print("Pogrešna lozinka! Developer režim nije omogućen.")
        else:
            print("Nevažeći unos! Pokušajte ponovo.")
            
dev = is_dev()

import psutil

def show_memory_usage():
    memory = psutil.virtual_memory()  # Dobijamo informacije o memoriji
    
    total_memory = memory.total / (1024 ** 3)  # Ukupna memorija u GB
    used_memory = memory.used / (1024 ** 3)    # Zauzeta memorija u GB
    free_memory = memory.free / (1024 ** 3)    # Slobodna memorija u GB
    percent_used = memory.percent            # Procenat zauzete memorije
    
    print(f"Total memory: {total_memory:.2f} GB")
    print(f"Used memory: {used_memory:.2f} GB ({percent_used}%)")
    print(f"Free memory: {free_memory:.2f} GB")
    

# Provera da li terminal podržava curses
      

# Pokreni program sigurno


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
    

import os
import time
from datetime import datetime

root_status = True  # Assuming root status starts as False

def terminal():
    global root_status
    print("RUBY terminal")
    print("Type 'help' for a list of commands.")
    
    while True:
        choice = input(f"~{dir}$ ").strip().lower()
        
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
- web        : Explore the web!
- mkdir [name]: Create a new directory.
- rmdir [name]: Remove an existing directory.
- touch [name]: Create a new file.
- cp [name]: Copys a file or directory
- mv [name]: moves a file or directory
- rm [name]  : Remove a file.
- cat [name]: Read and display a file's content.
- write [name]: Write content to a file.
- sysinfo    : Display system information.
- reboot     : Simulate a system reboot.
""")
        
        elif choice == "exit":
            print("Exiting RUBY terminal...")
            break


        elif choice == "mv":
           src = input("Unesite izvorni fajl ili direktorijum: ").strip()
           dst = input("Unesite odredište: ").strip()
           mv(src, dst)

        elif choice == "cp":
           src = input("Unesite izvorni fajl: ").strip()
           dst = input("Unesite odredište: ").strip()
           cp(src, dst)

        elif choice == "cp -r":
           src = input("Unesite izvorni direktorijum: ").strip()
           dst = input("Unesite odredište: ").strip()
           cp_r(src, dst)
           
        elif choice == "pip":
            pip()
                        
        elif choice == "pwd":
            print(f"{dir}")
            
        elif choice == "man":
            man()
            
        elif choice == "ruby update":
            print("Reading database...")
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Ostanite na istoj liniji
                time.sleep(1)
            print()
                
        elif choice.startswith("cd "):  # Fixed indentation error
            dir_name = choice[3:].strip()
            try:
                os.chdir(dir_name)
                print(f"Directory changed to {os.getcwd()}")
            except FileNotFoundError:
                print(f"Directory '{dir_name}' not found.")
            except NotADirectoryError:
                print(f"'{dir_name}' is not a directory.")
            except PermissionError:
                print(f"Permission denied to access '{dir_name}'.")
        
        elif choice == "rpm":
            pac()
            # Here you would add actual installation logic if needed.
            
        elif choice == 'sudo su':
            root_system()
            
        elif choice == 'code':
            programiranje()
            
        elif choice == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif choice == "date":
            print("Current date and time:", datetime.now())
        
        elif choice.startswith("echo "):
            print(choice[5:])
            
        elif choice == 'free':
            show_memory_usage()
            
        elif choice == 'scan disk':
            print("Scaning disk...")
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")  # Ostanite na istoj liniji
                time.sleep(5)
            print()
            
        elif choice == 'neofetch':
            neofetch()  # Assuming you have a neofetch function
        
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
            files = os.listdir(".")
            for f in files:
                print(f)
        
        elif choice.startswith("mkdir "):
            dir_name = choice[6:]
            try:
                os.mkdir(dir_name)
                print(f"Directory '{dir_name}' created.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("rmdir "):
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
            file_name = choice[3:]
            try:
                os.remove(file_name)
                print(f"File '{file_name}' removed.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice.startswith("cat "):
            file_name = choice[4:]
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
            konami_easter_egg()  # Assuming you have a konami_easter_egg function
            
        elif choice == "greet":
            print("Whats you name?:")
            name = input("enter your name : ")
            print(f"Hello {name}, welcome to Ruby OS!")
        
        elif choice == "about":
            print("Ruby OS - A custom operating system project made in 2024.")
        
        elif choice == "sysinfo":
            import platform
            print(f"System: {platform.system()}")
            print(f"Version: {platform.version()}")
            print(f"Release: {platform.release()}")
            print(f"Machine: {platform.machine()}")
        
        elif choice == "reboot":
            print("Rebooting system...")
            loading_kernel()  # Assuming you have a loading_kernel function
            
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
                        print("Usage: sudo config [key] [value]")
                elif command == "users":
                    print("Listing root users: [admin, root_user]")  # Example
                elif command == "shutdown":
                    print("System is shutting down...")
                    break
                elif command == "reboot":
                    print("System is rebooting with root permissions...")
                    loading_kernel()
                elif command == "logs":
                    print("script start:/start /hf /ruby /ebby64 /ruby os is starting echo {command}")
                elif command == "rm ":
                    file_name = choice[3:]
                try:
                      os.remove(file_name)
                      print(f"File '{file_name}' removed as root user.")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    print("Unknown root command. Type 'sudo -root -h' for a list of commands.")

def run_exe():
    folder = input("Unesi putanju do foldera sa .exe fajlovima: ")

    if not os.path.isdir(folder):
        print("Folder ne postoji!")
        return

    # Lista .exe fajlova
    exe_files = [f for f in os.listdir(folder) if f.endswith(".exe")]

    if not exe_files:
        print("Nema .exe fajlova u ovom folderu.")
        return

    print("\nDostupni .exe fajlovi:")
    for i, f in enumerate(exe_files):
        print(f"[{i}] {f}")

    try:
        choice = int(input("\nUnesi broj programa koju želiš da pokreneš: "))
        exe_path = os.path.join(folder, exe_files[choice])
        print(f"Pokrećem: {exe_path}")
        os.system(f"wine \"{exe_path}\"")
    except (IndexError, ValueError):
        print("Greška u izboru fajla.")
               
                    
            
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
    if not os.path.exists(SYSFILES):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print("E: File 'hal.dll' is misssing or corrupted")
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
        time.sleep(2)
        print(outputs[i])
        print("\nInstalling  INSTALLATION_FILE:")
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
    
import os
import time
import platform
from datetime import datetime

def term():
    print("Welcome to Ruby Term")
    print("Start the commands to start the system")

    while True:
        choice = input(f"~[localhost:6060] /instaler $ ")

        if choice == 'sudo apt install git':
            print("git installed")
            print("100% [############]")

        elif choice == "exit":
            print("Exiting RUBY terminal...")
            break

        elif choice == "ruby update":
            print("Reading database...")
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")
                time.sleep(1)
            print()

        elif choice.startswith("cd "):
            dir_name = choice[3:].strip()
            try:
                os.chdir(dir_name)
                print(f"Directory changed to {os.getcwd()}")
            except FileNotFoundError:
                print(f"Directory '{dir_name}' not found.")
            except NotADirectoryError:
                print(f"'{dir_name}' is not a directory.")
            except PermissionError:
                print(f"Permission denied to access '{dir_name}'.")

        elif choice == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == "date":
            print("Current date and time:", datetime.now())

        elif choice.startswith("echo "):
            print(choice[5:])

        elif choice == 'free':
            print("Memory usage: 512MB / 1024MB (Example)")  # Dodaj stvarni prikaz memorije ako želiš

        elif choice == 'scan disk':
            print("Scanning disk...")
            for i in range(11):
                bar = "█" * i + "-" * (10 - i)
                print(f"\r[{bar}] {i * 100 // 10}%", end="")
                time.sleep(1)
            print()

        elif choice == 'neofetch':
            print("Ruby OS - A custom operating system")
            print(f"System: {platform.system()}")
            print(f"Version: {platform.version()}")
            print(f"Release: {platform.release()}")
            print(f"Machine: {platform.machine()}")

        elif choice == "calc":
            try:
                expression = input("Enter calculation: ")
                result = eval(expression)
                print("Result:", result)
            except Exception as e:
                print("Error in calculation:", e)

        elif choice == "ls":
            files = os.listdir(".")
            print("Files in current directory:")
            for f in files:
                print(f)

        elif choice.startswith("mkdir "):
            dir_name = choice[6:]
            try:
                os.mkdir(dir_name)
                print(f"Directory '{dir_name}' created.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice.startswith("rmdir "):
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

        elif choice == "greet":
            name = input("Enter your name: ")
            print(f"Hello {name}, welcome to Ruby OS")

        elif choice == "about":
            print("Ruby OS - A custom operating system project made with love.")

        elif choice == "sysinfo":
            print(f"System: {platform.system()}")
            print(f"Version: {platform.version()}")
            print(f"Release: {platform.release()}")
            print(f"Machine: {platform.machine()}")

        elif choice == "reboot":
            print("Rebooting system...")
            time.sleep(2)

        elif choice == 'git clone https://github.com/OgnjenDev/ruby os':
            print("Copying Ruby OS to sys64")
            time.sleep(5)
            print(".")
            time.sleep(2)
            print("..")
            time.sleep(2)
            print("...")

        elif choice == 'mv ruby/sys/boot.asm ruby/sys/start/':
            print("Moving...")
            time.sleep(4)

        elif choice == 'font':
            print("\nAvailable fonts:")
            fonts = ["Monospace", "Courier New", "Consolas", "Arial", "Verdana", "Times New Roman"]
            for i, font in enumerate(fonts, start=1):
                print(f"{i}. {font}")
                
        elif choice == ("fontset"):
            font = input("font: ")  # Uzimamo tekst nakon "fontset "
            print(f"Font set to: {font}")
            
        elif choice == 'lsblk':
            print("""NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   20G  0 disk""")

        elif choice == 'genfstab -U /mnt >> /mnt/etc/fstab':
            print("")
          
        elif choice == 'ruby-chroot /mnt':
            print("")
            
        elif choice == 'pacman -S grub grub-install --target=i386-pc /dev/sda grub-mkconfig -o /boot/grub/grub.cfg':
            print("""Installing for i386-pc platform.
Installation finished. No error reported.
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-linux
Found initrd image: /boot/initramfs-linux.img
done""")

        elif choice == 'ruby':
            print("steps: { 0000 7289 0864 }")
            time.sleep(2)
            print("Loading boot/kernel.py...")
            time.sleep(3)
            print("Loading boot/kernel/loading.asm...")
            time.sleep(4)
            print("Setting setup.py...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("===== Linux Kernel =====")
            print("Connecting to localhost:6060")
            print("=" * 10)
            time.sleep(4)
            print(".")
            time.sleep(3)
            print("..")
            time.sleep(3)
            print("...")
            time.sleep(4)
            print("localhost is loading files")
            time.sleep(4)
            print("Ruby OS successfully started!")
            opt()
        else:
            print("Unknown command")
            
import os
import subprocess

def usb_reader():
    print("\n========== 💾 USB ČITAČ (PRO) 💾 ==========")
    
    # Pronađi USB uređaje pomoću lsblk
    result = subprocess.getoutput("lsblk -o NAME,SIZE,MODEL,MOUNTPOINT | grep -i 'media\|run/media'")
    if not result.strip():
        print("❌ Nije pronađen nijedan montirani USB uređaj.")
        return

    print("🔎 Pronađeni USB uređaji:\n")
    print(result)

    mount_points = []
    for line in result.splitlines():
        parts = line.split()
        if len(parts) >= 4:
            mount_points.append(parts[-1])

    for mount in mount_points:
        print(f"\n📂 Sadržaj USB-a ({mount}):")
        os.system(f'ls "{mount}"')
                                                                                   


def dodaci():
    print("Dobrodošli u dodatke!")
    print("1. Podešavanja")
    print("2. Backup")
    print("3. Prijavljivanje bagova")
    print("4. Network Wizard")
    print("5. Ruby Paket Menadžer")
    print("6. ZIP Menadžer")
    print("9. USB Čitač")

    if is_dev():
        print("7. Developer Opcije")
        print("8. Izlaz")
    elif is_server():
        print("7. Server Konzola")
        print("8. Izlaz")
    else:
        print("7. Izlaz")

    while True:
        user_input = input("Unesite opciju: ").strip()

        if user_input == '1':
            podešavanja()
        elif user_input == '2':
            try:
                if os.path.exists(INSTALLATION_FILE):
                    os.remove(INSTALLATION_FILE)
                    print("✅ INSTALLATION_FILE uspešno obrisan. Restartujte Ruby OS.")
                else:
                    print("⚠️ INSTALLATION_FILE nije pronađen.")
            except Exception as e:
                print(f"❌ Greška prilikom brisanja: {e}")
        elif user_input == '3':
            bugs()
        elif user_input == '4':
            netw()
        elif user_input == '5':
            pac()
        elif user_input == '6':
            zip_manager()
        elif user_input == '9':
            usb_reader()
        elif user_input == '7':
            if is_dev():
                dev_options()
            elif is_server():
                serverterm()
            else:
                print("👋 Izlaz iz dodataka.")
                break
        elif user_input == '8' and (is_dev() or is_server()):
            print("👋 Izlaz iz dodataka.")
            break
        else:
            print("❗ Nepoznata opcija. Pokušajte ponovo.")
            

server_status = False
server_ip = None

def start_server():
    global server_status, server_ip
    server_status = True
    server_ip = input("Enter the server IP address: ")
    print(f"Server started with IP: {server_ip}")

def stop_server():
    global server_status
    server_status = False
    print("Server stopped.")

def restart_server():
    global server_status, server_ip
    print("Restarting server...")
    time.sleep(1)
    server_status = True
    print(f"Server restarted with IP: {server_ip}")

def server_status_check():
    if server_status:
        print(f"Server is running with IP: {server_ip}")
    else:
        print("Server is not running.")

def handle_command(command):
    if command == "start":
        if not server_status:
            start_server()
        else:
            print("Server is already running.")
    elif command == "stop":
        if server_status:
            stop_server()
        else:
            print("Server is already stopped.")
    elif command == "restart":
        if server_status:
            restart_server()
        else:
            print("Server is not running.")
    elif command == "status":
        server_status_check()
    elif command == "exit":
        print("Exiting server terminal...")
        exit()
    else:
        print("Unknown command. Available commands: start, stop, restart, status, exit.")

def serverterm():
    print("Welcome to the Ruby Server Terminal")
    while True:
        time.sleep(1)
        user_input = input("Ruby Server> ").strip().lower()
        handle_command(user_input)


def dev_options():
                print("Dobrodošli developeri!!!!!!!!!!")  
                print("1. pravila developera")
                print("2. Ruby os nove ideje")
                print("3. izlaz")
                while True:
                    choice = input("Izaberite opciju: ")
                    
                    if choice == '1':
                        devpra()
                    elif choice == '2':
                        devrubyide()
                    elif choice == '3':
                         break
                         
def devpra():
                print("Developer pravila:")
                print("1. Zabranjeno obljavljivanja developer lozinke online posledice:( Uklonjena developer dozlova) ili (kazna od 12000 dinara ili 500 €)")
                print("2. Zabranjeno obljavljivanje novosti o ruby os online posledice:( Uklinjena developer dozvola) ili (kazna od 9000 dinara ili 800 €)")
                print("3. Zabranjeno hakovanje u developer servere razlog:( posle hakovanja serveri su oštećeni ) posledice:( Suđenje ) ili kazna:( 95000 dinara ili 2 godine zatvora)")
                
def devrubyide():
                print("Novosti!:")
                print("Poboljšanje servera")
                
def netw():
            print("Dobrodošli u network wizard")
            print("Podesućemo vaš internet!")
            print("Da li je vaš internet žičan ili bežičan")
            print("1. žičan")
            print("2. bežičan")
            print("3. izlaz")
            while True:
                choice = input("Izaberite opciju: ")
                
                if choice == '1':
                    netwž()
                elif choice == '2':
                    netwb()
                elif choice == '3':
                    break
                    
def netwž():
    print("Odlično! Sada ćemo da podesimo")
    print("Budite sigurni da je internet kabal povezan u LAN 1")
    
    import time
    import sys

    for i in range(11):
        bar = "█" * i + "-" * (10 - i)
        print(f"\r[{bar}] {i * 100 // 10}%", end="")
        sys.stdout.flush()  # Ručno osveži izlaz
        time.sleep(1.0)

    print()  # Novi red posle progress bara
    print("Uspešno podešeno!")

# Poziv funkcije

def netwb():
    print("Odlično! Sada ćemo da podesimo")
    print("Budite sigurni da je internet povezan na trenutnom OS")
    
    import time
    import sys

    for i in range(11):
        bar = "█" * i + "-" * (10 - i)
        print(f"\r[{bar}] {i * 100 // 10}%", end="")
        sys.stdout.flush()  # Ručno osveži izlaz
        time.sleep(1.0)

    print()  # Novi red posle progress bara
    print("Uspešno podešeno!")

            
def bugs():
            print("Izvinjavamo se za sve greške u Beta verziji")
            ime = input("Unesite vaše ime: ")
            opis = input("Opišite bug/glitch: ")
            print("Hvala vam što ste prijavili bug")
            
            
def podešavanja():
            print("Dobrodošli u podešavanja")
            print("1.User")
            print("2.Rezolucija")
            print("3. Izlaz")
            while True:
                choice = input("Unesite opciju:")
                
                if choice == '1':
                    print(f"{username}")
                    print(f"{hashed_password}")
                elif choice == '2':
                    print("1024 * 1024")
                elif choice == '3':
                     break                                
            
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

import os

def programiranje():
    program_code = ""
    current_language = "python"
    print("\n--- Dobrodošli u mod za programiranje ---")
    while True:
        print(f"\nTrenutni direktorijum: {os.getcwd()}")
        print("1. Izaberi programski jezik")
        print("2. Napiši novi program")
        print("3. Sačuvaj program")
        print("4. Prikaži dostupne programe")
        print("5. Pokreni program")
        print("6. Izmeni postojeći program")
        print("7. Idi u direktorijum")
        print("8. Idi nazad")
        print("9. Izlaz iz programiranja")

        izbor = input("Izaberite opciju: ")

        if izbor == "1":
            current_language = choose_language()
        elif izbor == "2":
            program_code = write_code(current_language)
        elif izbor == "3":
            save_program(program_code, current_language)
        elif izbor == "4":
            show_files()
        elif izbor == "5":
            run_selected_program()
        elif izbor == "6":
            program_code = edit_selected_program()
        elif izbor == "7":
            change_directory()
        elif izbor == "8":
            go_back_directory()
        elif izbor == "9":
            print("Izlaz iz modula za programiranje...")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo!")

def choose_language():
    print("\n--- Izaberite jezik ---")
    print("1. Python")
    print("2. C")
    print("3. C++")
    print("4. Java")
    izbor = input("Izaberite broj jezika: ")
    jezici = {"1": "python", "2": "c", "3": "cpp", "4": "java"}
    return jezici.get(izbor, "python")

def write_code(language):
    print(f"\n--- Pišite svoj {language} program (unesite 'KRAJ' za kraj) ---")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "KRAJ":
            break
        code_lines.append(line)
    print("Program je napisan.")
    return "\n".join(code_lines)

def save_program(program_code, language):
    if not program_code:
        print("Nema koda za čuvanje!")
        return

    ext = {"python": ".py", "c": ".c", "cpp": ".cpp", "java": ".java"}
    file_name = input(f"Unesite ime fajla (bez ekstenzije): ") + ext.get(language, ".txt")
    with open(file_name, "w") as f:
        f.write(program_code)
    print(f"Program je sačuvan kao {file_name}")

def show_files():
    print("\n--- Lista programa u trenutnom direktorijumu ---")
    ekstenzije = [".py", ".c", ".cpp", ".java"]
    fajlovi = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in ekstenzije]
    
    if not fajlovi:
        print("Nema programa.")
        return

    for i, f in enumerate(fajlovi, 1):
        print(f"{i}. {f}")

def run_selected_program():
    ekstenzije = [".py", ".c", ".cpp", ".java"]
    fajlovi = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in ekstenzije]

    if not fajlovi:
        print("Nema programa za pokretanje.")
        return

    show_files()
    izbor = input("Izaberite broj programa: ")
    try:
        idx = int(izbor) - 1
        if 0 <= idx < len(fajlovi):
            file_name = fajlovi[idx]
            ext = os.path.splitext(file_name)[1]
            print(f"Pokrećem {file_name}...")
            if ext == ".py":
                input("Ovaj fajld nije verifikovan i možda je opasan!!! PRESS ENTER")
                print("")
                os.system(f"python '{file_name}'")
            elif ext == ".c":
                input("Ovaj fajld nije verifikovan i možda je opasan!!! PRESS ENTER")
                print("")
                os.system(f"gcc '{file_name}' -o temp_c_prog && ./temp_c_prog")
            elif ext == ".cpp":
                input("Ovaj fajld nije verifikovan i možda je opasan!!! PRESS ENTER")
                print("")
                os.system(f"g++ '{file_name}' -o temp_cpp_prog && ./temp_cpp_prog")
            elif ext == ".java":
                input("Ovaj fajld nije verifikovan i možda je opasan!!! PRESS ENTER")
                print("")
                base = os.path.splitext(file_name)[0]
                os.system(f"javac '{file_name}' && java {base}")
            else:
                print("Nepodržana ekstenzija!")
        else:
            print("Nevažeći broj.")
    except ValueError:
        print("Unesite broj.")

def edit_selected_program():
    ekstenzije = [".py", ".c", ".cpp", ".java"]
    fajlovi = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in ekstenzije]

    if not fajlovi:
        print("Nema programa za izmenu.")
        return ""

    show_files()
    izbor = input("Izaberite broj programa koji želite da izmenite: ")
    try:
        idx = int(izbor) - 1
        if 0 <= idx < len(fajlovi):
            file_name = fajlovi[idx]
            with open(file_name, "r") as f:
                print(f"\n--- Trenutni sadržaj ({file_name}) ---")
                print(f.read())

            print("\n--- Novi kod (unesi 'KRAJ' za kraj) ---")
            code_lines = []
            while True:
                line = input()
                if line.strip().upper() == "KRAJ":
                    break
                code_lines.append(line)
            new_code = "\n".join(code_lines)
            with open(file_name, "w") as f:
                f.write(new_code)
            print(f"{file_name} je uspešno izmenjen.")
            return new_code
        else:
            print("Nevažeći broj.")
    except ValueError:
        print("Unesite broj.")
    return ""

def change_directory():
    print("\n--- Lista direktorijuma ---")
    dir_list = [d for d in os.listdir() if os.path.isdir(d)]
    if not dir_list:
        print("Nema dostupnih direktorijuma.")
        return
    for i, d in enumerate(dir_list, 1):
        print(f"{i}. {d}")
    izbor = input("Izaberite broj direktorijuma: ")
    try:
        idx = int(izbor) - 1
        if 0 <= idx < len(dir_list):
            os.chdir(dir_list[idx])
            print(f"Prebačeni ste u direktorijum: {os.getcwd()}")
        else:
            print("Nevažeći broj.")
    except ValueError:
        print("Unesite broj.")

def go_back_directory():
    os.chdir("..")
    print(f"Vraćeni ste nazad u: {os.getcwd()}")

                
def šta_je_novo():
        clear_screen()
        print("Šta je novo u Ruby OS 1.3.1")
        print("1.Optimizovali smo sistem maximalno")
        print("2.Popravljeni su dosta bagova")
        print("3.U ruby sada možete programirati u pythonu,java,c,cpp")
        print("4.Dodat je neofetch")
        

def check_installation():
    if not os.path.exists(INSTALLATION_FILE):
        print("Sistem nije instaliran. Pokrećem instalaciju...")
        ene()
    else:
        print("Sistem proverava instalaciju.")
        time.sleep(6)
        print("Sistem je pronašao instalaciju na /RUBY os/BOOT")
        time.sleep(2)
        clear_screen()

    # Dodajemo logiku za nastavak posle instalacije
    print("Pokretanje sistema...")

import os
import time

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def splash_screen(theme):
    ascii_logo = """
     ____  _   _ ______   _____  ____
    |  _ \| | | | __ ) \ / / _ \/ ___|
    | |_) | | | |  _ \ V / | | \___ \ 
    |  _ <| |_| | |_) || || |_| |___) |
    |_| \_\\___/|____/ |_| \___/|____/
    """

    spinner = ["|", "/", "-", "\\"]

    for _ in range(10):  # 10 iteracija animacije
        for spin in spinner:
            clear_screen()
            print(f"{theme['background']}{theme['text']}Dobro došli u Ruby OS!")
            print("=" * 40)
            print("\n".join(line.center(40) for line in ascii_logo.split("\n")))  # Centriranje logotipa
            print("\n" + " " * 19 + spin)  # Animirani pokazivač ispod loga
            print(" " * 16 + "1.3.3")
            print(" " * 8 + "© Copyright - ABC studio")
            time.sleep(0.2)

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

def draw_window(x, y, title, content, width=45, height=25):
    lines = content.split('\n')

    for _ in range(y):
        print()

    top = "+" + "-" * (width - 2) + "+"
    bottom = "+" + "-" * (width - 2) + "+"
    title_line = "|" + title.center(width - 2) + "|"
    empty = "|" + " " * (width - 2) + "|"

    print(" " * x + top)
    print(" " * x + title_line)
    print(" " * x + empty)

    for line in lines[:height - 5]:
        line_fixed = line[:width - 2]  # skrati ako je linija preduga
        print(" " * x + "|" + line_fixed.ljust(width - 2) + "|")

    for _ in range(height - 4 - len(lines)):
        print(" " * x + empty)

    print(" " * x + bottom)

def show_menu(theme):
    content = (
        f"{theme['background']}{theme['text']}"
        "Izaberite opciju:\n"
        "1. Prikaži datum i vreme\n"
        "2. Prikaži fajlove u trenutnom direktorijumu\n"
        "3. Kreiraj novi fajl\n"
        "4. Pročitaj fajl\n"
        "5. Kreiraj novu fasciklu\n"
        "6. Prikaži fajlove u specifičnoj fascikli\n"
        "7. Izbriši fajl ili fasciklu\n"
        "8. Promeni temu\n"
        "9. Očisti ekran\n"
        "10. Game Manager\n"
        "11. Kalkulator\n"
        "12. Upravljanje zadacima\n"
        "13. Web pretraživač\n"
        "14. Informacije o sistemu\n"
        "15. Šta je novo?\n"
        "16. Terminal\n"
        "17. Code mod\n"
        "18. Pokreni .exe fajldove\n"
        "19. Dodaci\n"
        "20. Isključi\n"
    )
    draw_window(4, 3, "Ruby OS Meni", content)

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

# Testiranje funkcije

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
                        bsod()
                else:
                    print("Nevažeći broj zadatka.")

        elif choice == '4':
            print("Izlaz iz upravljanja zadacima...")
            break

        else:
            print("Nevažeća opcija. Pokušajte ponovo.")
            

# ANSI boje
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
reset = "\033[0m"

# Simulacija Linux boot loga
clear_screen()
print("""
____  _   _ ______   _____  ____
|  _ \| | | | __ ) \ / / _ \/ ___|
| |_) | | | |  _ \ V / | | \___ \ 
|  _ <| |_| | |_) || || |_| |___) |
|_| \_\\___/|____/ |_| \___/|____/
    """)
time.sleep(4)
    
boot_logs = [
    "[    0.000000] Booting Linux Kernel...",
    "[    0.032000] Initializing CPU...",
    "[    0.064000] Loading drivers...",
    "[    0.096000] Detecting hardware...",
    "[    0.128000] Enabling power management...",
    "[    0.160000] Starting udev...",
    "[    0.192000] Loading kernel modules...",
    "[    0.224000] Setting up file system...",
    "[    0.256000] Mounting root filesystem...",
    "[    0.288000] Checking system integrity...",
    "[    0.320000] Starting network services...",
    "[    0.352000] Configuring network interfaces...",
    "[    0.384000] Starting system daemons...",
    "[    0.416000] Initializing SELinux...",
    "[    0.448000] Loading system services...",
    "[    0.480000] Initializing Ruby OS core...",
    "[    0.512000] Loading hardware abstraction layer...",
    "[    0.544000] Setting up memory management...",
    "[    0.576000] Checking available storage...",
    "[    0.608000] Starting Ruby shell...",
    "[    0.640000] Detecting connected devices...",
    "[    0.672000] Starting display server...",
    "[    0.704000] Configuring input devices...",
    "[    0.736000] Setting up security policies...",
    "[    0.768000] Launching Ruby process manager...",
    "[    0.800000] Loading user space applications...",
    "[    0.832000] Checking internet connection...",
    "[    0.864000] Running system diagnostics...",
    "[    0.896000] Boot optimization in progress...",
    "[    0.928000] Enabling sound system...",
    "[    0.960000] Starting background services...",
    "[    0.992000] Preparing graphical environment...",
    "[    1.024000] Verifying installed applications...",
    "[    1.056000] Checking for updates...",
    "[    1.088000] Loading Ruby runtime...",
    "[    1.120000] Enabling GPU acceleration...",
    "[    1.152000] Starting compositor...",
    "[    1.184000] Initializing user session...",
    "[    1.216000] Finalizing system setup...",
    "[    1.248000] Ruby OS boot complete!"
]

# Dodatnih 160 koraka
boot_logs += [
    "[    1.280000] Allocating process table...",
    "[    1.312000] Running garbage collector...",
    "[    1.344000] Initializing kernel modules...",
    "[    1.376000] Configuring system clock...",
    "[    1.408000] Loading device tree...",
    "[    1.440000] Checking disk partitions...",
    "[    1.472000] Verifying bootloader integrity...",
    "[    1.504000] Starting system monitoring service...",
    "[    1.536000] Enabling swap space...",
    "[    1.568000] Checking battery status...",
    "[    1.600000] Enabling wireless interfaces...",
    "[    1.632000] Detecting USB peripherals...",
    "[    1.664000] Mounting additional storage...",
    "[    1.696000] Configuring user permissions...",
    "[    1.728000] Initializing audio drivers...",
    "[    1.760000] Checking system temperature...",
    "[    1.792000] Starting Ruby desktop environment...",
    "[    1.824000] Enabling network time synchronization...",
    "[    1.856000] Running startup scripts...",
    "[    1.888000] Checking system logs...",
    "[    1.920000] Finalizing network configuration...",
    "[    1.952000] Starting firewall service...",
    "[    1.984000] Scanning for malware...",
    "[    2.016000] Loading user preferences...",
    "[    2.048000] Adjusting power settings...",
    "[    2.080000] Initializing Ruby software repository...",
    "[    2.112000] Verifying file system integrity...",
    "[    2.144000] Optimizing boot sequence...",
    "[    2.176000] Loading Ruby shell extensions...",
    "[    2.208000] Checking active connections...",
    "[    2.240000] Enabling touch input support...",
    "[    2.272000] Preparing graphical assets...",
    "[    2.304000] Starting Ruby OS services...",
    "[    2.336000] Configuring kernel scheduler...",
    "[    2.368000] Starting process manager...",
    "[    2.400000] Checking thermal management...",
    "[    2.432000] Applying system updates...",
    "[    2.464000] Validating user authentication...",
    "[    2.496000] Cleaning temporary files...",
    "[    2.528000] Configuring network security...",
    "[    2.560000] Initializing package manager...",
    "[    2.592000] Synchronizing time settings...",
    "[    2.624000] Running background maintenance tasks...",
    "[    2.656000] Setting default applications...",
    "[    2.688000] Checking hardware compatibility...",
    "[    2.720000] Tuning system performance...",
    "[    2.752000] Preparing user workspaces...",
    "[    2.784000] Monitoring system activity...",
    "[    2.816000] Starting event dispatcher...",
    "[    2.848000] Cleaning obsolete cache files...",
    "[    2.880000] Activating system monitoring tools...",
    "[    2.912000] Verifying user permissions...",
    "[    2.944000] Loading configuration settings...",
    "[    2.976000] Checking software dependencies...",
    "[    3.008000] Running system validation tests...",
    "[    3.040000] Enabling device synchronization...",
    "[    3.072000] Boot process finalizing...",
    "[    3.104000] Ruby OS is now ready!"
]

for i, log in enumerate(boot_logs):
    color = random.choice(colors)  # Nasumično bira boju
    print(color + log + reset)
    time.sleep(0.01)

# Simulacija Android boot animacije
frames = [
    "   █    ",
    "  ███   ",
    " █████  ",
    "███████ ",
    " █████  ",
    "  ███   ",
    "   █    "
]

print("GRUB 2.0\n")

for _ in range(10):  # Petlja za animaciju
    for frame in frames:
        sys.stdout.write("\r" + "\033[34m" + frame + reset)  # Plava boja
        sys.stdout.flush()
        time.sleep(0.2)

print("\n\nSystem Ready!")

  
       
def main():
    os.chdir("home/usr")
    welcome()
    loading_kernel()
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
            game_manager()
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
            run_exe()
        elif choice == '19':
            dodaci()
        elif choice == '20':
            clear_screen()
            print("Isključivanje...")
            print("-$ sudo stop kernel")
            print("...")
            time.sleep(2)
            print("-$ sudo stop system")
            time.sleep(2)
            break
        elif choice == 'konami':
            konami_easter_egg()
        elif choice == 'fridaythe13':
            friday_the_13th_easter_egg()
        else:
            print("Nevažeća opcija, pokušajte ponovo.")

if __name__ == "__main__":
    main()