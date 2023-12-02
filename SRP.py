# violation for a function:
def calculate_format_present():
    calculate = 1 + 4
    format_ = 'the' + 'result' + 'is' + '%d'
    print(format_ % calculate)
# fix:
def calculate():
    return 1 + 4

def format_():
    return 'the' + 'result' + 'is' + '%d'

def present(templ, result):
    print(templ % result)

def main():
    result = calculate()
    templ = format_()
    present(templ, result)

# violation for a class:
class DoThisDoThat:
    def do_this_for_group1(self): ...

    def do_that_for_group2(self): ...
# fix:
class DoThis: 
    def do_this_for_group1(self): ...

class DoThat:
    def do_that_for_group2(self): ...
