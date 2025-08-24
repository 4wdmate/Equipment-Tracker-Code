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

#todo (needs to check for returns that have a non existant user or item)

def FixDB():
    pass

#todo (clears any items that have already been returned)
def ClearOldReturns():
    pass

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

#gets a dictionary of a specific item in the database by its ID
def GetItemByID(itemID):
    db = GetDB()
    item = db.execute("""SELECT itemID, itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes, item_facID
                        FROM Items
                        WHERE itemID = ?""", (itemID,)).fetchone()
    db.close()
    if item:
        return dict(item)
    else:
        return None

#deletes an item from the database by its id
def DeleteItem(itemID):
    db = GetDB()
    db.execute("DELETE FROM Items WHERE itemID = ?", (itemID,))
    db.commit()
    db.close()

#gets a dictionary of all borrowers in the database
def GetAllBorrowers():
    db = GetDB()
    borrowers = db.execute("""SELECT borrowerID, borrowerName
                        FROM Borrowers""").fetchall()
    db.close()
    return [dict(row) for row in borrowers]

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

#updates an existing item in the database
def UpdateItem(itemID, itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes):
    db = GetDB()
    db.execute("""UPDATE Items
                SET itemName = ?, itemDescription = ?, itemCount = ?, itemLocation = ?, itemPurchaseDate = ?, itemNotes = ?
                WHERE itemID = ?""",
                (itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes, itemID))
    db.commit()
    db.close()

#gets a dictionary of all the returns in the database for a specific facility
def GetAllActiveReturns(facName):
    db = GetDB()
    loans = db.execute("""SELECT leaseID, lease_itemID, lease_borrowerID, lease_facID, leaseDate, leaseReturnDate, leaseSigned, leaseDamaged, itemName, itemDescription, itemCount, itemLocation, itemNotes, facName, borrowerName
                        FROM Lease
                        JOIN Facilities ON Lease.lease_facID = Facilities.facID
                        JOIN Items ON lease.lease_itemID = Items.itemID
                        JOIN Borrowers ON lease.lease_borrowerID = Borrowers.borrowerID
                        WHERE facName = ? AND leaseReturnDate = ''
                        """, (facName,)).fetchall()
    db.close()
    return [dict(row) for row in loans]

def ReturnItem(leaseID, itemNotes, itemDamaged, returnDate):
    db = GetDB()
    db.execute("""UPDATE Lease
                SET leaseReturnDate = ?, leaseDamaged = ?
                WHERE leaseID = ?""",
                (returnDate, itemDamaged, leaseID))
    db.execute("""UPDATE Items
                SET itemNotes = ?
                WHERE itemID = (SELECT lease_itemID FROM Lease WHERE leaseID = ?)""",
                (itemNotes, leaseID))
    db.commit()
    db.close()

def LeaseItem(itemID, borrowerID, facName, leaseDate, signed):
    db = GetDB()
    facID = db.execute("SELECT facID FROM Facilities WHERE facName = ?", (facName,)).fetchone()
    if facID:
        db.execute("""INSERT INTO Lease (lease_itemID, lease_borrowerID, lease_facID, leaseDate, leaseSigned, leaseDamaged, leaseReturnDate)
                    VALUES (?, ?, ?, ?, ?, 0, '')""",
                    (itemID, borrowerID, facID['facID'], leaseDate, signed))
        db.commit()
    db.close()