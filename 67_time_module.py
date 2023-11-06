import time

# print(time.__dir__())

def benchmark(upperBound):
    init = time.time()
    for i in range(upperBound):
        pass
    return time.time() - init

print(f"{benchmark(100_000_000)} ms")

