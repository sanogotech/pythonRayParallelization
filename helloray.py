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
ray.init(num_cpus=8, ignore_reinit_error=True)
#ray.init()


# Sleep a little to improve the accuracy of the timing measurements used below,
# because some workers may still be starting up in the background.
# time.sleep(sec) takes as arguments the number of seconds you want the program
# time.sleep(2.0)

def step0_callFindSitedeFacturation():
	print("Start step0_callFindSitedeFacturation:")

def step1_callApiforData(sitefacturation, numerofacture):
	print("Start step1_callApiforData:")
	time.sleep(0.1)

def step2_callProcessFacture(sitefacturation, numerofacture):
	print("Start step2_callProcessFacturation:")
	time.sleep(0.1)

def step3_callStoreFacture(sitefacturation, numerofacture):
	print("Start step3_callStoreFacture:")
	time.sleep(0.1)

# Call Facture function.
def calculfacture_regular_function(sitefacturation, numerofacture):
	print("--------------")
	print(" Start ccalculfacture_regular_function !")
	step1_callApiforData(sitefacturation, numerofacture)
	step2_callProcessFacture(sitefacturation, numerofacture)
	step3_callStoreFacture(sitefacturation, numerofacture)
	print("--------------")
	return 1

# A regular Python function.
def regular_function():
	time.sleep(0.001)
	print(" regular_function")
	return 1


# Call Facture function.
# A Ray remote function.
@ray.remote
def calculfacture_remote_function():
	print("-------***-------")
	print(" Start calculfacture_remote_function !")
	step1_callApiforData(1,25)
	step2_callProcessFacture(1,25)
	step3_callStoreFacture(1,25)
	print("-------***-------")
	return 1



# A Ray remote function.
@ray.remote
def remote_function():
	time.sleep(0.001)
	print(" remote_function")
	return 1


def myhelloRay():
	print("myhelloRay !")
    #-------------------
	# These are executed one at a time, back-to-back.
	result1 = 0
	start_time1 = int(time.time()*1000.0)

	for _ in range(4):
	    result1 += regular_function()
	#give resolution to the milliseconds  
	duration1 = int(time.time()*1000.0) - start_time1

	print("Le Temps total1 for regular  est :",duration1)
	assert result1 == 4

	#-------------------
	results = []
	start_time2 = int(time.time()*1000.0)
	for _ in range(4):
	    results.append(remote_function.remote())

	#give resolution to the  milliseconds
	duration2 = int(time.time()*1000.0) - start_time2
	print("Le Temps total ray.remote  est :",duration2)
	#assert duration < 1.1, ('The loop took {:.3f} seconds. This is too slow.'.format(duration))
	#assert duration > 1, ('The loop took {:.3f} seconds. This is too fast.'.format(duration))

	fullcalcul = sum(ray.get(results))
	print("Full calcul  est :",fullcalcul)
	assert fullcalcul == 4


def initRegularFacturation():
	countFacture = 0
	start_time1 = int(time.time()*1000.0)
	for _ in range(4):
	    countFacture += calculfacture_regular_function(1,25)
	#give resolution to the milliseconds  
	duration1 = int(time.time()*1000.0) - start_time1

	print("Le Temps total RegularFacturation  est :",duration1)
	return countFacture

def initRemoteRayFacturation():
	results = []
	start_time2 = int(time.time()*1000.0)
	for _ in range(4):
	    results.append(calculfacture_remote_function.remote())
	    print("Append test remote!")

	#give resolution to the  milliseconds
	duration2 = int(time.time()*1000.0) - start_time2
	print("Le Temps total RemoteRayFacturation  est :",duration2)

	fullcalcul = sum(ray.get(results))
	print("Full RemoteRayFacturation est :",fullcalcul)
	assert fullcalcul == 4

def main():
    print("Hello World!")
    #myhelloRay()
    initRegularFacturation()
    initRemoteRayFacturation()

if __name__ == "__main__":
    main()