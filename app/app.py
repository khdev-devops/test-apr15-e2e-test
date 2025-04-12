from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/horizontal_slider")
def horizontal_slider():
    return send_from_directory("static", "horizontal_slider.html")

@app.route("/dynamic_loading")
def dynamic_loading():
    return send_from_directory("static", "dynamic_loading.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)