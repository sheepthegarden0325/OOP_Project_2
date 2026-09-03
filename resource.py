class Resource:
    """Manage resources which is required for summoning undeads

    Attributes
    ----------
    _next_id : int
    _id : int
    __necrotic_runes : int
    __spirit_runes : int
    __bone_runes : int
    __flesh_runes : int
    __ectoplasm : int

    Methods
    add_quantity()
    """
    __next_id = 1
    __MIN_VALUE = 0

    def __init__(self):
        self._id = Resource.__next_id
        Resource.__next_id += 1
        self.__necrotic_runes = 0
        self.__spirit_runes = 0
        self.__bone_runes = 0
        self.__flesh_runes = 0
        self.__ectoplasms = 0

    def get_necrotic_runes(self):
        return self.__necrotic_runes

    def get_spirit_runes(self):
        return self.__spirit_runes

    def get_bone_runes(self):
        return self.__bone_runes

    def get_flesh_runes(self):
        return self.__flesh_runes

    def get_ectoplasm(self):
        return self.__ectoplasms

    necrotic_ruens = property(get_necrotic_runes)
    spirit = property(get_spirit_runes)
    bone = property(get_bone_runes)
    flesh = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)

    def __str__(self):
        result = f'This inventory has'
        if self.__necrotic_runes > 0:
            result += f'\n{self.__necrotic_runes} necrotic rune(s)'
        if self.__spirit_runes > 0:
            result += f'\n{self.__spirit_runes} spirit rune(s)'
        if self.__bone_runes > 0:
            result += f'\n{self.__bone_runes} bone rune(s)'
        if self.__flesh_runes > 0:
            result += f'\n{self.__flesh_runes} flesh rune(s)'
        if self.__ectoplasms > 0:
            result += f'\n{self.__ectoplasms} ectoplasm(s)'
        result += '.'
        return result

    def __validation(
        self,
        necrotic,
        spirit,
        bone,
        flesh,
        ectoplasm
    ):
        return (
            isinstance(necrotic, int)
            and isinstance(spirit, int)
            and isinstance(bone, int)
            and isinstance(flesh, int)
            and isinstance(ectoplasm, int)
            and necrotic >= 0
            and spirit >= 0
            and bone >= 0
            and flesh >= 0
            and ectoplasm >= 0
        )

    def add_resources(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        """Add quantity of each resource: 
        Necrotic, spirit, bone, flesh, and ectoplasm runes. 

            Parameters
            ---------
            necrotic : int, default 0
                The quantity of necrotic rune to add.
            spirit= : int, default 0
                The quantity of spirit rune to add.
            bone : int, default 0
                The quantity of bone rune to add.
            flesh : int, default 0
                The quantity of flesh rune to add.
            ectoplasm : int, default 0
                The quantity of ectoplasm to add.

            Returns
            -------
            bool
                True if each quantity is successfully added; otherwise False. 
        """
        if self.__validation(necrotic, spirit, bone, flesh, ectoplasm):
            self.__necrotic_runes += necrotic
            self.__spirit_runes += spirit
            self.__bone_runes += bone
            self.__flesh_runes += flesh
            self.__ectoplasms += ectoplasm
            return True

        else:
            return False

    def __check_requiremnts(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        '''Check requried amount of each resource:
        Necrotic, spirit, bone, flesh, and ectoplasm runes. 

        Parameters
        ----------
        necrotic : int, default 0
            The quantity of necrotic rune required.
        spirit= : int, default 0
            The quantity of spirit rune required.
        bone : int, default 0
            The quantity of bone rune required.
        flesh : int, default 0
            The quantity of flesh rune required.
        ectoplasm : int, default 0
            The quantity of ectoplasm required.

        Returns
        -------
        bool 
            True if each resource successfully meets the requirement; otherwise False.
        None
            if wrong arguements are provided
        '''
        if self.__validation(necrotic, spirit, bone, flesh, ectoplasm):
            if (self.__necrotic_runes >= necrotic and
                self.__spirit_runes >= spirit and
                self.__bone_runes >= bone and
                self.__flesh_runes >= flesh and
                    self.__ectoplasms >= ectoplasm):
                return True

            else:
                return False

        else:
            return

    def spend_resources(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        """"""
        if self.__check_requiremnts(
                necrotic,
                spirit,
                bone,
                flesh,
                ectoplasm):
            self.__necrotic_runes -= necrotic
            self.__spirit_runes -= spirit
            self.__bone_runes -= bone
            self.__flesh_runes -= flesh
            self.__ectoplasms -= ectoplasm
