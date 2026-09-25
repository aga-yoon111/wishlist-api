
from factory import db

class WishlistItem(db.Model):
    __tablename__ = "wish"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(255), nullable=True)
    purchased = db.Column(db.Boolean, default=False, nullable=False)
    sort_order = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return f"<User {self.name}>"