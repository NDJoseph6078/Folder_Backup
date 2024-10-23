from os import path
import shutil
from datetime import date
import time
import schedule
source_dir: None = None
target_dir: None = None

def copy_source_to_destination(source, destination) -> None:
    today = date.today()
    print(today)
    destination_dir: str = path.join(destination, str(today)) #Creates new directory at destination with today's date

    #Recursively copies source folder contents to the new destination directory if the directory doesn't already exist
    try: 
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"{destination_dir} already exists")

#copy_source_to_destination(source_dir, target_dir)