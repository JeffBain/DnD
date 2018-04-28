import graphene

from inventory.schema import Query as InventoryQuery

class Query(InventoryQuery):
    pass

schema = graphene.Schema(query=Query)
