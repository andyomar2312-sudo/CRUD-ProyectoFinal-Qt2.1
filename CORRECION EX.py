peliculas=[]
contador = 1

def agregar():

    global contador
     
    nombre=input("Ingrese el nombre de la película: ").strip()

    if nombre == "":
        print("El nombre de la película no puede estar vacío")
        return

    try:

        precio=float(input("Ingrese el precio de la película: "))
        if precio<=0:
            print("El precio debe ser mayor que 0")
            return
        
        stock=int(input("Ingrese el stock de la película: "))
        if stock<=0:
            print("El stock de la película debe ser mayor que 0")
            return
        
        pelicula=[contador, nombre, precio, stock]

        peliculas.append(pelicula)
        contador  += 1
        print("Película agregada correctamente")
        print("Daniela Martinez")

    except ValueError:
        print("Error, ingrese datos válidos ")
        return
    

def leer(): 

    if len(peliculas) == 0:
        print("Películas no registradas")
        return
           
    for pelicula in peliculas:

        print("----------------------------------")
        print("ID: ", pelicula[0])
        print("Nombre: ",pelicula[1])
        print("Precio: ", pelicula[2])
        print("Stock: ",pelicula[3])
        print("Daniela Martinez")
        print("----------------------------------")


def actualizar():

    if len(peliculas) == 0:
        print("Películas no registradas")
        return
     
    try:

        v_id=int(input("Ingrese el id de la película: "))

        for pelicula in peliculas:

            if pelicula[0] == v_id:
            
                nombre=input("Ingrese el nuevo nombre de la película:")
                if nombre == "":
                    print("El nombre de la película no puede estar vacío")
                    return

                precio=float(input("Ingrese el precio de la película: "))
                if precio<=0:
                    print("El precio debe ser mayor que 0")
                    return
                
                stock=int(input("Ingrese el stock de la película: "))
                if stock<=0:
                    print("El stock de la película debe ser mayor que 0")
                    return
                
                pelicula[1]=nombre
                pelicula[2]=precio
                pelicula[3]=stock

                print("Película actualizada correctamente")
                print("Daniela Martinez")
                print("----------------------------------")

        print("Película no encontrada")
        print("----------------------------------")
        return

    except ValueError:
        print("Error, ingrese datos válidos ")
        print("----------------------------------")
        return

    
def eliminar():

    if len(peliculas) == 0:
        print("Películas no registradas")
        return
    
    try:

        v_id=int(input("Ingrese el id de la película: "))

        for pelicula in peliculas:

            if pelicula[0] == v_id:
                peliculas.remove(pelicula)
                print("Película eliminada correctamente")
                print("Daniela Martinez")
                print("----------------------------------")
                return

        print("Película no encontrada")
        print("----------------------------------")
        return

    except ValueError:
        print("Ingrese datos válidos")


def menu():

    while True:

        print("------------MENÚ----------------------")
        print("1. Agregar peliculas")
        print("2. Leer peliculas")
        print("3. Actualizar peliculas")
        print("4. Eliminar peliculas")
        print("5. Salir")
        print("--------------------------------------")

        opcion=int(input("Ingrese una opcion: "))

        try:                

            if  opcion==1:
                print("Usted eligió la opción 1: 'Agregar peliculas'")
                agregar()
                
            elif opcion==2:
                print("Usted eligió la opción 2: 'Leer peliculas'")
                leer()

            elif opcion==3:
                print("Usted eligió la opción 3: 'Actualizar peliculas'")
                actualizar()

            elif opcion==4:
                print("Usted eligió la opción 4: 'Eliminar peliculas'")
                eliminar()

            elif opcion==5:
                print("Saliendo del  sistema.......")
                print("Daniela Martinez")
                break

        except ValueError:
            print("Ingrese una opción válida")
            return
       

menu()