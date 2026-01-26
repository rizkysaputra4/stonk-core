from sqlalchemy import func

from app.configuration.extension import db


class Feature(db.Model):
    __tablename__ = "features"

    feature_name = db.Column(db.Text, primary_key=True)
    version = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text)
    owner = db.Column(db.Text)
    source_table = db.Column(db.Text, nullable=False)
    source_column = db.Column(db.Text, nullable=False)
    compute_fn = db.Column(db.Text, nullable=False)
    default_params = db.Column(db.JSON, nullable=False)
    dtype = db.Column(db.Text, nullable=False)
    stability = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

