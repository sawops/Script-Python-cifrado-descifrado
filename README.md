# Script-Python
1. cifrarFernet.py:
  Importación de Librerías: Importamos las librerías necesarias, Fernet de cryptography y base64 para manejar la codificación Base64.
  Definición del Mensaje Original: Definimos el mensaje original que queremos codificar y luego cifrar.
  Codificación en Base64 del Mensaje Original: Convertimos el mensaje original a su representación en Base64. Esto es necesario porque        Fernet espera bytes como entrada.
  Generación de Clave Fernet: Generamos una clave aleatoria para ser utilizada por el algoritmo de Fernet.
  Creación de una Instancia de Fernet: Creamos una instancia de Fernet utilizando la clave generada.
  Cifrado del Mensaje en Base64 con Fernet: Ciframos el mensaje codificado en Base64 utilizando la instancia de Fernet.
  Mostrar los Resultados: Imprimimos la clave generada, el mensaje en Base64 y el mensaje cifrado con Fernet.

