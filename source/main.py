from logging import exception
from multiprocessing.sharedctypes import Value
from operator import truediv
import requests
import pandas as pd
import datetime

def date_check():
    while True:
        try:
            user_input=input("Enter date in format yyyy-mm-dd: ")
            if user_input == "":
                raise exception()
            date_str=pd.Timestamp(user_input)      
            break
        
        except:
            print("Please enter in the format yyyy-mm-dd")    
    
    return date_str

def str_to_value(text_input):
    text_input=text_input.split("\n")
    new_str=text_input[1].split(",")
    value=new_str[1]
    return value
    
def main():

    req_date=date_check()

    data=requests.get("https://data.nasdaq.com/api/v3/datasets/OPEC/ORB.csv?rows=1&end_date={0}&order=asc&api_key=szfUizy9_TxB5H-VJW2T".format(req_date))

    price=str_to_value(data.text)

    print("\n"+data.text)

    print("THE PRICE IS: {} USD".format(price))
    main()

main()














