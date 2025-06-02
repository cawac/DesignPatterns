import random
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import List, Optional


class EIndicator(StrEnum):
    NONE = "None"
    ISSUE = "Issue"
    PULLREQUEST = "PullRequest"
    BRANCH = "Branch"



class Blackboard(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def update(self, key, value):
        pass

class ConcreteBlackboard(Blackboard):
    def __init__(self):
        self.__data: dict = {}

    def get(self, key):
        return self.__data.get(key)

    def update(self, key, value) -> None:
        self.__data[key] = value

class KnowledgeSource(ABC):
    @abstractmethod
    def canExecute(self, blackboard: Blackboard) -> bool:
        pass

    @abstractmethod
    def execute(self, blackboard: Blackboard) -> None:
        pass

class IssueSensor(KnowledgeSource):
    def canExecute(self, blackboard: Blackboard) -> bool:
        return True

    def execute(self, blackboard: Blackboard) -> None:
        blackboard.update(EIndicator.ISSUE, blackboard.get(EIndicator.ISSUE) + random.randint(1, 5))

class PullRequestSensor(KnowledgeSource):
    def canExecute(self, blackboard: Blackboard) -> bool:
        return True

    def execute(self, blackboard: Blackboard) -> None:
        blackboard.update(EIndicator.PULLREQUEST, blackboard.get(EIndicator.PULLREQUEST) + 1)

class BranchSensor(KnowledgeSource):
    def canExecute(self, blackboard: Blackboard) -> bool:
        return True

    def execute(self, blackboard: Blackboard) -> None:
        blackboard.update(EIndicator.BRANCH, blackboard.get(EIndicator.BRANCH) + random.randint(0, 2))

class IssueAlert(KnowledgeSource):
    def canExecute(self, blackboard: Blackboard) -> bool:
        issue = blackboard.get(EIndicator.ISSUE)
        pull_request = blackboard.get(EIndicator.PULLREQUEST)
        branch = blackboard.get(EIndicator.BRANCH)
        return issue and pull_request and branch

    def execute(self, blackboard: Blackboard) -> None:
        if blackboard.get(EIndicator.ISSUE) > 10:
            print("[IssuesAlert] ALARM amount of issues more than 10!")
        else:
            print("[IssuesAlert] Everything fine")

class Controller:
    def __init__(self, blackboard: Blackboard, sources: List[KnowledgeSource]):
        self.blackboard: Blackboard = blackboard
        self.sources: List[KnowledgeSource] = sources

    def run(self):
        for source in self.sources:
            if source.canExecute(self.blackboard):
                source.execute(self.blackboard)