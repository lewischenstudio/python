from db import db


# Many-to-many relationship between items and tags
# item.tags.append(tag) will add an existing item_id and tag_id
# to this table
class ItemsTags(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
