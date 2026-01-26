from app.configuration.extension import db
from app.model.entity.feature import Feature


class FeatureRepository:
    @staticmethod
    def create(data):
        feature = Feature(**data)
        db.session.add(feature)
        db.session.commit()
        return feature

    @staticmethod
    def get_all(name=None, stability=None):
        q = Feature.query
        if name:
            q = q.filter(Feature.feature_name == name)
        if stability:
            q = q.filter(Feature.stability == stability)
        return q.all()

    @staticmethod
    def get_by_key(feature_name, version):
        return Feature.query.filter_by(
            feature_name=feature_name,
            version=version
        ).first()