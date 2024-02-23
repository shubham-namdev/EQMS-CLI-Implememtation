import product
import enquiry
import os
import time


def clear():
    os.system('cls')

clear()

class App:

    def run(self) :
        print("Welcome to our Website :)\n")
        print(
"""SERVICES OFFERED :
====================== 
1. Enquiry Page
2. Product Page
5. Exit
======================
>> """, end="")
        ch = int(input())
        if ch == 1:
            clear()
            enquiry.main_enquiry()
        elif ch == 2:
            clear()
            print("="*25)
            product.add_product()
        elif ch == 5:
            clear()
            print('='*30 + '\n' + ":: THANK YOU FOR VISITING ::" + '\n' + '='*30)
            time.sleep(1)
            exit()
        else:
            print('='*30 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*30)
            time.sleep(1)
            clear()
            self.run()
        
        self.run()
        

if __name__ == "__main__" :
    app = App()
    app.run()


   

    
    

