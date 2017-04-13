from sortedcontainers import SortedListWithKey

class Leaderboard:
    def __init__(self, title, options, keys, key):
        self.title = title
        self.options = options
        self.keys = keys
        self.orderedEntries = SortedListWithKey(key=key)

    def add_entry(self, leaderboardEntry):
        if (len(self.keys) != len(leaderboardEntry.data)):
            print("Keys and data length do not match, unable to add entry.")
            return -1
        self.orderedEntries.add(leaderboardEntry)

    def __str__(self):
        string = "{}\n-{}, {}-".format(leaderboard.title, leaderboard.keys, leaderboard.options["valueLabel"])
        for entry in leaderboard.orderedEntries:
            string = "{}\n{}, {}".format(string, entry.data, entry.value)
        return string

class LeaderboardEntry:
    def __init__(self, data, value):
        self.data = data
        self.value = value

if __name__=="__main__":
    title = "Pacman high scores"
    keys = ["Name", "Version"]
    options = {"valueLabel": "Score"}
    key = lambda a: a.value
    leaderboard = Leaderboard(title, options, keys, key)

    entries = []
    entries.append(LeaderboardEntry(["Robert", "Pacman"], 150))
    entries.append(LeaderboardEntry(["Max", "Ms. Pacman"], 180))
    entries.append(LeaderboardEntry(["Jiwan", "Pacman and Friends"], 120))

    for entry in entries:
        leaderboard.add_entry(entry)

    print(leaderboard)
