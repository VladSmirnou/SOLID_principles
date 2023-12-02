# violation for a class:
class TooManyMethods:
    def do_this(self): ...
    def do_that(self): ...
    def do_something_else(self): NestedDependency().do_some()

class MyCode:
    def perform_action(self):
        return TooManyMethods().do_that()
# fix:
class TooManyMethods:
    def do_this(self): ...
    def do_that(self): ...
    def do_something_else(self): NestedDependency().do_some()

class TooManyMethodsAdapterInterface(ABC):
    def do_that(self): ...

class TooManyMethodsAdapterImpl(TooManyMethodsAdapterInterface):
    def do_that(self):
        return TooManyMethods().do_that()

class MyCode:
    too_many_methods: TooManyMethodsAdapterInterface

    def __init__(self, obj: TooManyMethodsAdapterInterface) -> None:
        self.too_many_methods = obj
    
    def perform_action(self):
        self.too_many_methods.do_that()

# violation for an interface:
class HugeInterface(ABC):
    @abstractmethod
    def repair_car(self): ...

    @abstractmethod
    def make_bread(self): ...
    ...

class Baker(HugeInterface):
    def make_bread(self): ...
    def repair_car(self): raise

class Mechanic(HugeInterface): 
    def make_bread(self): raise
    def repair_car(self): ...
# fix:
class MakeBread(ABC):
    @abstractmethod
    def make_bread(self): ...

class RepairMeanOfTransport(ABC):
    @abstractmethod
    def repair_car(self): ...

class Baker(MakeBread):
    def make_bread(self): ...

class Mechanic(RepairMeanOfTransport): 
    def repair_car(self): ...
