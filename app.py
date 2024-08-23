from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    magnet_link = request.form['magnet']
    if magnet_link.startswith('magnet:?xt=urn:btih:'):
        # Encode the magnet link for inclusion in the URL
        encoded_magnet = request.form['magnet']
        # Generate the Webtor URL
        normal_link = f"https://webtor.io/#/show?magnet={encoded_magnet}"
        return render_template('index.html', normal_link=normal_link)
    else:
        return render_template('index.html', error="Invalid magnet link")

if __name__ == '__main__':
    app.run(debug=True)