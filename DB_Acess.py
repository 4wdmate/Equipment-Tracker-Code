import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Database Access Layer for Equipment Tracker
def GetDB():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database", "EquipmentTracker.db")
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

# gets a list of all facilities in the database
def GetAllFacilities():
    db = GetDB()
    facilities = db.execute("""SELECT facName
                        FROM Facilities""").fetchall()
    db.close()
    return [row[0] for row in facilities]

#gets a dictionary of all items in the database for a specific facility
def GetAllItems(facName):
    db = GetDB()
    items = db.execute("""SELECT itemID, itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes, item_facID, facName
                        FROM Items
                        JOIN Facilities ON Items.item_facID = Facilities.facID
                        WHERE facName = ?""", (facName,)).fetchall()
    db.close()
    return [dict(row) for row in items]

#adds a new item to the database
def AddItem(facName, itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes):
    db = GetDB()
    facID = db.execute("SELECT facID FROM Facilities WHERE facName = ?", (facName,)).fetchone()
    if facID:
        db.execute("""INSERT INTO Items (itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes, item_facID)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes, facID['facID']))
        db.commit()
    db.close()