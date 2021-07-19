from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
import mysql.connector
from searchpopupmenu import SearchPopupMenu
class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Wyndham911!',
            port='3306',
            database='python_video1'
        )
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()
MainApp().run()
