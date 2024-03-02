from cryptography.fernet import Fernet
import base64

# Mensaje original que quieres codificar y luego cifrar
mensaje_original = "mete aqui tu mensaje a codificar"

# Paso 1: Convertir el mensaje original a Base64
mensaje_base64 = base64.b64encode(mensaje_original.encode()).decode('utf-8')

# Paso 2: Generar una clave Fernet y crear una instancia de Fernet con esa clave
clave = Fernet.generate_key()
fernet = Fernet(clave)

# Paso 3: Cifrar el mensaje codificado en Base64 con Fernet
mensaje_cifrado = fernet.encrypt(mensaje_base64.encode()).decode('utf-8')

# Mostrar los resultados
print("Clave Fernet:", clave.decode())
print("Mensaje en Base64:", mensaje_base64)
print("Mensaje cifrado con Fernet:", mensaje_cifrado)
