import os

print(os.getcwd())

import os
import shutil

def mover_archivos(origen, destino):
    try:
        # Verificar si el directorio de destino existe, sino lo crea
        if not os.path.exists(destino):
            os.makedirs(destino)
        # Recorrer los archivos en el directorio origen
        for archivo in os.listdir(origen):
            if archivo.endswith('.docx'):
                ruta_origen = os.path.join(origen, archivo)
                ruta_destino = os.path.join(destino, archivo)
                # Mover el archivo
                shutil.move(ruta_origen, ruta_destino)
                print(f'Movido: {archivo}')
    except Exception as e:
        print(f'Error: {e}')

# Directorio origen y destino (simulando el remoto)
origen = '/Users/tsmg2/OneDrive/Desktop/IACC'
destino = '/Users/tsmg2/OneDrive/Desktop/IACC/Documentos'
mover_archivos(origen, destino)
