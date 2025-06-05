import broadway_bot

shows_bway_direct = {
    'aladdin': 2,
    'dbh-nyc': 1,
    'mj-ny': 2,
    'st-nyc': 2,
    'six-ny': 2,
    'the-lion-king': 2,
    'wicked': 1,
}
platforms = {
    'broadway_direct': shows_bway_direct
}

broadway_bot.start_lottery(platforms)
