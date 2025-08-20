import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

def GetDB():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database", "EquipmentTracker.db")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def GetAllFacilities():
    db = GetDB()
    facilities = db.execute("""SELECT facName
                        FROM Facilities""").fetchall()
    db.close()
    return [row[0] for row in facilities]