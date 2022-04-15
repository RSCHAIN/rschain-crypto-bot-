#----------------------Creation date:01/04/2022 -----------------------------------------------------------------------------------------------------------
#----------------------bY josias SEHI =====> LOMB12 -----------------------------------------------------------------------------------------------
#--------------------- Program Description --------------------------------------------------------------------------------------------------------

"""
    EN:This program is a crypto bot designed to retrieve information relating to the NFT auctioned on the rarible website.
    
    FR:ce fichier contient la classe qui permet la récupération des informations choisies sur le site rarible.
"""

import argparse
from nftsavedinformation import doFiles


# class that allows to launch the program 
class launchMenu(doFiles): 
    #contructor 
    def __init__(self):
          super().__init__()
          

    # function that launch user menu 
    def start_bot(self):

        parser = argparse.ArgumentParser(description="NFT at Auction  token information process...")
        parser.add_argument("sbot",help ="Start the cripto bot")
       
        args = parser.parse_args()
        print(args.sbot)
        
    # function that launch nft retrieve information  process 
    def launch_nftretrieve_data(self):

        self.fist_page()
        self.rarible_click_explore_button()
        self.rarible_click_onsale_button()
        self.rarible_click_apply_botton()
        self.select_element()
        self.take_information()   
        self.add_information()
       
    # function that starts the process of saving  retrieved nft information in different type of files
    def launch_dofiles_process(self):
        self.auction_information()
        self.do_csv_file()
        self.do_json_file()

    #the main function of the script who allows to starts all of the program
    def main(self):
        try:
            self.start_bot()
            self.launch_nftretrieve_data()
            self.launch_dofiles_process()
            self.driver.close()
        except self.mainexc:
            print("FIN DU PROGRAMME")
            self.driver.quit()



# class instantiation and main function call
if __name__ == '__main__':       
   
    m1 = launchMenu()
    m1.main()
  
