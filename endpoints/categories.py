from flask import Blueprint, request, jsonify
from src.services.category_service import CategoryService

bp = Blueprint("categories", __name__)
service = CategoryService()

@bp.route("/categories", methods=["POST"])
def create_category():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_category = service.create_category(data["name"])
    return jsonify({"id": new_category.id, "name": new_category.name}), 201

@bp.route("/categories", methods=["GET"])
def get_categories():
    categories = service.get_all_categories()
    result = [{"id": c.id, "name": c.name} for c in categories]
    return jsonify(result), 200

