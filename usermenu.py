#----------------------Creation date:01/04/2022 -----------------------------------------------------------------------------------------------------------
#----------------------bY josias SEHI =====> LOMB12 -----------------------------------------------------------------------------------------------
#--------------------- File Description --------------------------------------------------------------------------------------------------------

"""
    EN:This file is intended to allow the user to accurately retrieve information about NFTs at auction.
    
    FR:Ce fichier a pour but de permettre a l'utilisateur de recuperer de maniere precise des informations cncernant les NFT au encheres.
"""

import argparse
from email.policy import default
from unittest import case
from h11 import Data
import pandas as pd
import json

# class that allows to launch the program 
class launchMenu(): 
    #contructor 
    def __init__(self):
        self.data = Data
        self.nftname = str  
        self.nftprice = str
        self.nftdescr = str 
        self.nftendtime = str
        self.args = ""
    
          
          
    # function that allow to get nft name       
    def  nft_name(self):
        try:
         with open('/home/rschain4/Bureau/websraping_project/RARIBLE_NFT_INFORMATION.json') as self.json_data:
            self.data = json.load(self.json_data)
            self.nftname =self.data['name']
            print(self.nftname)
            
        except self.nftnamexc :
            print("error ,nft name not fond")
    # function that allow to get  nft name           
    def  nft_price(self):
        try:
         with open('/home/rschain4/Bureau/websraping_project/RARIBLE_NFT_INFORMATION.json') as self.json_data:
            self.data = json.load(self.json_data)
            self.nftprice =self.data['price']
            print(self.nftprice)
            
        except self.nftpricexc:
            print("error ,nft price not found")
    #  function that allow to get  nft description     
    def  nft_description(self):
        try:
         with open('/home/rschain4/Bureau/websraping_project/RARIBLE_NFT_INFORMATION.json') as self.json_data:
            self.data = json.load(self.json_data)
            self.nftdescr = self.data['description']
            print(self.nftdescr)
            
        except self.nftdescriptionexc:
            print("error ,nft description not found")
    # function that permit to get  nft on auction end time 
    def  nft_end_time(self):
        try:
         with open('/home/rschain4/Bureau/websraping_project/RARIBLE_NFT_INFORMATION.json') as self.json_data:
            self.data = json.load(self.json_data)
            self.nftendtime = self.data['end_time']
            print(self.nftendtime)
            
        except self.nftdecontexc:
            print("error ,nft end time not found")

    # function that launch user menu 
    def launch_user_menu(self):

        parser = argparse.ArgumentParser(description="NFT At Auction Token Information Process...")
        parser.add_argument("-n","--name",action="store_true",help ="The name of NFT at auction")
        parser.add_argument("-p","--price",action="store_true",help ="The price of NFT at auction")
        parser.add_argument("-t","--time",action="store_true",help ="Auction end time")
        parser.add_argument("-d","--description",action="store_true",help ="The NFT at auction description")
        
        self.args = parser.parse_args()
        
    # function that permit to select information expected by the user 
    def user_choice(self):   
        if self.args.name:
            print(self.nft_name())
        elif self.args.price:
            print(self.nft_price())
        elif self.args.time:
            print(self.nft_end_time())
        elif self.args.description:
            print(self.nft_description())  
        else:
            print("please refer you  to information above ")
            
    def start_menu(self):
        print("please if you want to print NFT information do this:\n""Press python3 usermenu.py followed by -h")
        self.launch_user_menu()
        self.user_choice()

        
        
if __name__=='__main__':
        m1 = launchMenu()
        m1.start_menu()
  
