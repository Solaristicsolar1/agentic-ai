import asyncio
import time
from pydantic import Basemodel

class Patient_data(Basemodel):
    name: str
    age: int

async def fetch_database():
    print("Fetching data...")
    await asyncio.sleep(4)
    print("data fetched")

async def fetch_weather():
    print("Fetching weather data...")
    await asyncio.sleep(2)
    print("weather data fetched")

async def main():
    start = time.time()

    await asyncio.gather(
        fetch_database(), fetch_weather()
    )

    end_time = time.time()
    print(f"Total time taken: {end_time - start}")
asyncio.run(main())