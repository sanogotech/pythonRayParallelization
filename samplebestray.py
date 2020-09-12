"""
There are a number of advantages to using Ray:

You can parallelize over multiple machines in addition to multiple cores (with the same code).
Efficient handling of numerical data through shared memory (and zero-copy serialization).
High task throughput with distributed scheduling.
Fault tolerance.
"""

import ray

ray.init()

@ray.remote(num_return_vals=3)
def calc_stuff(parameter=None):
    # Do something.
    print("parameter :", parameter)
    return 1, 2, 3



#and then invoke it in parallel
output1, output2, output3 = [], [], []

# Launch the tasks.
for j in range(10):
    id1, id2, id3 = calc_stuff.remote(parameter=j)
    output1.append(id1)
    output2.append(id2)
    output3.append(id3)

# Block until the results have finished and get the results.
output1 = ray.get(output1)
output2 = ray.get(output2)
output3 = ray.get(output3)
print("output1 :", output1)
print("output2 :", output2)
print("output3 :", output3)