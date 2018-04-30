# Inventory/models

from sqlalchemy import types, Column, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class ItemInventoryMap(Base):
    __tablename__ = 'inventory_items'
    inventory_id = Column(types.Integer, ForeignKey('inventory.id'), primary_key=True)
    item_id = Column(types.Integer, ForeignKey('item.id'), primary_key=True)
    item = relationship("Item", back_populates="inventories")
    inventory = relationship("Inventory", back_populates="items")
    quantity = Column(types.Integer)

class Item(Base):
    """
    A basic Inventory Item
    """
    __tablename__ = 'item'
    id = Column(types.Integer, primary_key=True)
    inventories = relationship(
            "ItemInventoryMap",
            )
    name = Column(types.String)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(types.Integer, primary_key=True)

    items = relationship(
            "ItemInventoryMap",
            )
    name = Column(types.String)
