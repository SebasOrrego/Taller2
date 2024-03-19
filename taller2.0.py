

import os  
import random  

# Define colores ANSI para resaltar el texto
color_amarillo = "\033[93m"
color_azul = "\033[94m"
color_rojo = "\033[91m"
color_reset = "\033[0m"

 # Inicializa un diccionario vacío para el inventario modificado
inventario_modificado = {} 

# Define un diccionario con productos y sus cantidades y umbrales
inventario = {  #
    'tornillos': [1000, 500],
    'placas': [1000, 200],
    'cables': [800, 300],
    'tuercas': [600, 400],
    'engranajes': [400, 200],
    'resistencias': [700, 300],
    'transistores': [500, 250],
    'leds': [1000, 500],
    'condensadores': [600, 350],
    'interruptores': [400, 200]
}
 # Crea una copia del inventario original en 'inventario_modificado'
inventario_modificado = dict(inventario) 

# Define una función para agregar un nuevo producto al inventario
def agregar_producto():
    limpiar_consola()  
    try:
        # Solicita al usuario el nombre del producto
        llave_nueva = str(input("Ingrese el nombre del nuevo producto con máximo 20 caracteres alfanuméricos: "))  
        # Solicita al usuario la cantidad del nuevo producto
        cantidad_nueva = int(input("Ingrese la cantidad con máximo 20 dígitos: "))  
        # Solicita al usuario el umbral mínimo del nuevo producto
        umbral_nuevo = int(input("Ingrese el umbral mínimo con máximo 20 dígitos: "))  
        
        # Verifica si los valores ingresados son válidos
        if (all(caracter.isalnum() or caracter in ['-', '_', ',', '.'] for caracter in llave_nueva)) and cantidad_nueva > 0 and umbral_nuevo > 0:
            if len(llave_nueva) > 20 or len(str(cantidad_nueva)) > 20 or len(str(umbral_nuevo)) > 20:
                raise ValueError()
            else:
                print("Datos ingresados exitosamente") 
                pausar_para_continuar()
                # Retorna un diccionario con el nuevo producto y sus detalles
                return {llave_nueva: [cantidad_nueva, umbral_nuevo]} 
        else:
            raise ValueError()
    except (ValueError, TypeError):
        print("Uno o más valores ingresados no son coherentes")  

# Define una función para mostrar un reporte del inventario
def mostrar_reporte_de_inventario(inventario_modificado_copy1):
    limpiar_consola()  
    print("Reporte de Inventario")  
    # Imprime el encabezado en amarillo
    print(f"{color_amarillo}| Producto \t\t| Cantidad \t\t| Umbral{color_reset}")  
    
    # Agrega una línea horizontal debajo del encabezado
    print("-"*60 )
    
    # Imprime los datos de inventario con colores según la cantidad
    for producto, detalles in inventario_modificado_copy1.items():
        cantidad = detalles[0]
        umbral = detalles[1]
        if cantidad <= umbral:
            print(f"| {color_azul}{producto:21}{color_reset} | {color_rojo}{str(cantidad):21}{color_reset} | {color_reset}{str(umbral)}{color_reset}")
        elif cantidad <= umbral * 1.1:
            print(f"| {color_azul}{producto:21}{color_reset} | {color_amarillo}{str(cantidad):21}{color_reset} | {color_reset}{str(umbral)}{color_reset}")
        else:
            print(f"| {color_azul}{producto:21}{color_reset} | {color_reset}{str(cantidad):21}{color_reset} | {color_reset}{str(umbral)}{color_reset}") 
    pausar_para_continuar()  

# Define una función para calcular el inventario total
def calcular_inventario_total(inventario_modificado_copy2):
    limpiar_consola()  
    # Calcula el inventario total
    inventario_total = sum(cantidad[0] for cantidad in inventario_modificado_copy2.values())  
    print(f"Inventario Total: {color_azul}{inventario_total}{color_reset}")  
    pausar_para_continuar()  
    
 # Define una función para simular el consumo de productos de forma aleatoria

# Simular consumo
def simular_consumo():
    limpiar_consola() 
    for producto, detalles in inventario_modificado.items():
        cantidad_actual = detalles[0]
        if cantidad_actual > 0:
             # Genera una cantidad aleatoria a consumir
            cantidad_consumida = random.randint(1, cantidad_actual) 
            print(f"Se consumieron {cantidad_consumida} unidades de {producto}.")  
            # Actualiza el inventario después del consumo
            inventario_modificado[producto][0] -= cantidad_consumida  
        else:
            print(f"No hay suficientes unidades de {producto} para consumir.")  # Imprime un mensaje si no hay suficientes unidades
    pausar_para_continuar()  # Pausa el programa para continuar

 # Define una función para verificar productos que están por debajo del umbral mínimo

