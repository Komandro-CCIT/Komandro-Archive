import argparse
from cores.broker import Broker

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processing app state.")
    parser.add_argument("--state", type=str, required=True, help="State of app")

    args = parser.parse_args()
    
    state = str(args.state).upper()
    
    b = Broker()
    b.set_state(state)
