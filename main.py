from Players import Players

com = Players()

players = com.getAllPlayers()
foreign_players = com.getforeignPlayers(players, country="India")
wk_players = com.getWicketKeeperPlayers(players, role='Wicket-keeper')
verify_foreign = com.validateForeignPlayers(foreign_players, maximum_foreign_player=4)
verify_wk = com.validateWKPlayers(wk_players, minimum_wk_player=1)

if verify_foreign is False:
    assert False
else:
    print(" Only 4 Foreign Players are available")
    assert True

if verify_wk is False:
    assert False
else:
    print(" Atleast one Wicket Keeper is availabe")
    assert True

















