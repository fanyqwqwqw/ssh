import paramiko

# Configuración de la conexión SSH
hostname = 'ssh-natureza.alwaysdata.net'
port = 22
username = 'natureza_anon'
password = '(123456)'  # Asegúrate de no usar contraseñas en texto plano en producción

# Ruta remota donde está almacenado el archivo
ruta_remota = 'chavez_marin.xlsx'  # Ruta del archivo en el servidor
ruta_local = 'chavez_marin_descargado.xlsx'  # Ruta local donde se guardará el archivo

# Crear una instancia SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Aceptar claves desconocidas automáticamente

try:
    # Conectarse al servidor
    ssh.connect(hostname, port=port, username=username, password=password)
    print("Conexión exitosa")

    # Usar SFTP para descargar el archivo
    sftp = ssh.open_sftp()

    # Descargar el archivo
    sftp.get(ruta_remota, ruta_local)  # Descargar el archivo desde el servidor remoto a la máquina local
    sftp.close()

    print(f'Archivo descargado con éxito y guardado como {ruta_local}')
except Exception as e:
    print(f"Error durante la transferencia: {e}")
finally:
    ssh.close()
