import os
import subprocess


def dimensione_file(nomefile):
    try:
        statinfo = os.stat(nomefile)
        return statinfo.st_size
    except:
        return -1


# stdout		se mostrare o meno l'output a schermo
def system_call(cmd, stdout, return_pipe, real_time_output):
    if (stdout):
        std_out = subprocess.PIPE
    else:
        std_out = subprocess.DEVNULL
    # creo l'oggetto
    process = subprocess.Popen(cmd, shell=True,
                               stdin=subprocess.DEVNULL,
                               stdout=std_out,
                               stderr=subprocess.STDOUT,
                               cwd=os.getcwd(), env=os.environ)
    if return_pipe is True:
        return process
    if real_time_output is False:
        output = process.communicate()[0]
        if output is not None:
            output = output.decode('utf8', 'replace')
        return output
    else:
        for line in iter(process.stdout.readline, b''):
            print(">>> " + line.decode('utf8', 'replace').rstrip())
        return None
    return None
