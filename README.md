# Object detection 
Object Detection

## Use Jupyter Lab in the container

a. Request a container

When submit a new container request with "algorithm-segmentation" template, in commmand, 
replace the following commmand
```shell
runuser $$username$$ -c "export HOME=/home/$$username$$/ && export LD_LIBRARY_PATH=/usr/local/nvidia/lib64/ && source /home/$$username$$/.bashrc && export PATH=/opt/conda/envs/pytorch-py35/bin/:$PATH && python3 -m ipykernel install --user && jupyter lab --no-browser --port=8888 --ip=0.0.0.0 --notebook-dir=/"
```
with
```shell
runuser $$username$$ -c "export HOME=/home/$$username$$/ && export LD_LIBRARY_PATH=/usr/local/nvidia/lib64/ && source /home/$$username$$/.bashrc && /bin/sleep infinity"
```
to keep the main container thread sleep, so we can install another ipython kernel.

b. Install conda if necessary, or Add exist conda path to $PATH, editing '~/.bashrc' is not working in container for some reason. 
```shell
$ export PATH=$PATH:~/anaconda3/bin

$ conda activate open-mmlab
(open-mmlab)$ conda install ipykernel
(open-mmlab)$ ipython kernel install --user --name=open-mmlab
(open-mmlab)$ conda deactivate
$ sudo ln -s ~/anaconda3/ /opt/conda  # this step is optional 
$ jupyter lab --no-browser --port=8888 --ip=0.0.0.0 --notebook-dir=/
```

