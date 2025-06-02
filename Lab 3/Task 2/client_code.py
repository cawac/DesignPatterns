from time import sleep
from blackboard import (
    ConcreteBlackboard,
    Controller,
    IssueSensor,
    PullRequestSensor,
    BranchSensor,
    IssueAlert,
    EIndicator
)

def main():
    blackboard = ConcreteBlackboard()
    blackboard.update(EIndicator.ISSUE, 1)
    blackboard.update(EIndicator.PULLREQUEST, 1)
    blackboard.update(EIndicator.BRANCH, 1)

    sources = [
        PullRequestSensor(),
        IssueSensor(),
        BranchSensor(),
        IssueAlert()
    ]

    controller = Controller(blackboard, sources)

    for step in range(10):
        print(f"\n--- Step {step + 1} ---")
        controller.run()
        print(f"Issues: {blackboard.get(EIndicator.ISSUE)}")
        print(f"PullRequests: {blackboard.get(EIndicator.PULLREQUEST)}")
        print(f"Branches: {blackboard.get(EIndicator.BRANCH)}")
        sleep(1)

if __name__ == "__main__":
    main()
