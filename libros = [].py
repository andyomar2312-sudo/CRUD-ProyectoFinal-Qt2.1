libros = []
contador_id = 1



def agregar():
  global contador_id
  
  nombre=str(input("Ingrese el titulo del libro:  ")).strip()
  if nombre.strip() == "":
    print("El titulo no puede estar vacio")
    return
         
  try:
    autor=str(input("Ingrese el autor del libro")).strip()
    if autor.strip() =="":
      print("El autor no puede estar vacio")
      return
    
    pag=int(input("Ingrese el numero de paginas: "))
    if pag <= 0:
      print("Error: el numero de paginas debe ser mayor que 0")
      return
    
    libro=[contador_id, nombre, autor, pag]
    libros.append(libro) 
    
    print("El libro se ha guardado ecitosamente") 
    contador_id += 1    
    
  except ValueError:
    print("Error: El titulo no puede estar vacio ")
    return
  
  
def mostrar():
  
  if len(libros) == 0:
    print("Aun no existen libros registrados")
    return
      
  for libro in libros:
    print("ID ", libro[0])
    print("Nombre ", libro[1]) 
    print("Autor ", libro[2]) 
    print("Numero de pag ", libro[3])
    
def actualizar():
  if libros == 0:
      print("No puede haber libros vacios")
      return
    
  try:
    valor_id=int(input("Ingrese el ID del ibro: "))
    
  except ValueError:
    print("Error: el id debe ser un valor numerico entero")
    return
  
  for libro in libros:
    
    if libro[0]==valor_id:
  
      nombre=str(input("Ingrese el nuevo titulo del libro:  ")).strip()
      if nombre.strip() == "":
        print("El titulo no puede estar vacio")
        return
            
      try:
        autor=str(input("Ingrese el autor del nuevo libro: ")).strip()
        if autor.strip() =="":
          print("El autor no puede estar vacio")
          return
        
        pag=int(input("Ingrese el numero de paginas del nuevo libro registrado: "))
        if pag <= 0:
          print("Error: el numero de paginas debe ser mayor que 0")
          return   
        
      except ValueError:
        print("Error: El titulo no puede estar vacio ")
        return
      
      libro[1]=nombre
      libro[2]=autor
      libro[3]=pag
      
      print("El libro ha sido actualizado exitosamente")
      return
    print("Participante no encontrado")
    
    
def eliminar():
  if len(libros) == 0:
   print("No existen libros registrados")
   return
    
  try:
    valor_id=int(input("Ingrese el ID del ibro: "))
    
  except ValueError:
    print("Error: el id debe ser un valor numerico entero")
    return
  
  for libro in libros:
    
    if libro[0]==valor_id:
      libros.remove(libro)
      print("El libro ha sido eliminado exitosamente")
      return
  print("Libro no encontrado")
     
        
def calcular_pag(pag):
  if pag == 1:
    return  1
  return pag + calcular_pag(pag-1) 

def calcular_paginas():
  try:
    pag=int(input("Ingrese el numero de paginas: "))
    if pag <= 0:
      print("Error: el numero de paginas debe ser mayor que 0")
      return
    total = calcular_pag(pag)
    print("Numero total de paginas: ", total)
    
    
  except ValueError:
    print("El numero de paginas debe ser un numero entero")
    return
  



def menu():
  user = "danis123"
  pasw = "epn123"

  intentos = 3

  while intentos > 0:

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == user and clave == pasw:
        print("Acceso concedido")
        break

    intentos -= 1

    if intentos > 0:
        print("Usuario o clave incorrectos")
        print("Intentos restantes:", intentos)
    else:
        print("Acceso bloqueado")
        return

  print("-------------Menu-----------")
  print("1. Agregar libro")
  print("2. Mostrar libro")
  print("3. Actaualizar libro")
  print("4. Eliminar libro")
  print("5. Calcular total de paginas")
  print("6. Salir")
  
  try: 
    opcion=int(input("Ingrese una opcion: "))
    
    if opcion == 1:
      print("Agregando libro .....")
      agregar()
    
    elif opcion == 2:
      print(" Mostrando libro ....")
      mostrar()
     
    elif opcion == 3:
      print("Actaualizando libro ....")
      actualizar()
       
    elif opcion == 4:
      print("Eliminando libro .....")
      eliminar()
       
    elif opcion == 5:
      print("Calculando total de paginas .....")
      calcular_paginas
       
    elif opcion == 6:
      print("Saliendo ......") 
    
  except ValueError:
    print("Error: se debe agregar un numero entre 1-6")
  
  
menu()
  
  