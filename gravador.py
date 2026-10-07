import subprocess
import time
import os

if not os.path.exists("buffer"):
    os.makedirs("buffer")

comando_ffmpeg = [
    "ffmpeg",
    "-f", "dshow",
    "-i", "video=Integrated Camera",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-pix_fmt", "yuv420p",
    "-g", "30",
    "-force_key_frames", "expr:gte(t,n_forced*2)",
    "-f", "segment",
    "-segment_time", "2",
    "-reset_timestamps", "1",
    "-strftime", "1",
    "buffer/%Y%m%d_%H%M%S.mp4",
]

print("Iniciando gravação em segundo plano...")
processo = subprocess.Popen(comando_ffmpeg, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Gravando por 15 segundos de teste...")
time.sleep(60)

print("Encerrando a gravação...")
processo.terminate()
processo.wait()

print("Gravação finalizada. Confira a pasta buffer/.")