import sys
import subprocess

def run(serial_number, cmds):
    cmd = ['adb', '-s', serial_number] + cmds.split(" ")
    ret = subprocess.call(' '.join(cmd), shell=True)
    if ret != 0:
        print_err("adb command failed to run: %s!" % " ".join(cmd))
        sys.exit(1)

