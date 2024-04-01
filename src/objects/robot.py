from enum import Enum


class RobotSize(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


class RobotSizeError(Exception):
    def __init__(self, message="Wrong type of robot size."):
        self.message = message
        super().__init__(self.message)


class Robot:
    def __init__(self, id: str, size: RobotSize = RobotSize.SMALL) -> None:
        self.id = id
        if not isinstance(size, RobotSize):
            raise RobotSizeError
        self.size = size
        self.load_capacity = self.calculate_capacity()
        self.velocity = self.calculate_velocity()

    def calculate_capacity(self):
        if self.size == RobotSize.SMALL:
            return 1
        elif self.size == RobotSize.MEDIUM:
            return 5
        elif self.size == RobotSize.LARGE:
            return 7
        else:
            raise RobotSizeError

    def calculate_velocity(self):
        if self.size == RobotSize.SMALL:
            return 7
        elif self.size == RobotSize.MEDIUM:
            return 5
        elif self.size == RobotSize.LARGE:
            return 1
        else:
            raise RobotSizeError
