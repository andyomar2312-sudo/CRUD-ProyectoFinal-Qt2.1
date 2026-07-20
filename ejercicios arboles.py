#DRONES


from datos import (
    drones,
    misiones,
    grafo,
    registrar_dron,
    registrar_mision,
    mostrar_drones,
    mostrar_misiones,
    eliminar_dron,
    eliminar_mision,
    agregar_zona,
    agregar_ruta,
    mostrar_grafo
)

from algoritmos import (
    burbuja_prioridad,
    insercion_bateria,
    merge_sort_velocidad,
    quick_sort_distancia,
    busqueda_lineal_dron,
    busqueda_lineal_mision,
    busqueda_binaria_dron
)

from cola import (
    agregar_mision_cola,
    atender_mision,
    mostrar_siguiente
)

from bst import (
    insertar_bst,
    buscar_bst,
    preorden,
    inorden,
    postorden
)

from grafo import (
    bfs,
    dijkstra
)

raiz = None


def menu():
    global raiz
    while True:
        print("\n==============================")
        print(" POLIRESCUE TECHNOLOGIES ")
        print("==============================")
        print("1. Registrar dron")
        print("2. Registrar misión")
        print("3. Registrar zona")
        print("4. Registrar ruta")
        print("5. Mostrar drones")
        print("6. Mostrar misiones")
        print("7. Mostrar zonas")
        print("8. Eliminar dron")
        print("9. Eliminar misión")
        print("10. Burbuja (Prioridad)")
        print("11. Inserción (Batería)")
        print("12. MergeSort (Velocidad)")
        print("13. QuickSort (Distancia)")
        print("14. Buscar dron")
        print("15. Buscar misión")
        print("16. Buscar binaria dron")
        print("17. Cola de misiones")
        print("18. Árbol BST")
        print("19. BFS")
        print("20. Dijkstra")
        print("21. Simulación completa")
        print("0. Salir")

        op = input("\nSeleccione: ")
        if op == "1":
            registrar_dron()
        elif op == "2":
            mision = registrar_mision()
            if mision is not None:
                raiz = insertar_bst(raiz, mision["codigo"])
        elif op == "3":
            agregar_zona()
        elif op == "4":
            agregar_ruta()
        elif op == "5":
            mostrar_drones()
        elif op == "6":
            mostrar_misiones()
        elif op == "7":
            mostrar_grafo()
        elif op == "8":
            eliminar_dron()
        elif op == "9":

            eliminar_mision()

        elif op == "10":

            burbuja_prioridad(misiones)

        elif op == "11":

            insercion_bateria(drones)

        elif op == "12":

            merge_sort_velocidad(drones)

        elif op == "13":

            quick_sort_distancia(misiones,0,len(misiones)-1)

        elif op == "14":

            codigo=input("Código: ")

            busqueda_lineal_dron(codigo)

        elif op == "15":

            codigo=input("Código: ")

            busqueda_lineal_mision(codigo)

        elif op == "16":

            codigo=input("Código: ")

            busqueda_binaria_dron(codigo)

        elif op == "17":

            while True:

                print("\nCOLA")

                print("1 Agregar misión")

                print("2 Atender")

                print("3 Mostrar siguiente")

                print("0 Salir")

                c=input("Opción: ")

                if c=="1":

                    codigo=input("Código misión: ")

                    agregar_mision_cola(codigo)

                elif c=="2":

                    atender_mision()

                elif c=="3":

                    mostrar_siguiente()

                elif c=="0":

                    break

        elif op=="18":

            while True:

                print("\nBST")

                print("1 Buscar")

                print("2 Preorden")

                print("3 Inorden")

                print("4 Postorden")

                print("0 Salir")

                b=input("Opción: ")

                if b=="1":

                    codigo=input("Código: ")

                    buscar_bst(raiz,codigo)

                elif b=="2":

                    preorden(raiz)

                    print()

                elif b=="3":

                    inorden(raiz)

                    print()

                elif b=="4":

                    postorden(raiz)

                    print()

                elif b=="0":

                    break

        elif op=="19":

            destino=input("Zona destino: ")

            bfs(grafo,"Base",destino)

        elif op=="20":

            destino=input("Zona destino: ")

            dijkstra(grafo,"Base",destino)

        elif op=="21":

            print("\n=== SIMULACIÓN ===")

            mision=registrar_mision()

            if mision is None:

                continue

            agregar_mision_cola(mision["codigo"])

            raiz=insertar_bst(raiz,mision["codigo"])

            burbuja_prioridad(misiones)

            print("\nBuscando dron disponible...")

            for dron in drones:

                if dron["estado"]=="Disponible":

                    print("Dron encontrado:",dron["codigo"])

                    existe=bfs(grafo,"Base",mision["zona"])

                    if existe:

                        dijkstra(grafo,"Base",mision["zona"])

                        dron["estado"]="Ocupado"

                        mision["estado"]="En proceso"

                    break

        elif op=="0":

            print("Hasta luego")

            break

        else:

            print("Opción inválida")


menu()