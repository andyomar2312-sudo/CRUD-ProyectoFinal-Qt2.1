participantes = []
contador_id = 1

def agregar():
  global contador_id 

  
  nombre=str(input("Ingrese el nombre del participante: "))
  if nombre.strip() == "":
    print("Error, el nombre no puede estar vacio")
    return
 
  try: 
    edad=int(input("Ingrese la edad del participante: "))
   
    if edad < 12: 
      print("La edad debe ser mayor o igual a 12")
      return 
    puntaje = float(input("Ingrese el nuevo puntaje inicial: "))
   
    if puntaje < 0:
      print("Error el puntaje no puede ser negativo: ")
      return
    participante= [contador_id, nombre, edad, puntaje ]
    participantes.append(participante)
    print("El participante se ha guardado correctamente")
    contador_id += 1
    print("----------------------------------------------")
    
  except ValueError:
      print("Error la edad debe ser un numero entero")
  return
   
  
def leer():
  if len(participantes) == 0:
    print("Aun no hay participantes registrados")
    return
  
  for participante in participantes: 
    
    print("ID ", participante[0])
    print("Nombre ", participante[1])
    print("Edad ", participante[2])
    print("Puntaje ", participante[3])
  
  
def actualizar():
  if len(participantes) == 0:
    print("Aun no hay participantes registrados")
    return
  try:
    id_buscado=int(input("Ingrese el id del participante: "))
    
  except ValueError: 
    print("Error: El ID debe ser numerico")
    
  for participante in participantes:
    
    if participante[0]== id_buscado:
      nombre=input("Ingrese el nombre del participante: ").strip()
      
      if nombre.strip() == "":
        print("Error, el nombre no puede estar vacio")
        return
      
      try: 
        edad=int(input("Ingrese la nueva edad del participante: "))
       
        if edad < 12: 
          print("La edad debe ser mayor o igual a 12")
          return 
        puntaje = float(input("Ingrese un nuevo puntaje inicial: "))
        
        if puntaje < 0:
          print("Error el puntaje no puede ser negativo: ")
          return
        
      except ValueError:
        print("Error edad o puntaje invalidos")
        return
    
      participante[1] =nombre
      participante[2] = edad
      participante[3] = puntaje

      print("El participante se ha actualizado correctamente")
      
      print("----------------------------------------------")
      return
  print("Participante no encontrado")
   
  
def eliminar ():
  if len(participantes) == 0:
    print("Aun no hay participantes registrados")
    return
  
  try:
    id_buscado=int(input("Ingrese el id del participante: "))
    
  except ValueError: 
    print("Error: El ID debe ser numerico")
    
  for participante in participantes:
    
    if participante[0]== id_buscado:
      participantes.remove(participante)
      print("Participante ha sido eliminado correctamente")
      return
  print("Participante no encontrado")
 
def calcular_puntos_recursiva(rondas):
  if rondas == 1:
   return 1
  return rondas + calcular_puntos_recursiva(rondas-1)
  
  
    
    
def calcular_rondas():
  try: 
    rondas= int(input("Ingrese el numero de rondas ganadas: "))
    if rondas <= 0 : 
      print("El numero de rondas debe ser mayor a 0")
      return
    total = calcular_puntos_recursiva(rondas)
    print("Total de puntos acumulados: ", total)
    
  except ValueError: 
    print("Error: Ingrese un numero entero")
    return
  
  

def menu():
  while True: 
    print("------------Menú torneo------------")
    print("1. Agregar participante")
    print("2. Leer participante")
    print("3. Actualizar participante")
    print("4. Eliminar participante")
    print("5. Calcular puntos por rondas")
    print("6. Salir")
    print("------------------------------------")
    try:
      opcion=int(input("Ingrese una opcion: ")) 
      if opcion == 1:
        print("Agregar participante")
        agregar()  
      elif opcion == 2:
        print("Leer participante")
        leer()
      elif opcion == 3:
        print("Actualizar participante")
        actualizar()
      elif opcion == 4:
        print("Eliminar participante")
        eliminar()
      elif opcion == 5:
        print("Calcular puntos por rondas")
        calcular_rondas()
      elif opcion == 6:
        print("Saliendo..")
        break
    
    except ValueError:
         print("Error: Se debe ingresar un numero entre 1 y 6")
    

  
menu()