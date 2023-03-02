from config import STD_AMT_TESTS


class Test:
    def __init__(self, name, cmd, data, generator=None, amount=STD_AMT_TESTS, condition=lambda _: True):
        self.name = name
        self.cmd = cmd
        self.data = data

        if not generator:
            generator = lambda: None
            # if there is no generator it makes no sense to test more than once
            amount = 1

        self.generator = generator
        self.amount = amount
        self.condition = condition
