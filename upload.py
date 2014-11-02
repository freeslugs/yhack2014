import opencv
import models
import subprocess

def upload(name, filename, interval):
	activate_venv = ". /home/lekez2005/Desktop/yhack/yhack2014/venv/bin/activate;"

	#command = "'import opencv;opencv.create_movie('"+name +"', '" +filename+"', "+str(interval)+")'"
	subprocess.Popen(['/home/lekez2005/Desktop/yhack/yhack2014/venv/bin/python', 'opencv.py', name,
					 filename, str(interval)])

