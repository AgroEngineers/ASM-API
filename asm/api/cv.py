from abc import abstractmethod
from enum import Enum
from typing import Union

import numpy

from asm.api.base import ASMBase, ContainerParameterResults


class FrameType(Enum):
    FULL = 0
    OBJECT = 1


class DetectedObject:
    def __init__(self, detected: bool, xmin: float, xmax: float, ymin: float, ymax: float):
        self.detected = detected
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


class ASMOpenCV(ASMBase):
    @abstractmethod
    def frame_type(self) -> FrameType:
        pass

    @abstractmethod
    async def process(self, frame: numpy.ndarray) -> list[ContainerParameterResults]:
        pass


class ASMDetector(ASMBase):
    @abstractmethod
    async def process(self, frame: numpy.ndarray) -> Union[DetectedObject, None]:
        pass
