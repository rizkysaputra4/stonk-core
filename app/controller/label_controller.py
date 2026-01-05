from flask import Blueprint, request, jsonify
from app.service.data.label_service import LabelService

label_bp = Blueprint("label_api", __name__)

@label_bp.route("/labels", methods=["POST"])
def create_label():
    payload = request.get_json()
    label = LabelService.create_label(payload)
    return jsonify({
        "label_name": label.label_name,
        "version": label.version
    }), 201

@label_bp.route("/labels", methods=["GET"])
def list_labels():
    labels = LabelService.list_labels()

    return jsonify([
        {
            "label_name": l.label_name,
            "version": l.version,
            "description": l.description,
            "compute_fn": l.compute_fn,
            "default_params": l.default_params,
            "dtype": l.dtype,
            "created_at": l.created_at.isoformat()
        }
        for l in labels
    ]), 200