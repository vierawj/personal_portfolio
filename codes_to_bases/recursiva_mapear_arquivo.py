import os
import json


current = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.dirname(current)

def recurse_keys(content, content_path_array, value, i=0, indent = '  ' ):
    for key in content.keys():
        print(indent+str(key), str(i))
        if isinstance(content[key], dict) and key == content_path_array[i]:
            recurse_keys(content[key], content_path_array, value, i+1, indent+'   ')
        elif isinstance(content[key], list) and key == content_path_array[i]:
            i += 1
            for item in range(0, len(content[key])):
                if item == int(content_path_array[i]):
                    recurse_keys(content[key][item],content_path_array, value, i+1, indent+'   ' + str(item) + '   ')
        elif i == len(content_path_array) - 1:
            content[content_path_array[i]] = value
            print('encontrado!', str(content))
            break


itens_to_process = [
    {
        "type" : "folder",
        "file_path" : "exemplo_folder",
        "content_path" : None,
        "value" : "exemplo_renamed_folder",
    },
    {
        "type" : "file",
        "file_path" : "exemplo.json",
        "content_path" : "fixed_value|to_alter",
        "value" : "altered_value_3",
    },
    {
        "type" : "file",
        "file_path" : "exemplo.json",
        "content_path" : "data|1|coluna_2",
        "value" : "A",
    },
]


for item_config in itens_to_process:
    # item_config=itens_to_process[0]
    if item_config["type"] == 'file':
        with open(os.path.join(project_root , 'bases', item_config["file_path"]), 'r') as file:
            content = json.loads(file.read())
        
        #content['fixed_value'] = item_config['value']
        recurse_keys(content, item_config['content_path'].split('|'), item_config['value'])
        
        with open(item_config["file_path"], 'w') as file:
            file.write(json.dumps(content))
    elif item_config["type"] == 'folder':
        for item in content['data']:
            print(item)
            recurse_keys(content, item_config['content_path'].split('|'), item_config['value'])
            

'''
for item_config in itens_to_process:
    # item_config=itens_to_process[0]
    if item_config["type"] == 'file':
        with open(item_config["file_path"], 'rb') as file:
            content = json.loads(file.read())
        
        content['fixed_value'] = item_config['value']
        
        with open(item_config["file_path"], 'w') as file:
            file.write(json.dumps(content))
    elif item_config["type"] == 'folder':
        for item in content['data']:
            print(item)       

'''
            

    



