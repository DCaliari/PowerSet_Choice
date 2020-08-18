def normalizza_eol(cont):
    cont = cont.replace("\r\n", "\n")
    cont = cont.replace("\r", "\n")
    return cont
