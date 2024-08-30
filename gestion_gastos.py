import csv
import os

FILE_NAME = "finanzas.csv"

def initialize_file():
    # Si el archivo no existe, crea el archivo CSV con el encabezado adecuado
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tipo", "Monto", "Descripción"])

def add_transaction(tipo, monto, descripcion):
    # Añade una nueva transacción (ingreso o gasto) al archivo CSV
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tipo, monto, descripcion])
    print(f"{tipo.capitalize()} de {monto} añadido: {descripcion}")

def show_balance():
    ingresos = 0
    gastos = 0
    # Lee el archivo CSV para calcular el balance
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Tipo"] == "ingreso":
                ingresos += float(row["Monto"])
            elif row["Tipo"] == "gasto":
                gastos += float(row["Monto"])
    balance = ingresos - gastos
    print(f"Ingresos totales: {ingresos}")
    print(f"Gastos totales: {gastos}")
    print(f"Balance actual: {balance}")

def main():
    initialize_file()
    while True:
        print("\n1. Añadir ingreso")
        print("2. Añadir gasto")
        print("3. Mostrar balance")
        print("4. Salir")
        choice = input("Selecciona una opción: ")
        if choice == '1':
            monto = input("Monto del ingreso: ")
            descripcion = input("Descripción: ")
            add_transaction("ingreso", monto, descripcion)
        elif choice == '2':
            monto = input("Monto del gasto: ")
            descripcion = input("Descripción: ")
            add_transaction("gasto", monto, descripcion)
        elif choice == '3':
            show_balance()
        elif choice == '4':
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
