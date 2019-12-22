"""
В мире много разных музыкальных групп. Давайте представим на секунду, что вы фанат рок-музыки и хотите написать
программу, которая работает с рок-группами.
Для этого вам нужен класс RockBand с такими атрибутами, как genre ("rock"), members  (пустой массив по дефолту) and
famous_songs (пустой словарь по дефолту: ключ - название песни, значение - кол-во прослушиваний). Создайте такой
класс и экземпляр такого класса, назвав переменную band
Создайте методы класса: n_members (считает количество участников в группе), add_member (добавляет участников в
группу), add_song (добавляет песню и кол-во прослушиваний для нее) и most_popular_song (выводит название наиболее
популярной песни).
Добавьте в музыкальную группу 4-ёх участников и пусть они выпустят 3 песни. Самая популярная будет называться Rock'n'roll
"""


class RockBand:
    genre = "rock"
    members = []
    famous_songs = {}

    def n_members(self):
        return len(self.members)

    def add_member(self, name_of_member):
        self.members.append(name_of_member)

    def add_song(self, name_of_song, num_of_plays):
        self.famous_songs[name_of_song] = num_of_plays

    def most_popular_song(self):
        the_value = -1
        the_key = None
        for key, value in self.famous_songs.items():
            if value > the_value:
                the_value = value
                the_key = key
        return the_key


band = RockBand()
band.add_member("Rick")
band.add_member("Morty")
band.add_member("Kat")
band.add_member("Maxwell")

band.add_song("Song_1", 100)
band.add_song("Song_2", 200)
band.add_song("Rock'n'roll", 1000)

print(band.members)
print(band.n_members())
print(band.most_popular_song())
