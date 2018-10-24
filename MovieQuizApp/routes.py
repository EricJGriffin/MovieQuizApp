from flask import Flask, url_for, render_template, request
from app import app
import redis

# connect to redis data store
r = redis.StrictRedis(host = 'localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

@app.route('/')
def hello():
    """Renders a sample page."""
    createLink = "<a href = '" + url_for("createEntry") + "'>Create Entry</a>"
    return """ <html> 
                     <head>
                          <title>Movie App!</title>
                     </head>
                     <body>
                        """ + createLink + """
                    </body>
                </html>"""
    
        
@app.route('/createEntry', methods=['GET', 'POST'])
def createEntry():
    if request.method == 'GET':
        return render_template('CreateEntry.html')
    elif request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        rating = request.form['rating']

        # enter data into data store
        r.set(title + ':year', year)
        r.set(title + ':rating', rating)

        return render_template('EntrySubmitted.html', title = title)
    else:
        return "<h2>Invalid Response</h2>"
    return "<h2>Create a movie entry</h2>"

@app.route('/quiz/<title>', methods=['GET', 'POST'])
def quiz(title):
    if request.method == 'GET':
        return render_template('MovieQuiz.html', title = title)
    elif request.method == 'POST':
        submittedYear = request.form['submittedYear']
        submittedRating = request.form['submittedRating']

        year = r.get(title + ":year")
        rating = r.get(title + ":rating")

        if (submittedYear == year) and (submittedRating == rating):
            return render_template('Correct.html')
        else:
            return render_template('Incorrect.html', submittedYear = submittedYear, submittedRating = submittedRating, 
                                   year = year, rating = rating)
    else:
        return "<h2>Invalid response</h2>"
