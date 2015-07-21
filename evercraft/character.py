class Character:
    # **kwargs => is an empty dictionary to set key and value arguments
    def __init__(self, in_name, in_alignment="evil", **kwargs):
        self.name = in_name
        self.alignment = in_alignment

    def __get_alignment(self):
        return self.__alignment

    def __set_alignment(self, in_alignment):
        if in_alignment not in ["good", "evil", "neutral"]:
            raise ValueError("Value has to be good, evil or neutral")

        self.__alignment = in_alignment

    alignment = property(__get_alignment, __set_alignment)
