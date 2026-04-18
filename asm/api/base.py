from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, Dict, List

import numpy


class ContainerParameterType(Enum):
    STRING = "string"
    RANGE = "range"


class ContainerParameterWebSpecAlignment(Enum):
    BEFORE = "before"
    AFTER = "after"


class ModuleRequirementVersionPolicy(Enum):
    ANY = 0
    EQUAL = 1
    HIGHER = 2


ModuleConfigurationPattern = Union[
    str,
    float,
    bool,
    int,
    None,
    Dict[str, "JSON"],
    List["JSON"]
]


class ContainerParameterWebSpec:
    def __init__(self, html: str, css: str, alignment: ContainerParameterWebSpecAlignment):
        """
        ContainerParameterWebSpec put HTML and CSS code in parameters table in WebUI

        Alignment set position before or after parameter text

        It automatically changes %__parameter_X% to X parameter content

        Example:
            ContainerParameterWebSpec("<p>Hello world</p>", "p { color: rgb(%__parameter_r%, %__parameter_g%, %__parameter_b%)}") ->

            ContainerParameterWebSpec("<p>Hello world</p>", "p { color: rgb(12, 134, 99)}") <if r = 12; g = 134; b = 99>
        """
        self.html = html
        self.css = css
        self.alignment = alignment

    def __str__(self):
        return f"ContainerParameterWebSpec({self.html}, {self.css}, {self.alignment})"


class ContainerParameter:
    def __init__(self, name: str, parameter_type: ContainerParameterType, web_spec: ContainerParameterWebSpec = None):
        """
        ContainerParameter request for return sort parameters

        Example:
            input: ContainerParameter("red", ContainerParameterType.RANGE)
        """
        self.name = name
        self.type = parameter_type
        self.web_spec = web_spec

    def __str__(self):
        return f"ContainerParameter({self.name}, {self.type})"


class ContainerParameterResults:
    def __init__(self, name: str, result: Union[int, str]):
        """
        Result of ContainerParameter, name must be same with ContainerParameter

        Example:
            input: ContainerParameterResult("red", 123)
        """
        self.name = name
        self.result = result

    def __str__(self):
        return f"ContainerParameterResult({self.name}, {self.result})"


class ModuleTaskInputPattern:
    def __init__(self, request_frame: bool, task_input: ModuleConfigurationPattern):
        self.request_frame = request_frame
        self.task_input = task_input


class ModuleTaskOutputPattern:
    def __init__(self, task_output: ModuleConfigurationPattern):
        self.task_output = task_output


class ModuleTask:
    def __init__(self, name: str, task_input: ModuleTaskInputPattern, task_output: ModuleTaskOutputPattern):
        self.name = name
        self.task_input = task_input
        self.task_output = task_output


class ModuleTaskInput:
    def __init__(self, task_input: ModuleTaskInputPattern, frame: Union[numpy.ndarray, None]):
        self.task_input = task_input
        self.frame = frame


class ModuleTaskOutput:
    def __init__(self, task_output: ModuleTaskOutputPattern, update_configuration: ModuleConfigurationPattern):
        self.task_output = task_output
        self.update_configuration = update_configuration


class ModuleRequirement:
    def __init__(self, name: str, version: str = "",
                 policy: ModuleRequirementVersionPolicy = ModuleRequirementVersionPolicy.ANY):
        self.name = name
        self.version = version
        self.policy = policy

    def __str__(self):
        return f"ModuleRequirement({self.name}, {self.version}, {self.policy})"


class ModuleConfiguration:
    def __init__(self, configuration: Dict[str, ModuleConfigurationPattern]):
        self.configuration = configuration

    def __str__(self):
        return f"ModuleConfiguration({self.configuration})"


class ModuleInformation:
    def __init__(self, name: str, version: str, requirements: Union[list[ModuleRequirement], None] = None,
                 configuration_pattern: Union[ModuleConfiguration, None] = None, parameters: Union[list[ContainerParameter], None] = None,
                 tasks: Union[list[ModuleTask], None] = None, web_spec: Union[ContainerParameterWebSpec, None] = None):
        self.name = name
        self.id = name.lower().replace(" ", "_").replace("/", "_").replace("\\", "_")
        self.version = version
        self.requirements = requirements
        self.parameters = parameters
        self.web_spec = web_spec
        self.configuration_pattern = configuration_pattern
        self.tasks = tasks

    def __str__(self):
        return f"ModuleInformation({self.name}, {self.version}, {self.requirements}, {self.configuration_pattern}, {self.parameters}, {self.web_spec})"


class ASMBase(ABC):
    @abstractmethod
    def module_info(self) -> ModuleInformation:
        pass

    @abstractmethod
    def configuration(self, configuration: ModuleConfiguration):
        pass

    @abstractmethod
    def task(self, task: ModuleTask, task_input: ModuleTaskInput) -> Union[ModuleTaskOutput, None]:
        pass
