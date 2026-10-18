from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self) -> None:
        self.decorations: list[BaseDecoration] = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decoration = next((x for x in self.decorations if x.__class__.__name__ == decoration_type), None)
        if decoration is not None:
            return decoration
        return "None"