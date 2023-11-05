def get(file, col, cond=''):
    """Gets a column from the specified csv file.
    Data is stored as player_id,nickname,tribe,vote
    If the player has not voted, vote equals "nobody"
    If cond is set, it will only return the specified column if cond is in
    any column."""
    with open(file) as f:
        col -= 1
        if cond:
            for line in f:
                data = line.strip().split(',')
                if cond in data:
                    return data[col]
        else:
            data = [line.strip().split(',')[col] for line in f]
            return data


def write(file, data, delete=False):
    """Writes a row to the specified csv file.
    Data is stored as player_id,nickname,tribe,vote
    Line to be written is passed as a list ([player_id, nickname, vote])
    If the player has not voted, vote equals "nobody"
    If delete is True, it will instead delete the row with the passed data"""
    new = ''
    with open(file) as f:
        for line in f:
            if data[0] not in line:
                new += line
        if not delete:
            new += ','.join(data) + '\n'
    with open(file, 'w') as f:
        f.write(new)


def exists(file, item):
    """Returns true if an item is in a file"""
    exist = get(file, 1, item)
    if exist:
        return True
    return False


def voted(voter):
    """Checks if player has already voted
    voter is the player's Discord id"""
    vote = get("players.csv", 4, voter)
    if vote != 'nobody':
        return True
    return False


def same(player, vote):
    """Checks to see if the vote is the same
    player is the player's Discord id
    vote is the nickname of the person they have voted"""
    who = get("players.csv", 4, player)
    if vote == who:
        return True
    return False


def get_players():
    """Return a list of all players"""
    ids = get("players.csv", 1)
    players = [Player(id) for id in ids]
    return players


def get_idols():
    players = get_players()
    idols = []
    for player in players:
        if get("idols.csv", 2, player.nick) == "yes":
            idols.append(player.nick)
    return idols
