from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_query():
    query = request.form['query']
    search_results = search(query, num_results=10)
    return render_template('results.html', query=query, results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
