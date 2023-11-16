def parse_folder(path):
    files = []
    folders = []
    
    for itm in path.iterdir():

        if itm.is_file():

             files.append(itm.name)

        if itm.is_dir():

             folders.append(itm.name) 
            
    return files, folders