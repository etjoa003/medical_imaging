# Attention-Gated-Networks_auxiliary
Working on Attention-Gated-Networks from https://github.com/ozan-oktay/Attention-Gated-Networks,
you might want to run the algorithm on the original datasets. One of them is PANCREAS CT-82 which
can be found from https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT.

The .dcm files store 2D slices. This code combines (and normalize) the slices of each patient 
into 3D volume. Each patient is coded as PANCREAS_0001, PANCREAS_0002 etc.

### 3.1. Usage
You can run the following in the command line:   
```
python ctpan.py -h
```

Dependencies: read the utils.py or Attention-Gated-Networks_auxiliary/README.txt

Note that tests are conducted in Windows 10, python 3.6. 
