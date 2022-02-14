class Effects:
    def __init__(self):
        self.attrs = {}
        self.periods = {}
        self.status = {}

    def toJson(self):
        return {
            "attrs": self.attrs,
            "periods": self.periods,
            "status": self.status
        }

    def fromJson(self, j):
        self.attrs = j["attrs"]
        self.periods = j["periods"]
        self.status = j["status"]
        return self
