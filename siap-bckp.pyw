# Backup y direccionamiento de S.I.Ap.
from datetime import datetime
import os
import zipfile
from tkinter import *

raiz = Tk()
raiz.title("Backup y direccionamiento de SIAps")
raiz.resizable(0,0)
raiz.geometry("420x250")
eleccion = IntVar()
eleccion.set(1) 

fecha = str(datetime.now())[:10]
destino = "e:\\SIAp\\"
destino="/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/"
bloqueo = "AFIP.ldb"
# rutas a los distintos SIAp # siapBackup(imppro, destino, "C:\\Carpetas compartidas\\Intercambio\\S.I.Ap\\AFIP\\")
siaps={}
siaps[1]=["imppro","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[2]=["impanu","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files2/"]
siaps[3]=["impmen","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[4]=["emerg1","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
siaps[5]=["emerg2","/home/ciie-tordillo/Escritorio/borrar/python/Siap-bckp/files/"]
opciones1 = [("Impuestos provinciales",1), ("Impuestos anuales c:\\intercambio\\DGI",2),
			("Impuestos mensuales c:\\SIAp",3), ("SIAp de emergencia 1 c:\\intercambio\\DGI2",4),
			("SIAp de emergencia 2 c:\\intercambio\\DGI3",5), ("Salir del programa",6),
			("Borrar la ruta",7)]

def siapBackup(archivo, ruta, origen):
	nombre = 'SIAp-'+archivo + '-'+fecha + '.zip' 
	if os.path.isfile(origen+bloqueo):
		mensaje.config(text='SIAp '+archivo+' abierto en una terminal\nCierre la sesión y ejecute otra vez la copia')
	elif os.path.isfile(nombre):
		mensaje.config(text='Ya existe un backup con esa fecha\nBorre primero el archivo y luego\nejecute otra vez el Backup')
	else:
		try:
			mensaje.config(text="Ejecutando ...")
			comprimido = zipfile.ZipFile(ruta + nombre, mode='w', compression = zipfile.ZIP_LZMA)
			for folder, subfolders, files in os.walk(origen):
				for file in files:
					comprimido.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), destino))
			comprimido.close()
		except:
			mensaje.config(text="Hubo un error al generar la copia")
		else:
			mensaje.config(text="Copia terminada\nSe generó " + nombre)

def borrar():
	if os.path.isfile("c:\\windows\\afipPath.sys"):
		try:
			os.remove("c:\\windows\\afipPath.sys")
		except:
			mensaje.config(text="El archivo afipPath.sys está en uso")
		else:
			mensaje.config(text="Se eliminó el archivo afipPath.sys")
	else:
		mensaje.config(text="No existe la ruta en el sistema")

def comandos():
	boton1.config(text="Ejecutando ...")
	boton1.config(state='disabled')
	entrada = eleccion.get()
	if entrada == 6:
		mensaje.config(text="Sale del programa")
		raiz.quit()
	elif entrada == 7:
		borrar()
	else: #implementar el case
		try:
			mensaje.config(text="Ejecutando ...")
			siapBackup(siaps[entrada][0],destino,siaps[entrada][1])
		except:
			mensaje.config(text="Opción no implementada")
	boton1.config(state='normal')
	boton1.config(text="Ejecutar")

Label(raiz, text="Elija la acción", justify = LEFT, padx = 20, font=("Arial",14)).pack()

Radiobutton(raiz, height=7).place(anchor=W)
for opcion, elec in opciones1:
    Radiobutton(raiz, text=opcion, padx = 20, variable=eleccion, value=elec).pack(anchor=W)

mensaje=Label(raiz, text="Ejecute una opción...", font=("Arial",10), padx=20, justify = LEFT)
mensaje.pack(side=LEFT)

boton1=Button(raiz, text="Ejecutar", font=("Arial",12), command=comandos)
boton1.place(x=300,y=200)

raiz.mainloop()
