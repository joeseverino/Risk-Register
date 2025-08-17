import sys


STATUSES = ["Open", "Closed Avoided", "Closed Accepted"]
RATINGS = ["High", "Medium", "Low"]
INVALID = "Invalid command"



class ProjectItem:
    """Class blueprint used for sublass risk"""
    id_counter = 1

    def __init__(self, name, probability="Low", severity="Low", status="Open", _id=None):
        if type(self) is ProjectItem:
            raise TypeError("Initialize a subclass (Risk)")
        cls = type(self)
        if _id is None:
            self._object_id = f"{cls.PREFIX}{cls.id_counter:03d}"
            cls.id_counter += 1
        else:
            self._object_id = _id
        self.probability = probability
        self.severity = severity
        self.status = status
        self.name = name

    def __str__(self):
        return f"{self._object_id}: {self._name} ({self._status})"

    @property
    def object_id(self):
        return self._object_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status in STATUSES:
            self._status = status
        else:
            raise ValueError("Invalid status")

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability):
        if probability in RATINGS:
            self._probability = probability
        else:
            raise ValueError("Invalid rating")

    @property
    def severity(self):
        return self._severity

    @severity.setter
    def severity(self, severity):
        if severity in RATINGS:
            self._severity = severity
        else:
            raise ValueError("Invalid rating")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Invalid name")
        else:
            self._name = name


class Risk(ProjectItem):
    """Subclass of ProjectItem used to initialize project risks"""
    PREFIX = "RSK"
    id_counter = 1
    def __init__(self, name, probability="Low", severity="Low", status="Open",
                 _id=None):
        super().__init__(name, probability, severity, status, _id=_id)


def main():
    items = {}
    main_menu(items)


def main_menu(items):
    """Prompts user for commands until exit"""

    while True:
        user_input = input(
            "\ninsert - Insert Risk\nview - View Risks\nedit <ID> - Edit a Risk's status\nremove <ID...>\nexit - Quit\n> ")
        if not user_input:
            print(INVALID)
            continue
        cmd, rest = (user_input.strip().lower().split(maxsplit=1) + [""])[:2]
        match cmd:
            case "insert":  add_risk(items)
            case "view":    view_risks(items)
            case "edit":    edit_risk(items, rest)
            case "remove":  delete_risk(items, rest)
            case "exit":    sys.exit()
            case _: print(INVALID)


def add_risk(items: dict[str, Risk]) -> None:
    """Init a new risk and add it to items dict"""
    name = name_input_helper("Risk Name: ").strip()
    probability = input_helper(f"Probability ({'/'.join(RATINGS)})", "Low", RATINGS)
    severity = input_helper(f"Severity ({'/'.join(RATINGS)})", "Low", RATINGS)
    status = input_helper(f"Status ({'/'.join(STATUSES)})", "Open", STATUSES)

    r = Risk(name=name, probability=probability, severity=severity, status=status)
    items[r.object_id] = r
    print(f"Added {r}")


def input_helper(label: str, default: str, allowed: list[str]) -> str:
    """Input helper to get values inside expected global variable lists"""
    while True:
        value = input(f"{label} [{default}]: ").strip().title() or default
        if value in allowed:
            return value
        print(f"Invalid. Expected one of: {', '.join(allowed)}")


def name_input_helper(label: str) -> str:
    """Helper function to get a non-empty risk name"""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Invalid name. Please enter a non-empty value.")


def edit_risk(items: dict[str, Risk], id_str: str) -> None:
    """Adjust the risk status"""
    id_str = (id_str or input("ID to edit (e.g., RSK001): ")).strip().upper()
    obj = items.get(id_str)
    if not obj:
        print(f"{id_str} not found")
        return
    new_status = input_helper(f"New Status ({'/'.join(STATUSES)})", obj.status, STATUSES)
    obj.status = new_status
    print(f"Updated {id_str} → {obj.status}")


def view_risks(items: dict[str, Risk]) -> None:
    """Print a list of all risks and a count"""
    print(f"\nCurrent Risks: {len(items)}\n")
    for object_id in sorted(items):
        item = items[object_id]
        print(f"{item.object_id}: {item.name} ({item.status}) | Probability: {item.probability} | Severity: {item.severity}")


def delete_risk(items, rest: str) -> None:
    """Delete n risks (by ID)"""
    if not rest:
        rest = input("ID(s) to remove (e.g., RSK001 RSK002 or RSK001,RSK002): ").strip()

    ids = [tok.upper() for tok in rest.replace(",", " ").split()]
    for id_ in ids:
        if items.pop(id_, None):
            print(f"\nRemoved {id_}")
        else:
            print(f"\n{id_} not found")


if __name__ == "__main__":
    main()
