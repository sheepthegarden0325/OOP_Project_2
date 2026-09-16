from undead import Undead


class WorriorUndead(Undead):

    def __init__(self, id, health, power, name=''):
        super().__init__(id, health, power, name)

    def command(self):
        effect = (
            f'{self.name} clashes its sword against its shield'
            'with a terrifying sound.'
        )

        behaviour = super().command()

        return f'{effect}\n{behaviour}'
