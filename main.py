import json

estudiantes = []

def registrar_estudiante():
    nombre = input("Nombre: ")
    id_est = input("ID: ")
    
    estudiante = {
        "nombre": nombre,
        "id": id_est,
        "notas": []
    }
    
    estudiantes.append(estudiante)
    print("✅ Estudiante registrado")


def agregar_notas():
    id_buscar = input("ID del estudiante: ")
    
    for est in estudiantes:
        if est["id"] == id_buscar:
            nota = float(input("Nota (0-5): "))
            est["notas"].append(nota)
            print("✅ Nota agregada")
            return
    
    print("❌ Estudiante no encontrado")


def calcular_promedio():
    id_buscar = input("ID del estudiante: ")

    for est in estudiantes:
        if est["id"] == id_buscar:
            if len(est["notas"]) == 0:
                print("No tiene notas")
                return
            
            promedio = sum(est["notas"]) / len(est["notas"])
            estado = "Aprobado" if promedio >= 3 else "Reprobado"
            
            print(f"Promedio: {promedio:.2f} - {estado}")
            return
    
    print("Estudiante no encontrado")


def reporte():
    print("\n--- REPORTE ---")
    for est in estudiantes:
        if len(est["notas"]) > 0:
            promedio = sum(est["notas"]) / len(est["notas"])
        else:
            promedio = 0
        
        print(f"{est['nombre']} | ID: {est['id']} | Prom: {promedio:.2f}")


def guardar():
    with open("datos.json", "w") as archivo:
        json.dump(estudiantes, archivo)
    print("💾 Datos guardados")


def cargar():
    global estudiantes
    try:
        with open("datos.json", "r") as archivo:
            estudiantes = json.load(archivo)
        print("📂 Datos cargados")
    except:
        print("No hay datos guardados")


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Registrar estudiante")
    print("2. Agregar nota")
    print("3. Calcular promedio")
    print("4. Ver reporte")
    print("5. Guardar")
    print("6. Cargar")
    print("7. Salir")


while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        agregar_notas()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        reporte()
    elif opcion == "5":
        guardar()
    elif opcion == "6":
        cargar()
    elif opcion == "7":
        break
    else:
        print("Opción inválida")