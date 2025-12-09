import os
import uuid
import json
import datetime
import time


# ==========================
#  TERMINAL COLOR CODES
# ==========================
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


# ==========================
# UI FUNCTIONS
# ==========================
def header(text, color=CYAN):
    print(color + "╔══════════════════════════════════════════╗")
    print(f"                 {text.upper()}")
    print("╚══════════════════════════════════════════╝" + RESET)

def option(num, text):
    print(f"{YELLOW}{num}.{WHITE} {text}" + RESET)

def success(msg):
    print(f"{GREEN}✔ {msg}{RESET}")

def error(msg):
    print(f"{RED}✘ {msg}{RESET}")

def loading():
    for l in ["[■□□□□]", "[■■□□□]", "[■■■□□]", "[■■■■□]", "[■■■■■]"]:
        print(CYAN + l + RESET, end="\r")
        time.sleep(.09)

def clear():
    os.system("cls")


# ==========================
# DATA HANDLING
# ==========================
def load_transactions():
    data = []
    if not os.path.exists("transactions.json"):
        open("transactions.json","w").close()

    with open("transactions.json", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def save_transaction(items, total, method, cash, change):
    receipt_id = str(uuid.uuid4())
    trans = {
        "receipt_id": receipt_id,
        "datetime": str(datetime.datetime.now()),
        "items": items,
        "total": total,
        "method": method,
        "cash": cash,
        "change": change
    }
    

    with open("transactions.json", "a") as file:
        file.write(json.dumps(trans) + "\n")

    print()
    success("Saved to transactions.json")
    print(f"{CYAN}Receipt ID: {WHITE}{receipt_id}\n")

def save_transaction_card(items, total, method, cash, change):
    receipt_id = str(uuid.uuid4())
    trans = {
        "receipt_id": receipt_id,
        "datetime": str(datetime.datetime.now()),
        "items": items,
        "total": total,
        "method": method,
        "cash": cash,
        "change": change
    }
    

    with open("transactions.json", "a") as file:
        file.write(json.dumps(trans) + "\n")

    print()
    success("Saved to transactions.json")
    print(f"{CYAN}Receipt ID: {WHITE}{receipt_id}\n")


# ==========================
# USERS
# ==========================
adminUser = "admin"
adminPass = "1234"

cashierUser = "cashier"
cashierPass = "1234"

er = 2
et = 2

products = [
    {"name": "ID Lace", "price": 75},
    {"name": "Logo", "price": 50},
    {"name": "Cartolina", "price": 20},
    {"name": "Bond Paper", "price": 1}
]


# ================================================================
#                            MAIN LOOP
# ================================================================
while er == 2:
    et = 2
    clear()
    header("login page")

    user = input(f"{WHITE}Enter User ▶ {RESET}")
    password = input(f"{WHITE}Enter Password ▶ {RESET}")

    # ===============================
    # ADMIN
    # ===============================
    if user.lower() == adminUser and password == adminPass:
        clear()
        while et == 2:
            header("Admin Panel")

            option(1, "View Transaction History")
            option(2, "Exit")

            choose = input("Choose ▶ ")

            if choose == "1":
                clear()
                header("Transaction List")

                transanction = load_transactions()

                if not transanction:
                    print(f"{YELLOW}No transactions found.{RESET}")
                    input("Press Enter...")
                    continue

                for index, item in enumerate(transanction, start=1):
                    print(f"{CYAN}{index}.{WHITE} {item['receipt_id']}")

                choice = input("\nSelect transaction number ▶ ")

                if not choice.isdigit():
                    error("Invalid input!")
                    continue

                choice = int(choice)
                if choice < 1 or choice > len(transanction):
                    error("Invalid selection!")
                    continue

                selected = transanction[choice - 1]
                clear()

                header("Transaction Details")

                print(f"{MAGENTA}Receipt ID:{WHITE} {selected['receipt_id']}")
                print(f"{MAGENTA}Datetime:{WHITE}   {selected['datetime']}")
                print(f"{MAGENTA}Items:{RESET}")

                for item in selected["items"]:
                    print(f" {GREEN}- {item['name']} x{item['qty']} = ₱{item['total']}")

                print(f"{MAGENTA}\nTOTAL:{WHITE} ₱{selected['total']}")
                print(f"{MAGENTA}Paid Using:{WHITE} {selected['method']}\n")
                print(f"{MAGENTA}Amount Paid:{WHITE} ₱{selected['cash']}\n")
                print(f"{MAGENTA}Change:{WHITE} ₱{selected['change']}\n")

                input("Press Enter...")
                clear()

            elif choose == "2":
                clear()
                print("1. Back to login")
                print("2. Exit Program")
                choose2 = input("Choose ▶ ")

                if choose2 == "1":
                    et = 1
                elif choose2 == "2":
                    er = 1
                    et = 1
                elif choose2 == "":
                    print("Triple B ka ba?!")
                else:
                    print("SBAPN!")

            elif choose == "":
                clear()
                print("Kupal, wala ka naman nilagay Boi~!")
            else:
                clear()
                print("Ang kulit mo Boi~!")

    # ===============================
    # CASHIER
    # ===============================
    elif user.lower() == cashierUser and password == cashierPass:
        clear()
        while et == 2:

            header("cashier")

            option(1, "Add Item to Cart")
            option(2, "Logout")
            print("")
            choose = input("Choose ▶ ")

            if choose == "1":
                clear()
                cart = []
                total = 0

                header("Products")

                print(f"{YELLOW} D = finish | C = clear cart | V = view cart | cancel = cancel{RESET}\n")

                for i in products:
                    print(f"{GREEN}{i['name']} {WHITE}- ₱{i['price']}")

                while True:
                    item = input("\nChoose product ▶ ").lower()

                    if item.lower() == "v":
                        clear()
                        header("cart")
                        for i in cart:
                            print(f"{WHITE}{i['name']} x{i['qty']} = ₱{i['total']}")
                        header("Products")

                        print(f"{YELLOW} D = finish | C = clear cart | V = view cart | cancel = cancel{RESET}\n")

                        for i in products:
                            print(f"{GREEN}{i['name']} {WHITE}- ₱{i['price']}")
                        
                        continue


                    if item.lower() == "c":
                        cart.clear()
                        total = 0
                        success("Cart Cleared!")
                        continue

                    if item.lower() == "cancel":
                        clear()
                        break

                    if item == "d":
                        if cart == []:
                            error("Cart is empty!")
                            continue

                        clear()

                        header("payment")
                        print("Cash | Card | Cancel")
                        method = input("Payment ▶ ").lower()

                        if method.lower() == "cancel": break
                        elif method.lower() == "cash" :
                            cash = input("Enter Amount: ")
                            if cash.isdigit():
                                cash = int(cash)
                                if cash >= total:
                                    change = cash - total
                                    header("receipt")

                                    for c in cart:
                                        print(f"{WHITE}{c['name']} x{c['qty']} - ₱{c['total']}")
                                    print("---------------------")
                                    print(f"{MAGENTA}TOTAL:{WHITE} ₱{total}")
                                    print(f"{MAGENTA}Payment Method:{WHITE} {method}")
                                    print(f"{MAGENTA}Amount Paid:{WHITE} ₱{cash}")
                                    print("---------------------")
                                    print(f"{MAGENTA}Change:{WHITE} {change}")
                                    save_transaction(cart, total, method, cash, change)
                                    input("Press Enter...")
                                    clear()
                                    break
                                else:
                                    clear()
                                    error("Insufficient Cash")
                                    header("Products")

                                    print(f"{YELLOW} D = finish | C = clear cart | V = view cart | cancel = cancel{RESET}\n")

                                    for i in products:
                                        print(f"{GREEN}{i['name']} {WHITE}- ₱{i['price']}")
                                    continue
                            else:
                                print("Cash!")
                        elif method.lower() == "card":
                            header("receipt")
                            cash = total
                            change = cash - total

                            for c in cart:
                                print(f"{WHITE}{c['name']} x{c['qty']} - ₱{c['total']}")
                            print("---------------------")
                            print(f"{MAGENTA}TOTAL:{WHITE} ₱{total}")
                            print(f"{MAGENTA}Payment Method:{WHITE} {method}")
                            print(f"{MAGENTA}Amount Paid:{WHITE} {method}")
                            print("---------------------")
                            print(f"{MAGENTA}Change:{WHITE} {change}")
                            save_transaction(cart, total, method, cash, change)
                            input("Press Enter...")
                            clear()
                            break
                        else:
                            clear()
                            error("Invalid Method")
                            header("Products")

                            print(f"{YELLOW} D = finish | C = clear cart | V = view cart | cancel = cancel{RESET}\n")

                            for i in products:
                                print(f"{GREEN}{i['name']} {WHITE}- ₱{i['price']}")
                            continue
                        
                        

                    found = None
                    for i in products:
                        if i["name"].lower() == item:
                            found = i
                            break

                    if found:
                        qty = input("Quantity ▶ ")
                        if not qty.isdigit():
                            error("Invalid Quantity!")
                            continue

                        qty = int(qty)
                        cost = found["price"] * qty

                        cart.append({
                            "name": found["name"],
                            "price": found["price"],
                            "qty": qty,
                            "total": cost
                        })

                        total += cost

                        success(f"Added {qty} x {found['name']} = ₱{cost}")
                    else:
                        error("There's no such product!")
                      

            elif choose == "2":
                clear()
                print("1. Back to login")
                print("2. Exit Program")
                choose2 = input("Choose ▶ ")

                if choose2 == "1":
                    et = 1
                elif choose2 == '2':
                    er = 1
                    et = 1
                elif choose2 == "":
                    print("Triple B ka ba?!")
                else:
                    print("SBAPN!")
                    
            elif choose == "":
                clear()
                print("Kupal, wala ka naman nilagay Boi~!")
            else:
                clear()
                print("Ang kulit mo Boi~!")

    else:
        error("Invalid user or password!")
        input("Press Enter to continue")
