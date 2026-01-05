from app.repository.feature_repository import FeatureRepository


class FeatureService:
    @staticmethod
    def create_feature(payload):
        return FeatureRepository.create(payload)

    @staticmethod
    def list_features(name=None, stability=None):
        return FeatureRepository.get_all(name, stability)

    @staticmethod
    def get_feature(feature_name, version):
        return FeatureRepository.get_by_key(feature_name, version)