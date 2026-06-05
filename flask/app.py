from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return '<h1>Крылатая фраза:</h1>' \
    '<p><i>"Впечатление - шахиды, которым не хватило взрывчатки, работают водителями маршруток."</i></p>' \
    '<p>— Форум ру.рыбалка</p>'

if __name__ == '__main__':
    app.run(debug=True)