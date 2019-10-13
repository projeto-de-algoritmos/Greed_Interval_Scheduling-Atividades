class atividade:
    def __init__(self, comeco, final):
        self.comeco = bool
        self.final = bool
    def __str__(self):
        return self.comeco 
        return self.final

    def comparar(self, s1, s2):
        return s1.final < s2.final
    def comparar2(self, s1, s2):
        return s1.comeco < s2.comeco
    def comparar3(self, s1, s2):
        return (s1.final - s1.comeco) < (s1.final - s2.comeco)