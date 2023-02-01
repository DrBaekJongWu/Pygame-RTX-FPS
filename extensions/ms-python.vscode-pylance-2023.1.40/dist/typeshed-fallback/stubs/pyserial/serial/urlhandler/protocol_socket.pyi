import logging

from serial.serialutil import SerialBase

LOGGER_LEVELS: dict[str, int]
POLL_TIMEOUT: float

class Serial(SerialBase):
    logger: logging.Logger | None
    def open(self) -> None: ...
    def from_url(self, url: str) -> tuple[str, int]: ...
    @property
    def in_waiting(self) -> int: ...
    def reset_input_buffer(self) -> None: ...
    def reset_output_buffer(self) -> None: ...
    @property
    def cts(self) -> bool: ...
    @property
    def dsr(self) -> bool: ...
    @property
    def ri(self) -> bool: ...
    @property
    def cd(self) -> bool: ...
