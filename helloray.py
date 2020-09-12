from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ray
import time
from datetime import datetime

print('Successfully imported ray!')

"""
Start the processes that make up the Ray runtime. 
By default, Ray does not schedule more tasks concurrently than there are CPUs,
but this example requires four tasks to run concurrently, so we tell Ray that there are four CPUs. 
In practice, you would usually just let Ray detect the number of CPUs on the machine.
"""
ray.init(num_cpus=4, ignore_reinit_error=True)
#ray.init()


# Sleep a little to improve the accuracy of the timing measurements used below,
# because some workers may still be starting up in the background.
# time.sleep(2.0)

# A regular Python function.
def regular_function():
	time.sleep(2.0)
	return 1
 
# A Ray remote function.
@ray.remote
def remote_function():
	time.sleep(2.0)
	return 1

#-------------------
# These are executed one at a time, back-to-back.
result1 = 0
start_time1 = int(time.time()*1000.0)

for _ in range(4):
    result1 += regular_function()
#give resolution to the second  
duration1 = int(time.time()*1000.0) - start_time1

print("Le Temps total1 for regular  est :",duration1)
assert result1 == 4

#-------------------
results = []
start_time2 = int(time.time()*1000.0)
for _ in range(4):
    results.append(remote_function.remote())

#give resolution to the  mili-seconds  
duration2 = int(time.time()*1000.0) - start_time2
print("Le Temps total ray.remote  est :",duration2)
#assert duration < 1.1, ('The loop took {:.3f} seconds. This is too slow.'.format(duration))
#assert duration > 1, ('The loop took {:.3f} seconds. This is too fast.'.format(duration))

fullcalcul = sum(ray.get(results))
print("Full calcul  est :",fullcalcul)
assert fullcalcul == 4