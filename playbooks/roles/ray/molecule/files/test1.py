# uv run --python 3.12.3 --with "ray[default]" python test.py

import ray
import os

# 1. Start Ray
ray.init(address=os.environ.get('RAY_ADDRESS', None), )

# 2. Define a remote function (task)
@ray.remote
def square(x):
    return x * x

# 3. Call the function asynchronously 
future = square.remote(4)

# 4. Get and print the result
result = ray.get(future)
print(f"Result: {result}")  # Prints Result: 16

# 5. Shut down Ray
ray.shutdown()
