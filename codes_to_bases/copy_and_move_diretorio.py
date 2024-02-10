import os
import shutil 

current = os.path.dirname(os.path.realpath(__file__)) # Identificar path atual
project_root = os.path.dirname(current) # Voltar uma pasta  

def copy_project(root_src_dir:str, root_dst_dir:str):
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                shutil.copy2(src_file, dst_file)

#Copiar o modelo
copy_project(
    os.path.join(project_root, 'bases',),
    os.path.join(project_root, 'bases', 'copy_all_base')
)