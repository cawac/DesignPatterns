from typing import Any, Dict, List

class Blackboard:
    def __init__(self) -> None:
        self.data: Dict[str, Any] = {}
        self.history: List[str] = []

    def write(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.history.append(f"Wrote {key}: {value}")

    def read(self, key: str) -> Any:
        value = self.data.get(key)
        self.history.append(f"Read {key}: {value}")
        return value

    def show_history(self) -> None:
        print("Blackboard history:")
        for entry in self.history:
            print(entry)

class KnowledgeSource:
    def __init__(self, name: str) -> None:
        self.name = name

    def process(self, blackboard: Blackboard) -> None:
        pass  # To be implemented by subclasses

class AddKnowledgeSource(KnowledgeSource):
    def process(self, blackboard: Blackboard) -> None:
        a = blackboard.read('a')
        b = blackboard.read('b')
        if a is not None and b is not None:
            result = a + b
            blackboard.write('sum', result)
            print(f"{self.name}: Added {a} + {b} = {result}")

class MultiplyKnowledgeSource(KnowledgeSource):
    def process(self, blackboard: Blackboard) -> None:
        a = blackboard.read('a')
        b = blackboard.read('b')
        if a is not None and b is not None:
            result = a * b
            blackboard.write('product', result)
            print(f"{self.name}: Multiplied {a} * {b} = {result}")

class Controller:
    def __init__(self, blackboard: Blackboard, sources: List[KnowledgeSource]) -> None:
        self.blackboard = blackboard
        self.sources = sources

    def run(self) -> None:
        for source in self.sources:
            source.process(self.blackboard)
        self.blackboard.show_history()

if __name__ == "__main__":
    blackboard = Blackboard()
    blackboard.write('a', 5)
    blackboard.write('b', 3)

    sources = [AddKnowledgeSource("Adder"), MultiplyKnowledgeSource("Multiplier")]
    controller = Controller(blackboard, sources)
    controller.run() 