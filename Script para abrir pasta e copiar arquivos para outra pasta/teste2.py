
import shutil
from os import listdir
from os.path import isfile, join, basename



pathOrigem = "/Users/italo/OneDrive/Área de Trabalho/auxiliar"
pathDestino = "/Users/italo/OneDrive/Área de Trabalho/Fotos"



def move(path_origem, path_destino):
    for item in [join(path_origem, f) for f in listdir(path_origem) if isfile(join(path_origem, f)) ]:
        shutil.move(item, join(path_destino, basename(item)))
        print('moved "{}" -> "{}"'.format(item, join(path_destino, basename(item))))


if __name__ == '__main__':
	dirs = listdir( pathOrigem )
	for pasta in dirs:
		pathPasta = pathOrigem + "/" + pasta
		move(pathPasta,pathDestino)
