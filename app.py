from flask import Flask, render_template, request, redirect, url_for, session
from dashi import cook
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return render_template('dashi-home.html')

@app.route('/dashi-app')
def dashi_app():
    return render_template('dashi-app.html')

@app.route('/process-form', methods=['POST'])
def process_form():
    flavors = request.form['flavors']
    response = cook(flavors)
    session['results'] = response
    print(response)
    # Now you can use the flavors variable in your script
    # For example, you could call a function from another file:
    # result = other_file.function(flavors)
    # And then return the result to the user
    return redirect(url_for('results'))

@app.route('/results')
def results():
    results = session.get('results', 'No results')
    result_one = ""
    result_two = ""
    result_three = ""
    parsed_results = results.split("1.", 1)
    if len(parsed_results) > 1:
        result_one = parsed_results[1]
    else:
        parsed_results = "null"
    parsed_results = parsed_results[1].split("2.", 1)
    result_one = parsed_results[0]
    if len(parsed_results) > 1:
        result_two = parsed_results[1]
    else:
        parsed_results = "null"
    parsed_results = parsed_results[1].split("3.", 1)
    result_two = parsed_results[0]
    if len(parsed_results) > 1:
        result_three = parsed_results[1]
    else:
        parsed_results = "null"
    
    return render_template('results.html', result1=result_one, result2=result_two, result3=result_three)

@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    print(email)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)