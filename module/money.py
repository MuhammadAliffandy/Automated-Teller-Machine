import os
import json

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "balances.json")

class Money:

    def __init__ (self,userId = None):
        self.userId = userId

# add a balance

    def create(self,balance):
        moneyJsonData = {
            "userId" : self.userId,
            "balance" : balance,
        }

        try:
            with open(json_path, "r") as file:
                prevData = json.load(file)

            balanceData = [
                *prevData,
                moneyJsonData,
            ]

        except json.JSONDecodeError:
            balanceData = [
                moneyJsonData,
            ]

        with open(json_path, "w") as file:
            json.dump(balanceData,file)

        return moneyJsonData
    
# read balance
    def read(self):
        try:
            with open(json_path, "r") as file:
                balanceData = json.load(file)
            
            for data in balanceData: 
                if(data['userId'] == self.userId):
                    return {
                        "status" : True,
                        "data" : data['balance'],
                    }

        except json.JSONDecodeError:
                return {
                        "status" : False,
                        "data" : 0,
                }
        
# add  or update more balance
            
    def update(self , balance , action ):
        with open(json_path, "r") as file:
            balanceData = json.load(file)
        
        for data in balanceData: 
            if(data['userId'] == self.userId):
                if(action == 'DEPOSIT'):
                    data['balance'] = data['balance'] + balance
                elif(action == 'PULL'):
                    data['balance'] = data['balance'] - balance
                
                with open(json_path, "w") as file:
                    json.dump(balanceData,file)
                    
# delete balances 
    def delete(self):
        with open(json_path, "r") as file:
            prevData = json.load(file)
        
        for index , data in enumerate(prevData): 
            if(data['userId'] == self.userId):
                if(len(prevData) == 1):
                    newData = []
                else:
                    newData = prevData[index - 1 :index]

                with open(json_path, "w") as file:
                    json.dump(newData,file)

# exchange money :
    def exchange(self,cash,moneyType): 
        if(moneyType == 'MLY'):
            value = cash * 3388
        elif(moneyType == 'JPN'):
            value = cash * 126
        elif(moneyType == 'KOR'):
            value = cash * 12
        elif(moneyType == 'USA'):
            value = cash * 14.344

        return value