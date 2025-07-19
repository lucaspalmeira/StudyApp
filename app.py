from flask import Flask, render_template, request, redirect, url_for, jsonify
from app.API.items import items_bp

app = Flask(__name__)
app.register_blueprint(items_bp)

@app.route('/')
def index():
    items = ['Item A', 'Item B', 'Item C']
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET"]) 
def contact_form(): 
    return render_template("contact.html") 

# PASSO 3: route to process the form 
@app.route("/contact", methods=["POST"]) 
def contact_process():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message") 
    
    if not name or not email:
        # Possibly redirect back with an error or handle the problem 
        return redirect(url_for("contact")) # Any additional logic, like saving to a database or sending an email 
    return f"Data received: {name}, {email}, {message}"

@app.route('/api')
def api():
    return render_template('api.html')

if __name__ == '__main__':
    app.run(debug=True)