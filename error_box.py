import time
import os
import sys
class Hellp_box:

     
     
     def __init__(self,error) -> None: # funkcja która dziedziczy bład z innej  classy
          self.error=error
          self.boot="Robert"






     def menu(self)->str:  #przedstawienie programu 
          os.system("cls")
          print(f"{self.boot} > witam cie w dziale pomocy drogi użytkowniku widze ze wydżył sie jakiś problem" )
    




     def loding(self)->None: # funkcja która daje na animacje Lodingu .... 
        print("Loading")     
        animation = "|/-\\"
        for i in range(20):
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
            time.sleep(0.1) 






     def error_box(self)->str: # wyszukiwarka błedów 
          
          match self.error:
               
               case "E40":
                    os.system("cls")
                    print(f"{self.boot}> Wychodzi na to że powstała pomyłka w klawiszach \n  "
                    f"{self.boot} > za  5 sekund przeniose cie  do Menu Głównego ")
                    time.sleep(5)
                    ret=Return()
                    ret.loding()
                    ret._return_Menu()
               case "Ex802":
                    os.system("cls")
                    print(f"{self.boot} > Hmmm bład Ex802 jest spowodowany ponieważ nie ma pod tym klawieszem przypisanej opcji ") 
                    ret=Return()
                    ret.loding()
                    ret._return_Menu()    








class Return:
      
      def loding(self)->None:
        os.system("cls")
        print("Loading")     
        animation = "|/-\\"
        for i in range(20):
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
            time.sleep(0.1) 

      def _return_Menu(self)->None:
            
              from main import _menu_go
              _menu_go()

              