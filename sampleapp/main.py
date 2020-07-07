import requests

def main(args):
    if len(args) != 2:
        raise ValueError('Only 1 arg is allowed')
    print("Making request")
    print(requests.get(args[1]))
