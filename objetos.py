from dieta import Dietas
import os
import sys

n1 = Dietas()

class Calculos:   
    
    def menu(self):
        print ("**************** Bienvenido al programa para calculo de peso y talla ideal ***********************")
        print ("Selecciona una opcion ")

        self.opcion1 = print("1. Conocer mi peso ideal ")
        self.opcion2 = print("2. Cual es mi talla ideal ")
        self.opcion3 = print("3. Dieta recomendada ")
        self.opcion4 = print("4. Salir del sitema, luego de salir escribes (exit + enter)")
        
        self.ingre = int(input("Que deseas saber? "))
        os.system ("cls")
        
        if self.ingre == 1:
           self.pesoIdeal()    
           self.herramientas.regresaSyN()
            
        elif self.ingre == 2:
            self.masaMuscular()      
            self.Calculos.masaMuscular()
        
        elif self.ingre == 3:
            n1.dietaNormal()
            self.regresaSyN()
        
        elif self.ingre == 4:
            sys.exit() 
        
        else:
            self.menu() 
    
    def pesoIdeal(self):
        self.estatura = float(input("Digite su estatura separada de un (.) : "))
        
        if self.estatura > 0:
            self.ideal = int((self.estatura - 1)*100)
            print("Su peso ideal es: ", self.ideal, " Kilogramos")
            self.regresaSyN() 
        
                
    def masaMuscular(self):
        
        self.peso = float(input("Digite su peso en KG: "))
        self.estatura = float(input("Digite su estatura separada de un (.): "))
        
        if self.peso > 0 and self.estatura > 0:
            self.masa = self.peso / self.estatura**2
            print("Su masa corporal es: ", int(self.masa))
            
            self.regresaSyN() 
            
        
    
    def regresaSyN(self):
        self.desi = input("Regresar al menú principal Y ")
        os.system ("cls") 
        if self.desi == "y" or self.desi == "Y":
            self.menu()
            os.system ("cls") 
              
        else:
            while self.desi != "y" or self.desi != "Y":
                self.desi = input("Entiendo que estas probando el sistema, quieres volver al menu principal Y ")
                os.system ("cls") 
                if self.desi == "y" or self.desi == "Y":
                    self.menu()
           





