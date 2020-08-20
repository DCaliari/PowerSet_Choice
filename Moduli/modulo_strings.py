# uniformare caratteri per andare a capo Linux, Windows, Mac

def normalizza_eol(cont):
    cont = cont.replace("\r\n", "\n")
    cont = cont.replace("\r", "\n")
    return cont


def is_empty(valore):
    if valore is None:
        return True
    valore = str(valore)
    return valore == ''
