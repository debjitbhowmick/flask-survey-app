from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def survey_form():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        q1 = request.form['q1']
        q2 = request.form['q2']
        
        # Save to CSV
        with open('responses.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, age, q1, q2])
        
        return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
    return "<h2>Thank you for your response!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
