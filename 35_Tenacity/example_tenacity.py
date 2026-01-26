"""
Exemplo rápido de uso da lib tenacity
- retry decorator (sync)
- async retry
- uso de Stop/Wait/Retry strategies
Execute: python example_tenacity.py
"""
import asyncio
import random
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    wait_exponential,
    retry_if_exception_type,
    RetryError,
    AsyncRetrying,
)

# Exemplo síncrono: tenta até 3 vezes, espera 2s entre tentativas
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(ValueError))
def flaky_sync():
    print("sync: tentando...")
    if random.random() < 0.7:
        print("sync: falhou, lançando ValueError")
        raise ValueError("erro temporário")
    return "sync: sucesso!"

# Exemplo assíncrono: exponential backoff
@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=1, max=4))
async def flaky_async():
    print("async: tentando...")
    await asyncio.sleep(0.1)
    if random.random() < 0.8:
        print("async: falhou, lançando RuntimeError")
        raise RuntimeError("erro temporário async")
    return "async: sucesso!"

async def run_async_example():
    try:
        result = await flaky_async()
        print(result)
    except RetryError as e:
        print("async: falhou após retries:", e)

def run_sync_example():
    try:
        result = flaky_sync()
        print(result)
    except RetryError as e:
        print("sync: falhou após retries:", e)

if __name__ == "__main__":
    print("-- Exemplo sync --")
    run_sync_example()
    print("\n-- Exemplo async --")
    asyncio.run(run_async_example())
