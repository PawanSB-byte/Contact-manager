"""
Project: Contact Management System
Name: KUMAR SUBODH
Date: 03-04-2026
Description: Flask CRUD App for managing contacts
"""
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# In-memory storage
contacts = []
id_counter = 1
# HOME (READ)
@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        filtered = [c for c in contacts if search.lower() in c['name'].lower() or search in c['phone']]
        return render_template('index.html', contacts=filtered)
    return render_template('index.html', contacts=contacts)
# CREATE
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    global id_counter
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        if not name or not phone or not email:
            return "All fields are required!"
        contacts.append({
            'id': id_counter,
            'name': name,
            'phone': phone,
            'email': email
        })
        id_counter += 1
        return redirect(url_for('index'))
    return render_template('add_contact.html')
# UPDATE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = next((c for c in contacts if c['id'] == id), None)
    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        return redirect(url_for('index'))
    return render_template('edit_contact.html', contact=contact)
# DELETE
@app.route('/delete/<int:id>')
def delete_contact(id):
    global contacts
    contacts = [c for c in contacts if c['id'] != id]
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
