import subprocess, time

while True:
    try:
        subprocess.call(["python","edge/app.py"])
    except Exception as e:
        print("Edge crashed:", e)
    time.sleep(2)
