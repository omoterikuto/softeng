class TelephoneNumber:
    _area_code: str
    _number: str
    def __init__(self, area_code: str, number: str):
        self._area_code = area_code
        self._number = number
    
    @property
    def area_code(self) -> str:
        return self._area_code
    
    @property
    def number(self) -> str:
        return self._number
  
    @area_code.setter
    def area_code(self, area_code):
        self._area_code = area_code
  
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def telephone_number(self):
        return self._area_code + "-" + self._number