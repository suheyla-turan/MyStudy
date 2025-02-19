#__init__n class'a eklme yapar
class Araba():
    def __init__(self,model,renk,beygir_gücü,silindir):
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir
        print(model,renk,beygir_gücü,silindir,sep="\n")
araba1=Araba("Renault Megane","Gümüş",110,4)