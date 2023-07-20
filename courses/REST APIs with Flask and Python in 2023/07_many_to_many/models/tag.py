from db import db


# One-to-many relationship between stores and tags
# Many-to-many relationship between items and tags
class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)

    # One-to-many relationship between stores and tags
    store = db.relationship("StoreModel", back_populates="tags")

    # Many-to-many relationship between items and tags
    # No need to define "items_tags_id"
    # Uses secondary table ItemTagModel to find the id of the instance
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
