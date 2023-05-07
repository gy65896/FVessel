# <p align=center> FVessel: Benchmark Dataset for Vessel Detection, Tracking, and Data Fusion</p>

<div align="center">

[![Paper](https://img.shields.io/badge/arXiv-Paper-red.svg)](https://arxiv.org/abs/2302.11283)
[![Code](https://img.shields.io/badge/DeepSORVF-Code-orange.svg)](https://github.com/gy65896/DeepSORVF)
[![Chinese](https://img.shields.io/badge/简体中文-Chinese-green.svg)](README_zh-CN.md)

</div>

---

>**Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways **<br>  Yu Guo, [Ryan Wen Liu](http://mipc.whut.edu.cn/index.html), Jingxiang Qu, Yuxu Lu, Fenghua Zhu, Yisheng Lv <br> 
>arXiv preprint arXiv:2302.11283

> **Introduction:** *The FVessel benchmark dataset is used to evaluate the reliability of AIS and video data fusion algorithms, which mainly contains 26 videos and the corresponding AIS data captured by the HIKVISION DS-2DC4423IW-D dome camera and Saiyang AIS9000-08 Class-B AIS receiver on the Wuhan Segment of the Yangtze River. To protect privacy, the MMSI for each vessel has been replaced with a random number in our dataset. As shown in Figure 1, these videos were captured under many locations (e.g., bridge region and riverside) and various weather conditions (e.g., sunny, cloudy, and low-light).*
<hr />

## News 🚀

* **2023.05.07**: 9 fusion data (Video-27~Video-35) and 3728 images for detection are captured, and new data will be made public soon.
* **2023.01.12**: We made the FVessel_V1.0 dataset public, containing 26 fusion data and 7625 images for detection.
## Examples

![Figure04_FVessel](https://user-images.githubusercontent.com/48637474/210925024-15dcbcbe-717b-47b6-ad4b-377d71141380.jpg)

## Details

The FVessel dataset consists of two parts:
* __01_Video+AIS__
* __02_Image+xml__

### 01_Video+AIS
`01_Video+AIS` contains many videos and the corresponding AIS data to evaluate the performance of the data fusion algorithm. Each video data contains the following files:

```
|-ais
     |- 2022_05_10_19_21_04.csv
     |- 2022_05_10_19_21_05.csv
     |- 2022_05_10_19_21_06.csv
     └─ ... (ais data)
|-2022_05_10_19_21_05_19_31_10_b.mp4
|-camera_para.txt
|-gt
     |- Video-02_gt.mp4
     |- Video-02_gt_detection.txt
        | - <second>, <0>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
     |- Video-02_gt_tracking.txt
     └─ Video-02_gt_fusion.txt
```



* __(a) AIS__

  Each csv file contains the AIS data received within ten minutes, and only the most recent data is kept.

  __2022_05_10_19_21_04__

  |Number|MMSI|Lon|Lat|Speed|Course|Heading|Type|Timestamp|
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  0|100000000|114.325327|30.60166 |0  |293.6|511|18|1652181559844
  1|130000000|114.302683|30.58059 |6.8|33.6 |33 |18|1652181659157
  2|140000000|114.31004 |30.599997|3.9|215.6|511|18|1652181655147
  3|600000000|114.3156  |30.59773 |7.2|39.6 |511|18|1652181649704
  ...|...|...|... |...|... |...|...|...

 * __(b) Video__

    __2022_05_10_19_21_05_19_31_10_b.mp4__  
    
    Starting time: 2022_05_10_19_21_05
    End time: 2022_05_10_19_31_10
    Type: b/r (bridge/riverside)
   
  * __(c) Camera Parameters__
  
    __camera_para.txt__

    |Lon|Lat|Horizontal Orientation|Vertical Orientation|Camera Height|Horizontal FoV|Vertical FoV|fx|fy|u0|v0|
    | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
    114.32583|30.60139|7|-1|20| 55 | 30.94 | 2391.26 | 2446.89 | 1305.04 | 855.214 |
    
    fx, fy, u0, and v0 are parameters in the internal matrix of the camera.
    
* __(d) GT (Ground Truth: adopt the multi-object tracking MOT format)__
    
    __Video-02_gt.mp4__
    
    Video containing ground truth, processed only once per second.
    
    __Video-02_gt_detection.txt__
    
    ```
    <second>, <0>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
    ```
    
    __Video-02_gt_tracking.txt__
    
    ```
    <second>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
    ```
    
    __Video-02_gt_fusion.txt__
    
    ```
    <second>, <mmsi>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
    ```


|Video|Video Length|Type|Weather|Times of Occlusions|Total Number of Vessels|Number of Vessels with AIS|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
01|10m07s|Bridge   |Low-light|2|5|4
02|19m52s|Bridge   |Sunny    |6|7|6
03|19m14s|Riverside|Sunny    |6|5|5
04|06m10s|Riverside|Sunny    |0|1|1
05|15m01s|Riverside|Sunny    |2|5|5
06|12m49s|Riverside|Sunny    |2|4|4
07|03m38s|Riverside|Sunny    |1|2|2
08|16m05s|Riverside|Sunny    |3|6|5
09|05m25s|Riverside|Sunny    |0|1|1
10|11m17s|Bridge   |Cloudy   |2|3|1
11|05m18s|Riverside|Sunny    |1|3|3
12|07m19s|Riverside|Sunny    |1|4|4
13|12m58s|Riverside|Sunny    |5|6|6
14|03m58s|Riverside|Sunny    |3|4|4
15|10m46s|Riverside|Sunny    |0|4|4
16|05m05s|Riverside|Sunny    |0|1|1
17|08m08s|Riverside|Sunny	   |1|2|2
18|23m57s|Riverside|Sunny    |10|10|6
19|11m28s|Riverside|Low-light|0|2|2
20|14m10s|Riverside|Low-light|0|3|3
21|24m01s|Riverside|Low-light|4|7|6
22|02m40s|Riverside|Low-light|0|2|1
23|19m24s|Riverside|Sunny    |2|4|4
24|08m39s|Riverside|Sunny    |2|3|3
25|24m05s|Riverside|Sunny    |4|8|8
26|07m26s|Riverside|Sunny    |0|5|5

### 02_Image+xml

`02_Image+xml` contains 7625 maritime images and the corresponding xml files for target detection network training. This dataset has only one class `vessel`.

## Download    

Link：https://pan.baidu.com/s/19R1qSq0xTBmER8tj9WcRGA

Extraction code：MIPC

## AIS Data Coordinate Transformation

* Copy the data into the `01_demo_transform/data` of this project.

* Run `01_demo_transformc/main.py`.

#### Example for Coordinate Transformation

Link：https://pan.baidu.com/s/1VBQc0QVNdOLGkpmqVZKSHg 

Extraction code：mipc 

#### Note that the AIS data in the example has been processed differently from the AIS data in the FVessel dataset.


https://user-images.githubusercontent.com/48637474/220854656-97ddb185-e33c-44d6-9379-0a03c2418751.mp4

(The blue line is the projection of the AIS data-based trajectory in the image, and the red letter is the corresponding mmsi number.)


## Evaluation

* Install [motmetrics](https://github.com/cheind/py-motmetrics).

* Copy the two files from the `02_demo_metric/motmetrics` of this project to the installed motmetrics folder.

* Save the test files to the `02_demo_metric/sample` folder.

* Choose the type of evaluation `detection`, `tracking`, and `fusion`.

* Run `02_demo_metric/eval.py`.

## DeepSORVF: Deep Learning-based Simple Online and Real-Time Vessel Data Fusion Method

The following videos show the data fusion results of our proposed [DeepSORVF](https://github.com/gy65896/DeepSORVF).

https://user-images.githubusercontent.com/48637474/220344086-5684a8e8-cb73-4786-a8dc-bdc9f68b5a35.mp4

## Acknowledgements

We deeply thank **Jianlong Su** from the School of Computer and Artificial Intelligence in Wuhan University of Technology who performs the data acquisition and algorithm implementation works.

## Future Work

We will capture more data of different scenes to expand the dataset.

## Citation

```
@article{guo2023asynchronous,
  title={Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways},
  author={Guo, Yu and Liu, Ryan Wen and Qu, Jingxiang and Lu, Yuxu and Zhu, Fenghua, and Lv, Yisheng},
  journal={arXiv preprint arXiv:2302.11283},
  year={2023}
}
```

#### If you have any questions, please get in touch with me (yuguo@whut.edu.cn & wenliu@whut.edu.cn).
