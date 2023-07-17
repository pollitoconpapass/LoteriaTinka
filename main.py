import random

respuesta = "Si"
while respuesta == "Si":
   print("\nLOTERIA INSTANTANEA DE LA TINKA")
   print ("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
  
   numeroganador = random.randint(0,5)
   ganador = False
   nombre = input("Ingrese nombre del jugador: ")
  
   for intento in range (1,4):
     numero = int(input("Ingrese un numero (0-5): "))
     
     while numero < 0 or numero > 5:
       print("ERROR. Número fuera de rango")
       numero = int(input("Ingrese un número (0-5):"))
       
     if numero == numeroganador:
       ganador = True
       break
     else:
       print ("Lo Siento, vuelve a intentarlo")
       
   if ganador:
     print("¡¡FELICITACIONES ERES UN GANADOR!!")
     if intento == 1:
       print("Ganaste 2000 soles")
     elif intento == 2:
       print("Ganaste 1000 soles")
     else:
       print("Ganaste 500 soles")
   else:
     print("LO SIENTO PERDISTE EL JUEGO, VUELVE A INTENTARLO")
   respuesta = input("Hay otro cliente Si/No: ")

print("JORNADA TERMINADA")
