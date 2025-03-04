import time
import requests
import math

# URLs to fetch data from
URLS = [
    "http://jsonplaceholder.typicode.com/posts",
    "http://jsonplaceholder.typicode.com/comments",
    "http://jsonplaceholder.typicode.com/albums",
    "http://jsonplaceholder.typicode.com/photos",
    "http://jsonplaceholder.typicode.com/todos",
    "http://jsonplaceholder.typicode.com/users",
]

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_in_range(start, end):
    """Count prime numbers in the given range."""
    count = 0
    for n in range(start, end):
        if is_prime(n):
            count += 1
    return count

def fetch_url(url):
    """Fetch data from a URL and return its size."""
    try:
        response = requests.get(url, timeout=10)
        data = response.text
        return len(data)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return 0

def split_range(start, end, chunks):
    """Split a range into chunks."""
    chunk_size = (end - start) // chunks
    return [(start + i * chunk_size, start + (i + 1) * chunk_size) for i in range(chunks)]