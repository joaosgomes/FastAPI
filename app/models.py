import json
from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    Id:  Optional[int]
    Value: Optional[str]

class Object(BaseModel):
    Id: Optional[int]
    Value: Optional[str]
    Item: Optional[Item]

class Model(BaseModel):
    Id: Optional[str]
    Value: Optional[str]
    Boolean: Optional[bool]
    List_Objects: Optional[List[Object]]


List_Objects = []


for i in range(5):
      List_Objects.append(Object(Id=i, Item= Item(Id= i)));


print(List_Objects);


List_Model = []

for i in range(5):
     List_Model.append(Model(Id = i, List_Objects = List_Objects))




print(List_Model);

print(type(List_Model))
# convert into JSON:
