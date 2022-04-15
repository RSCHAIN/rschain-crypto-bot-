
#----------------------Creation date:01/04/2022 -----------------------------------------------------------------------------------------------------------
#----------------------bY josias SEHI =====> LOMB12 -----------------------------------------------------------------------------------------------
#--------------------- File Description --------------------------------------------------------------------------------------------------------

"""
    EN: This file allows the creation of various file types in which the recovered information is saved.
    
    FR:Ce fichier permet la creation de divers type de fichier dans lesquels les informations recupere sont sauvegarder.
"""

import json
import time 
import csv
import pandas as pd
from yaml import load
from nftretrievedinformation import nftRetrieveData


#  file creation and backup class
class doFiles(nftRetrieveData):

   #constructor 
   def __init__(self):
      super().__init__()
      self.dico = {}
      self.json_doc = str


   #  auctioned nft information back up function        
   def auction_information(self):

      try:
        self.dico = {'name': self.NAME ,'price': self.PRICE,'description': self.DESCRIPTION,'end_time':
          self.END_TIME}
        self.dataframe = pd.DataFrame(self.dico)
      
      except self.dicoexc:
        print("fail to put auction information on dictionnary")
          
   #  function  that create "csv" file and saved auctionned information      
   def do_csv_file(self):
       
      self.filename = "RARIBLE_NFT_INFORMATION.csv"
      try:
         self.write_csvfile = open(self.filename,"w",encoding="utf-8")
         self.dataframe.to_csv("RARIBLE_NFT_INFORMATION.csv")
      except self.csvfilexc:
         print("failed to print informations in csv file")
         
         
   #  function that saved auction information in "json" file 
   def do_json_file(self):
      try:
         self.json_doc = json.dumps(self.dico,indent=2)
         with open('RARIBLE_NFT_INFORMATION.json',"w",encoding="utf-8") as self.json_file:
            json.dump(self.dico, self.json_file, indent=2)
      except self.jsonfilexc:
         
         print("failed to print informations in json file") 
     
           

if __name__=='__main__':

  d1 = doFiles()
  d1.fist_page()
  d1.rarible_click_explore_button()
  d1.rarible_click_onsale_button()
  d1.rarible_click_apply_botton()
  d1.select_element()
  d1.take_information()   
  d1.add_information()  
  d1.auction_information()
  d1.do_csv_file()
  d1.do_json_file()





   

      