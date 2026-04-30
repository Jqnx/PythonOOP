from abc import ABC, abstractmethod
import subprocess
import platform
from urllib.parse import urlparse


class Check(ABC):
    @abstractmethod
    def execute(self) -> bool:
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

    def execute(self) -> bool:
        param = "-n" if platform.system().title == "windows" else "-c"
        command = ["ping", param, "4", self.target]

        try:
            subprocess.check_output(command)
            return True
        except subprocess.CalledProcessError:
            return False


class HTTPCheck(Check):
    type_name = "http"

    def __init__(self, target):
        try:
            result = urlparse(target)
            if result:
                self.target = target
        except ValueError as e:
            raise e

    # TODO: Implement HTTPCheck execute()
    def execute(self) -> bool:
        return False
