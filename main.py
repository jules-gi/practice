import itertools


class Player:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f'{self.name} ({self.position})'


class Lineup(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def filter(self, position):
        """
        Filter players of the lineup given their position.

        :param position: Position of the players to return
        :type position: str

        :return: A list of filtered players
        """
        return [player for player in self if player.position == position]

    def get_all_formations(self, tactical_formation):
        """
        :param tactical_formation: The number of players per position
        in the order Defender-Midfielder-Striker.
        (Example: '442' means 4 defenders, 4 midfielders, 2 strikers)
        :type tactical_formation: str

        :return: The list of all possible combinations.
        """

        n_def, n_mid, n_st = map(int, tactical_formation)
        combinations_per_position = [
            list(itertools.combinations(self.filter('Goalkeeper'), 1)),
            list(itertools.combinations(self.filter('Defender'), n_def)),
            list(itertools.combinations(self.filter('Midfielder'), n_mid)),
            list(itertools.combinations(self.filter('Striker'), n_st)),
        ]

        lineups = list(itertools.product(*combinations_per_position))
        for i in range(len(lineups)):
            lineups[i] = list(itertools.chain(*lineups[i]))

        return lineups


if __name__ == '__main__':
    from random import randint, seed

    lineup = Lineup([
        Player(name='Steve Mandanda', position='Goalkeeper'),
        Player(name='Yohann Pele', position='Goalkeeper'),
        Player(name='Hiroki Sakai', position='Defender'),
        Player(name='Alvaro Gonzalez', position='Defender'),
        Player(name='Boubacar Kamara', position='Defender'),
        Player(name='Duje Caleta-Car', position='Defender'),
        Player(name='Jordan Amavi', position='Defender'),
        Player(name='Michael Cuisance', position='Midfielder'),
        Player(name='Pape Gueye', position='Midfielder'),
        Player(name='Valentin Rongier', position='Midfielder'),
        Player(name='Florian Thauvin', position='Midfielder'),
        Player(name='Dimitri Payet', position='Midfielder'),
        Player(name='Valere Germina', position='Striker'),
        Player(name='Arkadiusz Milik', position='Striker'),
        Player(name='Dario Benedetto', position='Striker'),
    ])

    tactical_formations = {
        '442': lineup.get_all_formations('442'),
        '433': lineup.get_all_formations('433'),
        '541': lineup.get_all_formations('541'),
        '532': lineup.get_all_formations('532'),
        '352': lineup.get_all_formations('352'),
        '343': lineup.get_all_formations('343'),
    }

    seed(16)
    for name, lineups in tactical_formations.items():
        n = randint(0, len(lineups))
        print(f'One example of {name} formation among '
              f'{len(lineups)} possibilities: {lineups[n]} \n')
