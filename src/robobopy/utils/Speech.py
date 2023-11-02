class Speech:
    def __init__(self, message, final):
        self.message = message
        self.final = final

    def __str__(self):
        return "Speech, message:"+ self.message+", final:"+str(self.final)
