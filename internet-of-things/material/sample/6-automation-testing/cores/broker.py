from redis import Redis


class Broker:
    def __init__(self, host="localhost", port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = Redis(host=self.host, port=self.port, db=self.db)

        self.prefix: str = "app:state"
        self.decoding: str = "utf-8"

    def get_state(self):
        state = self.redis_client.get(self.prefix)

        if not state:
            return ""

        state = state.decode(self.decoding)
        return state

    def set_state(self, state: str):
        state = self.redis_client.set(name=self.prefix, value=state)

        return state

    def create_single_data(self, key: str, values: object):
        return self.redis_client.set(key, values)

    def read_single_data(self, key: str):
        data = self.redis_client.get(key)
        
        if not data:
            return None
        
        return data.decode('utf-8')

    def flush_all_data(self, force=False):
        if not force:
            return
        
        self.redis_client.flushdb()
        self.redis_client.flushall()