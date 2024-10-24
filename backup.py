from os import path
import shutil
from datetime import date
import time
import schedule 

source_dir: str = r"C:\Users\Nathan Joseph\Documents\Dummy Data"
target_dir: str = r"C:/Users\Nathan Joseph\Desktop\Backups"
def main() -> None:
    #Schedules backup to be run every Thursday at 12pm and checks every minute to see whether the task is still pending or not
    schedule.every().thursday.at("13:00").do(lambda: copy_source_to_destination(source_dir, target_dir))

    while True:
        schedule.run_pending()
        time.sleep(60)

def copy_source_to_destination(source: str , destination: str) -> None:
    
    """
    Copies the contents from specified source directory to a specified destination directory with the current date as the directory name  
    """
    
    today = date.today()
    destination_dir: str = path.join(destination, str(today)) #Creates new directory at destination with today's date

    #Recursively copies source folder contents to the new destination directory if the directory doesn't already exist
    try: 
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"{destination_dir} already exists")



main()