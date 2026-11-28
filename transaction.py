import datetime 
import random
def transaction_details():
    tid=random.randint(1000,9999)
    date=datetime.datetime.now()
    print("Transaction id:",tid)
    print("Transaction date:",date)