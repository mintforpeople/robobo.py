class Speech:
    def __init__(self, message, recognized, final):
        self.message = message
        self.recognized = recognized
        self.final = final

    def __str__(self):
        return "Speech, message:"+ self.message+", recognized: [" + ", ".join(self.recognized) + "], final:"+str(self.final)
