import numpy as np
import pytest


class Cricket:
    def __init__(self, name_of_the_team: str, points: int, last_five_games: list[str]):
        """Construct Team Status object

        """
        self._name_of_the_team = name_of_the_team
        self._points = points
        self._last_five_games = last_five_games

    @property
    def name_of_the_team(self):
        """ to get the name of the team

        :return: str
        """
        return self._name_of_the_team

    @name_of_the_team.setter
    def name_of_the_team(self, value):
        """ to set value to the name of the team

        :return: None
        """
        self._name_of_the_team = value

    @property
    def points(self):
        """ to get the points

        :return: int
        """
        return self._points

    @points.setter
    def points(self, value):
        """ to set value to the points

        :return: None
        """
        self._points = value

    @property
    def last_five_games(self):
        """ to get the last five games

        :return: tuple of str
        """
        return tuple(self._last_five_games)

    @last_five_games.setter
    def last_five_games(self, value):
        """ to set value to the points

        :return: None
        """
        self._last_five_games = value

    def get_consecutive_status(self, consecutive_number=2, status_type='l'):
        for number in range(len(self._last_five_games) - consecutive_number):
            status = ''.join(self._last_five_games[number: number + consecutive_number]).lower()
            if status_type.lower() * consecutive_number == status:
                return True
        return False


def get_average_points_of_teams(list_of_teams: list[Cricket]):
    return np.mean([team.points for team in list_of_teams])


team1 = Cricket("team1", 20, ["w", "l", "l", "l", "w"])
team2 = Cricket("team2", 29, ["w", "l", "w", "l", "w"])
team3 = Cricket("team3", 15, ["w", "l", "w", "w", "w"])
team4 = Cricket("team4", 40, ["l", "l", "w", "l", "w"])
team5 = Cricket("team5", 9, ["l", "l", "l", "l", "w"])

l = [team1, team2, team3, team4, team5]


@pytest.mark.parametrize("team,status", [(team1, True), (team2, False), (team3, False), (team4, True), (team5, True)])
def test_consecutive_status(team, status):
    assert team.get_consecutive_status() == status
