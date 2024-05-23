import json

Suma = 0
ucs = 0

with open("Cedula-Codigo-Nota-Periodo.json", "r") as Cedula:
    data_cedula = json.load(Cedula)

with open("Cedula-Nombre-Apellido.json", "r") as Nombre:
    data_nombre = json.load(Nombre)

with open("Codigo-UC.json", "r") as Codigo:
    data_codigo = json.load(Codigo)


def nombre_del_alumno(Valor):
    for item in data_nombre:
        if item["dni"] == Valor:
            print(f"Encontrado: {Valor}")
            return item["nombre"] + " " + item["apellido"]


def calculo(item):
    for row in data_codigo:
        global Suma
        global ucs
        if row["Codigo"] == item["Codigo"]:
            Suma += item["nota"] * row["UC"]
            ucs += row["UC"]


def mostrar_menu():
    print("1. Nombre del alumno")
    print("2. Promedio ponderado")
    print("3. Agregar nota")
    print("4. Borrar nota")
    print("5. Salir")


def menu_opcion(opcion):
    if opcion == '1':
        buscar = input("Ingrese la cedula para buscar: ")
        vnombre = nombre_del_alumno(buscar)
        print(f"El nombre del alumno es: {vnombre}")

    elif opcion == '2':
        buscar = input("Ingrese cedula: ")
        for item in data_cedula:
            if item["dni"] == buscar:
                calculo(item)
                prom = Suma / ucs
                vnombre = nombre_del_alumno(buscar)
                print(f"El promedio ponderado de {vnombre} es: {prom:.2f}")
                
    elif opcion == '3':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia: ")
        nota = float(input("Ingrese la nota: "))
        periodo = input("Ingrese el periodo: ")
        
        nueva_nota = {
            "dni": cedula,
            "Codigo": codigo,
            "nota": nota,
            "Periodo": periodo
        }
        
        data_cedula.append(nueva_nota)
        
        with open("Cedula-Codigo-Nota-Periodo.json", "w") as file:
            json.dump(data_cedula, file, indent=4)
            
        print("Nota agregada exitosamente.")

    elif opcion == '4':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia a borrar: ")
        
        notas_borrar = []
        
        for i, item in enumerate(data_cedula):
            if item["dni"] == cedula and item["Codigo"] == codigo:
                notas_borrar.append(i)
        
        if len(notas_borrar) > 0:
            print(f"Se encontraron {len(notas_borrar)} notas con el mismo código.")
            for j, nota_idx in enumerate(notas_borrar):
                print(f"{j+1}. Nota {nota_idx+1}")
            
            nota_borrar = int(input("Seleccione el número de la nota que desea borrar: ")) - 1
            
            if 0 <= nota_borrar < len(notas_borrar):
                del data_cedula[notas_borrar[nota_borrar]]
                
                with open("Cedula-Codigo-Nota-Periodo.json", "w") as file:
                    json.dump(data_cedula, file, indent=4)
                    
                print("Nota borrada exitosamente.")
            else:
                print("Número de nota inválido.")
        else:
            print("No se encontraron notas con el mismo código.")

    elif opcion == '5':
        print("Cerrando Programa...")

    else:
        print("Error de Opcion. Por favor, elija una opción válida.")


mostrar_menu()
opcion = input("Ingrese la opcion que desea utilizar: ")
menu_opcion(opcion)

