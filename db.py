import sqlite3

con = sqlite3.connect("players.sqlite")

cur = con.cursor()
#cur.execute("DROP TABLE players")
#cur.execute("CREATE TABLE players(name, chat_id, present, player_present)")

def clearBD():
    cur.execute("DROP TABLE players")
    cur.execute("CREATE TABLE players(name, chat_id, present, player_present)")

if __name__ == "__main__":
    pass#clearBD()

def add_player(name, chat_id, present):
    inf = get_from_chat_id(chat_id)
    if inf:
        cur.execute(f"UPDATE players SET present = ?, name = ? WHERE chat_id = ?", [present, name, str(chat_id)])
        con.commit()
        return "update"
    else:
        cur.execute(f"INSERT INTO players VALUES (?, ?, ?, '')", [name, str(chat_id), present])
        con.commit()
        return "new"

def get_info():
    res = cur.execute("SELECT * FROM players")
    return res.fetchall()

def get_from_chat_id(chat_id):
    rees = get_info()
    for i in rees:
        if i[1] == str(chat_id):
            return i


#add_player("ANDRII", "666666", "rg4rgergergrtrthrth")
#print(get_from_chat_id("666666"))