from math import factorial
import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
database_url = os.getenv("DATABASE_URL", "sqlite:///number_analyzer.db")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class AnalysisHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    is_prime = db.Column(db.Boolean, nullable=False)
    parity = db.Column(db.String(10), nullable=False)
    digit_sum = db.Column(db.Integer, nullable=False)
    factorial_value = db.Column(db.Text, nullable=False)


def check_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


def sum_of_digits(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        user_input = request.form.get("number", "").strip()

        try:
            number = int(user_input)

            if number < 0:
                raise ValueError("Negative number is not allowed.")

            prime_status = check_prime(number)
            parity = "Even" if number % 2 == 0 else "Odd"
            digit_sum = sum_of_digits(number)
            factorial_value = factorial(number)

            result = {
                "number": number,
                "prime": "Prime" if prime_status else "Not Prime",
                "parity": parity,
                "digit_sum": digit_sum,
                "factorial": factorial_value,
            }

            row = AnalysisHistory(
                number=number,
                is_prime=prime_status,
                parity=parity,
                digit_sum=digit_sum,
                factorial_value=str(factorial_value),
            )
            db.session.add(row)
            db.session.commit()
        except ValueError as exc:
            message = str(exc)
            if message:
                error = message
            else:
                error = "Please enter a valid non-negative integer."

    history = AnalysisHistory.query.order_by(AnalysisHistory.id.desc()).limit(10).all()
    return render_template("index.html", result=result, error=error, history=history)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")), debug=True)
