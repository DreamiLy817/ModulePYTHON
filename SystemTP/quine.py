import random, subprocess
import os

dir_name = '/root/script/quineDossier/'
#list = os.listdir(dir_name) # dir is your directory path
#number_files = len(list)

def get_size():
	# On initialise la variable total à 0
	total = 0
	for dirpath, dirnames, filenames in os.walk(dir_name):
		for file in filenames:
			path = os.path.join(dirpath, file)
			total += os.path.getsize(path)
	return total

sizeFolder = get_size()

if sizeFolder < 5000: 
	content = open(__file__).read()
	new_file = f"{str(random.randint(1,10000))}.py"
	with open( new_file,'w') as f:
	     f.write(content)
	process = subprocess .Popen(["python3", new_file], shell=False)