import sqlite3
import random

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

def get_info2():
    res = cur.execute("SELECT name, chat_id, present FROM players")
    return res.fetchall()

def get_from_chat_id(chat_id):
    rees = get_info()
    for i in rees:
        if i[1] == str(chat_id):
            return i
        
def getAllesList(_list, player):
    while True:
        for i, item in enumerate(_list):
            randomint = random.randint(0, 15)
            if randomint == 4 and player != item:
                if (player[1] == "457362997" and item[1] == "498917488") or (player[1] == "498917488" and item[1] == "457362997") or (player[1] == "1003122100" and item[1] == "726623192") or (player[1] == "726623192" and item[1] == "1003122100"):
                    continue
                _list.pop(i)
                return item, _list
    
def distributePlayers():
    rees = list(get_info2())
    rees2 = rees.copy()
    rees_final = []
    for i, item in enumerate(rees):
        playergeschenke, rees2 = getAllesList(rees2, item)
        rees_final.append((item[0], item[1], playergeschenke))

    return rees_final

#distributePlayers()