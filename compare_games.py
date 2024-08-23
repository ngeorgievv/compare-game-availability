from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare():
    first_input = request.form['first_input']
    second_input = request.form['second_input']

    # Split the input by commas and strip any extra spaces
    set1 = set([title.strip() for title in first_input.split(',')])
    set2 = set([title.strip() for title in second_input.split(',')])

    # Find the difference: titles in set1 but not in set2
    difference = set1.difference(set2)

    # Join the result as a comma-separated string
    result = ', '.join(difference)

    return render_template('index.html', result=result, first_input=first_input, second_input=second_input)


if __name__ == '__main__':
    app.run(debug=True, port=8002, host='0.0.0.0')