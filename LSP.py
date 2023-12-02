# violation:
class Bird:
    def fly(self): ...
    def walk(self): ...

class Seagul(Bird):
    def scream(self): ...

class Penguin(Bird):
    def run(self): ...
    def fly(self): raise

def make_bird_fly(obj: Bird): 
    obj.fly()

# "If for each object o1 of type S(Penguin) there is an object o2
# of type T(Bird) such that for all programs P(make_bird_fly) 
# defined in terms of T, the behaviour of P is unchanged when o1 is substituted
# for o2 then S is a subtype of T."

# fix:
class FlyingWalkingBird:
    def fly(self): ...
    def walk(self): ...

class WalkingBird:
    def walk(self): ...

class Seagul(FlyingWalkingBird):
    def scream(self): ...

class Penguin(WalkingBird):
    def run(self): ...

def make_bird_fly(obj: FlyingWalkingBird): 
    obj.fly()
