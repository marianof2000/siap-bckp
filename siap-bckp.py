# Backup y direccionamiento de S.I.Ap.
from datetime import datetime
import os
import zipfile

fecha = str(datetime.now())[:10]
destino = "e:\\SIAp\\"
destino="/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/"
bloqueo = "AFIP.ldb"
opciones = ["A","B","C","D","E","S","Z"]

# rutas a los distintos SIAp # siapBackup(imppro, destino, "C:\\Carpetas compartidas\\Intercambio\\S.I.Ap\\AFIP\\")
siaps={}
siaps[opciones[0]]=["imppro","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[opciones[1]]=["impanu","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files2/"]
siaps[opciones[2]]=["impmen","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[opciones[3]]=["emerg1","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[opciones[4]]=["emerg2","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]

def siapBackup(archivo, ruta, origen):
	nombre = 'SIAp-'+archivo + '-'+fecha + '.zip' 
	if os.path.isfile(origen+bloqueo):
		print('SIAp '+archivo+' abierto en un terminal.\nCierre la sesión y ejecute otra vez la copia.')
	elif os.path.isfile(nombre):
		print('Ya existe un backup con esa fecha, borre primero el archivo\ny luego ejecute otra vez el Backup\n')
	else:
		try:
			comprimido = zipfile.ZipFile(ruta + nombre, mode='w', compression = zipfile.ZIP_LZMA)
			for folder, subfolders, files in os.walk(origen):
				for file in files:
					comprimido.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), destino))
			comprimido.close()
		except:
			print("Hubo un error al generar la copia.")
		else:
			print("Copia terminada!\nSe generó " + nombre + "\n")

def borrar():
	if os.path.isfile("c:\\windows\\afipPath.sys"):
		try:
			os.remove("c:\\windows\\afipPath.sys")
		except:
			print("El archivo afipPath.sys está en uso\n")
		else:
			print("Se eliminó el archivo afipPath.sys\n")
	else:
		print("No existe la ruta en el sistema.\n")

while True:
	while True:
		print("Impuestos provinciales - A\nImpuestos anuales c:\\intercambio\\DGI - B\nImpuestos mensuales c:\\SIAp- C")
		print("SIAp de emergencia 1 c:\\intercambio\\DGI2 - D\nSIAp de emergencia 2 c:\\intercambio\\DGI3 - E\nSalir del programa - S")
		print("Borrar la ruta - Z")
		letra=input("Ingrese la opción: (A/B/C/D/E/S/Z): ")
		if letra.upper() in opciones:
			break
		print("No ingresó una opción correta. Pruebe otra vez.\n")

	if letra.upper() == "S":
		print("Sale del programa.\n")
		break
	elif letra.upper() == "Z":
		borrar()
	else: #implementar el case
		try:
			siapBackup(siaps[letra.upper()][0],destino,siaps[letra.upper()][1])
		except:
			print("Opción no implementada.\n")
