from pathlib import Path as P

# Absolute path
# /usr/local/bin
# Relative path

path = P()
print(path.exists())
# path.mkdir() - makes new directory using path object
# path.rmdir() - remove directory
for file in path.glob('*'):
    print(file)





