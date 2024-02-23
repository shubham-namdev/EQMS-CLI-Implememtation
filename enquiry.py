import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to your file
enqFilePath = os.path.join(current_dir, "enquiry.txt")
#enqFilePath = "D:\VSCODE\Project\enquiry.txt"

def clear():
    os.system('cls')

def toDict(line : str) -> dict :
    line = line.split(sep=',')
    mapping = dict()
    for l in line:
        ls = l.split(sep = ":")
        mapping[ls[0].strip()] = ls[1].strip()
    
    return mapping

def get_lastEnqNo() -> int:
    ids = []
    file = open(file=enqFilePath, mode='r')
    for line in file:
        mapping = toDict(line)
        ids.append(int(mapping['Enq ID']))
    
    return max(ids)

def printEnquiry(enqno = None) -> None:
    clear()
    print('='*25 + '\n' + f":: ENQUIRY NO - {enqno} ::" + '\n' + '='*25)

    if enqno:
        with open(enqFilePath, 'r') as file:
            f = True
            for line in file:
                mapping = toDict(line)
                if next(iter(mapping.values())) == enqno:
                    for k, v in mapping.items():
                        print(f"{k}" + " "*(20 - len(k)) + ':' + f"{v}")
                    f = False
            if f:
                print("Enquiry Number Not Found :(")
                time.sleep(1)
                clear()
                return 1
    else:
        with open(enqFilePath, 'r') as file:
            for line in file:
                mapping = toDict(line)
                for k, v in mapping.items():
                        print(f"{k}" + " "*(20 - len(k)) + ':' + f"{v}")
                print("="*50)

def list_enquiry():
    print('='*25 + '\n' + ":: ENQUIRY LISTING ::" + '\n' + '='*25)
    ch = int(input("""
Please Choose -
================
1. See all the Enquiries
2. See enquiry by Enquiry number
5. Back to Enquiry Page
================
>> """))
    if ch == 1:
        printEnquiry()
    elif ch == 2:
        enqNo = input("Please Enter the Enquiry Number : ")
        printEnquiry(enqNo)
        list_enquiry()
    elif ch == 5:
        clear()
    else :
        clear()
        print('='*25 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*25)
        time.sleep(1.5)
        clear()
        list_enquiry()
    
def register_enquiry():

    print('='*25 + '\n' + ":: ENQUIRY REGISTERATION ::" + '\n' + '='*25)

    enqid = int(get_lastEnqNo()) + 1 

    customer_name = input("Enter your name : ")

    contact_Person = input("Enter name of person you contacted : ")

    address = input("Enter your registered address : ")

    telephone_number = int(input("Enter your telephone number : "))

    emailId = input("enter your email id : ")

    source = "online"

    remarks = input("Write remark : ")
    enq_details = f"Enq ID :{enqid}, Customer Name :{customer_name}, Contact Person :{contact_Person}, Address :{address}, Telephone Number :{telephone_number}, Email :{emailId}, Source :{source}, Remarks :{remarks}"

    with open(file=enqFilePath, mode='a') as file:
        file.write(enq_details + '\n')
        file.flush
        print("Enquiry added Successfully :)")
    
    ch = input("Do you wanna add more enquiries (y/n) : ")
    if ch.lower() == 'y':
        clear()
        register_enquiry()
    else:
        clear()

def delete_enquiry():
    print('='*25 + '\n' + ":: DELETE ENQUIRY ::" + '\n' + '='*25)
    no = input("Enter the Enquiry No : ")

    if int(no) > int(get_lastEnqNo()):
        print('='*25 + '\n' + ":: INVALID ENQUIRY NO ::" + '\n' + '='*25)
        clear()
        delete_enquiry()
    else:
        print('='*25 + '\n' + F":: ENQUORY NO {no}::" + '\n' + '='*25)
        fl = printEnquiry(no)
        if not fl:
            print("="*30)
            choice = input("Are you sure you wanna delete (y/n) : ")
            if choice.lower() == 'y':          
                with open(enqFilePath, "r") as file:
                    lines = file.readlines()
                with open(enqFilePath, "w") as output_file:
                    for line in lines:
                        if f'Enq ID :{no}' not in line:
                            # Write the line to the output file
                            output_file.write(line)
                print('='*25 + '\n' + F":: DELETED ENQUIRY NO - {no} ::" + '\n' + '='*25)
                time.sleep(1.5)
                clear()

def main_enquiry() -> None:
    exc = 0
    print('='*25 + '\n' + ":: ENQUIRY PAGE ::" + '\n' + '='*25)
    print(
"""SERVICES OFFERED :
====================== 
1. Register Enquiry
2. Delete Enquiry 
3. View Enquiry
5. Main Page
======================
>> """, end="")
    ch = int(input())
    if ch == 1:
        clear()
        register_enquiry()
    elif ch == 2:
        clear()
        delete_enquiry()
    elif ch == 3:
        clear()
        list_enquiry()
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
        main_enquiry()   
   
    if not exc :
        main_enquiry()


