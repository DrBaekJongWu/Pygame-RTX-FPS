from _typeshed import Incomplete
from collections.abc import Callable

from urllib3 import Retry

logger: Incomplete

class WritesRetry(Retry):
    jitter_interval: Incomplete
    total: Incomplete
    retry_interval: Incomplete
    max_retry_delay: Incomplete
    max_retry_time: Incomplete
    exponential_base: Incomplete
    retry_timeout: Incomplete
    retry_callback: Incomplete
    def __init__(
        self,
        jitter_interval: int = ...,
        max_retry_delay: int = ...,
        exponential_base: int = ...,
        max_retry_time: int = ...,
        total: int = ...,
        retry_interval: int = ...,
        retry_callback: Callable[[Exception], int] | None = ...,
        **kw,
    ) -> None: ...
    def new(self, **kw): ...
    def is_retry(self, method, status_code, has_retry_after: bool = ...): ...
    def get_backoff_time(self): ...
    def get_retry_after(self, response): ...
    def increment(
        self,
        method: Incomplete | None = ...,
        url: Incomplete | None = ...,
        response: Incomplete | None = ...,
        error: Incomplete | None = ...,
        _pool: Incomplete | None = ...,
        _stacktrace: Incomplete | None = ...,
    ): ...
