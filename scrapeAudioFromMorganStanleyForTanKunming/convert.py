
from pydub import AudioSegment

output_mp3 = "download.mp3"
audio = AudioSegment.from_file(output_file, format='ts')
audio.export(output_mp3, format='mp3')

