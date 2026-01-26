

from app.configuration.extension import db
from app.model.entity.label import Label


class LabelRepository:
    @staticmethod
    def create(data):
        label = Label(**data)
        db.session.add(label)
        db.session.commit()
        return label

    @staticmethod
    def get_all():
        return Label.query.all()
