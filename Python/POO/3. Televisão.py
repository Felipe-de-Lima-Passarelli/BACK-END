class Televisao:
    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 1
        self.volume_max = 99
        self.canal_min = 1
        self.canal_max = 45
        self.ligada = False

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        else:
            if self.canal < self.canal_max:
                self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        else:
            if self.canal > self.canal_min:
                self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return
        else:
            if self.volume < self.volume_max:
                self.volume += 1

    def diminuir_volume(self):
        if not self.ligada:
            return
        else:
            if self.volume > self.volume_min:
                self.volume -= 1

    def __str__(self) -> str:
        return f'''Ligada: {self.ligada}
Canal: {self.canal}
Volume: {self.volume}'''

tv_1 = Televisao()
print(tv_1)
