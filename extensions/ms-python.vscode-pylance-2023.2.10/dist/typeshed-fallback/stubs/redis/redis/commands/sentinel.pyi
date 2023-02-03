class SentinelCommands:
    def sentinel(self, *args): ...
    def sentinel_get_master_addr_by_name(self, service_name): ...
    def sentinel_master(self, service_name): ...
    def sentinel_masters(self): ...
    def sentinel_monitor(self, name, ip, port, quorum): ...
    def sentinel_remove(self, name): ...
    def sentinel_sentinels(self, service_name): ...
    def sentinel_set(self, name, option, value): ...
    def sentinel_slaves(self, service_name): ...
    def sentinel_reset(self, pattern): ...
    def sentinel_failover(self, new_master_name): ...
    def sentinel_ckquorum(self, new_master_name): ...
    def sentinel_flushconfig(self): ...

class AsyncSentinelCommands(SentinelCommands):
    async def sentinel(self, *args) -> None: ...
