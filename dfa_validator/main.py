from flask import Flask, render_template, request

from dfa.password_dfa import check_password
from dfa.url_dfa import check_url
from dfa.email_dfa import check_email
from dfa.phone_dfa import check_phone

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        input_type = request.form["type"]
        value = request.form["value"]

        if input_type == "password":
            result = "Strong Password ✅" if check_password(value) else "Weak Password ❌"

        elif input_type == "url":
            result = "Valid URL ✅" if check_url(value) else "Invalid URL ❌"

        elif input_type == "email":
            result = "Valid Email ✅" if check_email(value) else "Invalid Email ❌"

        elif input_type == "phone":
            result = "Valid Phone Number ✅" if check_phone(value) else "Invalid Number ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
