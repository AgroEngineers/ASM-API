from abc import abstractmethod
from enum import Enum

import numpy

from asm.api.base import ASMBase, ContainerParameterResults


class FrameType(Enum):
    FULL = 0
    OBJECT = 1


class ASMOpenCV(ASMBase):
    @abstractmethod
    def frame_type(self) -> FrameType:
        pass

    @abstractmethod
    def process(self, frame: numpy.ndarray) -> list[ContainerParameterResults]:
        pass
