import subprocess
import time

for i in range(10000):
	if i % 100 == 0:
		time.sleep(0.2)
	subprocess.call(["/home/leviathan6/leviathan6", str(i).zfill(4)])
