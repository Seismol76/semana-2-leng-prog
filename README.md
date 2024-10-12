# William de los Santos 2021 1368
## Ejercicios semana 2 Leng Prog

### Ejer 1
Conversión de Temperaturas y Hashing
import  hashlib

  

	def  convert_temperature(value, scale):

	# Validate the scale

	if  scale  not  in ['C', 'F']:

	raise  ValueError("The scale must be 'C' or 'F'")

	# Perform the conversion

	if  scale == 'C':

	converted_temperature = (value * 9/5) + 32

	new_scale = 'F'

	else:

	converted_temperature = (value - 32) * 5/9

	new_scale = 'C'

	# Round to 2 decimal places

	converted_temperature = round(converted_temperature, 2)

	# Convert to string and generate hash

	temp_str = f"{converted_temperature:.2f}"

	hash_object = hashlib.sha256(temp_str.encode())

	hash_hex = hash_object.hexdigest()

	return  converted_temperature, new_scale, hash_hex

	  

	# Function to get user input

	def  get_user_input():

	while  True:

	try:

	value = float(input("Enter the temperature to convert: "))

	scale = input("Enter the scale (C or F): ").upper()

	if  scale  not  in ['C', 'F']:

	raise  ValueError("The scale must be 'C' or 'F'")

	return  value, scale

	except  ValueError  as  e:

	print(f"Error: {e}. Please try again.")

	  

	# Example usage

	try:

	value, scale = get_user_input()

	temp, new_scale, hash_value = convert_temperature(value, scale)

	print(f"{value}°{scale} is equal to {temp}°{new_scale}")

	print(f"SHA-256 Hash: {hash_value}")

	except  ValueError  as  e:

	print(f"Error: {e}")

### Ejer 2 
Filtrar y Procesar Datos con List Comprehensions

	from  hashlib  import  sha1

	  

	# Listas de nombres y números

	names = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Federico"]

	numbers = [3, 7, 2, 8, 5, 1]

	  

	# Función para aplicar el hash SHA-1

	def  apply_hash(name, number):

	string = f"{name}{number}"

	return  sha1(string.encode()).hexdigest()

	  

	# Filtrar, procesar y aplicar hash usando list comprehension

	result = [(name, number**2, apply_hash(name, number**2))

	for  name, number  in  zip(names, numbers)

	if  len(name) > 5]

	  

	# Imprimir el resultado

	for  name, squared_number, hash_value  in  result:

	print(f"Name: {name}, Squared number: {squared_number}, Hash: {hash_value}")

### Ejer 3
Validación de Contraseñas con Manejo de Errores y Hashing

	from  hashlib  import  md5

	import  re

	  

	class  PasswordError(Exception):

	"""Custom exception for password validation errors."""

	pass

	  

	def  validate_password(password):

	"""

	Validates the password and returns its MD5 hash if valid.

	Raises PasswordError if the password is invalid.

	"""

	# chequear longitud

	if  len(password) < 8:

	raise  PasswordError("Password must be at least 8 characters long.")

	# chequear si tiene mayus

	if  not  re.search(r'[A-Z]', password):

	raise  PasswordError("Password must include at least one uppercase letter.")

	# chequear si tiene minus

	if  not  re.search(r'[a-z]', password):

	raise  PasswordError("Password must include at least one lowercase letter.")

	# chequear si tiene numeros

	if  not  re.search(r'\d', password):

	raise  PasswordError("Password must include at least one number.")

	# si cumple con todo, genera y devuelve un MD5 hash

	return  md5(password.encode()).hexdigest()

	  
	  
	  

	try:

	result = validate_password("MyPassword1")

	print(f"Password is valid. Hash: {result}")

	except  PasswordError  as  e:

	print(f"Password is invalid: {str(e)}")
