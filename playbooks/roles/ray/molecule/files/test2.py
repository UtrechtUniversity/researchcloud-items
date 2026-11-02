import os
import ray

# Connect to the running local or multi-node cluster
ray.init(address=os.environ.get('RAY_ADDRESS', None))

# Print total cluster resources
print("Cluster resources:", ray.cluster_resources())

# Print currently available resources
print("Available resources:", ray.available_resources())

ray.shutdown()