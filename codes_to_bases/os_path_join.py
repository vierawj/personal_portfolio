import os

this_root = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.dirname(this_root)


#Passo caminho todo que ele tem que percorrer até o arquivo
config = {
    "path": "bases|folder_1|sub_folder_1|sub_sub_folder_1|file.txt"
}

# Abre o arquivo, seguindo todo diretorio, lê , volta marcador ao zero e escreve em cima.
with open(os.path.join(project_root, *config['path'].split('|')), 'r+') as file:
    content = file.read()
    file.truncate(0)
    file.seek(0)
    
    print(str(content))
    
    file.write('ACHEI e ALTEREI!')