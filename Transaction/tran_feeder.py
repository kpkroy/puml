from a_LocalConfig.log_handler import LogHandler
from Transaction.adapted_tran import AdaptedTran
from abc import abstractmethod
from abc import ABC


class TransactionFeeder(ABC):
    def __init__(self, lha=None):
        if lha:
            self.lh = lha
        else:
            self.lh = LogHandler()
        self.logger = self.lh.get_logger(__name__)

    @abstractmethod
    def generate(self) -> [AdaptedTran]:
        pass
