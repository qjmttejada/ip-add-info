import ipapi
from flask import Flask, request, render_template
 
# enter "pip install ipapi" first in terminal
 
app = Flask(__name__)
 
@app.route('/', methods = ['GET', 'POST'])
def Index(): #function for index.html to request user input, and output the ip add info 
    search = request.form.get('search') # user input
    data = ipapi.location(ip=search, output='json') # get data for the ip input 
    return render_template('index.html', data=data) # open index.html and return data

if __name__ == "__main__":
    app.run(debug=True)