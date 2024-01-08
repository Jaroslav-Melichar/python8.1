from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        num1 = request.form.get('num1').replace(',', '.')
        num2 = request.form.get('num2').replace(',', '.')
        operation = request.form.get('operation')

        if num1 and num2 and operation:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Error: Division by zero is not allowed."
            else:
                return "Error: Invalid operation."

            return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)