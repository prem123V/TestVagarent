import numpy as np
import pytest

from Source.Cricket import Cricket

team1 = Cricket("team1", 20, ["w", "l", "l", "l", "w"])
team2 = Cricket("team2", 29, ["w", "l", "w", "l", "w"])
team3 = Cricket("team3", 15, ["w", "l", "w", "w", "w"])
team4 = Cricket("team4", 40, ["l", "l", "w", "l", "w"])
team5 = Cricket("team5", 9, ["l", "l", "l", "l", "w"])

l = [team1, team2, team3, team4, team5]


@pytest.mark.parametrize("team,status", [(team1, True), (team2, False), (team3, False), (team4, True), (team5, True)])
def test_consecutive_status(team, status):
    assert team.get_consecutive_status() == status
