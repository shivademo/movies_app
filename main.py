from flask import Flask, jsonify, request
#from storage import all_movies
from data1 import data
app = Flask(__name__)


@app.route('/popular-movies')
def popular_movies():
    """ popular_movies = []
    for movie in all_movies:
        d = {
            "title": movie[19], 
            "poster_link": movie[27], 
            "release_date": movie[13] or "N/A", 
            "duration": movie[15], 
            "rating": movie[20], 
            "overview": movie[9]
        }
        popular_movies.append(d) """
   

    return jsonify({
        'data': data,
        'status': 'success'
    })

if(__name__ == '__main__'):
    app.run()

