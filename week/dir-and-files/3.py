import os
path = r"\Users\Админ\Documents\kbtu\pp2_2024\week\dir-and-files"

if os.access(path, os.F_OK):
    print("File name:", os.path.basename(path))
    print("Diretory:", os.path.dirname(path))