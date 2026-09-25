from typing import Optional

from pydantic import BaseModel, ConfigDict

class WishlistItemCreate(BaseModel):
    name: str
    description: Optional[str]=None
    link: Optional[str] = None
    sort_order: Optional[int] = None
    
class WishlistItemUpdate(BaseModel):
    name: str
    description: Optional[str]=None
    link: Optional[str] = None
    sort_order: Optional[int] = None
    purchased: bool
    

class WishlistItemResponse(BaseModel):
    model_config =ConfigDict(from_attributtes=True)
    id: int
    name: str
    description: Optional[str]
    link: Optional[str]
    purchased: bool
    sort_order: Optional[int]
    



class WishlistItemResponseList(BaseModel):
   item: list[WishlistItemResponse]


class WishlistItemMessage(BaseModel):
    id = int
    msg = str
