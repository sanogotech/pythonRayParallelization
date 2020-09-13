# pythonRayParallelization

```
pip uninstall -y pyarrow
pip install ray[debug]==0.7.5
pip install bs4

ray start --head  --include-webui

View the dashboard at http://192.xx.xx.xx:8080/?token=xxxxxx

Started Ray on this node. You can add additional nodes to the cluster by calling

ray start --redis-address 192.168.1.105:52871

from the node you wish to add. You can connect a driver to the cluster from Python by running

import ray
ray.init(redis_address="192.168.1.105:52871")


If you have trouble connecting from a different machine, check that your firewall is configured properly. If you wish to terminate the processes that have been started, run

    ray stop
sanogo@DESKTOP-O



```

##  Docs

- https://linuxconfig.org/how-to-install-kubernetes-on-ubuntu-20-04-focal-fossa-linux
- Ray Clusters mode manual config
- https://docs.ray.io/en/latest/cluster/launcher.html
https://docs.ray.io/en/releases-0.8.5/using-ray-on-a-cluster.html

- https://colab.research.google.com/github/ray-project/tutorial/blob/master/exercises/colab01-03.ipynb#scrollTo=zCb7eB-l_-HH

- https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1

- https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8
- https://docs.ray.io/en/latest/walkthrough.html

- https://rise.cs.berkeley.edu/blog/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray/

- https://rise.cs.berkeley.edu/blog/ray-tips-for-first-time-users/
