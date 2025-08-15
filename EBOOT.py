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
        "id": "tool4",
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
        "id": "tool6",
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
KERNL = "kernel/kernel.py"
ntoskrnl = "kernel/ntoskrnl.sys"
bootmgfw = "kernel/bootmgfw.efi"
rukernel = "kernel/rukernel.sys"
keyboarddriver = "drivers/keyboard.c"
displaydriver = "drivers/display.c"
batterydriver = "drivers/battery.c"
mousedriver = "drivers/mouse.c"
networkdriver = "drivers/network.c"
powerdriver = "drivers/power.c"
sounddriver = "drivers/sound.c"
storagedriver = "drivers/storage.c"
usbdriver = "drivers/usb.c"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def welcome():
    clear_screen()
    print(f"Welcome to{BLUE} Ruby OS")
    print("\033[0m")
    
        
def man():
    man_pages = {
        "help": "Displays all available commands.",
        "clear": "Clears the screen.",
        "exit": "Closes the terminal.",
        "man": "Displays an explanation for a command.",
        "echo": "Prints the text entered by the user.",
        "date": "Shows the date and time.",
        "cp": "Copies a file from one place to another.",
        "mv": "Moves a file from one place to another.",
        "ls": "Lists the files in the current directory.",
        "cd": "Changes the directory.",
        "web": "Opens the web browser.",
        "sudo su": "Grants you root access.",
        "free": "Shows how much disk space is available.",
        "rpm": "Opens the Ruby Packing Manager where you can install various tools.",
        "ruby update": "Updates the system.",
        "pwd": "Displays the current directory."
    }

    choice = input("Which command do you want? ").strip()
    if choice in man_pages:
        print(man_pages[choice])
    else:
        print("We haven't added that command yet!")
        
        
def adminmode():
    while True:
        print("\n=== Ruby OS Admin Mode ===")
        print("1) View users")
        print("2) System information")
        print("3) Show log file")
        print("4) Restart system")
        print("5) Emergency Shutdown")
        print("6) Exit admin mode")

        choice = input("admin> ").strip()

        if choice == "1":
            print("root")
        elif choice == "2":
            print("Ruby OS v1.0\nKernel: Ruby krnl 1.3.6\nUptime: {unknown_s__m__h__d__w__m__y}")
        elif choice == "3":
            print("[INFO] - Request boot() function in kernel/kernel.py to EBOOT.py")
            print("[INFO] - Request to start RUBY OS from 0x0001 in kernel/kernel.py")
            print("[LOG] - Trying to start Ruby OS from 0x0001 ...")
            print("[INFO] - Ruby OS is started in 0x0001")
            print("[INFO] - Checking for drivers and system files...")
            print("[INFO] - Request to show grubboot() function to user")
            print("[INFO] - Trying to show grubboot() function to user")
            print("[INFO] - Booting Ruby OS in memory 0x0001")
            print("[WARNING] - In mode 0x0001 file ntoskrnl.sys is trying to launch mode 0x0000000")
            print("[INFO] - Request to put Ruby OS in RAM in 0x0001")
            print("[INFO] - Trying to put Ruby OS in 0x0000012 ...")
            print("[ERROR] - Attemt to put Ruby OS in slot 0x0000012 is Unsuccesful (error code : A0xz6sn)")
            print("[WARNING] - RAM slot 0x0000012 is full!")
            print("[INFO] - RUBY OS is put in slot 0x000034!")
            print("[INFO] - System installed!")
            print("[INFO] - Logged as root")
        elif choice == "4":
            print("Restarting system...")
            loading_kernel()
        elif choice == "5":
            shutdown = input("Are you sure you want to emergency shutdown the system? You will lose all unsaved data (y/n): ").strip().lower()
            if shutdown == "y":
                print("Emergency shutdown initiated.")
                clear_screen()
                print("Shutting down the system...")
                sys.exit()
            else:
                print("Emergency shutdown canceled.")

        elif choice == "6":
            print("Exiting admin mode.")
            break
        else:
            print("Unknown option.")
        

def add_device():
    devices = [
        # Original list
        "Standard USB Host Controller",
        "Intel 8255x Ethernet Adapter",
        "VIA AC'97 Audio Controller",
        "Microsoft PS/2 Mouse",
        "Standard VGA Graphics Adapter",
        "Realtek RTL8139 Fast Ethernet NIC",
        "Generic USB Hub",
        "Generic Mass Storage Device",
        "Standard Floppy Disk Controller",
        "Creative Sound Blaster 16",
        "Intel Pentium CPU",
        "PS/2 Compatible Keyboard",
        "IDE Channel Primary",
        "IDE Channel Secondary",
        "Matrox Millennium G200",
        "NEC PCI to USB Enhanced Host Controller",
        "Legacy Game Port",
        "Infrared Port",
        "PCI Bus",
        "Plug and Play Software Device Enumerator",
        "Intel 82801 PCI Bridge",
        "ACPI-compliant System",
        "Texas Instruments OHCI Compliant IEEE 1394 Host Controller",
        "NVIDIA RIVA TNT2 Model 64",
        "Intel 440BX AGPset",
        "Dial-Up Modem",
        "COM1 Serial Port",
        "LPT1 Printer Port",
        "Generic Infrared Serial Port",
        "Standard Enhanced PCI to USB Host Controller",
        "Generic IDE Disk Type 47",
        "3Com EtherLink XL 10/100 PCI NIC",
        "S3 Trio64V2/DX",
        "Cirrus Logic GD5446",
        "AMD PCNET Family PCI Ethernet Adapter",
        "ALi M5229 PCI Bus Master IDE Controller",
        "Intel i810 Graphics Controller",
        "Yamaha OPL3-SAx Sound System",

        # Extra modern & retro hardware
        "Intel Core 2 Duo CPU",
        "Intel HD Graphics 4000",
        "NVIDIA GeForce GTX 1050 Ti",
        "AMD Radeon RX 570",
        "Intel AX200 Wi-Fi 6 Adapter",
        "Qualcomm Atheros AR9285 Wireless Network Adapter",
        "Broadcom NetXtreme Gigabit Ethernet",
        "Logitech USB Webcam",
        "HP LaserJet 1018 Printer",
        "Canon PIXMA iP2700 Printer",
        "Bluetooth Radio Adapter",
        "Samsung SSD 860 EVO 500GB",
        "Western Digital WD Blue 1TB",
        "Kingston HyperX Fury DDR4 8GB",
        "Corsair Vengeance LPX DDR4 16GB",
        "Raspberry Pi GPIO Controller",
        "Arduino Uno R3",
        "Elgato Game Capture HD",
        "Xbox 360 Controller",
        "PlayStation DualShock 4 Controller",
        "Wacom Intuos Graphics Tablet",
        "Oculus Rift VR Headset",
        "HTC Vive Base Station",
        "Intel Optane Memory Module",
        "TP-Link TL-WN722N USB Wi-Fi Adapter",
        "Seagate Barracuda 2TB HDD",
        "Asus Xonar DGX Sound Card",
        "M-Audio Fast Track USB Audio Interface",

        # Keyboards
        "Logitech G Pro Mechanical Keyboard",
        "Razer Huntsman Elite Keyboard",
        "Corsair K70 RGB MK.2 Keyboard",
        "SteelSeries Apex Pro Keyboard",
        "HyperX Alloy FPS Pro Keyboard",
        "Apple Magic Keyboard",
        "Microsoft Ergonomic Keyboard",
        "Cooler Master CK550 Mechanical Keyboard",

        # Mice
        "Logitech G502 HERO Mouse",
        "Razer DeathAdder Elite Mouse",
        "SteelSeries Rival 600 Mouse",
        "Glorious Model O Gaming Mouse",
        "Apple Magic Mouse 2",
        "Microsoft Classic IntelliMouse",
        "Cooler Master MM710 Lightweight Mouse",

        # Headsets & Headphones
        "HyperX Cloud II Gaming Headset",
        "SteelSeries Arctis 7 Wireless Headset",
        "Razer Kraken Tournament Edition",
        "Corsair HS60 Pro Surround Headset",
        "Sony WH-1000XM4 Headphones",
        "Bose QuietComfort 35 II",
        "Apple AirPods Pro",
        "Logitech G935 Wireless Gaming Headset",

        # Touchscreens & Touch devices
        "Dell P2418HT Touchscreen Monitor",
        "ASUS VT229H Touchscreen Monitor",
        "HP EliteDisplay E230t Touchscreen",
        "Wacom Cintiq Pro 24 Touch",
        "Microsoft Surface Touchscreen",
        "Samsung Galaxy Tab S7 Touch Display",
        "Lenovo ThinkPad Touch Display",
        "iPad Pro Touchscreen"
    ]

    print("Add New Hardware Wizard\n------------------------")
    input("Press Enter to begin hardware installation...")

    print("\nAvailable Devices:")
    for i, device in enumerate(devices, start=1):
        print(f"{i}. {device}")

    choice = input("\nEnter the name of the device you connected: ")

    print(f"\nSearching for drivers for '{choice}'...")

    # Loading bar animation
    for i in range(11):
        bar = "█" * i + "-" * (10 - i)
        print(f"\r[{bar}] {i * 10}%", end="")
        sys.stdout.flush()
        time.sleep(random.uniform(0.15, 0.4))

    print(f"\n\nDevice '{choice}' successfully installed.")
    print("System may require restart for changes to take effect.\n")
    os.system("cd ..")
    os.system("cd ..")
    print("Restarting...")
    time.sleep(5)
    loading_kernel()


