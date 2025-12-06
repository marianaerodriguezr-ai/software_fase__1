# endpoints/auth.py

from flask_restful import Resource
from flask import request


class AuthenticationResource(Resource):

    VALID_TOKEN = "abcd1234"

    @staticmethod
    def verify_token():
        token = request.headers.get("Authorization")
        if not token:
            return False, {"message": "Unauthorized acces token not found"}, 401

        if token != AuthenticationResource.VALID_TOKEN:
            return False, {"message": "Invalid token"}, 401

        return True, None, 200
