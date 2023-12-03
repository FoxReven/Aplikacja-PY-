import os
import time
from error_box import *

def __Start_app()->None: # Funkcja prywatna która przyjmuje obiekt menu głownego 
     os.system("cls")
     start=menu_start()
     start._menu()
     start._opcion()
     start._key_opicon()

def _menu_go(): #odczyt funcki prywatnej 
       __Start_app()

class menu_start: # obiekt 
     
      def _menu(self)->str: 
             print("\t\t\tWitamy W aplikajci MXr \n" 
                   "Zaraz Wyswietlą sie opcje dowyboru")
             

      def _opcion(slef)->None: # lista poleceni 
            time.sleep(1)
            lista_opcion={"Nowe Zamówienie ", "Podgląd Zamówienia" , "Dział Pomocy " } 

            for x , y in enumerate(lista_opcion):

                  print(x+1,y)
      
      



      def _key_opicon(self)->int:

            try : # klawisz 
                  key=int(input("Kliknij odpowieni kalwisz : "))

            except ValueError : # wyłapywanie błednego klawiszuu 
                   os.system("cls")
                   NameError="E40" 
                   print(f"wystąpił  bład :  {NameError} zaraz program cie przeniesie do działu pomocy ")
                   error="E40"
                   time.sleep(2)
                   errorbox=Hellp_box(error)
                   errorbox.menu()
                   errorbox.loding()
                   errorbox.error_box()

            else: # przenoszenie do odpowiedniego działu 
                  os.system('cls')
                  self._next_opicon()
                                               
            

      def _next_opicon(self)->int: # pole wyboru 

            match  self.key:

                  case 1 : 
                        print("dział w budowie ")
                  case 2: 
                        pass
                  case 3 : 
                        pass 
                  case _ : 
                        pass  
                         
            

        


_menu_go()