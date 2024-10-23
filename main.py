from os import path
import shutil
import datetime
import time
import schedule
source_dir = None
target_dir = None

def copy_source_to_destination(source, destination) -> None:
    today = datetime.date.today()
    destination_dir: str = path.join(destination, str(today))
    