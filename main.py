from flask import Flask, render_template, request, session, redirect, jsonify
import DB_Acess
from datetime import datetime

app = Flask(__name__)
app.secret_key = "gtg"

#homepage
@app.route("/")
def home():
    return render_template("home.html")

#login page
@app.route("/login")
def login():
    return render_template("login.html")

#facilty list page
@app.route("/facilities")
def facilities():
    AllFacilities = DB_Acess.GetAllFacilities()
    print('test' + str(AllFacilities))
    return render_template("All-Facilities.html", facilities=AllFacilities)

#individual facility homepage
@app.route("/facility/<facName>")
def facility(facName):
    return render_template("Facility.html", facname=facName)

#lease item page (facility specific)
@app.route('/facility/<facName>/loan', methods=["GET", "POST"])
def loan(facName):
    if request.method == "POST":
        itemID = request.form.get("ItemId")
        borrowerID = request.form.get("BorrowerId")
        signed = request.form.get("studentSignoff")
        if signed == 'on':
            signed = 1
        else:
            signed = 0
        leaseDate = datetime.today().strftime('%Y-%m-%d')
        DB_Acess.LeaseItem(itemID, borrowerID, facName, leaseDate, signed)
        return redirect(f"/facility/{facName}/returns")
    return render_template("loan.html", facname=facName)

# searches for items when leasing an item (not a page)
@app.route('/search_Item')
def loan_search_items():
    query = request.args.get('query', '').lower()
    facName = request.args.get('facName', '')

    # Fetch all items for the facility and convert to a list of names and IDs
    all_items = DB_Acess.GetAllItems(facName)
    results = [
               {'id': item["itemID"], 'name': item["itemName"]} 
               for item in all_items 
               if query in item["itemName"].lower()
               ]

    return jsonify(results)

# searches for borrowers when leasing an item (not a page)
@app.route('/search_Borrower')
def loan_search_borrowers():
    query = request.args.get('query', '').lower()

    all_borrowers = DB_Acess.GetAllBorrowers()
    results = [
               {'id': borrower["borrowerID"], 'name': borrower["borrowerName"]} 
               for borrower in all_borrowers
               if query in borrower["borrowerName"].lower()
               ]

    return jsonify(results)

#return page (facility specific)
@app.route("/facility/<facName>/returns", methods=["GET", "POST"])
def returns(facName):
    if request.method == "POST":
        leaseID = request.form.get("leaseID")
        itemNotes = request.form.get("itemNotes")
        itemDamaged = request.form.get("itemDamaged")
        if itemDamaged == 'on':
            itemDamaged = 1
        else:
            itemDamaged = 0
        returnDate = datetime.today().strftime('%Y-%m-%d')
        print(f"Lease ID: {leaseID}, Notes: {itemNotes}, Damaged: {itemDamaged}")
        DB_Acess.ReturnItem(leaseID, itemNotes, itemDamaged, returnDate)
        return redirect(f"/facility/{facName}/returns")
    
    returns = DB_Acess.GetAllActiveReturns(facName)
    return render_template("return.html", facname=facName, returns=returns)


#item list page for a specific facility (also includes popup with form to add new items)
@app.route("/facility/<facName>/items", methods=["GET", "POST"])
def items(facName):
    if request.method == "POST":
        # Handle form submission for adding a new item
        itemName = request.form.get("itemName")
        itemDescription = request.form.get("itemDescription")
        itemCount = request.form.get("itemCount")
        itemLocation = request.form.get("itemLocation")
        itemPurchaseDate = request.form.get("itemPurchaseDate")
        itemNotes = request.form.get("itemNotes")

        # add item to the database
        DB_Acess.AddItem(facName, itemName, itemDescription, itemCount, itemLocation, itemPurchaseDate, itemNotes)

        return redirect(f"/facility/{facName}/items")
    
    items = DB_Acess.GetAllItems(facName)
    return render_template("items.html", facname=facName, items=items)

#TODO
@app.route("/facility/<facName>/items/(itemID)")
def item(facName, itemID):
    return render_template("individual_item.html", )

app.run(debug=True, port=5000)