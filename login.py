from os import mkdir
from os import path



Telegram_Token="Tu Token";

#patch_Descargas="c:/Users/ruben/OneDrive/Escritorio/Entorno/venv/bot/Descargas/";

ruta = './Archivos'
def patch_ruta():
# verificamos si el directorio ya existe
    if not path.exists(ruta):
       mkdir(ruta)
       print("Directorio %s creado!" % ruta)
       return ruta;
    else:
       print("Directorio %s ya existe" % ruta)
       return ruta

