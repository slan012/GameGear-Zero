import os

flag=True
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
os.system("/etc/init.d/S31emulationstation stopbattery")
while flag:
	flag = False
	for pid in pids:
		try:
			print pid
			commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
			if "emulationstation" in commandpath:
				flag = True
		except IOError:
			continue
os.system("shutdown -h now")