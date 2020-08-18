import os
from Moduli import modulo_system
from Moduli import modulo_strings


def from_mac_to_ip(mac):
    """
    Trova l'indirizzo IP corrispondente ad un determinato indirizzo MAC.
    Il formato dell'indirizzo mac puo' essere sia col trattino che con i due punti.
    """

    mac = mac.lower()
    # costruisco il comando a seconda del sistema operativo
    if os.name == 'nt':
        mac = mac.replace(":", "-")
        cmd = 'arp -a | findstr "' + mac + '"'
    elif os.name == 'posix':
        mac = mac.replace("-", ":")
        cmd = 'arp | grep "' + mac + '"'
    else:
        return None
    # eseguo il comando
    output = modulo_system.system_call(cmd, True, False, False)
    if output == "":
        return None
    # ricavo l'ip
    riga = modulo_strings.normalizza_eol(output).split("\n")[0].strip()
    ip = riga.split(" ")[0]
    return ip
