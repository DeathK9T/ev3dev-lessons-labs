import threading

def fun_hello(name: str) -> None:
    print(f'Hello {name}!')

if __name__ == "__main__":
    name = "World"
    thr = threading.Thread(target=fun_hello, args=(name,))
    thr.start()