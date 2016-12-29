import mp3play
import time

filename = r'C:\Documents and Settings\Michael\Desktop\music.mp3'
mp3 = mp3play.load(filename)

mp3.play()

# Let it play for up to 30 seconds, then stop it.
import time

time.sleep(min(30, mp3.seconds()))
mp3.stop()
