class Undead:
    ''''''
    # TODO distribute those special constants to specific undeads when a relevant instruction is provided.
    __INITIAL_LEVEL = 1
    __MAX_HEALTH = 100
    __MIN_HEALTH = 5
    __MAX_POWER = 100
    __MIN_POWER = 5
    __MAX_LEVEL = 100
    __HEALTH_GAINED_PER_LEVEL = 5
    __POWER_GAINED_PER_LEVEL = 5

    def __init__(self, id, health, power, name=''):
        self.__id = id

        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = f'Undead_{self.__id}'

        if isinstance(health, int):
            if health < Undead.__MIN_HEALTH:
                self.__health = Undead.__MIN_HEALTH
            elif health > Undead.__MAX_HEALTH:
                self.__health = Undead.__MAX_HEALTH
            else:
                self.__health = health
        else:
            self.__health = Undead.__MIN_HEALTH

        if isinstance(power, int):
            if power < Undead.__MIN_POWER:
                self.__power = Undead.__MIN_POWER
            elif power > Undead.__MAX_POWER:
                self.__power = Undead.__MAX_POWER
            else:
                self.__power = power
        else:
            self.__power = Undead.__MIN_POWER

        self.__level = Undead.__INITIAL_LEVEL

    # -----------------
    # String conversion
    # -----------------

    def __str__(self):
        return (
            f'{self.__name}\n'
            f'LV. {self.__level}\n'
            f'HP. {self.__health}/{Undead.__MAX_HEALTH}\n'
            f'STR. {self.__power}/{Undead.__MAX_POWER}'
        )

    def __repr__(self):
        return (
            f'id: {self.__id}, '
            f'name: {self.__name}, '
            f'level: {self.__level}, '
            f'health: {self.__health}, '
            f'power: {self.__power}.'
        )
    # -------
    # GETTERS
    # -------

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level

    # ----------
    # PROPERTIES
    # ----------

    id = property(get_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    # ---------
    # Methods
    # ---------

    def level_up(self):
        '''Increases an undead's level by 1. 
        Also, raises its health and power by invoking helper methods.

        Parameter
        ---------
        None

        Return
        ------
        bool
            True if the level successfully increases; otherwise False.
        '''

        if self.__level >= Undead.__MAX_LEVEL:
            return False

        self.__level += 1
        self.__health_up()
        self.__power_up()
        return True

    def __health_up(self):
        '''Increases an undead's health by __HEALTH_GAINED_PER_LEVEL 
        until __MAX_HEALTH. 

        Parameter
        ---------
        None

        Return
        ------
        bool
            True if the health successfully increases; otherwise False.
        '''

        self.__health += Undead.__HEALTH_GAINED_PER_LEVEL
        if self.__health > Undead.__MAX_HEALTH:
            self.__health = Undead.__MAX_HEALTH

    def __power_up(self):
        '''Increases an undead's power by __POWER_GAINED_PER_LEVEL 
        until __MAX_POWER. 

        Parameter
        ---------
        None

        Return
        ------
        bool
            True if the power successfully increases; otherwise False.
        '''

        self.__power += Undead.__POWER_GAINED_PER_LEVEL
        if self.__power > Undead.__MAX_POWER:
            self.__power = Undead.__MAX_POWER

    def command(self):
        # TODO define what the behaviour parameter type will be and put relevant validatoin.
        return f'{self}\n follows your command'
