
import ray
from ray.util.iter import ParallelIterator

ray.init()

# Create an iterator with 2 worker actors over the list [1, 2, 3, 4].
it = ray.util.iter.from_items([1, 2, 3, 4], num_shards=2)
ParallelIterator[from_items[int, 4]]