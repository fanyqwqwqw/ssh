from flask import Flask
import paramiko
import os

app = Flask(__name__)

# Configuración del servidor SSH
hostname = 'ssh-natureza.alwaysdata.net'
port = 22
username = 'natureza_anon'
password = '(123456)'
remote_file_path = 'chavez_marin.xlsx'  # Ruta remota del archivo
local_file_path = os.path.join(os.getcwd(), remote_file_path)  # Ruta local donde se guardará

def download_file_via_ssh():
    try:
        # Crear una instancia del cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Conectarse al servidor
        print(f"Conectando a {hostname}...")
        ssh.connect(hostname, port, username, password)
        print("Conexión establecida.")
        
        # Crear una sesión SFTP
        sftp = ssh.open_sftp()
        print(f"Descargando el archivo {remote_file_path}...")
        
        # Descargar el archivo
        sftp.get(remote_file_path, local_file_path)
        print(f"Archivo descargado exitosamente en: {local_file_path}")
        
        # Cerrar la conexión SFTP y SSH
        sftp.close()
        ssh.close()
        
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
        return str(e)

@app.route('/download', methods=['GET'])
def download():
    download_file_via_ssh()
    return "Archivo descargado correctamente."

if __name__ == '__main__':
    app.run(debug=True)
