"""
Run This File
"""

import product
import enquiry
from utils import clear, color
import time


class App:
    def run(self) :
        print('='*30 + '\n' + ":: WELCOME TO EQMS CLI ::" + '\n' + '='*30)
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
            color('white')
            enquiry.main_enquiry()
        elif ch == 2:
            clear()
            color('white')
            print("="*25)
            product.main_product()
        elif ch == 5:
            clear()
            color('green')
            print('='*30 + '\n' + ":: THANK YOU FOR VISITING ::" + '\n' + '='*30)
            time.sleep(1)
            color('white')
            exit()
        else:
            color('red')
            clear()
            print('='*30 + '\n' + ":: INVALID CHOICE ::" + '\n' + '='*30)
            time.sleep(1)
            color('white')
            clear()
            self.run()
        
        self.run()
        
if __name__ == "__main__" :
    clear()
    app = App()
    app.run()
