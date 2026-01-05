from flask import Blueprint, request, jsonify

from app.service.data.feature_service import FeatureService

feature_bp = Blueprint("feature_bp", __name__)
@feature_bp.route("/features", methods=["POST"])
def create_feature():
    payload = request.get_json()
    feature = FeatureService.create_feature(payload)
    return jsonify({
        "feature_name": feature.feature_name,
        "version": feature.version
    }), 201

@feature_bp.route("/features", methods=["GET"])
def list_features():
    name = request.args.get("name")
    stability = request.args.get("stability")

    features = FeatureService.list_features(name, stability)

    return jsonify([
        {
            "feature_name": f.feature_name,
            "version": f.version,
            "description": f.description,
            "source_table": f.source_table,
            "source_column": f.source_column,
            "compute_fn": f.compute_fn,
            "default_params": f.default_params,
            "dtype": f.dtype,
            "stability": f.stability,
            "created_at": f.created_at.isoformat()
        }
        for f in features
    ]), 200