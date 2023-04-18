import toml


def get_classes(path: str) -> list[str]:
    """
    Get the classes from a toml file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return toml.load(f)["classes"]


