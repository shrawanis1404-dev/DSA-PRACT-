from datetime import datetime 
import threading
import time
import transaction
class InsufficientBalance(Exception):
        pass
class Account:
            count=0
            def __init__(self,acno,name,atype,bal):
                     self.acno=acno
                     self.name=name
                     self.atype=atype
                     self.__bal=bal
                     self.lock=threading.Lock()
                     Account.count+=1
            def get_balance(self):
                    return self.__bal
            def set_balance(self,balance):
                    self.__bal=balance
            def display(self):
                print(self.acno,self.name,self.atype,self.__bal)
            def deposit(self,amt):
                    if amt<=0:
                            raise ValueError("Invalid amount")
                    else:
                            with self.lock:
                              self.__bal+=amt
                            print("Amount deposited successfully")
            def withdraw(self,amt):
                    if amt<=0:
                            raise ValueError("Invalid amount")
                    with self.lock:
                        if amt>self.__bal:
                            raise InsufficientBalance("Insufficient balance")
                        self.__bal-=amt
                    print("amount withdrawn successfully")
            
            def cal_interest(self):
                    return 0
            @classmethod
            def total_accounts(cls):
                    return cls.count
class SavingsAccount(Account):
        def cal_interest(self):
                return self.get_balance() * 0.05
class CurrentAccount(Account):
        def cal_interest(self):
                return 0
class Bank:
            def __init__(self):
                    self.accounts=[]
            def add_account(self,acc):
                    self.accounts.append(acc)
            def search(self,acno):
                    for a in self.accounts:
                        if a.acno==acno:
                                return a
                    return None
            def display_all(self):
                    for a in self.accounts:
                            a.display()
def generate_report(account):
                    print(account.name,"Report generating")
                    time.sleep(1)
                    print(account.name,"Report generated")
a1=SavingsAccount(101,"varun","savings",10000)
a2=CurrentAccount(1012,"shravya","current",18272)

bank=Bank()
bank.add_account(a1)
bank.add_account(a2)
bank.display_all()
print("Balance:",a1.get_balance())
a1.set_balance(120009)
print("updated balance:",a1.get_balance())
print("\nDEPOSIT")
a1.deposit(2019)
print("\nWITHDRAWAL")
a1.withdraw(1000)

print("\nFINAL BALANCE")
print(a1.get_balance())
print(a2.get_balance())
print("\nAccount Search")

acc = bank.search(1012)

if acc:
    print("Account Found Successfully")
    acc.display()
else:
    print("Account not found")
print("\nException handling")
try:
        a1.deposit(-890)
except ValueError as e:
        print(e)
try:
        a1.withdraw(40000)
except InsufficientBalance as i:
        print(i)
except ValueError as e:
        print(e)
finally:
        print("transaction completed")
print("\n----Transaction Details")
transaction.transaction_details()
print("\nInterest Calculation")
print("Account 1 Interest:", a1.cal_interest())
print("Account 2 Interest:", a2.cal_interest())
print("\nTotal accounts:",Account.total_accounts())
t1=threading.Thread(target=generate_report,args=(a1,))
t2=threading.Thread(target=generate_report,args=(a2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(" all reports generated successfully")

        

                     