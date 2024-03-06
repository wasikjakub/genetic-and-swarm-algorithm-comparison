class Robot:
    def __init__(self, id: str, velocity: float, load_capacity: int) -> None:
        self.id = id
        self.load_capacity = load_capacity
        self.velocity = velocity
