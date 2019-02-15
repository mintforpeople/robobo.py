

class Note:
    """
    Represents a note detected:
        * Name: (string) The musical note in text format, according to the English nomenclature, that is:

            +----+-----+----+-----+----+----+-----+-----+------+----+-----+----+
            | DO | DO# | RE | RE# | MI | FA | FA# | SOL | SOL# | LA | LA# | SI |
            +----+-----+----+-----+----+----+-----+-----+------+----+-----+----+
            | C  | Cs  | D  |  Ds | E  | F  | Fs  |  G  |  Gs  | A  |  As | B  |
            +----+-----+----+-----+----+----+-----+-----+------+----+-----+----+

        * Duration: (int) The note's duration in milliseconds
    """
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return "Note, name:"+ self.name+", duration:"+str(self.duration)
