from resource_pool import ResourcePool
from summoning_ritual import SummoningRitual


class Necromancer:
    __MAX_UNDEADS = 10

    def __init__(self, name):
        self.__summon_id = 0
        self.__name = name
        self.__resource = ResourcePool()
        self.__undeads = []

    def get_summon_id(self):
        return self.__summon_id

    def get_name(self):
        return self.__name

    summon_id = property(get_summon_id)
    name = property(get_name)

    def add_resources(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        return self.__resource.add_resources(
            necrotic,
            spirit,
            bone,
            flesh,
            ectoplasm
        )
        # True || False, validation is performed by ResourcePool

    def summon(self, summoning_ritual):
        if not (
            isinstance(summoning_ritual, SummoningRitual)
            and len(self.__undeads) < Necromancer.__MAX_UNDEADS
        ):
            return False

        if summoning_ritual.require(self.__resource):
            summoning_ritual.consume(self.__resource)
            self.__undeads.append(
                summoning_ritual.create_undead(
                    self.__summon_id
                )
            )
            self.__summon_id += 1
            return True

        else:
            return False

    def __find_undead(self, id):
        for undead in self.__undeads:
            if undead.id == id:
                return undead

    def dismiss(self, id):
        undead = self.__find_undead(id)

        if undead:
            self.__undeads.remove(undead)
            return True

        else:
            return False

    def level_undead(self, id):
        undead = self.__find_undead(id)

        if undead is None:
            return False

        undead.level_up()
