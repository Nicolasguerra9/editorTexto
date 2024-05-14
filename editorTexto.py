import sys # esto es para que la opcion de salir funcione
import os # esto es para add y remove archivos

# esta libreria es para los estilos del documento
import rich
from rich.console import Console
from rich.markdown import Markdown


# 1- CREAR / GUARDAR / MODIFICAR ARCHIVOS
# 2- Estilos en texto (Negrita/Subrayado/Cursiva)
# 3- Modificar menú (Introducir, Eliminar, Imprimir línea editada)
# Agregamos: crear nuevo doc, guardar doc, elimianr doc y abrir doc

# esto es para la parte de editoe de lineas
texto = []

# esto es para la parte de DOC
nombreFicheroCreado = []
nombreArchivo = []


# Utilizamos una función para imprimir el menú por pantalla y pedirle al usuario que introduzca una opción
def mostrar_menu():
    print("--------------------------------------------")
    print("|                  MENU                    |")
    print("--------------------------------------------")
    print("|    LINEA:                                |")
    print("|    1) Introducir nueva línea             |")# terminado
    print("|    2) Eliminar última línea introducida  |")# terminado
    print("|    3) Imprimir línea editada             |")# terminado
    print("|------------------------------------------|")
    print("|    DOC:                                  |")
    print("|    4) Crear nuevo doc                    |")# terminado
    print("|    5) Abrir el doc                       |")# terminado
    print("|    6) Modificar y Guardar doc            |")# terminado
    print("|    7) Eliminar doc                       |")# terminado
    print("|    0) Salir                              |")# terminado
    print("--------------------------------------------")
    return input("Introduzca su opción: ")


# Utilizamos un while para crear un bucle
while True:
    console = Console()
    #llamamos a la funcion de abrir el menu
    opcion = mostrar_menu()
    

    # ***************************************************************************************
    # PARTE DE LINEAS
    # ***************************************************************************************

    # ---------------------------- INTRODUCIR NUEVA LINEA ------------------------------
    # Introducir nueva linea
    if opcion.lower() == '1':
        # Solicita al usuario que añada un texto
        nuevoTexto = input("Texto a añadir: ")
        # Añade el texto a la linea
        texto.append(nuevoTexto)

    # ----------------------------------------------------------------------------------
    
    
    # ---------------------------- ELIMINAR ULTIMA LINEA -------------------------------
    # Eliminar ultima linea
    elif opcion.lower() == '2':
        if texto:  # Si hay texto en la lista
            # Elimina la última línea
            ultimaLinea = texto.pop()
            print(f'Se ha eliminado la ultima linea : "{ultimaLinea}")')
        else:
            print("No hay nada")
    # ----------------------------------------------------------------------------------
    
        
    # ----------------------- IMPRIMIR LINEAS --------------------------------------------
    # imprimir linea editada
    elif opcion == "3":
        if texto:
            print("El contenido del documento es:")
            for linea in texto:
                print(linea)
        else:
            print("No hay nada para ver")

    # ------------------------------------------------------------------------------------
    

    
    # ***************************************************************************************
    # PARTE DE ARCHIVOS
    # ***************************************************************************************

    # ----------------------- CREAR ARCHIVO ----------------------------------------------
    # crear archivo
    elif opcion == "4":
        nombreArchivo = input("Nombre que quieres en tu documento: ")
        with open(nombreArchivo, 'w') as archivo:
            nombreFicheroCreado.append(nombreArchivo)
            print("- Para negrita(**texto**))")
            print("- Para cursiva(*texto*)")
            print("- Para code(`texto`)")
            contenido_documento = input("Texto de tu documento: ")
            archivo.write(contenido_documento)
        print('Se ha creado guay :)')
    # ------------------------------------------------------------------------------------
    
    
    # ---------------------- ABRIR ARCHIVO -----------------------------------------------
    # abrir archivo
    elif opcion == "5":
        nombreArchivo = input("Nombre del archivo que queires abrir: ")
        if os.path.isfile(nombreArchivo): 
            with open(nombreArchivo, 'r') as contenido: 
                contenido_documento = contenido.read()
            console.print(Markdown(contenido_documento))
        else:
            print("No existe")
    # ------------------------------------------------------------------------------------
    
    
    # ------------------------------- MODIFICAR Y GUARDAR DOC ----------------------------------------
    # Modificar y guardar doc
    elif opcion == "6":
        nombreArchivoModificado = input("Pon el nombre del archivo que queires modificar: ")
        # si el fichero existe hace el if
        if os.path.exists(nombreArchivoModificado):
            # Solicitar al usuario que introduzca el contenido actualizado del documento
            print("- Para negrita(**texto**))")
            print("- Para cursiva(*texto*)")
            print("- Para code(`texto`)")
            contenidoActualizado = input("Pon el nuevo texto:\n")
            
            # Crear un archivo temporal para escribir el contenido actualizado
            nombreTemporal = nombreArchivoModificado + "_temp"
            with open(nombreTemporal, 'w') as archivoTemporal:
                archivoTemporal.write(contenidoActualizado)
            
            # Eliminar el archivo original
            os.remove(nombreArchivoModificado)
            
            # Renombrar el archivo temporal con el nombre del archivo original
            os.rename(nombreTemporal, nombreArchivoModificado)
            
            print(f"El documento '{nombreArchivoModificado}' lo has midificado y guardado bien gracias")
        else:
            print("Este archivo no existe, gracias")
    # ------------------------------------------------------------------------------------


    # ----------------------- MODIFICAR DOC ----------------------------------------------
    # Modificar doc
    #elif opcion == "7":
    #    print("no va")
    # ------------------------------------------------------------------------------------
    

    # ----------------------------- ELIMINAR DOC -----------------------------------------
    # Eliminar doc
    elif opcion == "7":
        nombreArchivo = input("¿Que archivo quieres eliminar de los guardados?: ")
        if os.remove(nombreArchivo):
            nombreFicheroCreado.remove(nombreArchivo)
            print("Se ha eliminado perfectamente")
        else:
            print("Este archivo no existe, gracias")
    # ------------------------------------------------------------------------------------
    

    # ----------------------- SALIR DEL PROGRAMA -----------------------------------------
    # salir
    elif opcion == "0":
        sys.exit()
    # ------------------------------------------------------------------------------------


    # ------------------ TRY CATCH ----------------------------------
    # esto pasa cuando no introduce algo de lo que toca
    else:
        print("Pon un numero que hay en el menu")
    # ---------------------------------------------------------------