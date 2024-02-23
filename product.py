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
    mapping = dict()
    for l in line:
        ls = l.split(sep = ":")
        mapping[ls[0].strip()] = ls[1].strip()
    
    return mapping

def get_ProcductNo() -> int:
    file = open(file=productfilePath, mode='r')

    file.seek(0, 2)
    end_position = file.tell() - 2
    current_position = end_position
    last_line = ""
    while current_position > 0:
        file.seek(current_position - 1)
        current_position -= 1
        char = file.read(1)
        if char == '\n':
            break
        last_line = char + last_line
    if not last_line:
        return 0
    last_line = last_line.split(sep=',')
    mapping = toDict(last_line)
    return next(iter(mapping.values()))

def add_product() -> None: 
    print('='*25 + '\n' + ":: ADD PRODUCT ::" + '\n' + '='*25)
    productid = int(get_ProcductNo()) + 1
    product_name = input("Enter product name: ") 
    product_description = input("Enter product description: ") 
    price = float(input("Enter product price: ")) 
    quantity = int(input("Enter product quantity: "))
    
    product_detail = f"""Product ID :{productid}, Name :{product_name}, Description :{product_description}, Price : {price}, Quantity :{quantity}"""
    

    
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
        print('='*30 + '\n' + ":: THANK YOU FOR VISITING ::" + '\n' + '='*30)
        time.sleep(1)
        clear()
   
    
