class ResourcePool:
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
        self.__id = ResourcePool.__next_id
        ResourcePool.__next_id += 1
        self.__necrotic = ResourcePool.__MIN_VALUE
        self.__spirit = ResourcePool.__MIN_VALUE
        self.__bone = ResourcePool.__MIN_VALUE
        self.__flesh = ResourcePool.__MIN_VALUE
        self.__ectoplasms = ResourcePool.__MIN_VALUE

    # ---------
    # Getters
    # ---------

    def get_necrotic_runes(self):
        return self.__necrotic

    def get_spirit_runes(self):
        return self.__spirit

    def get_bone_runes(self):
        return self.__bone

    def get_flesh_runes(self):
        return self.__flesh

    def get_ectoplasm(self):
        return self.__ectoplasms

    # ----------
    # Properties
    # ----------

    necrotic = property(get_necrotic_runes)
    spirit = property(get_spirit_runes)
    bone = property(get_bone_runes)
    flesh = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)

    def __str__(self):
        result = f'This inventory has'
        if self.__necrotic > ResourcePool.__MIN_VALUE:
            result += f'\n{self.__necrotic} necrotic rune(s)'
        if self.__spirit > ResourcePool.__MIN_VALUE:
            result += f'\n{self.__spirit} spirit rune(s)'
        if self.__bone > ResourcePool.__MIN_VALUE:
            result += f'\n{self.__bone} bone rune(s)'
        if self.__flesh > ResourcePool.__MIN_VALUE:
            result += f'\n{self.__flesh} flesh rune(s)'
        if self.__ectoplasms > ResourcePool.__MIN_VALUE:
            result += f'\n{self.__ectoplasms} ectoplasm(s)'
        result += '.'
        return result

    def __repr__(self):
        return (
            f'id: {self.__id},'
            f'necrotic: {self.__necrotic}, '
            f'spirit: {self.__spirit}, '
            f'bone: {self.__bone}, '
            f'flesh: {self.__flesh}, '
            f'ectoplasms: {self.__ectoplasms}.'
        )

    def __validation(
        self,
        necrotic,
        spirit,
        bone,
        flesh,
        ectoplasm
    ):
        '''validate whether given resource arguments are >= __MIN_VALUE and int type.

        Parameters
        ---------
        necrotic : int
            The quantity of necrotic rune to check.
        spirit= : int
            The quantity of spirit rune to check.
        bone : int
            The quantity of bone rune to check.
        flesh : int
            The quantity of flesh rune to check.
        ectoplasm : int
            The quantity of ectoplasm to check.    

        Returns
        -------
        bool
            True if every arguements are >= and int type; otherwise False.
        '''

        return (
            isinstance(necrotic, int)
            and isinstance(spirit, int)
            and isinstance(bone, int)
            and isinstance(flesh, int)
            and isinstance(ectoplasm, int)
            and necrotic >= ResourcePool.__MIN_VALUE
            and spirit >= ResourcePool.__MIN_VALUE
            and bone >= ResourcePool.__MIN_VALUE
            and flesh >= ResourcePool.__MIN_VALUE
            and ectoplasm >= ResourcePool.__MIN_VALUE
        )

    def add_resources(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        """Add each resource by given quantity: 
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
            self.__necrotic += necrotic
            self.__spirit += spirit
            self.__bone += bone
            self.__flesh += flesh
            self.__ectoplasms += ectoplasm
            return True

        else:
            return False

    def check_requirements(
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
        spirit : int, default 0
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
            True if the quantity of each resource successfully meets the requirement; 
            otherwise False.
        None
            if wrong arguements are provided
        '''
        if self.__validation(necrotic, spirit, bone, flesh, ectoplasm):
            if (self.__necrotic >= necrotic and
                self.__spirit >= spirit and
                self.__bone >= bone and
                self.__flesh >= flesh and
                    self.__ectoplasms >= ectoplasm):
                return True

            else:
                return False

        else:
            return

    def spend(
        self,
        necrotic=0,
        spirit=0,
        bone=0,
        flesh=0,
        ectoplasm=0
    ):
        '''Spend each resource by given quantities, 
        while preventing any resource falling below 0. 

        Parameters
        ----------
        necrotic : int, default 0
            The quantity of necrotic rune will be spent.
        spirit : int, default 0
            The quantity of spirit rune will be spent.
        bone : int, default 0
            The quantity of bone will be spent.
        flesh : int, default 0
            The quantity of flesh will be spent.
        ectoplasm : int, default 0
            The quantity of ectoplasm will be spent.

        Returns
        -------
        bool 
            True if nothing falling below zero; otherwise False.
        '''

        if self.check_requirements(
                necrotic,
                spirit,
                bone,
                flesh,
                ectoplasm):
            self.__necrotic -= necrotic
            self.__spirit -= spirit
            self.__bone -= bone
            self.__flesh -= flesh
            self.__ectoplasms -= ectoplasm
            return True

        else:
            return False
