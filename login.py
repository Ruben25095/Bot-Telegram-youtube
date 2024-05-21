from os import mkdir
from os import path



Telegram_Token="6943437955:AAFh7T9-iCH1ZNNCvHATdhv47IUzcFayGd0";

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

