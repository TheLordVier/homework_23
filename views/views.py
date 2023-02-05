from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from functions.converter import build_query
from models.models import BatchRequestSchema

main_bp = Blueprint("main", __name__)


@main_bp.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json

    try:
        validated_data = BatchRequestSchema().load(data)  # validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in validated_data["queries"]:
        result = build_query(
            cmd=query["cmd"],
            value=query["value"],
            file_name=validated_data["file_name"],
            data=result,
        )

    return jsonify(result)