# Alertas de Reorden
def verificar_alertas_reorden():
    limpiar_consola() 
    print("Productos en alerta de reorden:")  
    # Define color rojo ANSI para resaltar el texto
    color_rojo = "\033[91m"  
    # Define el color de texto predeterminado ANSI
    color_reset = "\033[0m"  
    
    # Imprime el encabezado de la tabla
    print(f"{color_amarillo}| Producto \t\t| Cantidad \t\t| Umbral{color_reset}")  
    
    # Agrega una línea horizontal debajo del encabezado
    print("-"*60 )
    
    # Imprime los productos en alerta de reorden con colores
    for producto, detalles in inventario_modificado.items():
        cantidad_actual = detalles[0]
        umbral_minimo = detalles[1]
        if cantidad_actual < umbral_minimo:
            print(f"| {color_azul}{producto:21}{color_reset} | {color_rojo}{str(cantidad_actual):21}{color_reset} | {color_reset}{str(umbral_minimo)}{color_reset}")
    
    pausar_para_continuar()  

 # Define una función para reabastecer un producto específico en el inventario

# Rebastecer Producto
def reabastecer_producto():
    limpiar_consola() 
    producto_reabastecer = input("Ingrese el nombre del producto que desea reabastecer: ")  
    producto_reabastecer = producto_reabastecer.lower()  
    # Verifica si el producto existe en el inventario
    if producto_reabastecer in inventario_modificado:  
        # Solicita al usuario la cantidad a agregar
        cantidad_a_agregar = int(input(f"Ingrese la cantidad que desea agregar al producto '{producto_reabastecer}': "))  
        # Verifica si la cantidad ingresada es válida
        if cantidad_a_agregar > 0:  
            inventario_modificado[producto_reabastecer][0] += cantidad_a_agregar  # Actualiza el inventario con la cantidad reabastecida
            print(f"Se han reabastecido {cantidad_a_agregar} unidades del producto '{producto_reabastecer}'.")  # Imprime un mensaje de éxito
        else:
            print("La cantidad ingresada no es válida. Debe ser un número positivo.") 
    else:
        print("El producto ingresado no existe en el inventario.") 
    pausar_para_continuar()  

# Define una función para limpiar la consola 
def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')

# Define una función para pausar el programa hasta que el usuario presione enter
def pausar_para_continuar():  
    input("Presione la tecla enter para continuar...")
    limpiar_consola()  # Limpia la consola después de presionar enter

# Inicia el bucle del menú
while True:  
    try:
        opcion_usuario = input("""  # Solicita al usuario seleccionar una opción del menú
Menú de gestión de inventario:
1. Agregar Producto
2. Simular consumo
3. Mostrar reporte de inventario
4. Calcular el inventario Total
5. Verificar alertas de Reorden
6. Rebastecer Producto
7. Salir
Seleccione una opción: """)
        
        
        if opcion_usuario == "1":  
            try:
                # Llama a la función para agregar un nuevo producto
                nuevo_producto = agregar_producto()  
                 # Actualiza el inventario con el nuevo producto
                inventario_modificado.update(nuevo_producto) 
                # Maneja excepciones si ocurren errores al agregar el producto
            except (KeyError, TypeError, ValueError):  
                print("Error al agregar el producto. No se realizaron cambios en el inventario.") 
                pausar_para_continuar()  
                                
        elif opcion_usuario == "2":  
            # Llama a la función para simular el consumo de productos
            simular_consumo()  
       
        # Ejecuta la opción para mostrar el reporte del inventario
        elif opcion_usuario == "3":  
            # Llama a la función para mostrar el reporte del inventario
            mostrar_reporte_de_inventario(inventario_modificado)  
            
        elif opcion_usuario == "4":  # 
            # Llama a la función para calcular el inventario total
            calcular_inventario_total(inventario_modificado)  
            
        elif opcion_usuario == "5": 
            # Llama a la función para verificar alertas de reorden 
            verificar_alertas_reorden()  
            
        elif opcion_usuario == "6":  
            # Llama a la función para reabastecer un producto
            reabastecer_producto()  
            
        elif opcion_usuario == "7":  
            print("**********SALIENDO DEL PROGRAMA***********")
            print("*********Realizado por:**************")
            print("Daniel Francisco Calderón Lebro")
            print("Sebastian Orrego Urrea")  
            break  
        else:
            raise ValueError()  
    except ValueError:
        print('Oops! Opción no válida. Intente de nuevo.')  
        pausar_para_continuar()
