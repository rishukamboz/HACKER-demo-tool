import time
import os

def clear():
    os.system("clear")

def loading(text):
    print("\n" + text)
    for i in range(0, 101, 20):
        print(f"[+] Progress : {i}%")
        time.sleep(0.5)

def instagram():
    clear()
    print("===== INSTAGRAM HACK (DEMO) =====")
    loading("Connecting to Instagram server...")
    loading("Bypassing firewall...")
    loading("Fetching credentials...")
    print("\n[✓] DEMO COMPLETED")
    print("[!] This is a FAKE demo\n")

def facebook():
    clear()
    print("===== FACEBOOK HACK (DEMO) =====")
    loading("Scanning Facebook database...")
    loading("Injecting fake payload...")
    loading("Access granted...")
    print("\n[✓] DEMO COMPLETED")
    print("[!] This is a FAKE demo\n")

def website():
    clear()
    print("===== WEBSITE HACK (DEMO) =====")
    loading("Scanning website ports...")
    loading("Running SQL Injection (Demo)...")
    loading("Admin panel found...")
    print("\n[✓] DEMO COMPLETED")
    print("[!] This is a FAKE demo\n")

while True:
    clear()
    print("===================================")
    print("        HACKER TOOL  (DEMO)")
    print("===================================")
    print("1. Instagram Hack")
    print("2. Facebook Hack")
    print("3. Website Hack")
    print("0. Exit")
    print("===================================")

    choice = input("Select Option : ")

    if choice == "1":
        instagram()
        input("Press Enter...")
    elif choice == "2":
        facebook()
        input("Press Enter...")
    elif choice == "3":
        website()
        input("Press Enter...")
    elif choice == "0":
        print("Exiting HACKER Tool...")
        break
    else:
        print("Invalid Option")
        time.sleep(1)
