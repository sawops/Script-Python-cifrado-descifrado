from cryptography.fernet import Fernet
import base64

# La clave Fernet que usaste para cifrar el mensaje
clave = b"Clave que usaste para cifrar en el anterior script"

# El mensaje cifrado que quieres descifrar
mensaje_cifrado = b"aqui el mensaje cifrado"

# Crear una instancia de Fernet con la clave
fernet = Fernet(clave)

# Descifrar el mensaje
mensaje_descifrado_base64 = fernet.decrypt(mensaje_cifrado)

# Decodificar el mensaje de Base64 a su forma original
mensaje_descifrado = base64.b64decode(mensaje_descifrado_base64).decode('utf-8')

print("Mensaje descifrado:", mensaje_descifrado)
