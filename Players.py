import json
from UpMan import Constany as Cons


class Players:

    def getforeignPlayers(self, players, country):
        foreign_players = []
        for player in players:
            if player.get("country") not in country:
                foreign_players.append(player.get("name"))
        return foreign_players

    def getWicketKeeperPlayers(self, players, role):
        wk_players = []
        for player in players:
            if player.get("role") in role:
                wk_players.append(player.get("name"))
        return wk_players

    def getAllPlayers(self):
        with open(Cons.TEAM_INPUT) as f:
            data = json.load(f)
        players = data.get("player")
        return players

    def validateForeignPlayers(self, foreign_players, maximum_foreign_player):

        flag = True
        if len(foreign_players)>maximum_foreign_player:
            flag = False
            return flag

    def validateWKPlayers(self, wk_players, minimum_wk_player):
        flag = True
        if len(wk_players) < minimum_wk_player:
            flag = False
            return flag

