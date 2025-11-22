fichier  = open("README.md", "r")

line  = fichier.readline()

print(line)


fichier.close()

#If an error happens before close()
#fichier = open("README.md", "r")
#line = fichier.readline()

# imagine an error happens here (crash, exception)
#x = 10 / 0

#fichier.close()   # <-- this will NEVER run
# Now the file is never closed.

# That can cause:

# File descriptor leaks

# Hitting OS “too many open files” limit

# Problems accessing the file later

# Memory / resource leaks in long-running programs

# This is the same type of problem as forgetting free() in C.
