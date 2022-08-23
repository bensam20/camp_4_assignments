from flask import Flask, redirect, url_for, request, jsonify, abort
import pyodbc


#creating an application instance
#the argument for the constructor is the main module name
#main module  name will be there in the dunder __name__
app = Flask(__name__)


#Connecting with the server
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-CSCIVVL\SQLEXPRESS;
    Database=phonebook;
    Trusted_Connection=yes;
''')
cursor = conn.cursor()

def listAll():
    cursor.execute(''' 
        select * from PhBook
        order by name;
    ''')
    phoneBook={}
    a=cursor.fetchall()
    for i in a:
        phoneBook[i[0]] =i[1]
    return phoneBook

# GET request to get the data in json format
@app.route('/contacts',methods=["GET"])
def contacts():
    return jsonify(listAll())


# POST request to save the data into the list
@app.route('/contacts', methods=['POST'])
def create_contact():
    #checking if the string is a valid json
    if not request.json:
        abort(400) #400 means a bad request
    # create a new book as an item which can be inserted into the list
    # the id will be the next id number, use negative index for the last item
    
    try:
        name = request.json['name']
        number = int(request.json['number'])
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PhBook VALUES (?, ?);'''
            ,(name,number)
        )
    except Exception as e:
        print(type(e).__name__)
    conn.commit()
    
    #jsonify will convert dictionary to json
    return jsonify("name : "+request.json['name'],"phNumber : "+str(request.json['number'])),201

#GET method to get a contact by name
@app.route('/contacts/<name>', methods=['GET'])
def get_contact(name):
    phbook = listAll()
    #List comprehension, iterate through a list and obtain a sublist
    names = phbook.keys()
    if name in names:
        return jsonify({'contact':{'name': name, 'phone': phbook[name]}})
    else:
        abort(404)

#GET method to get a contact by number
@app.route('/contacts/<int:number>', methods=['GET'])
def get_contact_by_number(number):
    phbook = listAll()
    #List comprehension, iterate through a list and obtain a sublist
    numbers = phbook.values()
    if number in numbers:
        for i in phbook:
            if phbook[i]==number:
                name = i
                break
        return jsonify({'contact':{'name': name, 'phone': number}})
    else:
        abort(404)


#DELETE request to delete the data by name
@app.route('/contacts/<name>', methods=['DELETE'])
def delete_contact(name):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM PhBook
            WHERE Name=(?);'''
            ,(name)
        )
        conn.commit()
        return jsonify({'status':'deleted'})
    except Exception as e:
        print(type(e).__name__)
    conn.commit()


#check if its the main module, then run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)