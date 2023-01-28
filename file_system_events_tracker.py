import sys 
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "D:/project 103"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("{event.src_path} has been created.")
    def on_modified(self,event):
        print("{event.src_path} has been modified.")
    def on_moved(self,event):
        print("{event.src_path} has been moved/renamed.")
    def on_deleted(self,event):
        print("{event.src_path} has been deleted.")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()