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
        number = request.json['number']
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PhBook VALUES (?, ?);'''
            ,(name,number)
        )
    except Exception as e:
        print(type(e).__name__)
    conn.commit()
    
    #jsonify will convert dictionary to json
    return jsonify("name : "+request.json['name'],"phNumber : "+request.json['number']),201





# # GET request to get the data with specified id
# @app.route('/phonebook/<int:phBook_id>', methods=['GET'])
# def get_book(phBook_id):
#     #List comprehension, iterate through a list and obtain a sublist
#     phbook = [phbook for phbook in phoneBook if phbook['id']==phBook_id]
#     if len(phbook) == 0:
#         abort(404)
#     else:
#         return jsonify({'phoneBook':phbook[0]})

# # POST request to save the data into the list
# @app.route('/phonebook', methods=['POST'])
# def create_contact():
#     #checking if the string is a valid json
#     if not request.json:
#         abort(400) #400 means a bad request
#     # create a new book as an item which can be inserted into the list
#     # the id will be the next id number, use negative index for the last item
#     phbook = {'id':phoneBook[-1]['id']+1,
#     'name':request.json['name'],
#     'ph':request.json['ph']}
#     #append the new item into the books list
#     phoneBook.append(phbook)
#     #jsonify will convert dictionary to json
#     return jsonify({'phbook':phbook}),201


# #PUT request to edit the data
# @app.route('/phonebook/<int:phbook_id>', methods=['PUT'])
# def upadate_book(phbook_id):
#     #List comprehension, iterate through a list and obtain a sublist
#     phbook = [phbook for phbook in phoneBook if phbook['id']==phbook_id]
#     if len(phbook) == 0:
#         abort(404)
#     #checking if the json from the client has valid title, author keys
#     if 'name' in request.json and type(request.json['name']) != str:
#         abort(400)
#     if 'ph' in request.json and type(request.json['ph']) != str:
#         abort(400)

#     # if no abort conditions occur, update the entry with the specific id
#     phbook[0]['name'] = request.json['name']
#     phbook[0]['ph'] = request.json['ph']

#     #return the updated record
#     return jsonify({'phbook':phbook[0]})


# #DELETE request to delete the data
# @app.route('/phonebook/<int:phbook_id>', methods=['DELETE'])
# def delete_contact(phbook_id):
#     #List comprehension, iterate through a list and obtain a sublist
#     phbook = [phbook for phbook in phoneBook if phbook['id']==phbook_id]
#     if len(phbook) == 0:
#         abort(404)

#     #remove that item from the list
#     phoneBook.remove(phbook[0])

#     #return the status
#     return jsonify({'status':'deleted'})





#check if its the main module, then run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)