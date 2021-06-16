import re

class Calculator:
    def __init__(self):
        self.reset()
        self.ope_re = re.compile(r'=|+|-|/|*|**')

        self.dict_ope = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.truediv,
            "**":operator.pow
        }

    def reset(self):
        self.state = "num"
        self.memory = None
        self.in_mem = None
        self.operand = None

    def input(self,callback):
        if self.state = "num":
            if type(callback) is int:
                if self.in_mem is None:
                    self.in_mem = callback
                else:
                    self.in_mem = self.in_mem*10 + callback
            elif self.ope_re.match(callback) is not None:
                if callback == '=':
                    #aaa


        elif self.state = "ope":
            pass
        elif self.state = "result":
            pass

    def calc(self):
        if self.memory is None or self.in_mem is None or self.operand is None:
            print("can't calculation.")
            return
        else:
            if self.operand == "+":
                result = self.dict_ope[self.operand](self.memory,self.in_mem)
