import requests

BASE_URL = 'http://127.0.0.1:8000/api/numeros/'

def listar_numeros():
    """Listar todos los números en la base de datos."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Números registrados:")
        for numero in response.json():
            print(f"- {numero['numero']} (Spam: {numero['es_spam']}, Reportes: {numero['reportes']})")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def crear_numero():
    """Crear un nuevo número en la base de datos."""
    numero = input("Ingresa el número: ")
    es_spam = input("¿Es spam? (true/false): ").lower() == 'true'
    data = {'numero': numero, 'es_spam': es_spam}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Número creado exitosamente.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def actualizar_numero():
    """Actualizar un número existente."""
    numero_id = input("Ingresa el ID del número a actualizar: ")
    numero = input("Ingresa el nuevo número: ")
    es_spam = input("¿Es spam? (true/false): ").lower() == 'true'
    data = {'numero': numero, 'es_spam': es_spam}
    response = requests.put(f"{BASE_URL}{numero_id}/", json=data)
    if response.status_code == 200:
        print("Número actualizado exitosamente.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def eliminar_numero():
    """Eliminar un número de la base de datos."""
    numero_id = input("Ingresa el ID del número a eliminar: ")
    response = requests.delete(f"{BASE_URL}{numero_id}/")
    if response.status_code == 204:
        print("Número eliminado exitosamente.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def menu():
    """Menú principal del CRUD en terminal."""
    while True:
        print("\n=== Menú CRUD ===")
        print("1. Listar Números")
        print("2. Crear Número")
        print("3. Actualizar Número")
        print("4. Eliminar Número")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            listar_numeros()
        elif opcion == '2':
            crear_numero()
        elif opcion == '3':
            actualizar_numero()
        elif opcion == '4':
            eliminar_numero()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
