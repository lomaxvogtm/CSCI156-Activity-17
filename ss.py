__author__ = 'Madeleine'

class InvalidSocial:
    pass

class SS:
    class InvalidSocial(ValueError):
        pass

    def __init__(self, ss=None):
        if ss is None:
            self.getsocial()
        else:
            self.ss = ss

    def __str__(self):
        return self.ss

    def validatess(self):
        try:
            area, group, serial = self.ss.split("-")
            if "666" in area:
                raise InvalidSocial
            elif "00" in area or "000" in group or "0000" in serial:
                raise InvalidSocial
            elif len(area) != 3 or len(group) != 2 or len(serial) != 4:
                raise InvalidSocial
            elif "078" in area and "05" in group and "1120" in serial:
                raise InvalidSocial
            int(area)
            int(group)
            int(serial)
        except ValueError:
            raise InvalidSocial

    def getsocial(self):
        self.ss = input("Social: ")
        try:
            self.validatess()
        except InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getsocial()

