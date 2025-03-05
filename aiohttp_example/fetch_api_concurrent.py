import asyncio
import aiohttp

BASE_URL = "http://pokeapi.co/api/v2/pokemon/"

# Fetch data from a URL asynchronously
async def fecth_pokemon_data(id):
    url = f"{BASE_URL}{id}"
    print(f"Fetching data for id {id}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

# Fetch 151 pokemons concurrently
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fecth_pokemon_data(id) for id in range(1, 152)]
        results = await asyncio.gather(*tasks)
        print(f"Received {len(results)} results")

# It takes around 3 seconds to fetch all 151 Pokemons
asyncio.run(main())