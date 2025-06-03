# <p align=center> [TITS 2023] FVessel: Benchmark Dataset for Vessel Detection, Tracking, and Data Fusion</p>

<div align="center">

[![Paper](https://img.shields.io/badge/PDF-Paper-red.svg)](https://ieeexplore.ieee.org/abstract/document/10159572)
[![Web](https://img.shields.io/badge/DeepSORVF-Web-blue.svg)](https://gy65896.github.io/projects/TITS2023_DeepSORVF/index.html)
[![Code](https://img.shields.io/badge/DeepSORVF-Code-orange.svg)](https://github.com/gy65896/DeepSORVF)
[![Chinese](https://img.shields.io/badge/简体中文-Chinese-green.svg)](README_zh-CN.md)
<!--[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgy65896%2FFVessel&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visitor&edge_flat=false)](https://hits.seeyoufarm.com)-->

</div>

---

>**Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways** <br>
>[Yu Guo](https://scholar.google.com/citations?user=klYz-acAAAAJ&hl=zh-CN), [Ryan Wen Liu](http://mipc.whut.edu.cn/index.html)<sup>* </sup>, [Jingxiang Qu](https://scholar.google.com/citations?user=9zK-zGoAAAAJ&hl=zh-CN), [Yuxu Lu](https://scholar.google.com/citations?user=XXge2_0AAAAJ&hl=zh-CN), Fenghua Zhu*, Yisheng Lv <br>
>(* Corresponding Author) <br> 
>IEEE Transactions on Intelligent Transportation Systems

> **Introduction:** *The FVessel benchmark dataset is used to evaluate the reliability of AIS and video data fusion algorithms, which mainly contains 26 videos and the corresponding AIS data captured by the HIKVISION DS-2DC4423IW-D dome camera and Saiyang AIS9000-08 Class-B AIS receiver on the Wuhan Segment of the Yangtze River. To protect privacy, the MMSI for each vessel has been replaced with a random number in our dataset. As shown in Figure 1, these videos were captured under many locations (e.g., bridge region and riverside) and various weather conditions (e.g., sunny, cloudy, and low-light).*
<hr />

## News 🚀
* **2024.07.20**: [New Website](https://gy65896.github.io/projects/TITS2023_DeepSORVF/index.html) is created.
* **2024.04.03**: FVessel dataset is included in the [CVonline: Image Databases](https://homepages.inf.ed.ac.uk/rbf/CVonline/Imagedbase.htm) at the University of Edinburgh.
* **2023.08.01**: 9 fusion data (Video-27~Video-35) have marked. When requesting the FVessel2.0, please contact us using your institutional or school email address exclusively for research purposes.
* **2023.06.08**: "Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways" has been accepted by IEEE Transactions on Intelligent Transportation Systems.
* **2023.05.07**: 9 fusion data (Video-27~Video-35) and 3728 images for detection are captured.
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
     |-2022_05_10_19_21_04.csv
        |-[Number, MMSI, Lon, Lat, Speed, Course, Heading, Type, Timestamp]
        └─...
     |-2022_05_10_19_21_05.csv
     |-2022_05_10_19_21_06.csv
     └─... (ais data)
|-2022_05_10_19_21_05_19_31_10_b.mp4
|-camera_para.txt
   |-[Lon, Lat, Horizontal Orientation, Vertical Orientation, Camera Height, Horizontal FoV, Vertical FoV, fx, fy, u0, v0]
|-gt
     |-Video-02_gt.mp4
     |-Video-02_gt_detection.txt
        |-<second>, <0>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
        └─...
     |-Video-02_gt_tracking.txt
        |-<second>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
        └─...
     └─Video-02_gt_fusion.txt
        |-<second>, <mmsi>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
        └─...
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

* __V1.0 (26 videos)__

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

* __V2.0 (9 videos)__


### 02_Image+xml

`02_Image+xml` contains many maritime images and the corresponding xml files for target detection network training. This dataset has only one class `vessel`.

```
|-JPEGImages
     |-000001.png
     |-000002.png
     |-000003.png
     └─... (image data)
|-Annotations
     |-000001.xml
        |-<vessel>, <x1>, <y1>, <x2>, <y2>
        └─...
     |-000002.xml
     |-000003.xml
     └─... (xml data)
└─-ImageSets
```

* __V1.0 (7625 images)__

## Download

**FVessel_V1.0** 

|Name|***Baidu Skydisk***|***Onedrive***|
| :-: | :-: | :-: |
|link|[https://pan.baidu.com/s/1-VNeZvWqYh7ESLXQxreCDg](https://pan.baidu.com/s/1-VNeZvWqYh7ESLXQxreCDg)|[https://1drv.ms/u/s!As3rCDROnrbLeWE-RMXAGbwAMa4](https://1drv.ms/u/s!As3rCDROnrbLeWE-RMXAGbwAMa4)|
|code|MIPC||

**FVessel_V2.0**

[onedrive](https://1drv.ms/u/c/cbb69e4e3408ebcd/Ec3rCDROnrYggMt6AAAAAAABp7ya-82994C3cOKucHX2Yg?e=r7DCJG)

## AIS Data Coordinate Transformation

* Copy the data into the `01_demo_transform/data` of this project.

* Run `01_demo_transformc/main.py`.

#### Example for Coordinate Transformation

Example: [[mipc](https://pan.baidu.com/s/1VBQc0QVNdOLGkpmqVZKSHg)]

#### Note that the AIS data in the example has been processed differently from the AIS data in the FVessel dataset.


https://github.com/gy65896/FVessel/assets/48637474/78f2409b-7148-46ec-9bff-bd796c73cb9a



(The blue line is the projection of the AIS data-based trajectory in the image, and the red letter is the corresponding mmsi number.)


## Evaluation

* Install [motmetrics](https://github.com/cheind/py-motmetrics).

* Copy the two files from the `02_demo_metric/motmetrics` of this project to the installed motmetrics folder.

* Save the test files to the `02_demo_metric/sample` folder.

* Choose the type of evaluation `detection`, `tracking`, and `fusion`.

* Run `02_demo_metric/eval.py`.

## DeepSORVF: Deep Learning-based Simple Online and Real-Time Vessel Data Fusion Method

The following videos show the data fusion results of our proposed [DeepSORVF](https://github.com/gy65896/DeepSORVF).

https://github.com/gy65896/FVessel/assets/48637474/8fa420ff-9621-4b88-8b2a-59fc5edc0571



## Acknowledgements

We deeply thank **Jianlong Su** from the School of Computer and Artificial Intelligence in Wuhan University of Technology who performs the data acquisition and algorithm implementation works.

## Future Work

We will capture more data of different scenes to expand the dataset.

## Citation

```
@article{guo2023asynchronous,
  title={Asynchronous trajectory matching-based multimodal maritime data fusion for vessel traffic surveillance in inland waterways},
  author={Guo, Yu and Liu, Ryan Wen and Qu, Jingxiang and Lu, Yuxu and Zhu, Fenghua and Lv, Yisheng},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  volume={24},
  number={11},
  pages={12779--12792},
  year={2023}
```

#### If you have any questions, please get in touch with me (guoyu65896@gmail.com).

</div>
<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/gy65896_FVessel/count.svg" />
</p>
