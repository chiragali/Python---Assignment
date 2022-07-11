from Players import Players
from UpMan import Constany as Cons

com = Players()

players = com.getAllPlayers()
foreign_players = com.getforeignPlayers(players, country=Cons.COUNTRY)
wk_players = com.getWicketKeeperPlayers(players, role=Cons.ROLE)
verify_foreign = com.validateForeignPlayers(foreign_players, maximum_foreign_player=Cons.MAX_FOREIGN_PLAYER)
verify_wk = com.validateWKPlayers(wk_players, minimum_wk_player=Cons.MIN_WK_PLAYER)

if verify_foreign is False:
    assert False
else:
    print(" Only",Cons.MAX_FOREIGN_PLAYER,"Foreign Players are available")
    assert True

if verify_wk is False:
    assert False
else:
    print(" Atleast",Cons.MIN_WK_PLAYER,"Wicket Keeper is availabe")
    assert True

















