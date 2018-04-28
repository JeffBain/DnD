import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from inventory.models import Item as ItemModel

class Item(SQLAlchemyObjectType):

    class Meta:
        model = ItemModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_items = SQLAlchemyConnectionField(Item)
