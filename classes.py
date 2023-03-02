from config import STD_AMT_TESTS


class Test:
    def __init__(self, name, cmd, data, generator, amount=STD_AMT_TESTS, condition=lambda _: True):
        self.name = name
        self.cmd = cmd
        self.data = data
        self.generator = generator
        self.amount = amount
        self.condition = condition
