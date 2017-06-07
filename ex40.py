class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to ge sued",
                    "So i'll stop right there"])

happy_bday.sing_me_a_song()

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

bulls_on_parade.sing_me_a_song()

horra = Song(["Aho, aho, copii si frati",
                "Stati putin si nu minati",
                "Pe linga noi va alaturati",
                "Si cuvintul mi'l ascultati!"])
horra.sing_me_a_song()

hora2 = ["Vine iarna",
            "Toamna trece!"]

hora3 = Song(hora2)

hora3.sing_me_a_song()
