"""
THIS PART IS DONE
No NEED to change ANYTHING

~Shubham
""" 
import os
import time


current_dir = os.path.dirname(os.path.abspath(__file__))

productfilePath = os.path.join(current_dir, "products.txt")

#productfilePath = "D:\VSCODE\Project\products.txt"

def clear():
    os.system('cls')


def toDict(line : list) -> dict :
    line = line.split(sep=',')
    mapping = dict()
    for l in line:
        ls = l.split(sep = ":")
        mapping[ls[0].strip()] = ls[1].strip()
    return mapping

def get_ProcductNo() -> int:
    ids = []
    file = open(file=productfilePath, mode='r')
    for line in file:
        mapping = toDict(line)
        ids.append(int(mapping.get('Prod ID')))
    file.close()
    if not ids:
        return 0
    return max(ids)

def delete_product() -> None:
    print('='*25 + '\n' + ":: DELETE Product ::" + '\n' + '='*25)
    no = input("Enter the Product No : ")

    if int(no) > int(get_ProcductNo()):
        print('='*25 + '\n' + ":: INVALID PRODUCT NO ::" + '\n' + '='*25)
        time.sleep(1)
        clear()
        main_product()
    else:
        print('='*25 + '\n' + F":: PRODUCT NO {no}::" + '\n' + '='*25)
        fl = print_product(no)
        if not fl:
            print("="*30)
            choice = input("Are you sure you wanna delete (y/n) : ")
            if choice.lower() == 'y':          
                with open(productfilePath, "r") as file:
                    lines = file.readlines()
                with open(productfilePath, "w") as output_file:
                    for line in lines:
                        if f'Prod ID :{no}' not in line:
                            # Write the line to the output file
                            output_file.write(line)
                print('='*25 + '\n' + F":: DELETED PRODUCT NO - {no} ::" + '\n' + '='*25)
                time.sleep(1.5)
                clear()

def print_product(prodno = None) -> int:
    clear()
    print('='*25 + '\n' + f":: PRODUCT NO - {prodno} ::" + '\n' + '='*25)

    if prodno:
        with open(productfilePath, 'r') as file:
            f = True
            for line in file:
                mapping = toDict(line)
                if next(iter(mapping.values())) == prodno:
                    for k, v in mapping.items():
                        print(f"{k}" + " "*(20 - len(k)) + ':' + f"{v}")
                    f = False
            if f:
                print("Product Number Not Found :(")
                time.sleep(1)
                clear()
                return 1
    else:
        with open(productfilePath, 'r') as file:
            for line in file:
                mapping = toDict(line)
                for k, v in mapping.items():
                        print(f"{k}" + " "*(20 - len(k)) + ':' + f"{v}")
                print("="*50)

def list_product() -> None:
    print('='*25 + '\n' + ":: PRODUCT LISTING ::" + '\n' + '='*25)
    ch = int(input("""
Please Choose -
================
1. See all the Products
2. See product by Product number
5. Back to Product Page
================
>> """))
    if ch == 1:
        print_product()
    elif ch == 2:
        prodNo = input("Please Enter the Product Number : ")
        print_product(prodNo)
        list_product()
    elif ch == 5:
        clear()
    else :
        clear()
        print('='*25 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*25)
        time.sleep(1.5)
        clear()
        list_product()

def add_product() -> None: 
    print('='*25 + '\n' + ":: ADD PRODUCT ::" + '\n' + '='*25)
    productid = get_ProcductNo() + 1
    product_name = input("Enter product name: ") 
    product_description = input("Enter product description: ") 
    price = float(input("Enter product price: ")) 
    quantity = int(input("Enter product quantity: "))
    
    product_detail = f"""Prod ID :{productid}, Name :{product_name}, Description :{product_description}, Price : {price}, Quantity :{quantity}"""
    
    with open(file=productfilePath, mode='a') as file :
        file.write(product_detail + '\n')
        file.flush()
        print("Product added successfully!") 
        
    ch = input("Do you wanna add more product (y/n) : ")
    if ch.lower() == 'y':
        clear()
        add_product()
    else :
        clear()
        print('='*30 + '\n' + ":: THANK YOU ::" + '\n' + '='*30)
        time.sleep(1)
        clear()

def main_product() :
    exc = 0
    print('='*25 + '\n' + ":: PRODUCT PAGE ::" + '\n' + '='*25)
    print(
"""SERVICES OFFERED :
====================== 
1. Add Product
2. Delete Product 
3. View Product
5. Main Page
======================
>> """, end="")
    ch = int(input())
    if ch == 1:
        clear()
        add_product()
    elif ch == 2:
        clear()
        delete_product()
    elif ch == 3:
        clear()
        list_product()
    elif ch == 5:
        clear()
        print('='*30 + '\n' + ":: THANK YOU ::" + '\n' + '='*30)
        time.sleep(1)
        clear()
        exc = 1
    else:
        clear()
        print('='*30 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*30)
        time.sleep(1)
        clear()
        main_product()   
   
    if not exc :
        main_product()    
