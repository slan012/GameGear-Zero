**************************************************************
************   INSTALLATION DES FICHIERS *********************
**************************************************************

IMPORTANT => Avant de copier/coller les différents fichiers : 

ouvrir un terminal puis:  

mount -o remount , rw /
mount -o remount, rw /boot

A placer dans /etc/init.d/ :

	- S31emulationstation # rajout de l'option stopbattery : permet de fermer ES avec message spécifique en cas de batterie faible avant un safeshutdown
	- S32batteryled # déclenche batteryled.py au démarrage
	- S32battery-monitoring # déclenche battery-monitoring.py au démarrage
	- S98exit-emu-1b # rajout de l'option qui permet d'éteindre le système (safeshutdown) en maintenant les boutons START + BOUTON_1 + BOUTON_BAS de la GameGear
	- S99backlight-control # déclenche backlight-control.py au démarrage
	- S99retroarchmenu # déclenche retroarchmenu.py au démarrage

A placer dans /recalbox/scripts/ :

	- backlight-control.py # modifie le rétroéclairage de l'écran MPI3508 avec la molette d'origine de la GameGear (utilise un ads1015 pour la conversion ADC)
	- batteryled.py # déclenche le clignottement de la LED "power" quand la tension batterie devient trop faible (par default = 3.29V)
	- battery-monitoring.py # surveille la tension batterie toute les 10 secondes et déclenche un safeshutdown si tension batterie < 3.20V
	- retroarchmenu.py # permet de quitter retroarch avec 1 bouton (START) et de déclencher un safeshutdown avec START + BOUT1 + BAS
	- rpi-exit-emu-1b.py # idem S98exit-emu-1b

A placer dans /boot/ :

	- cmdline.txt # Activation I2C
	- config # Activation I2C

A placer dans /etc/ :

	-  modules.conf # Activation I2C

A placer dans /recalbox/share/system/:

	- recalbox.conf # Activation et remapping des GPIO, configuration de l'affichage.

