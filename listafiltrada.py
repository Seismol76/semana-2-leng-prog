from hashlib import sha1

# Listas de nombres y números
names = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Federico"]
numbers = [3, 7, 2, 8, 5, 1]

# Función para aplicar el hash SHA-1
def apply_hash(name, number):
    string = f"{name}{number}"
    return sha1(string.encode()).hexdigest()

# Filtrar, procesar y aplicar hash usando list comprehension
result = [(name, number**2, apply_hash(name, number**2))
          for name, number in zip(names, numbers)
          if len(name) > 5]

# Imprimir el resultado
for name, squared_number, hash_value in result:
    print(f"Name: {name}, Squared number: {squared_number}, Hash: {hash_value}")