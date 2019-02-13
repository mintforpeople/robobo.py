

class Note:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return "Note, name:"+ self.name+", duration:"+str(self.duration)
