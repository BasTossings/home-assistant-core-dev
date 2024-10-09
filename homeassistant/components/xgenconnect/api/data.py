"""xGenConnect Data Types."""


class PartitionInfo:
    """xGenConnect Partition."""

    index: int
    name: str

    def __init__(self, index: int, name: str) -> None:
        """Initialize a new partition."""

        self.index = index
        self.name = name

    def __repr__(self) -> str:
        """Return a nicely printable representation of this PartitionInfo."""
        return f"Partition {self.index}: {self.name}"
