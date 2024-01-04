from redis import Redis


class Broker:
    def __init__(self, host="localhost", port=6379):
        self.host = host
        self.port = port
        self.redis_client = Redis(host=self.host, port=self.port)
        
        self.prefix: str = "app:state"
        self.decoding: str = "utf-8"

    def get_state(self):
        state = self.redis_client.get(self.prefix)
        
        if not state:
            return ""
        
        state = state.decode(self.decoding)
        return state
    
    def set_state(self, state: str):
        state = self.redis_client.set(
            name=self.prefix, 
            value=state
        )
    
        return state
