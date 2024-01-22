import os
import json
import random

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "users.json")
cache_json_path = os.path.join(data_folder_path, "user_cache.json")

class User:
# constructor
    def __init__(self,username = None , password = None):
        self.username = username
        self.password = password

# read account cache
    @staticmethod
    def session():
        with open(cache_json_path, "r") as file:
            cacheData = json.load(file)

        return cacheData

# create account
    def create(self):
        
        id = random.random()

        userJsonData = {
            "id" : id,
            "username": f"{self.username}",
            "password": f"{self.password}"
        }

        try:
            with open(json_path, "r") as file:
                prevData = json.load(file)

            userData = [
                *prevData,
                userJsonData,
            ]

        except json.JSONDecodeError:
            userData = [
                userJsonData,
            ]

        with open(json_path, "w") as file:
            json.dump(userData,file)

        return userJsonData

# update account  

    def edit(self , userId):
        with open(json_path, "r") as file:
            userData = json.load(file)

        for data in userData: 
            if(data['id'] == userId):
                data['username'] = self.username
                data['password'] = self.password

                with open(cache_json_path, "w") as file:
                    cacheDataUpdate = json.dump(data,file)
                    
                with open(json_path, "w") as file:
                    json.dump(userData,file)

                return True
            

# read account with username
        
    def readByUserAndPass(self):
        with open(json_path, "r") as file:
            userData = json.load(file)


        for data in userData:
            if(data['username'] == self.username and data['password'] == self.password ):
                with open(cache_json_path, "w") as file:
                    json.dump(data,file)

                return {
                    "status" : True,
                    "msg" : 'Sign in is Successfully',
                }

            
# delete account 
            
    def delete(self, userId):
        with open(json_path, "r") as file:
            prevData = json.load(file)
        
        for index , data in enumerate(prevData):
            if(data['id'] == userId ):
                if(len(prevData) == 1):
                    newData = []
                else:
                    newData = prevData[index - 1 :index]

                with open(json_path, "w") as file:
                    json.dump(newData,file)
            
                return {
                    "status" : True,
                    "msg" : 'Okay, your account has been deleted'
                }         
