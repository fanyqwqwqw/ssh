import paramiko
import pandas as pd
from io import BytesIO

# Datos de conexión SSH
hostname = 'ssh-natureza.alwaysdata.net'
username = 'natureza_anon'
password = '(123456)'

# Ruta del archivo Excel en el servidor remoto
remote_path = '/path/to/datos_estadisticos.xlsx'

# Establecer la conexión SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

# Usamos SFTP para descargar el archivo Excel
sftp = client.open_sftp()
local_path = 'datos_estadisticos_descargados.xlsx'
sftp.get(remote_path, local_path)
sftp.close()

# Cargar el archivo Excel descargado
df = pd.read_excel(local_path)

# Mostrar estadísticas simples sobre los datos
print("Datos cargados desde el archivo Excel:")
print(df.head())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Cerrar la conexión SSH
client.close()
