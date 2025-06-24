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

@app.route('/responses')
def view_responses():
    responses = []
    with open('responses.csv', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)  # skip header
        for row in reader:
            responses.append(row)
    return render_template('responses.html', responses=responses, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
