import datetime
from enum import Enum
from pathlib import Path
import inspect


class LogType(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    WEB_SERVER = "WEB SERVER"
    PIP = "PIP"


class EventBus:
    def __init__(self):
        self._events = {}

    def subscribe(self, event_name, handler):
        self._events.setdefault(event_name, []).append(handler)

    async def emit(self, event_name, *args, **kwargs):
        for handler in self._events.get(event_name, []):
            if inspect.iscoroutinefunction(handler):
                await handler(*args, **kwargs)
            else:
                handler(*args, **kwargs)


bus = EventBus()
log_file: Path
log_history: str = "Logging History starts here"


def _check_logs_folder():
    Path("logs").mkdir(parents=True, exist_ok=True)


def _load_logfile():
    global log_file
    _check_logs_folder()
    log_file = Path(f"logs/{datetime.datetime.now()}.log")
    with open(log_file, 'x') as f:
        f.write(f"LOG FROM {datetime.datetime.now()}\n")


def log(content: str, log_type: LogType = LogType.INFO):
    global log_history
    if content == "":
        log_str = f"[EMPTY LINE]"
    else:
        log_str = f"[{log_type.value}] <{datetime.datetime.now()}>: {content}"
    print(log_str)
    log_history += "\n" + log_str
    bus.emit("onLog", log_str)
    with open(log_file, 'a') as f:
        f.write(log_str + "\n")


def get_log_history():
    return log_history


def stop_logger():
    with open(log_file, 'a') as f:
        f.write(f"LOG FINAL AT {datetime.datetime.now()}")


def init_logman():
    _load_logfile()

    log("LogMan here!")
    log(f"LogFile: {str(log_file.absolute())}")
