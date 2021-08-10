import subprocess

def execute(cmd,inp=None):
    cmd = cmd.split()
    out = subprocess.run(cmd, capture_output=True, text=True, input = inp)
    if "fio" in cmd:
        return out.returncode
    else:
        return out.stdout

def fio(cmd):
    
    out = subprocess.check_output(cmd,shell = True, text = True)
    return out
