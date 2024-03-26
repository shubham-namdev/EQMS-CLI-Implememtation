"""
Contains Enquiry Page functions. 
"""

import os
import time
from utils import clear, color

current_dir = os.path.dirname(os.path.abspath(__file__))
enqFilePath = os.path.join(current_dir, "enquiry.txt")

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
        ids.append(int(mapping.get('Enq ID')))
    file.close()
    if not ids:
        return 0
    return max(ids)

def printEnquiry(enqno = None) -> int:
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
                clear()
                color('red')
                print('='*40 + '\n' + f":: ENQUIRY NO - {enqno} NOT FOUND ::" + '\n' + '='*40)
                time.sleep(1)
                color('white')
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
        color('red')
        print('='*25 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*25)
        time.sleep(1)
        color('white')
        clear()
        list_enquiry()

def register_enquiry():

    def add_source() -> str:
        code = int(input(
"""Enter Source (select from below options) - 
1. Walk In
2. Seminar
3. Website
4. Exhibition
5. Paper Advertisement
>> """))
        if code == 1:
            return "Walk In"
        elif code == 2:
            return "Seminar"
        elif code == 3:
            return "Website"
        elif code == 4:
            return "Exhibition"
        elif code == 5:
            return "Paper Advertisement"
        else:
            clear()
            color('red')
            print('='*25 + '\n' + ":: INVALID RESPONSE ::" + '\n' + '='*25)
            time.sleep(1)
            color('white')
            clear()
            add_source()


    print('='*25 + '\n' + ":: ENQUIRY REGISTERATION ::" + '\n' + '='*25)

    enqid = int(get_lastEnqNo()) + 1 

    customer_name = input("Enter your name : ")

    contact_Person = input("Enter name of person you contacted : ")

    address = input("Enter your registered address : ")

    telephone_number = int(input("Enter your telephone number : "))

    emailId = input("enter your email id : ")

    source = add_source()

    remarks = input("Write remark : ")

    enq_details = f"Enq ID :{enqid}, Customer Name :{customer_name}, Contact Person :{contact_Person}, Address :{address}, Telephone Number :{telephone_number}, Email :{emailId}, Source :{source}, Remarks :{remarks}"

    with open(file=enqFilePath, mode='a') as file:
        file.write(enq_details + '\n')
        file.flush
        clear()
        color('green')
        print('='*35 + '\n' + ":: ENQUIRY ADDED SUCCESSFULLY ::" + '\n' + '='*35)
        time.sleep(1)
        clear()
        color('white')
    
    ch = input("Do you wanna add more enquiries (y/n) : ")
    if ch.lower() == 'y':
        clear()
        register_enquiry()
    else:
        clear()

def delete_enquiry():
    print('='*25 + '\n' + ":: DELETE ENQUIRY ::" + '\n' + '='*25)
    
    with open(file=enqFilePath) as file:
         for line in file:
                mapping = toDict(line)
                print(f"Enq No {mapping['Enq ID']} --> {mapping['Customer Name']}")
    print()
    print("Enter * to exit")
    print()
    no = input("Enter the Enquiry No : ")
    if no == '*':
        clear()
        color('green')
        print('='*30 + '\n' + ":: REDIRECTING ::" + '\n' + '='*30)
        time.sleep(1)
        color('white')
        clear()
    elif int(no) > int(get_lastEnqNo()):
        clear()
        color('red')
        print('='*25 + '\n' + ":: INVALID ENQUIRY NO ::" + '\n' + '='*25)
        time.sleep(1)
        color('white')
        clear()
        main_enquiry()
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
                color('green')
                print('='*25 + '\n' + F":: DELETED ENQUIRY NO - {no} ::" + '\n' + '='*25)
                time.sleep(1)
                color('white')
                clear()

def main_enquiry() -> None:
    color('white')
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
        color('green')
        print('='*30 + '\n' + ":: THANK YOU ::" + '\n' + '='*30)
        time.sleep(1)
        color('white')
        clear()
        exc = 1
    else:
        clear()
        color('red')
        print('='*30 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*30)
        time.sleep(1)
        color('white')
        clear() 
   
    if not exc :
        main_enquiry()

