from abc import abstractmethod
from pathlib import Path
from typing import Union

import numpy

from asm.api.base import ASMBase, ContainerParameterResults


class AIResult:
    def __init__(self, model: str, label: Union[str, None] = None):
        """
        Saves AI result

        :return: AIResult

        Example:
            input: "vegetables", "cucumber"
        """
        self.model = model
        self.label = label

    def __str__(self):
        return f"AIResult({self.model}, {self.label})"


class AIExpansion:
    def __init__(self, model_expansion: list[str], labels_expansion: Union[list[str], None] = None):
        """
        Labels and models file expansions

        :return: AIExpansion

        Example:
            input: ["txt", "yaml"], ["tflite", "h5"]
        """
        self.labels_expansion = labels_expansion
        self.model_expansion = model_expansion

    def __str__(self):
        return f"AIExpansion({self.labels_expansion}, {self.model_expansion})"


class ASMAI(ASMBase):
    @abstractmethod
    def expansions(self) -> AIExpansion:
        """
        :return: File expansions

        Example:
            output: AIExpansion(["txt", "yaml"], ["tflite", "h5"])
        """
        pass

    @abstractmethod
    def available_labels(self) -> list[str]:
        """
        Return available labels for model

        :return: Labels for model

        Example:
            input: Path(./models/tflite/vegetables.txt)

            output: ["tomato", "cucumber"]
        """
        pass

    @abstractmethod
    def process(self, frame: numpy.ndarray) -> tuple[Union[AIResult, None], Union[list[ContainerParameterResults], None]]:
        """
        Return AI result with parameters

        :return: AI result with parameters

        Example:
            input: Camera Frame

            output: AIResult("vegetables", "cucumber"), [ContainerParameterResults("positionX", 120)]
        """
        pass

    @abstractmethod
    def load(self, model: Path, labels: Union[Path, None]) -> bool:
        """
        Load model and return load result (Success or failure)

        :return: Load result (Success or failure)

        Example:
            input: Path(./models/tflite/vegetables.tflite), Path(./models/tflite/vegetables.txt)

            output: True
        """
        pass

    @abstractmethod
    def unload(self) -> None:
        """
        Unload model and labels

        :return: None
        """
        pass
