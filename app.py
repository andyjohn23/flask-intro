from flask import Flask, render_template, url_for
app = Flask(__name__)

music_list = [
    {
        "id": 1,
        "music_title": "roi manitou",
        "music_artist": "fally ipupa",
        "music_image": "/static/images/fally-ipupa.jpeg"
    },
    {
        "id": 2,
        "music_title": "skol mandra manda",
        "music_artist": "koffi olomide",
        "music_image": "/static/images/fally-ipupa.jpeg"
    }
]


@app.route('/')
def index():
    return render_template('index.html', music_item=music_list)


if __name__ == '__main__':
    app.run(debug=True)
