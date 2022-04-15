#----------------------Creation date:01/04/2022 -----------------------------------------------------------------------------------------------------------
#----------------------bY josias SEHI =====> LOMB12 -----------------------------------------------------------------------------------------------
#--------------------- file Description --------------------------------------------------------------------------------------------------------

"""
    EN:this file allows the recovery of information concerning the NFTs auctioned on the rarible site.
    
    FR:ce fichier permet la recuperation des informations concernant les NFT mis au enchere sur le site rarible .
""" 

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Class for retrieving information from nfts auctioned on the rarible website
class nftRetrieveData:
    
    #contructor 
    def __init__(self):
     self.PRICE =[]
     self.DESCRIPTION =[]
     self.END_TIME =[]
     self.NAME =[]
     self.name = ""
     self.price= ""
     self.description = ""
     self.end_time = ""
     self.text_format = ""
     self.onsale_price = ""
     self.onsale_name = ""  
     
        

    # function to open the chrome browser and launch the rarible website
    def fist_page(self):
      try:
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
        self.driver.get('https://rarible.com/')
        self.driver.maximize_window()
        time.sleep(2)  # wait for the website for 2 second 
      except self.fistpagexc:
        print("error open page")
        self.re_init()
      
    # function allowing to redo the actions of the function "fist_page" in case of failure.
    def re_init(self):
        time.sleep(10)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://rarible.com/')
        self.driver.maximize_window()
        
    # function that go to rarible website and click some buttons
    def rarible_click_explore_button(self):
      try:
        self.driver.find_element(By.XPATH,"//span[@class='sc-bdvvtL sc-hKwDye sc-eCImPb klyGzw'][normalize-space()='Explore']").click() # find explore button and click on it 
        self.driver.find_element(By.XPATH,"//span[@class='sc-bdvvtL sc-hKwDye sc-eCImPb cUywCO'][normalize-space()='Ethereum']").click()
        time.sleep(3)

      except self.clickexplorexc:
        print("failed to click on explore or ethreuim button")
        self.re_click_explore_button()



    # function allowing to click on "on sale" button  
    def rarible_click_onsale_button (self):

      try:
        self.driver.find_element(By.XPATH,"//span[contains(text(),'On sale')]").click()         
        self.driver.find_element(By.XPATH,"//div[normalize-space()='Buy now']").click()    
        time.sleep(3)
      except self.clickonsalexc:
        self.re_click_onsale_button()
        

    # function 
    def rarible_click_apply_botton(self):
      try:
        self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
        time.sleep(5)
      except self.clickapplyexc:

        self.re_click_apply_button()
        print("failed to click explore elements") 

    # function 
    def re_click_explore_button(self):
       time.sleep(5)
       self.driver.find_element(By.XPATH,"//span[contains(text(),'On sale')]").click()         
       self.driver.find_element(By.XPATH,"//div[normalize-space()='Buy now']").click()    
          

    def re_click_onsale_button(self):

       time.sleep(5)
       self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
      

    def re_click_apply_button(self):

       self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
       time.sleep(5)

    # function that select the first nft on top list
    def select_element(self): 
      time.sleep(2)
      try:
        self.fist_element = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-cCcXHH ebRXgR clOqDW dbbKCr']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-jCHUfY eHCPOb clOqDW htmjuM']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-dFtzxp sc-brSvTw sc-cfJLRR ebRXgR clOqDW gSCbae EGfMV fgiRQY']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-ctqQKy ffQRNb clOqDW hrYNC']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-chSlKD ebRXgR clOqDW ckvJRQ']/div[@aria-label='grid']/div[@role='rowgroup']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
        self.achains = ActionChains(self.driver)
        self.achains.move_to_element(self.fist_element).perform()
        time.sleep(3)
        self.fist_element.click()
        time.sleep(10)

      except self.selectelementexc:
        print("failed to select the fist element")
        self.re_select_elements()


    def re_select_elements(self):

        self.r_fist_element = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-cCcXHH ebRXgR clOqDW dbbKCr']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-jCHUfY eHCPOb clOqDW htmjuM']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-dFtzxp sc-brSvTw sc-cfJLRR ebRXgR clOqDW gSCbae EGfMV fgiRQY']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-ctqQKy ffQRNb clOqDW hrYNC']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-chSlKD ebRXgR clOqDW ckvJRQ']/div[@aria-label='grid']/div[@role='rowgroup']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
        self.r_achains = ActionChains(self.driver)
        self.r_achains.move_to_element(self.t).perform()
        time.sleep(3)
        self.r_fist_element.click()
        time.sleep(10)


    # function set up to return the information we need
    def take_information(self):
  
      try:
        self.price = self.driver.find_element(By.XPATH,"//div[@data-marker='root/appPage/token/sidebar/header']//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN kQBJUo clOqDW']").text
        self.description = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
        self.end_time = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cSJSBE clOqDW']").text
        self.name = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
        self.text_format = self.end_time.split('\n')
        time.sleep(7)
      except self.takeinformationexc:
        # planned to return nft "on sale"  informations 
        print("error to take information")
        self.re_take_information()
        self.add_on_bids_information()

    #   function that permit to save nft recovery data
    def add_information(self):
      
      try:
        # puting information in list
        self.NAME.append(self.name)
        self.PRICE.append(self.price)
        self.END_TIME.append(self.text_format)
        self.DESCRIPTION.append(self.description)
        time.sleep(5)
     
      except self.addinformationexc:
            print("failed to add informations")

    def re_take_information(self):

        self.onsale_name = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
        self.onsale_price = self.driver.find_element(By.XPATH,"//div[@data-marker='root/appPage/token/sidebar/header']//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN kQBJUo clOqDW']").text
          
         
    def add_on_bids_information(self):
        self.NAME.append(self.onsale_name)
        self.PRICE.append(self.onsale_price)
        time.sleep(5)
           

if __name__=='__main__':

  r1 = nftRetrieveData()

  r1.fist_page()
  r1.rarible_click_explore_button()
  r1.rarible_click_onsale_button()
  r1.rarible_click_apply_botton()
  r1.select_element()
  r1.take_information()   
  r1.add_information()  
  

       


         
         
