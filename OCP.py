# violation for a function:
def do_some(obj):
    isinstance(obj, ...) and obj.do_this() or
    isinstance(obj, ...) and obj.do_that()
    ...
# fix:
def do_some(obj: CommonInterface):
    obj.perform_action()

# violation for a class:
class StrConverter:
    def str_to_int(self): ...
    def str_to_float(self): ...
    ...
# fix:
from abc import ABC, abstractmethod

class StrConverter(ABC):
    def convert(self):
        return self.perform_conversion()

    @abstractmethod
    def perform_conversion(self): ...

class StrToInt(StrConverter):
    def perform_conversion(self): ...

class StrToFloat(StrConverter):
    def perform_conversion(self): ...
