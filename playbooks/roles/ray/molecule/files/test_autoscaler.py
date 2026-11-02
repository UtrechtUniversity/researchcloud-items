import ray
import os
from ray.autoscaler.sdk import request_resources
ray.init(address=os.environ.get('RAY_ADDRESS'))
request_resources(num_cpus=1)
