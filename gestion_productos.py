# Lista donde se guardan todos los productos (empieza vacia)
productos = []

# Guarda lo que elige el usuario en el menú
opcion = ""

# El programa se repite hasta que el usuario elija la opcion 5
while opcion != "5":
    # Muestra el menu
    print()
    print("=" * 40)
    print("SISTEMA DE GESTIÓN DE PRODUCTOS".center(40))
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    # Pedir la opcion a ejecutar 
    opcion = input("Elegí una opción (1-5): ").strip()

    match opcion:

        # --- OPCION 1: AGREGAR ---
        case "1":
            print("\n--- Agregar producto ---")

            # Pide nombre y repite si esta vacio
            nombre = input("Nombre del producto: ").strip()
            while nombre == "":
                print("Error: el nombre no puede estar vacío.")
                nombre = input("Nombre del producto: ").strip()

            # Pide la categoria y repite si esta vacia
            categoria = input("Categoría del producto: ").strip()
            while categoria == "":
                print("Error: la categoría no puede estar vacía.")
                categoria = input("Categoría del producto: ").strip()

            # Pide el precio (numero entero mayor a 0)
            precio_texto = input("Precio (sin centavos): ").strip()
            while not precio_texto.isdigit() or int(precio_texto) == 0:
                print("Error: ingresá un número entero mayor a 0.")
                precio_texto = input("Precio (sin centavos): ").strip()

                
            precio = int(precio_texto)

            # Guarda el producto en la lista
            productos.append([nombre.title(), categoria.title(), precio])
            print("Producto agregado correctamente.")

        # OPCION 2: MOSTRAR 
        case "2":
            print("\n--- Productos registrados ---")

            # Si la lista esta vacia avisa
            if len(productos) == 0:
                print("Todavía no hay productos cargados.")
            else:
                # Recorre la lista y muestra cada producto con el numero
                for i in range(len(productos)):
                    print(f"{i + 1}. {productos[i][0]} | {productos[i][1]} | ${productos[i][2]}")

        # OPCION 3: BUSCAR 
        case "3":
            print("\n--- Buscar producto ---")

            if len(productos) == 0:
                print("Todavía no hay productos cargados.")
            else:
                # Pedir el texto a buscar
                busqueda = input("Nombre a buscar: ").strip().lower()
                while busqueda == "":
                    print("Error: escribí algo para buscar.")
                    busqueda = input("Nombre a buscar: ").strip().lower()

                # Contador de productos encontrados
                encontrados = 0

                # Revisar todos los productos
                for i in range(len(productos)):
                    # Si encuentra coincidencias, debe mostrar la informacion completa
                    if busqueda in productos[i][0].lower():
                        print(f"{i + 1}. {productos[i][0]} | {productos[i][1]} | ${productos[i][2]}")
                        encontrados += 1

                # Resultado de la busqueda
                if encontrados == 0:
                    print("No se encontraron resultados.")
                else:
                    print(f"Productos encontrados: {encontrados}")

        # OPCION 4: ELIMINAR 
        case "4":
            print("\n--- Eliminar producto ---")

            if len(productos) == 0:
                print("Todavía no hay productos cargados.")
            else:
                # Mostrar los productos exponiendo los numeros
                for i in range(len(productos)):
                    print(f"{i + 1}. {productos[i][0]} | {productos[i][1]} | ${productos[i][2]}")

                # Pide el numero y repite si no es valido
                numero = input("Número del producto a eliminar: ").strip()
                while not numero.isdigit() or int(numero) < 1 or int(numero) > len(productos):
                    print(f"Error: ingresá un número entre 1 y {len(productos)}.")
                    numero = input("Número del producto a eliminar: ").strip()

                # Borra el producto (se resta 1 porque la lista empieza en 0)
                eliminado = productos.pop(int(numero) - 1)
                print(f"Se eliminó el producto: {eliminado[0]}")

        # OPCION 5: SALIR 
        case "5":
            print("¡Gracias por usar el sistema!")

        # OPCION NO VALIDA 
        case _:
            print("Opción no válida. Elegí un número del 1 al 5.")
