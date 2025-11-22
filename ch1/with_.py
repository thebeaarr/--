with open("README.md" , "r") as fichier:
	line = fichier.readline()
	print(line)
	raise exception("oups")

