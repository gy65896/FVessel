## FVessel: Benchmark Dataset for Vessel Detection, Tracking, and Data Fusion 用于船舶检测、跟踪、数据融合的基准数据集

---

## 目录 Catalog
1. [数据集介绍 Dataset Introduction](#Introduction)
2. [数据集细节 Dataset Details](#Details)
3. [数据集下载 Dataset Download](#Download)
4. [评估 Evaluation](#Evaluation)
5. [引用 Citation](#Citation)

## Introduction
FVessel benchmark dataset is used to evaluate the reliability of AIS and video data fusion algorithms, which mainly contains 26 videos and corresponding AIS data captured by HIKVISION DS-2DC4423IW-D dome camera and Saiyang AIS9000-08 Class-B AIS receiver on the Wuhan Segment of the Yangtze. Since the Maritime Mobile Service Identity (MMSI) contains AIS data reveals the vessel identity, we replaced it with a random number. As shown in Figure 1, these videos were captured under many locations (e.g., bridge region and riverside) and various weather conditions (e.g., sunny, cloudy, and low-light).

![Figure04_FVessel](https://user-images.githubusercontent.com/48637474/210925024-15dcbcbe-717b-47b6-ad4b-377d71141380.jpg)
**Figure 1. Some samples of the FVessel dataset, which contains massive images and videos captured on the bridge region and riverside under the sunny, cloudy, and low-light conditions.**

## Details

FVessel dataset consists of two parts:
* __01_Video+AIS__
* __02_Image+xml__

### 01_Video+AIS
`01_Video+AIS` contains 26 videos and corresponding AIS data to evaluate the performance of the data fusion algorithm.
```
|视频名称 <br>   Video|视频时长 <br> Video Length| 类型 <br> Type| 天气 <br> Weather| 船舶遮挡次数 <br> Times of Occlusions| 船舶总数 <br> Total Number of Vessels| AIS船舶总数 <br> Number of Vessels with AIS|
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
```
Each video data contains the following files:
* __(a) AIS__


  __2022_05_10_19_21_04.csv__

  |序号<br>Number|MMSI|经度<br>Lon|纬度<br>Lat|航速<br>Speed|航向<br>Course|船首向<br>Heading|类型<br>Type|时间戳<br>Timestamp|
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

    |经度<br>Lon|纬度<br>Lat|水平朝向<br>Horizontal Orientation|俯仰角<br>Vertical Orientation|相机高度<br>Camera Height|水平视场角<br>Horizontal FoV|垂直视场角<br>Vertical FoV|
    | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
    114.32583|30.60139|7|-1|20| 55 | 30.94

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
FVessel数据集可在百度网盘中下载。         
链接: https://pan.baidu.com/s/1jcheiu2jArDzmHX0RhK6Fg     
提取码: MIPC    

## Evaluation

* Install [motmetrics](https://github.com/cheind/py-motmetrics).

* Copy the two files from the `motmetrics` of this project to the installed motmetrics folder.

* Save the test files to the `sample` folder.

* Choose the type of evaluation `detection`, `tracking`, and `fusion`.

* Run `eval.py`.

## Citation
```
@inproceedings{Guo2023video,
  title={},
  author={},
  booktitle={},
  year={2023}
}
```
#### If you have any questions, please get in touch with me (yuguo@whut.edu.cn).
