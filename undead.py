class Undead:
    ''''''
    __INITIAL_LEVEL = 1
    __MAXIMUM_HEALTH = None
    __MINIMUM_HEALTH = None
    __MAXIMUM_POWER = None
    __MINIMUM_POWER = None
    __MAXIMUM_LEVEL = None
    __HEALTH_GAINED_PER_LEVEL = None
    __POWER_GAINED_PER_LEVEL = None

    def __init__(self):
        self.__id
        self.__name
        self.__health
        self.__power
        self.__level = Undead.__initial_level

# -------
# GETTERS
# -------

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

    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