def game_manager():
    print("\n🎮 Welcome to Ruby OS Game Manager! 🎮")
    games = {
        "1": ("Guess the Number", game_guess_number),
        "2": ("Snake (Coming Soon)", game_snake),
        "3": ("Rock, Paper, Scissors", game_rps),
        "4": ("Tic Tac Toe", game_ttt),
        "5": ("Quick Numbers", game_quick_numbers)
    }
    
    while True:
        print("\nChoose a game or 0 to exit:")
        for key, (name, _) in games.items():
            print(f"{key}. {name}")
        print("0. Exit Game Manager")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '0':
            print("Exiting Game Manager...")
            break
        elif choice in games:
            print(f"\nLaunching game: {games[choice][0]}\n")
            games[choice][1]()
        else:
            print("Unknown option, please try again.")

def game_guess_number():
    number = random.randint(1, 50)
    attempts = 0
    print("Guess the number between 1 and 50!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < number:
                print("The number is higher.")
            else:
                print("The number is lower.")
        except ValueError:
            print("Please enter a valid number.")

def game_snake():
    print("The Snake game is under development. Please enjoy the other games for now!")

def game_rps():
    options = ['rock', 'paper', 'scissors']
    print("Game: Rock, Paper, Scissors!")
    while True:
        user = input("Choose (rock/paper/scissors) or 'exit' to quit: ").lower()
        if user == 'exit':
            print("Exiting game.")
            break
        if user not in options:
            print("Unknown option.")
            continue
        
        comp = random.choice(options)
        print(f"Computer chose: {comp}")
        
        if user == comp:
            print("It's a draw!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("You win!")
        else:
            print("You lose!")

def game_ttt():
    # Two-player Tic Tac Toe game
    board = [' ' for _ in range(9)]
    
    def print_board():
        print()
        for i in range(3):
            print(" " + " | ".join(board[i*3:(i+1)*3]))
            if i < 2:
                print("---+---+---")
        print()

    def check_win(player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # horizontal
            [0,3,6], [1,4,7], [2,5,8],  # vertical
            [0,4,8], [2,4,6]            # diagonal
        ]
        for cond in win_conditions:
            if all(board[i] == player for i in cond):
                return True
        return False

    def check_draw():
        return all(s != ' ' for s in board)

    player_turn = 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Player {player_turn}, choose a cell (1-9): "))
            if move < 1 or move > 9:
                print("Enter a number between 1 and 9.")
                continue
            if board[move-1] != ' ':
                print("Cell is already occupied.")
                continue
            board[move-1] = player_turn
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if check_win(player_turn):
            print_board()
            print(f"Player {player_turn} wins! 🎉")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
        player_turn = 'O' if player_turn == 'X' else 'X'

def game_quick_numbers():
    print("Welcome to 'Quick Numbers'!")
    print("Type the numbers as fast as you can. You have 10 seconds.")
    start = time.time()
    score = 0
    while time.time() - start < 10:
        number = random.randint(1, 100)
        print(f"Type this number: {number}")
        try:
            response = int(input("Your input: "))
            if response == number:
                score += 1
                print("Correct! +1 point")
            else:
                print("Incorrect!")
        except ValueError:
            print("Invalid input.")
    print(f"Game over! You scored {score} points.")
    
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
        print(f"\n📁 Current directory: {current_dir}")
        for item in os.listdir(current_dir):
            print(" └──", item)
        print()

    def change_dir(new_path):
        nonlocal current_dir
        if os.path.isdir(new_path):
            current_dir = os.path.abspath(new_path)
            print(f"✅ Changed directory to: {current_dir}")
        else:
            print("❌ Path does not exist.")

    def extract_zip():
        zip_path = input("📦 Enter ZIP file name (or full path): ")
        full_zip_path = os.path.join(current_dir, zip_path) if not os.path.isabs(zip_path) else zip_path
        if not os.path.isfile(full_zip_path):
            print("❌ ZIP file does not exist.")
            return
        extract_to = input("📁 Enter extraction directory (or press Enter for default): ") or os.path.splitext(full_zip_path)[0]
        os.makedirs(extract_to, exist_ok=True)
        os.system(f'unzip -o "{full_zip_path}" -d "{extract_to}"')
        print(f"✅ Extracted to '{extract_to}'\n")

    def create_zip():
        folder = input("📂 Enter folder name to ZIP: ")
        full_folder_path = os.path.join(current_dir, folder) if not os.path.isabs(folder) else folder
        if not os.path.isdir(full_folder_path):
            print("❌ Folder does not exist.")
            return
        zip_name = input("📦 Enter name for ZIP file (or press Enter for default): ") or (folder.rstrip("/").rstrip("\\") + ".zip")
        zip_name = os.path.join(current_dir, zip_name) if not os.path.isabs(zip_name) else zip_name
        os.system(f'zip -r "{zip_name}" "{full_folder_path}"')
        print(f"✅ ZIP file created: {zip_name}\n")

    while True:
        print("\n========== 📦 ZIP MENU 📦 ==========")
        print(f"📂 Current dir: {current_dir}")
        print("1️⃣  List files")
        print("2️⃣  Change directory")
        print("3️⃣  Extract ZIP file")
        print("4️⃣  Create ZIP file")
        print("5️⃣  Exit")
        choice = input("👉 Choose an option (1-5): ")

        if choice == "1":
            list_dir()
        elif choice == "2":
            new_path = input("📂 Enter new path: ")
            change_dir(new_path)
        elif choice == "3":
            extract_zip()
        elif choice == "4":
            create_zip()
        elif choice == "5":
            print("👋 Exiting ZIP Manager.")
            break
        else:
            print("⚠️ Invalid option, please try again.")

    

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Successfully moved: {source} → {destination}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}")

def cp(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Successfully copied: {source} → {destination}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}")

def cp_r(source, destination):
    try:
        shutil.copytree(source, destination)
        print(f"Successfully copied directory: {source} → {destination}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}")
    
import os
import sys
import time
import shutil
import random

def bsod(auto_reboot=True, reboot_delay=5):
    """
    Fake 'Red Screen of Death' sa Linux kernel panic porukom za Ruby OS.
    """
    # Dimenzije terminala
    try:
        cols, rows = shutil.get_terminal_size(fallback=(80, 24))
    except Exception:
        cols, rows = (80, 24)

    # ANSI boje: crvena pozadina, crni tekst
    RED_BG = "\033[41m"
    BLACK_FG = "\033[30m"
    RESET   = "\033[0m"

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    clear()

    # Kernel panic poruka
    title = "Kernel panic - not syncing: Ruby OS kernel encountered fatal exception"
    stop_code = f" STOP CODE: RUBY_OS_KERNEL_PANIC_{random.randint(1000,9999)}"
    hint = " Please report this incident to rubyosofficial@gmail.com and reboot the system manualy"
    percent = 0

    while percent <= 100:
        clear()
        print(RED_BG + BLACK_FG, end="")

        # ASCII znak upozorenja
        face = " [!!] KERNEL PANIC"
        print(face.ljust(cols))

        # Wrap funkcija za tekst
        def wrap(txt, width):
            words, line, lines = txt.split(), "", []
            for w in words:
                if len(line) + len(w) + 1 <= width:
                    line = (line + " " + w).strip()
                else:
                    lines.append(line)
                    line = w
            if line:
                lines.append(line)
            return lines

        for tline in wrap(title, cols - 1):
            print(tline.ljust(cols))

        pct_line = f" Collecting crash dump... {percent}%"
        print(pct_line.ljust(cols))

        # Popuni ostatak ekrana
        used = 1 + len(wrap(title, cols - 1)) + 1
        remaining = max(rows - used - 4, 0)
        for _ in range(remaining):
            print(" ".ljust(cols))

        print(stop_code.ljust(cols))
        print(hint.ljust(cols))
        print(RESET, end="")

        percent += random.choice([1, 2, 3, 4])
        percent = min(percent, 100)
        time.sleep(0.08)

    if auto_reboot:
        for sec in range(reboot_delay, 0, -1):
            clear()
            print(RED_BG + BLACK_FG, end="")
            msg = f" Rebooting system in {sec}..."
            print(msg.ljust(cols))
            for _ in range(rows - 1):
                print(" ".ljust(cols))
            print(RESET, end="")
            time.sleep(1)
        try:
            loading_kernel()
        except NameError:
            clear()
            print("Rebooting (simulation)...")
            time.sleep(1)
    else:
        print("\nPress Enter to continue...")
        input()
    
def ram4test():
    
    if total_ram < 64:
        print("Not enough RAM for Ruby OS!")
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
    
    
options = ["Ruby OS", "Ruby OS Recovery", "Ruby OS RAM Recovery", "Shutdown"]


def draw_menu(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(0)
    stdscr.timeout(100)
    
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 5, "GRUB 2.0 Bootloader", curses.A_BOLD)
        stdscr.addstr(1, 5, "Use ↑ and ↓ to navigate, Enter to select", curses.A_DIM)

        
        for idx, option in enumerate(options):
            x = 5
            y = idx + 3
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
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
        elif key == ord("\n"):
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
            
            break

curses.wrapper(draw_menu)                        
    

def web():
    print("🌐 Welcome to the Web")
    print("1. Google")
    print("2. DuckDuckGo")
    print("3. Firefox")
    print("4. HTML Reader")
    print("5.Costum URL")
    print("6. Exit")

    while True:
        choice = input("Choose an option: ")

        if choice == '1':
            webbrowser.open("https://google.com")
        elif choice == '2':
            webbrowser.open("https://duckduckgo.com")
        elif choice == '3':
            webbrowser.open("https://firefox.com")
        elif choice == '4':
            html()
        elif choice == '5':
            url = input("Enter the url : ")
            webbrowser.open(url)
        elif choice == '6':
            print("Exiting Web...")
            break
        else:
            print("❌ Invalid option, try again.")
                

import requests
from bs4 import BeautifulSoup

def html():
    url = input("Enter URL: ").strip()

    # If the user doesn't include http or https, prepend https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        print("\n📄 HTML Content:\n")
        print(soup.prettify())
    except requests.exceptions.RequestException as e:
        print(f"❌ Error while fetching the URL: {e}")
            

def init_screen():
    curses.initscr()
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    curses.curs_set(0)  # Hide cursor
    win.keypad(1)
    win.nodelay(0)
    return win

def draw_pixel(win, x, y, char="█"):
    win.addch(y, x, char)

def main4paint(win):
    win.clear()
    curses.curs_set(0)

    h, w = win.getmaxyx()
    x, y = w // 2, h // 2  # Starting "mouse" position

    pixels = set()  # Set to store drawn pixels

    while True:
        win.clear()

        # Draw all pixels
        for px, py in pixels:
            draw_pixel(win, px, py)

        # Show cursor
        draw_pixel(win, x, y, "X")

        win.refresh()
        key = win.getch()

        if key == ord('q'):  # Exit
            break
        elif key == curses.KEY_UP:
            y = max(0, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(h - 1, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(w - 1, x + 1)
        elif key == 10:  # Enter - draw pixel
            pixels.add((x, y))
        elif key == 8 or key == 127:  # Backspace - erase pixel
            pixels.discard((x, y))

# Game parameters
screen_width = 20
screen_height = 10
player_x = 1
player_y = 1
score = 0

# World map with walls, empty space and points
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

# Function to draw the map
def draw_map():
    global player_x, player_y
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

    # Convert map to list of characters to update player position
    map_lines = [list(line) for line in game_map]

    # Set player position on the map
    map_lines[player_y][player_x] = '@'

    # Print the map
    for row in map_lines:
        print(''.join(row))

    # Show score
    print(f"Score: {score}")

# Function to move the player
def move_player(direction):
    global player_x, player_y, score

    # Move based on pressed key if not hitting wall
    if direction == 'w' and game_map[player_y - 1][player_x] != '#':
        player_y -= 1
    elif direction == 's' and game_map[player_y + 1][player_x] != '#':
        player_y += 1
    elif direction == 'a' and game_map[player_y][player_x - 1] != '#':
        player_x -= 1
    elif direction == 'd' and game_map[player_y][player_x + 1] != '#':
        player_x += 1

    # If player collects a point
    if game_map[player_y][player_x] == '*':
        score += 1
        # Replace it with empty space
        game_map[player_y] = game_map[player_y][:player_x] + '.' + game_map[player_y][player_x + 1:]

# Main function to run the game
def main2testgame():
    global player_x, player_y, score

    while True:
        draw_map()
        key = input("Press W/A/S/D to move or Q to quit: ")

        if key.lower() == 'q':
            print(f"Game over. Score: {score}")
            break
        elif key.lower() in ['w', 'a', 's', 'd']:
            move_player(key.lower())

        time.sleep(0.2)


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
    url = "https://www.google.com"
    start_time = time.time()
    
    response = requests.get(url)
    
    end_time = time.time()
    download_time = end_time - start_time
    print(f"Download time: {download_time:.2f} seconds")
    
    
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
        
installed_tools = []

def display_menu():
    print("=== XHack ===")
    print("1. Display data")
    print("2. Network scanning")
    print("3. File downloading")
    print("4. Create backdoor")
    print("5. Data encryption")
    print("6. Execute script")
    print("7. WiFi hacking")
    print("8. Bluetooth hacking")
    print("9. Password generation")
    print("10. Server attack")
    print("11. Bluetooth spam")
    print("12. RFID card emulation")
    print("13. IR signal scanning")
    print("14. IR remote imitation")
    print("15. USB device scanning")
    print("16. GPS location emulation")
    print("17. WiMAX network scanning")
    print("18. Facebook hacking")
    print("19. Virus generation")
    print("20. Social engineering attack simulation")
    print("21. USB device scanning")
    print("22. GPS location emulation")
    print("23. WiMAX network scanning")
    print("24. Facebook hacking")
    print("25. Virus generation")
    print("0. Exit")
    print("=============================")

def fake_hacking(action, details):
    print(f"\nExecuting: {action}...")
    time.sleep(2)
    print(details)
    time.sleep(random.uniform(1, 3))
    print(f"Operation '{action}' completed!\n")

def generate_fake_password():
    length = random.randint(8, 12)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated fake password: {password}\n")

def simulate_server_attack():
    print("Simulating server attack...")
    time.sleep(2)
    print("Gathering server information...")
    time.sleep(2)
    print("Launching DDoS attack...")
    time.sleep(2)
    print("Attack successful! Server is under control!\n")

def bluetooth_spam():
    print("Starting Bluetooth spam...")
    time.sleep(2)
    print("Scanning available Bluetooth devices...")
    time.sleep(2)
    devices = ["Samsung A54", "Oppo XC", "Lenovo 4th Gen", "ASUS"]
    for device in devices:
        print(f"Sending spam messages to {device}...")
        time.sleep(1)
        print(f"Spam message successfully sent to {device}!")
    print("Bluetooth spam completed!\n")

def emulate_rfid():
    print("Emulating RFID card...")
    time.sleep(2)
    print("Searching for available RFID readers...")
    time.sleep(2)
    print("Emulation successful! RFID card is active and ready to use!\n")

def scan_ir_signals():
    print("Scanning infrared signals...")
    time.sleep(2)
    print("Collecting information about available IR devices...")
    time.sleep(2)
    print("Scan complete! Found IR devices: TV, Air Conditioner, DVD Player.\n")

def imitate_ir_remote():
    print("Imitating IR remote control...")
    time.sleep(2)
    devices = ["TV", "Air Conditioner", "DVD Player"]
    for device in devices:
        print(f"Sending power-on command to {device}...")
        time.sleep(1)
        print(f"{device} powered on successfully!")
    print("\nChoose a device to control:")
    print("1. TV")
    print("2. Air Conditioner")
    choice = input("Choose an option (1-2): ")
    if choice == '1':
        control_tv()
    elif choice == '2':
        print("Controlling Air Conditioner... Power on/off successful!")
    else:
        print("Unknown option.")

def control_tv():
    print("Controlling TV...")
    time.sleep(1)
    print("Choose an option:")
    print("1. Turn on TV")
    print("2. Turn off TV")
    choice = input("Choose an option (1-2): ")
    if choice == '1':
        print("Turning on TV... Success!")
    elif choice == '2':
        print("Turning off TV... Success!")
    else:
        print("Unknown option.")

def scan_usb_devices():
    print("Scanning USB devices...")
    time.sleep(2)
    print("Found USB devices: USB flash drive, USB keyboard, USB mouse...")
    time.sleep(2)
    print("Scan complete!\n")

def emulate_gps_location():
    print("Emulating GPS location...")
    time.sleep(2)
    print("Searching available GPS locations...")
    time.sleep(2)
    print("Emulation successful! GPS location is active and ready to use!\n")

def scan_wimax_network():
    print("Scanning WiMAX network...")
    time.sleep(2)
    print("Gathering information about WiMAX network...")
    time.sleep(2)
    print("Scan complete! WiMAX network information found...\n")

def fake_facebook_hack():
    print("Fake hacking Facebook profile...")
    time.sleep(2)
    print("Gathering Facebook profile information...")
    time.sleep(2)
    print("Fake hack successful! Facebook profile is under control!\n")

def generate_fake_virus():
    print("Generating fake virus...")
    time.sleep(2)
    print("Creating fake virus...")
    time.sleep(2)
    print("Fake virus created! Ready to use...\n")

def main2hack():
    while True:
        display_menu()
        choice = input("Choose an option (0-25): ")

        if choice == '1':
            fake_hacking("Displaying data", "Showing user data and sensitive information... Accessing database and searching user profiles...")
        elif choice == '2':
            fake_hacking("Network scanning", "Scanning available IP addresses and open ports... Gathering network topology and active devices...")
        elif choice == '3':
            fake_hacking("File downloading", "Downloading secret files from remote server... Verifying file integrity before download...")
        elif choice == '4':
            fake_hacking("Creating backdoor", "Creating a secret entrance for future attacks... Establishing persistent connection with server for further control...")
        elif choice == '5':
            fake_hacking("Data encryption", "Encrypting sensitive data to protect it... Using AES encryption algorithm and storing data securely...")
        elif choice == '6':
            fake_hacking("Executing script", "Running attack automation script... Script runs with administrator privileges for faster execution...")
        elif choice == '7':
            fake_hacking("WiFi hacking", "Collected information about nearby WiFi networks... Trying to connect to the strongest network using brute-force attack...")
        elif choice == '8':
            fake_hacking("Bluetooth hacking", "Scanning available Bluetooth devices... Finding vulnerable devices nearby and attempting connection...")
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
        elif choice == '17':
            scan_wimax_network()
        elif choice == '18':
            fake_facebook_hack()
        elif choice == '19':
            generate_fake_virus()
        elif choice == '20':
            print("Simulating social engineering attack...")
            time.sleep(2)
            print("Collecting victim information...")
            time.sleep(2)
            print("Simulation successful! Victim is under control!\n")
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
            print("Exiting program...")
            break
        else:
            print("Unknown option, please try again.")
            
INSTALLED_TOOLS_FILE = "installed_tools.json"


installed_tools = []

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

def save_installed_tools():
    with open(INSTALLED_TOOLS_FILE, "w") as file:
        json.dump([tool["id"] for tool in installed_tools], file)

def list_tools():
    print("\n=== Available Tools ===")
    for idx, tool in enumerate(tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
        print(f"   Description: {tool['description']}")
        print(f"   Category: {tool['category']}\n")

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
            time.sleep(2)
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
            time.sleep(1)
            print("Setting up liberror-perl (x.x.x) ...")
            time.sleep(3)
            print(f"Setting up '{tool['name']}'-man (x.x.x) ...")
            time.sleep(4)
            print(f"Setting up '{tool['name']}' (x.x.x) ...")
            time.sleep(3)
            print("Processing triggers for man-db (x.x.x) ...")
            time.sleep(5)
            print(f"'{tool['name']}' successfully installed!")
            time.sleep(2)
            installed_tools.append(tool)
            save_installed_tools()
            print(f"'{tool['name']}' installed successfully!\n")
    except IndexError:
        print("\nInvalid choice. Please try again.\n")

def list_installed_tools():
    if not installed_tools:
        print("\nNo tools installed yet.\n")
        return

    print("\n=== Installed Tools ===")
    for idx, tool in enumerate(installed_tools, start=1):
        print(f"{idx}. {tool['name']} (v{tool['version']})")
    print()

def run_installed_tool(choice):
    try:
        tool = installed_tools[choice - 1]
        print(f"\nRunning '{tool['name']}'...\n")
        tool["function"]()
    except IndexError:
        print("\nInvalid choice. Please try again.\n")

def pac():
    load_installed_tools()
    
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
   
    
ROOT_STATUS_FILE = "root_status.txt"

def save_root_status(status):
    with open(ROOT_STATUS_FILE, 'w') as f:
        f.write(str(status))

def load_root_status():
    try:
        with open(ROOT_STATUS_FILE, 'r') as f:
            return f.read().strip() == 'True'
    except FileNotFoundError:
        return False

root_status = load_root_status()

def root_system():
    global root_status  # Use global variable for root status
    
    # Prompt for username and password
    username = input("[ SUDO ] Enter username: ")
    password = input("[ SUDO ] Enter password: ")
    
    # Hash the entered password for secure comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Open the users file and verify credentials
        with open(USERS_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(',')
                
                # Check if username and hashed password match
                if username == stored_username and hashed_password == stored_password:
                    print("✅ Root access granted!")
                    root_status = True  # Set root status to True
                    save_root_status(True)  # Save root status persistently
                    print("Type 'sudo -root -h' to see root commands.")
                    return  # Exit after successful login

        # If no matching user found
        print("❌ Incorrect username or password.")
    
    except FileNotFoundError:
        print(f"⚠️ Error: The file {USERS_FILE} does not exist.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")    
      

DEV_FILE = os.path.join(BASE_DIR, "home", "usr", "dev_file.txt")
DEV_PASSWORD = "rubyisgood666"
SERVER_FILE = os.path.join(BASE_DIR, "home", "usr", "server_file.txt")

def is_dev():
    if os.path.exists(DEV_FILE):
        with open(DEV_FILE, "r") as f:
            return f.read().strip() == "dev=True"
    return False

def set_dev_status(status):
    with open(DEV_FILE, "w") as f:
        f.write(f"dev={status}")
        
def is_server():
    if os.path.exists(SERVER_FILE):
        with open(SERVER_FILE, "r") as f:
            return f.read().strip() == "server=True"
    return False

def set_server_status(status):
    with open(SERVER_FILE, "w") as f:
        f.write(f"server={status}")

def opt():
    print("Select your device for installation:")
    print("1. Standard Installation (Desktop PC)")
    print("2. Portable Installation (Laptop, Phone, Tablet)")
    print("3. Server Installation (For Servers)")
    print("4. Developer Installation (Developers only)")

    while True:
        choice = input("Enter setup option: ").strip()

        if choice == '1':
            set_dev_status("False")
            print("Please restart your computer.")
            sys.exit()
        elif choice == '2':
            set_dev_status("False")
            print("Please restart your computer.")
            sys.exit()
        elif choice == '3':
            set_server_status("True")
            print("Please restart your computer.")
            sys.exit()
        elif choice == '4':
            password = input("Enter developer mode password: ")
            if password == DEV_PASSWORD:
                print("Password verified. Developer mode enabled.")
                set_dev_status("True")
                print("Please restart your computer.")
                sys.exit()
            else:
                print("Invalid password! Developer mode not enabled.")
        else:
            print("Invalid input! Please try again.")

dev = is_dev()


def show_memory_usage():
    memory = psutil.virtual_memory()
    
    total_memory = memory.total / (1024 ** 3)
    used_memory = memory.used / (1024 ** 3)
    free_memory = memory.free / (1024 ** 3)
    percent_used = memory.percent
    
    print(f"Total memory: {total_memory:.2f} GB")
    print(f"Used memory: {used_memory:.2f} GB ({percent_used}%)")
    print(f"Free memory: {free_memory:.2f} GB")
    


def neofetch():
    ascii_logo = """
____  _   _ ______   _____  ____
|  _ \| | | | __ ) \ / / _ \/ ___|
| |_) | | | |  _ \ V / | | \___ \ 
|  _ <| |_| | |_) || || |_| |___) |
|_| \_\\___/|____/ |_| \___/|____/
    """

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
        choice = input("~root@ruby$ ").strip().lower()
        
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
            src = input("Enter source file or directory: ").strip()
            dst = input("Enter destination: ").strip()
            mv(src, dst)
            
        elif choice == "cp":
            src = input("Enter source file: ").strip()
            dst = input("Enter destination: ").strip()
            cp(src, dst)
        
        elif choice == "cp -r":
            src = input("Enter source directory: ").strip()
            dst = input("Enter destination: ").strip()
            cp_r(src, dst)
           
        elif choice == "pip":
            pip()
            
        elif choice == "sudo selcboot-adminmode && sudo reboot":
            print("Selecting Boot Mode to Admin Mode...")
            time.sleep(3)
            clear_screen()
            time.sleep(2)
            print("Rebooting...")
            time.sleep(3)
            clear_screen()
            adminmode()
                        
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
            
        elif choice == 'sudo su':
            root_system()
            
        elif choice == 'code':
            programming()
            
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
                print(f"\r[{bar}] {i * 100 // 10}%", end="")
                time.sleep(5)
            print()
            
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
            konami_easter_egg()
            
        elif choice == "greet":
            print("Whats you name?")
            name = input("Enter your name : ")
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
        else:
                        print(f"Command not found : {choice}")
                        

def run_exe():
    folder = input("Enter the path to the folder containing .exe files: ").strip()

    if not os.path.isdir(folder):
        print("❌ Folder does not exist!")
        return

    # List .exe files in the folder
    exe_files = [f for f in os.listdir(folder) if f.lower().endswith(".exe")]

    if not exe_files:
        print("⚠️ No .exe files found in this folder.")
        return

    print("\nAvailable .exe files:")
    for i, f in enumerate(exe_files):
        print(f"[{i}] {f}")

    try:
        choice = int(input("\nEnter the number of the program you want to run: ").strip())
        if choice < 0 or choice >= len(exe_files):
            print("❌ Invalid selection number.")
            return
        exe_path = os.path.join(folder, exe_files[choice])
        print(f"▶️ Running: {exe_path}")
        os.system(f"wine \"{exe_path}\"")
    except ValueError:
        print("❌ Invalid input, please enter a valid number.")
               
                                
def sys_info():
                print(f"System: {platform.system()}")
                print(f"Version: {platform.version()}")
                print(f"Release: {platform.release()}")
                print(f"Machine: {platform.machine()}")

def loading_kernel():
    print("Loading kernel.py")
    time.sleep(1)
    print("Starting kernel.py")
    os.chdir("..")
    os.chdir("..")
    os.system("python kernel/kernel.py")
    
    
    if not os.path.exists(KERNL):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print("E : File 'kernel/kernel.py' is misssing or corrupted")
        sys.exit()
    
    if not os.path.exists(SYSFILES):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")
        print("E: File 'hal.dll' is misssing or corrupted")
        kernelres()
        
    
    if not os.path.exists(ntoskrnl):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")
        print("E: File 'ntoskrnl.sys' is misssing or corrupted")
        kernelres()
        
    
    if not os.path.exists(bootmgfw):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")
        print("E: File 'bootmgfw.efi' is misssing or corrupted")
        kernelres()
        
    if not os.path.exists(rukernel):
        clear_screen()
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")
        print("E: File 'rukernel.sys' is misssing or corrupted")
        kernelres()

    if not os.path.exists(keyboarddriver):
        clear_screen()
        print("Driver 'drivers/keyboard.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")
        print("E: Driver 'drivers/keyboard.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(batterydriver):
        clear_screen()
        print("Driver 'drivers/battery.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/battery.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(displaydriver):
        clear_screen()
        print("Driver 'drivers/display.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/display.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(mousedriver):
        clear_screen()
        print("Driver 'drivers/mouse.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/mouse.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(networkdriver):
        clear_screen()
        print("Driver 'drivers/network.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/network.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(powerdriver):
        clear_screen()
        print("Driver 'drivers/power.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/power.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(sounddriver):
        clear_screen()
        print("Driver 'drivers/sound.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/sound.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(storagedriver):
        clear_screen()
        print("Driver 'drivers/storage.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/storage.c' is misssing or corrupted")
        kernelres()

    if not os.path.exists(usbdriver):
        clear_screen()
        print("Driver 'drivers/usb.c' is missing!")
        print("""RUBY DEBUGGER""")
        print(r"""
╔════════════════════════════════════════════════════════╗
║                ***  CRITICAL SYSTEM ERROR  ***         ║
╚════════════════════════════════════════════════════════╝

EXCEPTION: GENERAL PROTECTION FAULT (INT 0x0D)
ERROR CODE: 0x00000013
FAULTING ADDRESS: 0xBADC0DE

--- REGISTER DUMP ---
RAX=0x0000000000000000
RBX=0x00000000CAFEBABE
RCX=0x000000001337F00D
RDX=0x00000000DEADBEEF
RSI=0x00000000FEEDFACE
RDI=0x000000000BADF00D
RBP=0x000000008BADF00D
RSP=0x00000000BAADF00D
R8 =0x00000000DEFACED0
R9 =0x00000000B16B00B5

--- SEGMENT REGISTERS ---
CS=0x0010 DS=0x002B ES=0x002B FS=0x0053 GS=0x002B SS=0x002B

--- FLAGS ---
EFLAGS=0x00010282

--- STACK TRACE ---
> 0x0040:0x0000BADF
> 0x0040:0x1337FACE
> 0x0040:0x0DEADBAD
> 0x0040:0xC001D00D

--- SYSTEM INFORMATION ---
CPU : (f{sys.cpu.output})
CORE: (f{sys.cpu.core.output})
RAM : (f{sys.ram.output})
OS  : (f{sys.os.output})

-- SYSTEM INFO FAILED --

at line.2163.EBOOT.py
at line.2164.EBOOT.py
at line.2165.EBOOT.py
at line.2166.EBOOT.py

info : (f{sys.cpu.output}) not found!
info : (f{sys.cpu.core.output}) not found!
info : (f{sys.ram.output}) not found!
info : (f{sys.os.output}) not found!

at 0X000000013.line
at 0X000000014.line

--- CONTEXT ---
PROCESS: RUNY_PROCESS.PRG
THREAD : MAIN_THREAD
UPTIME : 00:00:13.37

-- CONTEXT ERROR --

at line.2184.EBOOT.py
info : RUNY_PROCESS.PRG not found! / unknown file format!

-- KERNEL ERROR --

error : import os
error : import time
error : os.system("clear" if os.name != "nt" else "cls")
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.8)
error : time.sleep(0.5)
error : boot()

at line.3.kernel/kernel.py
at line.4.kernel/kernel.py
at line.11.kernel/kernel.py
at line.14.kernel/kernel.py
at line.16.kernel/kernel.py
at line.18.kernel/kernel.py
at line.20.kernel/kernel.py
at line.22.kernel/kernel.py
at line.24.kernel/kernel.py
at line.27.kernel/kernel.py

info : Unknown function 'import os'!
info : Unknown function 'import time'!
info : Unknown function 'os.system("clear" if os.name != "nt" else "cls")'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.8)'!
info : Unknow function 'time.sleep(0.5)'!
info : No function named 'boot()'!

at 0X0000023.line.kernel

!!! *** SYSTEM HALTED *** !!!
Press RESET or POWER OFF to reboot.

-- KERNEL PANIC --

[  00.0042 ] KERNEL PANIC - NOT SYNCING: Attempted to kill init!
CPU: 0 PID: 1 Comm: init
Call Trace:
 [<deadbeef>] panic+0x101/0x202
 [<cafebabe>] do_exit+0xa0/0x400
 [<feedface>] do_group_exit+0x3e/0x60

System halted.
""")

        print("E: Driver 'drivers/storage.c' is misssing or corrupted")
        kernelres()

    
    print("kernel.py loaded successfully.")
    check_installation()
    
def kernelres():
    print("Welcome to Kernel Fixer")
    print("1. Repair system")
    print("2. Terminal")
    print("3. Exit")

    while True:
        choice = input(">> ").strip()

        if choice == '1':
            try:
                with open(sysfiles, 'w') as f:
                    f.write("01101000 01100001 01101100 00101110 01100100 01101100 01101100 00100000 01101001 01110011 00100000 01100110 01101001 01111000 01100101 01100100 ")
                print("✅ System repaired successfully!")
            except Exception as e:
                print(f"❌ Error while repairing system: {e}")
        elif choice == '2':
            terminal()
        elif choice == '3':
            sys.exit()
        else:
            print("⚠️ Invalid choice, please try again.")
               

def ene():
    width = 60
    height = 10
    options = ["1. Install system", "2. Repair system/installation", "3. Exit"]
    selected = 0

    while True:
        clear_screen()
        print("#" * width)

        # Print empty lines above options
        for _ in range(height - len(options) - 3):
            print("#" + " " * (width - 2) + "#")

        # Print options with arrow on selected
        for i, option in enumerate(options):
            if i == selected:
                line = "# > " + option.ljust(width - 5) + "#"
            else:
                line = "#   " + option.ljust(width - 5) + "#"
            print(line)

        print("#" * width)

        key = input("\nPress 'w' to move up, 's' to move down, and Enter to select: ").lower()

        if key == 'w' and selected > 0:
            selected -= 1
        elif key == 's' and selected < len(options) - 1:
            selected += 1
        elif key == '':
            if selected == 0:
                install_sys()
            elif selected == 1:
                res()
            elif selected == 2:
                print("Exiting program.")
                sys.exit()
        else:
            print("Unknown option, please try again.")
                     
            
def res():
    clear_screen()
    print("Welcome to Ruby OS reset")
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
    print()
            

def install_sys():
    package_name = "python"
    print(f"Installing package '{package_name}'...\n")

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
        "Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease\n...",
        "Reading package lists... Done\nBuilding dependency tree\n...",
        "Installing python...\n[##########] 100% | Installed python version 3.8.10.\n",
        "Requirement already up-to-date: pip in /usr/local/lib/python3.8/dist-packages (21.2.4)\n",
        "Requirement already satisfied: requests in /usr/local/lib/python3.8/dist-packages ...\n",
        "Reading package lists... Done\nBuilding dependency tree\nRemoving python3-pip...\n",
        "Cleaning up package cache...\nAll cached packages cleaned.\n",
        "Distributor ID: Ubuntu\nDescription: Ubuntu 20.04 LTS\nRelease: 20.04\n...",
        "Directory '/home/user/test' created.\n",
        "Permissions for '/home/user/test' set to 755.\n",
        "Ownership of '/home/user/test' set to user:user.\n",
        "NAME=\"Ubuntu\"\nVERSION=\"20.04 LTS (Focal Fossa)\"\nID=ubuntu\n...",
        "--2025-01-03 12:34:56--  https://example.com/package.tar.gz\n...",
        "package/\npackage/file1.txt\npackage/file2.txt\n...",
        "[Opened nano editor, displaying /etc/hosts content]\n",
        "[Opened vi editor, displaying /etc/hostname content]\n",
        "USER       PID %CPU %MEM ...\nroot         1  0.0  0.1 ...\n",
        "top - 12:45:12 up 10 days,  3:14,  2 users,  load average: ...\n",
        "              total        used        free      shared  buff/cache   available\n...",
        " 12:45:12 up 10 days,  3:14,  2 users,  load average: 0.10, ...\n",
        "user\n",
        "hostname\n",
        "Thu Jan  3 12:45:12 UTC 2025\n",
        "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1 50G 10G 40G 20% /\n",
        "du: cannot read directory '/home/user': Permission denied\n",
        "COMMAND     PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME\n...",
        "inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0\n",
        "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\n...",
        "PING google.com (8.8.8.8) 56(84) bytes of data.\n64 bytes from 8.8.8.8: ...\n",
        "HTTP/1.1 200 OK\nDate: Thu, 03 Jan 2025 12:45:12 GMT\n...",
        "Active Internet connections (only servers)\nProto Recv-Q Send-Q Local Address ...",
        "Chain INPUT (policy ACCEPT)\ntarget     prot opt source destination\n...",
        "● apache2.service - The Apache HTTP Server\n Loaded: loaded ...\n Active: active (running)\n",
        "● apache2.service - The Apache HTTP Server\n Loaded: loaded ...\n Active: inactive (dead)\n",
        "apache2.service - The Apache HTTP Server\n Loaded: loaded ...\n Active: active (running)\n",
        "The Apache HTTP Server is now active and running.",
        "systemd[1]: Stopping Apache HTTP Server...\n systemctl[1]: apache2.service stopped successfully.",
        "systemctl restart apache2\nThe Apache HTTP Server has been successfully restarted."
    ]

    for i, command in enumerate(commands):
        print(f"~$ {command}")
        time.sleep(2)
        print(outputs[i])


    print("\nSetting System Kernel")
    show_progress(20)
    with open(INSTALLATION_FILE, 'w') as f:
        f.write(
            "00000000  4e 54 4f 53 4b 52 4e 4c  53 59 53 00 00 00 00 00  |NTOSKRNL SYS.......|\n"
            "00000010  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|\n"
            "00000020  30 30 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |00............|\n"
            "00000030  00 00 00 00 00 00 00 00  30 00 00 00 00 00 00 00  |........0.......|\n"
            "00000040  04 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|\n"
            "00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|\n"
            "..."
        )

    print("Installation completed successfully!")
    time.sleep(3)
    clear_screen()
    print("Starting system...")
    term()

def term():
    print("Welcome to Ruby Term")
    print("Hello! Welcome to Ruby OS ,This is the console you need to setup the hole system by your self , the tutorial is at www.github.com/OgnjenDev/RUBY in readme.md file.")

    while True:
        choice = input(f"~[ruby-os] /instaler $ ")

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
            print("Connecting to ruby data base")
            print("=" * 10)
            time.sleep(4)
            print(".")
            time.sleep(3)
            print("..")
            time.sleep(3)
            print("...")
            time.sleep(4)
            print("ruby database is loading files")
            time.sleep(4)
            print("Ruby OS successfully started!")
            opt()
        else:
            print("Unknown command")
            
import os
import subprocess

def usb_reader():
    print("\n========== 💾 USB READER (PRO) 💾 ==========")
    
    # Find USB devices using lsblk
    result = subprocess.getoutput("lsblk -o NAME,SIZE,MODEL,MOUNTPOINT | grep -i 'media\|run/media'")
    if not result.strip():
        print("❌ No mounted USB devices found.")
        return

    print("🔎 Detected USB devices:\n")
    print(result)

    mount_points = []
    for line in result.splitlines():
        parts = line.split()
        if len(parts) >= 4:
            mount_points.append(parts[-1])

    for mount in mount_points:
        print(f"\n📂 USB contents ({mount}):")
        os.system(f'ls "{mount}"')
                                                                                   


def addons():
    print("Welcome to Extras!")
    print("1. Settings")
    print("2. System Backup")
    print("3. Report Bugs")
    print("4. Network Wizard")
    print("5. Ruby Package Manager")
    print("6. ZIP Manager")
    print("9. USB Reader")

    if is_dev():
        print("7. Developer Options")
        print("8. Exit")
    elif is_server():
        print("7. Server Console")
        print("8. Exit")
    else:
        print("7. Exit")

    while True:
        user_input = input("Enter an option: ").strip()

        if user_input == '1':
            settings()

        elif user_input == '2':
            confirm = input("Are you sure you want to delete 'RUBY OS SYSTEM'? (y/n): ").strip().lower()
            if confirm == 'y':
                try:
                    if os.path.exists(INSTALLATION_FILE):
                        os.remove(INSTALLATION_FILE)
                        print("✅ INSTALLATION_FILE successfully deleted. Please restart Ruby OS.")
                    else:
                        print("⚠️ INSTALLATION_FILE not found.")
                except Exception as e:
                    print(f"❌ Error while deleting: {e}")
            else:
                print("❎ Backup canceled.")

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
                server_console()
            else:
                print("👋 Exiting Extras.")
                break

        elif user_input == '8' and (is_dev() or is_server()):
            print("👋 Exiting Extras.")
            break

        else:
            print("❗ Unknown option. Please try again.")
            

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
    print("Welcome, Developers!")  
    print("1. Developer Rules")
    print("2. Ruby OS New Ideas")
    print("3. Exit")
    while True:
        choice = input("Select an option: ")
        
        if choice == '1':
            dev_rules()
        elif choice == '2':
            dev_ruby_ideas()
        elif choice == '3':
            break

def dev_rules():
    print("Developer Rules:")
    print("1. Publishing the developer password online is forbidden. Consequences: (Developer access revoked) or (Fine of 12,000 RSD or €500)")
    print("2. Sharing Ruby OS updates online is forbidden. Consequences: (Developer access revoked) or (Fine of 9,000 RSD or €800)")
    print("3. Hacking developer servers is strictly prohibited. Reason: (Server damage after hacking). Consequences: (Trial) or penalty: (95,000 RSD or 2 years of prison)")

def dev_ruby_ideas():
    print("Ideas and Improvements for Ruby OS:")
    print("- Improved server stability")
    print("- Faster boot time")
    print("- Secure remote access for developers")
    print("- Package Manager with auto-updater")
    print("- Developer-only debug console")
    print("- Built-in log viewer")
    print("- New Ruby Shell with auto-complete")
    print("- Support for virtual devices and emulation")
    print("- More modular system architecture")

def netw():
    print("Welcome to Network Wizard")
    print("We will help you set up your internet connection!")
    print("Is your internet connection wired or wireless?")
    print("1. Wired")
    print("2. Wireless")
    print("3. Exit")
    while True:
        choice = input("Select an option: ")
        
        if choice == '1':
            net_wired()
        elif choice == '2':
            net_wireless()
        elif choice == '3':
            break
                    
def net_wired():
    print("Great! Now we will set it up")
    print("Make sure the internet cable is plugged into LAN 1")
    
    import time
    import sys

    for i in range(11):
        bar = "█" * i + "-" * (10 - i)
        print(f"\r[{bar}] {i * 100 // 10}%", end="")
        sys.stdout.flush()  # Manually refresh the output
        time.sleep(1.0)

    print()
    print("Successfully configured!")


def net_wireless():
    print("Great! Now we will configure it")
    print("Make sure the internet is connected on the current OS")
    
    import time
    import sys

    for i in range(11):
        bar = "█" * i + "-" * (10 - i)
        print(f"\r[{bar}] {i * 100 // 10}%", end="")
        sys.stdout.flush()  # Manually refresh the output
        time.sleep(1.0)

    print()  # New line after the progress bar
    print("Successfully configured!")

            
import datetime

def bugs():
    print("We apologize for any bugs in the Beta version.")
    name = input("Enter your name: ")
    description = input("Describe the bug/glitch: ")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("bugs.log", "a") as f:
        f.write(f"[{timestamp}] {name}: {description}\n")

    print("Thank you for reporting the bug! Your report has been saved.")
            
            
def settings():
    print("Welcome to Settings")
    print("1. User Info")
    print("2. Screen Resolution")
    print("3. Exit")
    while True:
        choice = input("Enter option: ").strip()
        
        if choice == '1':
            print("Username: {root_username}")
            print("Password Hash: {root_hashed_password}")
        elif choice == '2':
            print("Current resolution: 1024 x 1024")
        elif choice == '3':
            break
        else:
            print("Unknown option, please try again.")                                
            
def konami_easter_egg():
    print("You have discovered a secret! Activating Easter Egg...")
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
    print("Congratulations! You have unlocked a hidden part of the system!")
    time.sleep(2)
    print("Keep exploring...")



def programming():
    program_code = ""
    current_language = "python"
    print("\n--- Welcome to Programming Mode ---")
    while True:
        print(f"\nCurrent directory: {os.getcwd()}")
        print("1. Choose programming language")
        print("2. Write new program")
        print("3. Save program")
        print("4. Show available programs")
        print("5. Run program")
        print("6. Edit existing program")
        print("7. Change directory")
        print("8. Go back")
        print("9. Exit programming mode")

        choice = input("Select an option: ")

        if choice == "1":
            current_language = choose_language()
        elif choice == "2":
            program_code = write_code(current_language)
        elif choice == "3":
            save_program(program_code, current_language)
        elif choice == "4":
            show_files()
        elif choice == "5":
            run_selected_program()
        elif choice == "6":
            program_code = edit_selected_program()
        elif choice == "7":
            change_directory()
        elif choice == "8":
            go_back_directory()
        elif choice == "9":
            print("Exiting programming mode...")
            break
        else:
            print("Invalid input, please try again!")

def choose_language():
    print("\n--- Choose a language ---")
    print("1. Python")
    print("2. C")
    print("3. C++")
    print("4. Java")
    choice = input("Select language number: ")
    languages = {"1": "python", "2": "c", "3": "cpp", "4": "java"}
    return languages.get(choice, "python")

def write_code(language):
    print(f"\n--- Write your {language} program (type 'END' to finish) ---")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)
    print("Program written.")
    return "\n".join(code_lines)

def save_program(program_code, language):
    if not program_code:
        print("No code to save!")
        return

    extensions = {"python": ".py", "c": ".c", "cpp": ".cpp", "java": ".java"}
    file_name = input("Enter file name (without extension): ") + extensions.get(language, ".txt")
    with open(file_name, "w") as f:
        f.write(program_code)
    print(f"Program saved as {file_name}")

def show_files():
    print("\n--- Programs in current directory ---")
    extensions = [".py", ".c", ".cpp", ".java"]
    files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in extensions]

    if not files:
        print("No programs found.")
        return

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

def run_selected_program():
    extensions = [".py", ".c", ".cpp", ".java"]
    files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in extensions]

    if not files:
        print("No programs available to run.")
        return

    show_files()
    choice = input("Select program number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            file_name = files[idx]
            ext = os.path.splitext(file_name)[1]
            print(f"Running {file_name}...")
            warning = "This file is not verified and may be dangerous!!! PRESS ENTER to continue"
            if ext == ".py":
                input(warning)
                print("")
                os.system(f"python '{file_name}'")
            elif ext == ".c":
                input(warning)
                print("")
                os.system(f"gcc '{file_name}' -o temp_c_prog && ./temp_c_prog")
            elif ext == ".cpp":
                input(warning)
                print("")
                os.system(f"g++ '{file_name}' -o temp_cpp_prog && ./temp_cpp_prog")
            elif ext == ".java":
                input(warning)
                print("")
                base = os.path.splitext(file_name)[0]
                os.system(f"javac '{file_name}' && java {base}")
            else:
                print("Unsupported file extension!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def edit_selected_program():
    extensions = [".py", ".c", ".cpp", ".java"]
    files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1] in extensions]

    if not files:
        print("No programs available for editing.")
        return ""

    show_files()
    choice = input("Select program number to edit: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            file_name = files[idx]
            with open(file_name, "r") as f:
                print(f"\n--- Current content of ({file_name}) ---")
                print(f.read())

            print("\n--- Enter new code (type 'END' to finish) ---")
            code_lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                code_lines.append(line)
            new_code = "\n".join(code_lines)
            with open(file_name, "w") as f:
                f.write(new_code)
            print(f"{file_name} has been successfully edited.")
            return new_code
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")
    return ""

def change_directory():
    print("\n--- Directory list ---")
    dir_list = [d for d in os.listdir() if os.path.isdir(d)]
    if not dir_list:
        print("No directories available.")
        return
    for i, d in enumerate(dir_list, 1):
        print(f"{i}. {d}")
    choice = input("Select directory number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(dir_list):
            os.chdir(dir_list[idx])
            print(f"Changed directory to: {os.getcwd()}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def go_back_directory():
    os.chdir("..")
    print(f"Moved back to: {os.getcwd()}")

                
def whats_new():
    clear_screen()
    print("What's New in Ruby OS 1.3.5")
    print("1. System has been fully optimized for better performance")
    print("2. Many bugs have been fixed")
    print("3. Added 'man' command to the terminal (manual/help)")
    print("4. Improved boot time by 40%")
    print("5. Added support for external Python scripts")
    print("6. Terminal now supports colored output")
    print("7. More error handling in system modules")
    print("8. Updated system logs with timestamps")
        


def check_installation():
    if not os.path.exists(INSTALLATION_FILE):
        print("System not installed. Launching installation...")
        ene()
    else:
        print("Checking existing system installation...")
        time.sleep(6)
        print("Installation found at /RUBY os/BOOT")
        time.sleep(2)
        clear_screen()

    # Logic for continuing after installation check
    print("Starting system...")
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

    for _ in range(10):
        for spin in spinner:
            clear_screen()
            print(f"{theme['background']}{theme['text']}Welcome to Ruby OS!")
            print("=" * 40)
            print("\n".join(line.center(40) for line in ascii_logo.split("\n")))
            print("\n" + " " * 19 + spin)
            print(" " * 16 + "1.3.6")
            print(" " * 8 + "© Copyright - ABC studio")
            time.sleep(0.2)

    clear_screen()
  
def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open(USERS_FILE, 'a') as f:
        f.write(f"{username},{hashed_password}\n")
    
    print("Registration successful! Welcome aboard.")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        with open(USERS_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(',')
                if username == stored_username and hashed_password == stored_password:
                    print("Login successful! Access granted.")
                    return True
            print("Invalid username or password.")
            return False
    except FileNotFoundError:
        print("No registered users found. Please register first.")
        return False

def login_or_register():
    while True:
        choice = input("Would you like to (l)ogin or (r)egister? ").lower()
        if choice == 'r':
            register_user()
            break
        elif choice == 'l':
            if login_user():
                break
            else:
                print("Please try again.")
        else:
            print("Invalid option. Please enter 'l' to login or 'r' to register.")

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

    for line in lines[:height - 6]:
        line_fixed = line[:width - 2]  # shorten if line is too long
        print(" " * x + "|" + line_fixed.ljust(width - 2) + "|")

    for _ in range(height - 4 - len(lines)):
        print(" " * x + empty)

    print(" " * x + bottom)


def show_menu(theme):
    print(f"{theme['background']}{theme['text']}")
    print("Choose an option:")
    print("1. Show date and time")
    print("2. List files in the current directory")
    print("3. Create a new file")
    print("4. Read a file")
    print("5. Create a new folder")
    print("6. Show files in a specific folder")
    print("7. Delete a file or folder")
    print("8. Change theme")
    print("9. Clear screen")
    print("10. Game Manager")
    print("11. Calculator")
    print("12. Task Manager")
    print("13. Web Browser")
    print("14. System Information")
    print("15. What's new?")
    print("16. Terminal")
    print("17. Code Mode")
    print("18. Run .exe files")
    print("19. Add New Device")
    print("20. Add-ons")
    print("21. Shutdown")

def select_theme():
    clear_screen()  # Clear the screen before showing themes
    print("Select a theme:")
    for idx, theme_name in enumerate(themes.keys(), start=1):
        print(f"{idx}. {theme_name.capitalize()} theme")
    
    choice = input(f"Enter your choice (1-{len(themes)}): ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(themes):
            return list(themes.values())[choice_index]
        else:
            print("Invalid choice, defaulting to light theme.")
            return themes['light']
    except ValueError:
        print("Invalid input, defaulting to light theme.")
        return themes['light']

def display_datetime():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")

def list_files():
    files = os.listdir('.')
    print("Files in the current directory:")
    for file in files:
        print(file)

def create_file():
    filename = input("Enter the name of the new file: ")
    with open(filename, 'w') as f:
        content = input("Enter file content: ")
        f.write(content)
    print(f"File '{filename}' has been created.")

def read_file():
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Contents of file '{filename}':")
            print(content)
    except FileNotFoundError:
        print("File not found.")

def create_directory():
    dirname = input("Enter the name of the new folder: ")
    try:
        os.makedirs(dirname)
        print(f"Folder '{dirname}' has been created.")
    except FileExistsError:
        print("Folder already exists.")

def list_specific_directory():
    dirname = input("Enter the folder name: ")
    try:
        files = os.listdir(dirname)
        print(f"Files in folder '{dirname}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Folder not found.")

def delete_file_or_directory():
    name = input("Enter the name of the file or folder to delete: ")
    
    try:
        if os.path.isfile(name):
            os.remove(name)
            print(f"File '{name}' has been deleted.")            
        elif os.path.isdir(name):
            os.rmdir(name)
            print(f"Folder '{name}' has been deleted.")
        else:
            print("File or folder does not exist.")
    except Exception as e:
        print(f"Error deleting: {e}")

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

def calculator():
    print("Calculator")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator.")
        return
    
    print(f"Result: {result}")

def manage_tasks():
    while True:
        print("\nTask Manager:")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added.")

        elif choice == '2':
            if not tasks:
                print("No tasks to display.")
            else:
                print("\nAll tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\nAll tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print("Task deleted.")

                    # Check if all "IMPORTANT" tasks are deleted
                    if "[IMPORTANT]" not in " ".join(tasks):
                        bsod()
                else:
                    print("Invalid task number.")

        elif choice == '4':
            print("Exiting task manager...")
            break

        else:
            print("Invalid option. Please try again.")
            

# ANSI boje
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
reset = "\033[0m"

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
    color = random.choice(colors)
    print(color + log + reset)
    time.sleep(0.01)

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

for _ in range(2):
    for frame in frames:
        sys.stdout.write("\r" + "\033[34m" + frame + reset)
        sys.stdout.flush()
        time.sleep(0.1)

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
        choice = input("Select an option (1–20): ")
        
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
            whats_new()
        elif choice == '16':
            terminal()
        elif choice == '17':
            programming()  
        elif choice == '18':
            run_exe()
        elif choice == '19':
            add_device()
        elif choice == '20':
            addons()
        elif choice == '21':
            print("Shutting Down...")
            time.sleep(3)
            sys.exit()
        elif choice == 'konami':
            konami_easter_egg()
        elif choice == 'fridaythe13':
            friday_the_13th_easter_egg()
        else:
            print("Invalid option!")

if __name__ == "__main__":
        main()
