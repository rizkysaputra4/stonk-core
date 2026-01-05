from app.repository.label_repository import LabelRepository


class LabelService:
    @staticmethod
    def create_label(payload):
        return LabelRepository.create(payload)

    @staticmethod
    def list_labels():
        return LabelRepository.get_all()