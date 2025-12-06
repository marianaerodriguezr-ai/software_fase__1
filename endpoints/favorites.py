from flask_restful import Resource

# Este recurso no es probado por los tests, así que ponemos un mínimo
class FavoritesResource(Resource):
    def get(self):
        return {"message": "Favorites endpoint not implemented"}, 200
