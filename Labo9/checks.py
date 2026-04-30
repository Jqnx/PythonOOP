from abc import ABC, abstractmethod


class Check(ABC):
    @abstractmethod
    def execute(self):
        pass

    @classmethod
    def create_check(cls, check_type, target):
        for check in cls.__subclasses__():
            if check.type_name == check_type:
                return check(target)
        raise ValueError(f"Onbekend check type: {check_type}")


# TODO: Do some checks on target.
class PingCheck(Check):
    type_name = "ping"

    def __init__(self, target):
        self.target = target

    def execute(self):
        pass


class HTTPCheck(Check):
    type_name = "http"

    def __init__(self, target):
        self.target = target

    def execute(self):
        pass
