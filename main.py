# main.py

from modules import database_handler as dbh
from modules import gui

if __name__ == "__main__":
    dbh.create_tables()
    gui.startGui()  # mainWindow'u bu şekilde alın

