from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/json")
def json_example():
    return jsonify({
        "message": "Hello, this is a JSON response",
        "status": "success"
    })

@app.route("/image")
def image_example():
    return send_from_directory(
        directory="static",
        path="placeholder.png",
        mimetype="image/png"
    )

@app.route("/pdf")
def pdf_example():
    return send_from_directory(
        directory="static",
        path="placeholder.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
