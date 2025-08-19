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
('Tripod', 1, 'its a tripod', 1, 'C25', '2024-10-28', 'none'),
('Camera' , 1, 'its a camera', 2, 'C25', '2024-10-28', 'none');

CREATE TABLE Loans(
loanID INTEGER PRIMARY KEY AUTOINCREMENT,
loan_ItemID INTEGER,
loan_borrowerID INTEGER,
signed BOOLEAN,
damaged BOOLEAN
);

INSERT INTO Loans (loan_ItemID, loan_borrowerID, signed, damaged) VALUES
(1, 1, True, False);

CREATE TABLE Borrowers(
borrowerID INTEGER PRIMARY KEY AUTOINCREMENT,
borrowerName TEXT NOT NULL
);

INSERT INTO Borrowers (borrowerName) VALUES
('Timmothy');