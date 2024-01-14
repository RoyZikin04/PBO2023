# Fahrenheit
class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_FCelcius(self):
        val = (32 - float(self.suhu)) * 5/9
        return val

    def get_Freamur(self):
        val = (32 - float(self.suhu)) * 4/9
        return val

    def get_Fkelvin(self):
        val = (32 - float(self.suhu)) * 5/9 + 273
        return val


# Reamur
class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_Rcelcius(self):
        val = float(self.suhu) * 5/4
        return val

    def get_Rfahrenheit(self):
        val = (float(self.suhu) * 9/4) + 32
        return val

    def get_Rkelvin(self):
        val = (float(self.suhu) * 5/4) + 273
        return val


# Kelvin
class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_KCelcius(self):
        val = float(self.suhu) - 273
        return val

    def get_Kreamur(self):
        val = 4/5 * (float(self.suhu) - 273)
        return val

    def get_Kfahrenheit(self):
        val = 9/5 * (float(self.suhu) - 273) + 32
        return val
