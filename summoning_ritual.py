from resource_pool import ResourcePool
from undead import Undead


class SummoningRitual:
    '''
    '''

    def __init__(
            self,
            name,
            undead_class,
            undead_name,
            health,
            power,
            necrotic=0,
            spirit=0,
            bone=0,
            flesh=0,
            ectoplasm=0):

        if (
            not isinstance(name, str)
            or not issubclass(undead_class, Undead)
            or not isinstance(undead_name, str)
            or not isinstance(health, int)
            or health < 0
            or not isinstance(power, int)
            or power < 0
            or not isinstance(necrotic, int)
            or necrotic < 0
            or not isinstance(spirit, int)
            or spirit < 0
            or not isinstance(bone, int)
            or bone < 0
            or not isinstance(flesh, int)
            or flesh < 0
            or not isinstance(ectoplasm, int)
            or ectoplasm <= 0
        ):
            self.__requirements = [0, 0, 0, 0, 0]
            self.__name = None
            self.__undead_class = Undead
            self.__undead_name = None
            self.__health = None
            self.__power = None
            self.__is_valid = False
        else:
            self.__requirements = [necrotic, spirit, bone, flesh, ectoplasm]
            self.__name = name
            self.__undead_class = undead_class
            self.__undead_name = undead_name
            self.__health = health
            self.__power = power
            self.__is_valid = True

    # TODO Add string conversion, docstrings, getters, and read-only properties.

    # -----------------
    # String conversion
    # -----------------

    def __str__(self):
        runes = ['necrotic', 'sprit', 'bone', 'flesh']
        result = f'{self.name} ritual for summoning {self.__undead_name}\n'
        result += f'Requirements:\n'
        for n in range(len(runes)):
            if self.__requirements[n] > 0:
                result += f'{self.__requirements[n]} {runes[n]} rune(s)\n'
        result += f'{self.__requirements[4]} ectoplasm(s)'
        return result

    def __repr__(self):
        return (
            f'name: {self.__name}\n'
            f'undead_name: {self.__undead_name}\n'
            f'requirements: {self.__requirements}'
            f'health: {self.__health}\n'
            f'power: {self.__power}\n'
            f'is_valid: {self.__is_valid}'
        )

    # -------
    # Getters
    # -------

    def get_name(self):
        return self.__name

    def get_undead_name(self):
        return self.__undead_name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def require(self, resource):
        '''Check whether present resource is 
        possible to perform the ritual 
        by invoking ResourcePool's checking method.

        Parameter
        ---------
        resource : ResourcePool
            an instance of ResourcePool to inspect

        Return
        ------
        bool
            True if the resource instance meets the requirement;
            False if the calling requirement is not valid 
            or the instance does not meet the requirements.
        None
            if a wrong argument is given in the resource method.
        '''
        if not self.__is_valid:
            return False

        if isinstance(resource, ResourcePool):
            return resource.check_requirements(
                self.__requirements[0],
                self.__requirements[1],
                self.__requirements[2],
                self.__requirements[3],
                self.__requirements[4]
            )

    def consume(self, resource):
        '''Consume required resources in the given resource 
        by invoking ResourcePool's spending method.

        Parameter
        ---------
        resource : ResourcePool
            an instance of ResourcePool to spend

        Return
        ------
        bool
            True if the resource instance meets the requirement;
            False if the calling requirement is not valid 
            or the instance does not meet the requirements.
        '''
        if not self.__is_valid:
            return False

        if isinstance(resource, ResourcePool):
            return resource.spend(
                self.__requirements[0],
                self.__requirements[1],
                self.__requirements[2],
                self.__requirements[3],
                self.__requirements[4]
            )
        else:
            return False

    def create_summon(self, id):
        '''Create an undead

        Parameter
        ---------
        id : int
            id for the undead

        Return
        ------
        bool
            False if the calling ritual is invalid
        Undead
            An Undead or its sublcass instance created
        '''
        if not (
            self.__is_valid
            and isinstance(id, int)
        ):
            return False

        return self.__undead_class(
            id,
            self.__health,
            self.__power,
            self.__undead_name
        )
