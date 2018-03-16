import graphene
import json

with open('default.json') as f:
    items = json.load(f)

class DamageType(graphene.Enum):
    BLUDGEONING = 'Bludgeoning'
    PIERCING = 'Piercing'
    SLASHING = 'Slashing'

class WeaponProperties(graphene.ObjectType):
    finesse = graphene.Boolean()
    thrown = graphene.Boolean()
    light = graphene.Boolean()
    two_handed = graphene.Boolean()

    def resolve_finesse(self, info):
        return self['finesse']

    def resolve_thrown(self, info):
        return self['thrown']

    def resolve_light(self, info):
        return self['light']

    def resolve_two_handed(self, info):
        return self['two-handed']


class Weapon(graphene.ObjectType):
    name = graphene.String()
    cost = graphene.Float(description="Cost in gold pieces")
    damage = graphene.String()
    damage_type = DamageType()
    ranged = graphene.Boolean(description="Whether a weapon is a ranged weapon")
    martial = graphene.Boolean(description="Whether a weapon is martial or not")
    properties = graphene.Field(WeaponProperties, description="Weapon Properties")

    def resolve_damage(self, info):
        return self['damage']

    def resolve_name(self, info):
        return self['name']

    def resolve_properties(self, info):
        return self['properties']

    def resolve_martial(self, info):
        return self['martial']

    def resolve_ranged(self, info):
        return self['ranged']

    def resolve_damage_type(self, info):
        return self['damageType']


class Query(graphene.ObjectType):
    weapon = graphene.Field(Weapon, id=graphene.Int())
    weapons = graphene.List(Weapon)
    test = graphene.String(description='blah')

    def transform_weapon(self, weapon):
        return Weapon(
            name=weapon['name']
        )

    def resolve_weapon(self, info, id):
        return items['weapons'][id]

    def resolve_weapons(self, info):
        return items['weapons']

    def resolve_test(self, info):
        return "Test"

schema = graphene.Schema(query=Query)

query = '''
query getWeaponNames {
    weapons {
        name
        damageType
        damage
        properties {
            finesse
        }
    }
}
'''

result = schema.execute(query)
if result.invalid:
    print(result.errors)
else:
    print (json.dumps(result.data, indent=4))
