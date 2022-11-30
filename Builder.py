class User():
    def __init__(self, namadepan, namabelakang, umur, agama):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.umur = umur
        self.agama = agama

    def getnamadepan(self):
        return self.namadepan

    def setnamadepan(self, namadepan):
        self.namadepan = namadepan

    def getnamabelakkang(self):
        return self.namabelakang

    def setnamabelakang(self, namabelakang):
        self.namabelakang = namabelakang

    def getumur(self):
        return self.umur

    def setumur(self, umur):
        self.umur = umur

    def getalagama(self):
        return self.agama

    def setagama(self, agama):
        self.agama = agama

    def print(self):
        print("=== User ===")
        print("Nama: ", self.namadepan + " " + self.namabelakang)
        print("umur: ", self.umur)
        print("agama: ", self.agama)

from Builder import User

class UserBuilder():
    def __init__(self):
        self.namadepan = ""
        self.namabelakang = ""
        self.umur = 0
        self.alamat = ""

    @staticmethod
    def item():
        return UserBuilder()

    def withnamadepan(self, nama):
        self.namadepan = nama
        return self

    def withnamabelakang(self, nama):
        self.namabelakang = nama
        return self

    def withumur(self, umur):
        self.umur = umur
        return self

    def liveInagama(self, agama):
        self.agama = agama
        return self

    def build(self):
        return User(self.namadepan,
                    self.namabelakang,
                    self.umur,
                    self.agama)

from Builder import UserBuilder

user = UserBuilder.item().withnamadepan("Destiera").withnamabelakang("Fitryani").withumur(19).liveInagama(
    "Islam").build()
user.print()
