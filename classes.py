from config import STD_AMT_TESTS


class Test:
    def __init__(self, name: str, cmd, data: str):
        self.name = name
        self.cmd = cmd
        self.data = data


class MultiTest(Test):
    def __init__(self, name: str, cmd, data: str, generator, amount: int = STD_AMT_TESTS,
                 condition=lambda _: True):

        super().__init__(name, cmd, data)

        self.generator = generator
        self.amount = amount
        self.condition = condition
