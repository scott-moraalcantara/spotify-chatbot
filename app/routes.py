from flask import Blueprint, request, jsonify
from app.handlers.intent_handler import handle_query

main = Blueprint("main", __name__)

@main.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("query", "")
    response = handle_query(user_query)
    return jsonify({"response": response})