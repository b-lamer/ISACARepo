from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/reposts")
def getReposts():
    reposts = {
        "repost count" : "100"
    }
    return jsonify(reposts), 200

@app.route("/likes")
def getLikes():
    likes = {
        "like count" : "200"
    }
    return jsonify(likes), 200

@app.route("/bookmarks")
def getBookmarks():
    bookmarks = {
        "bookmark count" : "300 bookmarks"
    }
    return jsonify(bookmarks), 200


if __name__ == "__main__":
    app.run(debug=True)