## FVessel: Benchmark Dataset for Vessel Detection, Tracking, and Data Fusion

---
### Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways [[Paper](http://arxiv.org/abs/2302.11283)]

![video](https://user-images.githubusercontent.com/48637474/220859261-33458b91-2f2b-4d58-8c26-73610c53ca37.gif)



## Introduction
English | [简体中文](README_zh-CN.md)

The FVessel benchmark dataset is used to evaluate the reliability of AIS and video data fusion algorithms, which mainly contains 26 videos and the corresponding AIS data captured by the HIKVISION DS-2DC4423IW-D dome camera and Saiyang AIS9000-08 Class-B AIS receiver on the Wuhan Segment of the Yangtze River. To protect privacy, the MMSI for each vessel has been replaced with a random number in our dataset. As shown in Figure 1, these videos were captured under many locations (e.g., bridge region and riverside) and various weather conditions (e.g., sunny, cloudy, and low-light).

![Figure04_FVessel](https://user-images.githubusercontent.com/48637474/210925024-15dcbcbe-717b-47b6-ad4b-377d71141380.jpg)
**Figure 1. Some samples of the FVessel dataset, which contains massive images and videos captured on the bridge region and riverside under sunny, cloudy, and low-light conditions.**

## Details

The FVessel dataset consists of two parts:
* __01_Video+AIS__
* __02_Image+xml__

### 01_Video+AIS
`01_Video+AIS` contains 26 videos and the corresponding AIS data to evaluate the performance of the data fusion algorithm.

|Video|Video Length|Type|Weather|Times of Occlusions|Total Number of Vessels|Number of Vessels with AIS|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
video-01|10m07s|Bridge   |Low-light|2|5|4
video-02|19m52s|Bridge   |Sunny    |6|7|6
video-03|19m14s|Riverside|Sunny    |6|5|5
video-04|06m10s|Riverside|Sunny    |0|1|1
video-05|15m01s|Riverside|Sunny    |2|5|5
video-06|12m49s|Riverside|Sunny    |2|4|4
video-07|03m38s|Riverside|Sunny    |1|2|2
video-08|16m05s|Riverside|Sunny    |3|6|5
video-09|05m25s|Riverside|Sunny    |0|1|1
video-10|11m17s|Bridge   |Cloudy   |2|3|1
video-11|05m18s|Riverside|Sunny    |1|3|3
video-12|07m19s|Riverside|Sunny    |1|4|4
video-13|12m58s|Riverside|Sunny    |5|6|6
video-14|03m58s|Riverside|Sunny    |3|4|4
video-15|10m46s|Riverside|Sunny    |0|4|4
video-16|05m05s|Riverside|Sunny    |0|1|1
video-17|08m08s|Riverside|Sunny	   |1|2|2
video-18|23m57s|Riverside|Sunny    |10|10|6
video-19|11m28s|Riverside|Low-light|0|2|2
video-20|14m10s|Riverside|Low-light|0|3|3
video-21|24m01s|Riverside|Low-light|4|7|6
video-22|02m40s|Riverside|Low-light|0|2|1
video-23|19m24s|Riverside|Sunny    |2|4|4
video-24|08m39s|Riverside|Sunny    |2|3|3
video-25|24m05s|Riverside|Sunny    |4|8|8
video-26|07m26s|Riverside|Sunny    |0|5|5

Each video data contains the following files:
* __(a) AIS__


  __2022_05_10_19_21_04.csv__

  |Number|MMSI|Lon|Lat|Speed|Course|Heading|Type|Timestamp|
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  0|100000000|114.325327|30.60166 |0  |293.6|511|18|1652181559844
  1|130000000|114.302683|30.58059 |6.8|33.6 |33 |18|1652181659157
  2|140000000|114.31004 |30.599997|3.9|215.6|511|18|1652181655147
  3|600000000|114.3156  |30.59773 |7.2|39.6 |511|18|1652181649704
  ...|...|...|... |...|... |...|...|...

  __2022_05_10_19_21_05.csv__   
  __2022_05_10_19_21_06.csv__   
  __...__
  
  
    (Each csv file contains the AIS data received within ten minutes, and only the most recent data is kept.)
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

### 02_Image+xml

`02_Image+xml` contains 7625 maritime images and the corresponding xml files for target detection network training. This dataset has only one class `vessel`.

## Download
We only publish four videos and AIS data from `01_Video+AIS`. If you need more datasets, please contact us.     

Link：https://pan.baidu.com/s/1yeY1Igund8gjTnqZsyqI_A 

Extraction code：oinv 

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

The following videos show the data fusion results of our proposed DeepSOORVF.

https://user-images.githubusercontent.com/48637474/220344086-5684a8e8-cb73-4786-a8dc-bdc9f68b5a35.mp4


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
