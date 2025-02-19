class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        #Yazılımcı objelerinin özellikleri
        self.isim = isim
        self.soyisim = soyisim
        self.numara =numara
        self.maaş=maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Yazılımcı objesinin özellikleri 
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
        yazılımcı=Yazılımcı["Süheyla Melike",12345,70000,["Python","Java","C","C++"]]
        yazılımcı.bilgilerigöster()