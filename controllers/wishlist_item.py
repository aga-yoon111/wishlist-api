
from flask import Blueprint, request

from sqlalchemy import select
from spectree import Response

from factory import api, db
from models.wishlist_item import WishlistItem

from schemas.wishlist_item import(
    WishlistItemCreate,
    WishlistItemUpdate,
    WishlistItemResponse,
    WishlistItemResponseList,
    WishlistItemMessage,

)


wish_controller = Blueprint("wish_controller", __name__, url_prefix="/api/wishlist")


@wish_controller.get("/")
@api.validate(resp=Response(HTTP_200=WishlistItemResponse), tags=["wishlist"])

def get_users():
    """
    Get all wishes
    """
    items = db.session.scalars(select(WishlistItem)).all()

    return {
        "items":[
            WishlistItemResponse.model_validate(item)
            for item in items
        ]
    }, 200


@wish_controller.get("/<int:item_id>")
@api.validate(
    resp=Response(HTTP_200=WishlistItemResponse, HTTP_404=WishlistItemMessage), tags=["wishlist"]
)

def get_wishlist_item(item_id):
    """
    Get a specified item
    """
    item = db.session.get(WishlistItem, item_id)

    if item is None:
        return {
            "id":item_id,
            "msg": f"There is no item with this id"}, 404

    response = WishlistItemResponse.model_validate(item)

    return response, 200


@wish_controller.post("")
@api.validate(
    json=WishlistItemCreate,
    resp=Response(HTTP_201=WishlistItemResponse),
    security={},
    tags=["wishlist"],
)
def create_wishlist_item():
    """
    Create an wish
    """
    data = request.json

    item= WishlistItem(
        name=data["name"],
        description=data["description"],
        link=data["link"],
        sort_order=data["sort_order"],
    )

    db.session.add(item)
    db.session.commit()

    return {"msg": "Item created successfully."}, 201


@wish_controller.put("/<int:item_id>")
@api.validate(
    json=WishlistItemUpdate,
    resp=Response(
        HTTP_200=WishlistItemMessage,
        HTTP_404=WishlistItemMessage,
    ),
    tags=["wishlist"],
)



def update_wishlist_item(item_id):
    item = db.session.get(WishlistItem, item_id)

    if item is None:
        return {
            "id": item_id,
            "msg": "Item não encontrado."
        }, 404

    data = request.json

    item.name = data["name"]
    item.description = data.get("description")
    item.link = data.get("link")
    item.sort_order = data.get("sort_order")
    item.purchased = data["purchased"]

    db.session.commit()

    return {
        "id": item.id,
        "msg": "Item atualizado com sucesso."
    }, 200


@wish_controller.delete("/<int:item_id>")
@api.validate(
    resp=Response(
        HTTP_200=WishlistItemMessage,
        HTTP_404=WishlistItemMessage,
    ),
    tags=["wishlist"],
)
def delete_wishlist_item(item_id):
    item = db.session.get(WishlistItem, item_id)

    if item is None:
        return {
            "id": item_id,
            "msg": "Item não encontrado."
        }, 404

    db.session.delete(item)
    db.session.commit()

    return {
        "id": item_id,
        "msg": "Item removido com sucesso."
    }, 200