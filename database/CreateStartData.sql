CREATE TABLE Facilities(
facID INTEGER PRIMARY KEY AUTOINCREMENT,
facName TEXT NOT NULL
);

INSERT INTO Facilities (facName) VALUES
('TAS'),
('Science'),
('Music');

CREATE TABLE Items(
itemID INTEGER PRIMARY KEY AUTOINCREMENT,
item_facID INTEGER,
itemName TEXT NOT NULL,
itemDescription TEXT NOT NULL,
itemCount INTEGER,
itemLocation TEXT NOT NULL,
itemPurchaseDate TEXT NOT NULL,
itemNotes TEXT NOT NULL
);

INSERT INTO Items (itemName, item_facID, itemDescription,  itemCount, itemLocation, itemPurchaseDate, itemNotes) VALUES
('Tripod', 1, 'its a tripod', 1, 'C25', '2024-10-28', ''),
('Camera' , 1, 'its a camera', 2, 'C25', '2024-10-28', '');

CREATE TABLE Lease(
leaseID INTEGER PRIMARY KEY AUTOINCREMENT,
lease_ItemID INTEGER,
lease_borrowerID INTEGER,
lease_facID INTEGER,
leaseDate TEXT NOT NULL,
leaseReturnDate TEXT NOT NULL,
leaseSigned BOOLEAN,
leaseDamaged BOOLEAN
);

INSERT INTO Lease (lease_ItemID, lease_borrowerID, lease_facID, leaseDate, leaseReturnDate, leaseSigned, leaseDamaged) VALUES
(1, 1, 1, '2025-08-23', '', True, False),
(2, 1, 1, '2025-08-20', '2025-08-21', True, False);

CREATE TABLE Borrowers(
borrowerID INTEGER PRIMARY KEY AUTOINCREMENT,
borrowerName TEXT NOT NULL
);

INSERT INTO Borrowers (borrowerName) VALUES
('Timmothy'),
('Alex'),
('John'),
('Jane'),
('Doe'),
('Smith'),
('Emily'),
('Michael'),
('Sarah'),
('David'),
('Laura');
