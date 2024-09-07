from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample movie data organized by genre
movies_by_genre = {
    'Action': [
        {'id': 1, 'title': 'Mad Max: Fury Road', 'rating': 8.1},
        {'id': 2, 'title': 'Die Hard', 'rating': 8.2},
        {'id': 3, 'title': 'John Wick', 'rating': 7.4},
        {'id': 4, 'title': 'The Dark Knight', 'rating': 9.0},
        {'id': 5, 'title': 'Gladiator', 'rating': 8.5},
        {'id': 6, 'title': 'Terminator 2: Judgment Day', 'rating': 8.5},
        {'id': 7, 'title': 'The Matrix', 'rating': 8.7},
        {'id': 8, 'title': 'Inception', 'rating': 8.8},
        {'id': 9, 'title': 'Casino Royale', 'rating': 8.0},
        {'id': 10, 'title': 'The Bourne Identity', 'rating': 7.9},
        {'id': 11, 'title': 'Mission: Impossible - Fallout', 'rating': 7.7},
        {'id': 12, 'title': 'Kingsman: The Secret Service', 'rating': 7.7},
        {'id': 13, 'title': 'The Avengers', 'rating': 8.0},
        {'id': 14, 'title': 'Speed', 'rating': 7.2},
        {'id': 15, 'title': 'Jurassic Park', 'rating': 8.1},
        {'id': 16, 'title': 'RoboCop', 'rating': 7.5},
        {'id': 17, 'title': 'Predator', 'rating': 7.8},
        {'id': 18, 'title': '300', 'rating': 7.6},
        {'id': 19, 'title': 'Lethal Weapon', 'rating': 7.6},
        {'id': 20, 'title': 'Bloodsport', 'rating': 6.8},
    ],
    'Comedy': [
        {'id': 1, 'title': 'Superbad', 'rating': 7.6},
        {'id': 2, 'title': 'The Hangover', 'rating': 7.7},
        {'id': 3, 'title': 'Anchorman: The Legend of Ron Burgundy', 'rating': 7.2},
        {'id': 4, 'title': 'Bridesmaids', 'rating': 6.8},
        {'id': 5, 'title': 'Step Brothers', 'rating': 6.9},
        {'id': 6, 'title': 'Ghostbusters', 'rating': 7.8},
        {'id': 7, 'title': 'Ferris Bueller’s Day Off', 'rating': 7.8},
        {'id': 8, 'title': 'The Big Lebowski', 'rating': 8.1},
        {'id': 9, 'title': 'Office Space', 'rating': 7.8},
        {'id': 10, 'title': 'Groundhog Day', 'rating': 8.0},
        {'id': 11, 'title': 'Dumb and Dumber', 'rating': 7.3},
        {'id': 12, 'title': 'Tropic Thunder', 'rating': 7.0},
        {'id': 13, 'title': '21 Jump Street', 'rating': 7.2},
        {'id': 14, 'title': 'Borat', 'rating': 7.3},
        {'id': 15, 'title': 'Pineapple Express', 'rating': 6.9},
        {'id': 16, 'title': 'This Is Spinal Tap', 'rating': 8.0},
        {'id': 17, 'title': 'Hot Fuzz', 'rating': 7.8},
        {'id': 18, 'title': 'Rushmore', 'rating': 7.7},
        {'id': 19, 'title': 'Legally Blonde', 'rating': 6.3},
        {'id': 20, 'title': 'The Nice Guys', 'rating': 7.4},
    ],
    'Drama': [
        {'id': 1, 'title': 'The Shawshank Redemption', 'rating': 9.3},
        {'id': 2, 'title': 'Forrest Gump', 'rating': 8.8},
        {'id': 3, 'title': 'The Godfather', 'rating': 9.2},
        {'id': 4, 'title': 'Fight Club', 'rating': 8.8},
        {'id': 5, 'title': 'The Godfather: Part II', 'rating': 9.0},
        {'id': 6, 'title': 'Pulp Fiction', 'rating': 8.9},
        {'id': 7, 'title': 'The Dark Knight', 'rating': 9.0},
        {'id': 8, 'title': '12 Angry Men', 'rating': 9.0},
        {'id': 9, 'title': 'Schindler’s List', 'rating': 8.9},
        {'id': 10, 'title': 'Good Will Hunting', 'rating': 8.3},
        {'id': 11, 'title': 'One Flew Over the Cuckoo’s Nest', 'rating': 8.7},
        {'id': 12, 'title': 'A Beautiful Mind', 'rating': 8.2},
        {'id': 13, 'title': 'The Departed', 'rating': 8.5},
        {'id': 14, 'title': 'Whiplash', 'rating': 8.5},
        {'id': 15, 'title': 'The Social Network', 'rating': 7.7},
        {'id': 16, 'title': 'Her', 'rating': 8.0},
        {'id': 17, 'title': 'The Revenant', 'rating': 8.0},
        {'id': 18, 'title': 'The Big Short', 'rating': 7.8},
        {'id': 19, 'title': 'Moonlight', 'rating': 7.4},
        {'id': 20, 'title': 'Lady Bird', 'rating': 7.4},
    ],
    'Horror': [
        {'id': 1, 'title': 'Get Out', 'rating': 7.7},
        {'id': 2, 'title': 'The Exorcist', 'rating': 8.0},
        {'id': 3, 'title': 'The Shining', 'rating': 8.4},
        {'id': 4, 'title': 'Psycho', 'rating': 8.5},
        {'id': 5, 'title': 'Hereditary', 'rating': 7.3},
        {'id': 6, 'title': 'The Conjuring', 'rating': 7.5},
        {'id': 7, 'title': 'A Quiet Place', 'rating': 7.5},
        {'id': 8, 'title': 'It', 'rating': 7.3},
        {'id': 9, 'title': 'The Babadook', 'rating': 6.8},
        {'id': 10, 'title': 'Get Out', 'rating': 7.7},
        {'id': 11, 'title': 'The Witch', 'rating': 6.9},
        {'id': 12, 'title': 'It Follows', 'rating': 6.8},
        {'id': 13, 'title': 'The Ring', 'rating': 7.1},
        {'id': 14, 'title': 'Paranormal Activity', 'rating': 6.3},
        {'id': 15, 'title': 'Rosemary’s Baby', 'rating': 8.0},
        {'id': 16, 'title': 'The Cabin in the Woods', 'rating': 7.0},
        {'id': 17, 'title': 'Halloween', 'rating': 7.7},
        {'id': 18, 'title': 'Saw', 'rating': 7.6},
        {'id': 19, 'title': 'Sinister', 'rating': 6.8},
        {'id': 20, 'title': 'Annihilation', 'rating': 6.8},
    ],
    'Sci-Fi': [
        {'id': 1, 'title': 'Inception', 'rating': 8.8},
        {'id': 2, 'title': 'Blade Runner 2049', 'rating': 8.0},
        {'id': 3, 'title': 'The Matrix', 'rating': 8.7},
        {'id': 4, 'title': 'Interstellar', 'rating': 8.6},
        {'id': 5, 'title': '2001: A Space Odyssey', 'rating': 8.3},
        {'id': 6, 'title': 'The Terminator', 'rating': 8.0},
        {'id': 7, 'title': 'E.T. the Extra-Terrestrial', 'rating': 7.8},
        {'id': 8, 'title': 'The Fifth Element', 'rating': 7.7},
        {'id': 9, 'title': 'Alien', 'rating': 8.4},
        {'id': 10, 'title': 'Arrival', 'rating': 7.9},
        {'id': 11, 'title': 'Gattaca', 'rating': 7.8},
        {'id': 12, 'title': 'Ex Machina', 'rating': 7.7},
        {'id': 13, 'title': 'Minority Report', 'rating': 7.6},
        {'id': 14, 'title': 'Her', 'rating': 8.0},
        {'id': 15, 'title': 'District 9', 'rating': 7.9},
        {'id': 16, 'title': 'Dune', 'rating': 7.6},
        {'id': 17, 'title': 'Predestination', 'rating': 7.5},
        {'id': 18, 'title': 'Star Wars: Episode IV - A New Hope', 'rating': 8.6},
        {'id': 19, 'title': 'Dark City', 'rating': 7.6},
        {'id': 20, 'title': 'Children of Men', 'rating': 7.9},
    ],
}


# Function to recommend a random movie based on genre
def recommend_movie(selected_genre):
    movies = movies_by_genre.get(selected_genre, [])
    if movies:
        return random.choice(movies)  # Randomly select a movie from the list
    return None

@app.route('/')
def index():
    return render_template('index.html', genres=movies_by_genre.keys())

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genre = request.form.get('genre')
    recommended_movie = recommend_movie(selected_genre)
    return render_template('recommend.html', movie=recommended_movie)

if __name__ == '__main__':
    app.run(debug=True)
