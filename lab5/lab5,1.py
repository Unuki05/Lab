class Oyutan:
    def __init__(self, ner, kod):
        self.ner = ner
        self.kod = kod
        self.dunguud = []
        self.hicheeluud = []
    
    def sudalsan_hicheel(self, hicheel, dun):
        self.dunguud.append(dun)
        self.hicheeluud.append(hicheel)
    
    def dunguud_hevleh(self):
        i = 0
        while i < len(self.dunguud):
            print(f"{self.hicheeluud[i]} - {self.dunguud[i]}")
            i += 1
    
    def golch(self):
        if len(self.dunguud) == 0:
            return 0
        return sum(self.dunguud) / len(self.dunguud)

if __name__ == '__main__':
    o = Oyutan('Zorigoo', 'SW19D001')
    o.sudalsan_hicheel('Монгол хэл', 80)
    o.sudalsan_hicheel('Компьютерийн хэрэглээ', 100)
    o.dunguud_hevleh()
    print(o.golch())
