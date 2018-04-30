import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from inventory.models import (Item as ItemModel,
                              Inventory as InventoryModel,
                              ItemInventoryMap as ItemInventoryMapModel)
from database import db_session

class Item(SQLAlchemyObjectType):

    class Meta:
        model = ItemModel
        interfaces = (relay.Node, )

class QuantifiedItem(SQLAlchemyObjectType):

    class Meta:
        model = ItemInventoryMapModel
        only_fields = ('item', 'quantity')

class Inventory(SQLAlchemyObjectType):

    class Meta:
        model = InventoryModel

class Query(graphene.ObjectType):
    all_items = SQLAlchemyConnectionField(Item)
    inventory = graphene.Field(Inventory)

    def resolve_inventory(self, info):
        return db_session.query(InventoryModel).first()
