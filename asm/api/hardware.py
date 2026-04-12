from abc import abstractmethod
from enum import Enum
from typing import Union

from asm.api.base import ASMBase, ContainerParameterResults


class Direction(Enum):
    STOP = 0
    FORWARD = 1
    BACKWARD = 2


class AvailableDevices:
    def __init__(self, available_machines: list[str], available_cameras: list[str]):
        self.available_machines = available_machines
        self.available_cameras = available_cameras

    def __str__(self):
        return f'AvailableDevices({self.available_machines}, {self.available_cameras})'


class ASMHardware(ASMBase):
    @abstractmethod
    def get_available_devices(self) -> AvailableDevices:
        pass

    @abstractmethod
    def connect_camera(self, port: int) -> bool:
        pass

    @abstractmethod
    def connect_machine(self, port: int) -> bool:
        pass

    @abstractmethod
    def disconnect_camera(self) -> None:
        pass

    @abstractmethod
    def disconnect_machine(self) -> None:
        pass

    @abstractmethod
    def set_direction(self, direction: Direction) -> None:
        pass

    @abstractmethod
    def set_container(self, container: int) -> None:
        pass

    @abstractmethod
    def canvas(self) -> str:
        pass

    @abstractmethod
    def process(self) -> Union[list[ContainerParameterResults], None]:
        pass
