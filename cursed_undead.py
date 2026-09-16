from undead import Undead


class CursedUndead(Undead):

    def __init__(self, id, health, power, name=''):
        super().__init__(id, health, power, name)

    def command(self):
        effect = (
            f'{self.name} lets out a horryfying scream'
            'while releasing a foul stench.'
        )

        behaviour = super().command()

        return f'{effect}\n{behaviour}'
