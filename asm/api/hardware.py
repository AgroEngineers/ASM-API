from abc import abstractmethod
from enum import Enum
from typing import Union

import numpy

from asm.api.base import ASMBase, ContainerParameterResults


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
    def is_camera_connected(self) -> bool:
        pass

    @abstractmethod
    def is_machine_connected(self) -> bool:
        pass

    @abstractmethod
    def canvas(self) -> str:
        pass

    @abstractmethod
    def process(self) -> Union[list[ContainerParameterResults], None]:
        pass

    @abstractmethod
    async def connect_camera(self, port: str) -> bool:
        pass

    @abstractmethod
    async def disconnect_camera(self) -> None:
        pass

    @abstractmethod
    def frame(self) -> numpy.ndarray:
        pass

    @abstractmethod
    async def connect_machine(self, port: str) -> bool:
        pass

    @abstractmethod
    async def disconnect_machine(self) -> None:
        pass

    @abstractmethod
    def get_available_gates(self) -> int:
        pass

    @abstractmethod
    def get_available_gate_states(self) -> list[str]:
        pass

    @abstractmethod
    def get_current_states(self) -> dict[int, str]:
        pass

    @abstractmethod
    def set_gate(self, gate: int, state: str) -> None:
        pass

    @abstractmethod
    def set_direction(self, direction: str) -> None:
        pass

    @abstractmethod
    def set_container(self, container: int) -> None:
        pass

    @abstractmethod
    def get_container_count(self) -> int:
        pass

    @abstractmethod
    def get_forward_direction(self) -> int:
        pass
