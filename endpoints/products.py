from flask import Blueprint, request, jsonify
from src.services.product_service import ProductService
from src.services.category_service import CategoryService

bp = Blueprint("products", __name__)
service = ProductService()
category_service = CategoryService()

@bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "category_id" not in data:
        return jsonify({"error": "Missing fields"}), 400

    category = category_service.get_category_by_id(data["category_id"])
    if not category:
        return jsonify({"error": "Category not found"}), 404

    new_product = service.create_product(data["name"], data["price"], category)
    return jsonify({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price,
        "category_id": category.id
    }), 201

@bp.route("/products", methods=["GET"])
def get_products():
    products = service.get_all_products()
    result = [{"id": p.id, "name": p.name, "price": p.price, "category_id": p.category.id} for p in products]
    return jsonify(result), 200
