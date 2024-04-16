from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201



def getReposts(post_data):
    reposts = {
        "repost count" : "100"
    }
    return jsonify(reposts), 200

def getLikes():
    likes = {
        "like count" : "200"
    }
    return jsonify(likes), 200

def getBookmarks():
    bookmarks = {
        "bookmark count" : "300 bookmarks"
    }
    return jsonify(bookmarks), 200



if __name__ == "__main__":
    app.run(debug=True)