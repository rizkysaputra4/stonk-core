from sqlalchemy import func

from app.configuration.extension import db


class Label(db.Model):
    __tablename__ = "labels"

    label_name = db.Column(db.Text, primary_key=True)
    version = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text)
    compute_fn = db.Column(db.Text, nullable=False)
    default_params = db.Column(db.JSON, nullable=False)
    dtype = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(),
                           nullable=False)