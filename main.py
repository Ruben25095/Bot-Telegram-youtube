from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from login import *
from pytube import YouTube
import os

async def Descargar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensaje recibido del    usuario
    
    print(update.message.text)
    
    # Instancia de YouTube para el video deseado
    yt = YouTube(update.message.text)
   
    nombre = yt.title
    #Formateo de Texto
    nombre = "".join([c for c in nombre if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    print(nombre)
    #descarga = yt.streams.get_highest_resolution()
    
    descarga = yt.streams.get_audio_only("mp4")
    size= descarga.filesize
    size_mb = size / (1024 * 1024)
    print(size_mb)
    # Se especifica el nombre del archivo para la descarga
    descarga.download(output_path=patch_Descargas, filename=f"{nombre}.mp4")
    video_path = os.path.join(patch_Descargas, f"{nombre}.mp4")
    print(video_path)
    #await update.message.reply_video(video_path)
    await update.message.reply_audio(video_path)

    # Subir el video a Telegram
    #await context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_path, 'rb'))
    # Opcional: eliminar el archivo después de subirlo si no se necesita
    #  mantener
    os.remove(video_path)

# Configuración del bot
app = ApplicationBuilder().token(Telegram_Token).read_timeout(60) .write_timeout(60).build()
app.add_handler(CommandHandler("descargar", Descargar))

app.run_polling(allowed_updates=Update.ALL_TYPES)







