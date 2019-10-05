# Object detection 


## Use Jupyter Lab in the container

### Request a container

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

### Install conda if necessary, or Add exist conda path to $PATH, editing '~/.bashrc' is not working in container for some reason. 
```shell
$ export PATH=$PATH:~/anaconda3/bin

$ conda activate open-mmlab
(open-mmlab)$ conda install ipykernel
(open-mmlab)$ ipython kernel install --user --name=open-mmlab
(open-mmlab)$ conda deactivate
$ sudo ln -s ~/anaconda3/ /opt/conda  # this step is optional 
$ jupyter lab --no-browser --port=8888 --ip=0.0.0.0 --notebook-dir=/
```

After this step, you should be able to use public ip to visit Jupyter Lab with new kernal -- "open-mmlab".



## Use MMDetection Training the container

Edit the config file first. 
*Important*: The default learning rate in config files is for 8 GPUs and 2 img/gpu (batch size = 8*2 = 16). According to the Linear Scaling Rule, you need to set the learning rate proportional to the batch size if you use different GPUs or images per GPU, e.g., lr=0.01 for 4 GPUs * 2 img/gpu and lr=0.08 for 16 GPUs * 4 img/gpu.

Multi GPUs
```shell
$ ~/code/mmdetection/tools/dist_train.sh /data/wedward/configs/faster_rcnn_x101_32x4d_fpn_1x_apulis_train_openimgs_with_test_set.py 4 --validate
```

Restart the job if failed. Kill processes to release GPU memory.
```shell
$ ps -aef
$ kill -9 111 222 444
```

Single GPUs example
```shell
$ python ~/code/mmdetection/tools/train.py 191003_cascades_rcnn/faster_rcnn_x101_32x4d_fpn_1x_apulis.py --gpus 1 --work_dir  $WORK_DIR
```
