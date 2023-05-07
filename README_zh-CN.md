# <p align=center> FVessel: 用于船舶检测、跟踪、数据融合的基准数据集</p>

<div align="center">

[![Paper](https://img.shields.io/badge/arXiv-Paper-red.svg)](https://arxiv.org/abs/2302.11283)
[![Code](https://img.shields.io/badge/DeepSORVF-Code-orange.svg)](https://github.com/gy65896/DeepSORVF)
[![English](https://img.shields.io/badge/英文-English-green.svg)](README.md)

</div>

---

>**内河船舶交通监管中基于异步轨迹匹配的多模态海事数据融合**<br> 郭彧, [刘文](http://mipc.whut.edu.cn/index.html), 瞿晶祥, 卢煜旭, 朱凤华, 吕宜生 <br> 
>arXiv preprint arXiv:2302.11283

> **简介：** *FVessel基准数据集用于评估AIS和视频数据融合算法的可靠性，主要包含海康威视DS-2DC4423IW-D球型摄像机和赛扬AIS9000-08 B类AIS接收机在武汉长江段拍摄的26个视频和相应的AIS数据。为了保护隐私，在我们的数据集中每艘船的 MMSI 已替换为随机数。图1展了FVessel数据集的部分样本。*

## 新闻 🚀
* **2023.05.07**: 9个融合数据(Video-27~Video-35)和3728张用于检测的图片被采集，新的数据将在不久后公开。
* **2023.01.12**: 我们公开了FVessel_V1.0数据集，其中包含26个融合数据和7625张用于检测的图像。

## 样本
![Figure04_FVessel](https://user-images.githubusercontent.com/48637474/210925024-15dcbcbe-717b-47b6-ad4b-377d71141380.jpg)

## 细节

FVessel数据集包含两部分:
* __01_Video+AIS__
* __02_Image+xml__

### 01_Video+AIS
`01_Video+AIS`包含大量个视频和对应的AIS数据以评估数据融合算法的性能。每一个视频数据包含如下文件:
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

* __(a) AIS文件__

  每个csv文件包含十分钟内的AIS数据并且仅保存每艘船舶最近时刻的数据。

  __2022_05_10_19_21_04.csv__

  |序号|MMSI|经度|纬度|航速|航向|船首向|类型|时间戳|
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  0|100000000|114.325327|30.60166 |0  |293.6|511|18|1652181559844
  1|130000000|114.302683|30.58059 |6.8|33.6 |33 |18|1652181659157
  2|140000000|114.31004 |30.599997|3.9|215.6|511|18|1652181655147
  3|600000000|114.3156  |30.59773 |7.2|39.6 |511|18|1652181649704
  ...|...|...|... |...|... |...|...|...

  __2022_05_10_19_21_05.csv__   
  __2022_05_10_19_21_06.csv__   
  __...__

 * __(b) 视频__

    __2022_05_10_19_21_05_19_31_10_b.mp4__  
    
    开始时间: 2022_05_10_19_21_05
    结束时间: 2022_05_10_19_31_10
    类型: b/r (桥区/江边)
   
  * __(c) 相机参数__
  
    __camera_para.txt__

    |经度|纬度|水平朝向|俯仰角|相机高度|水平视场角|垂直视场角|fx|fy|u0|v0|
    | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
    114.32583|30.60139|7|-1|20| 55 | 30.94 | 2391.26 | 2446.89 | 1305.04 | 855.214 |
    
    fx, fy, u0, 和v0是相机内参矩阵。
* __(d) GT (真实情况：采用多目标跟踪MOT格式)__
    
    __Video-02_gt.mp4__
    
    包含真实情况的视频，每秒仅一次。
    
    __Video-02_gt_detection.txt__
    
    ```
    <秒>, <0>, <边界框_左>, <边界框_上>, <边界框_宽度>, <边界框_高度>, <置信度>, <x>, <y>, <z>
    ```
    
    __Video-02_gt_tracking.txt__
    
    ```
    <秒>, <id号>, <边界框_左>, <边界框_上>, <边界框_宽度>, <边界框_高度>, <置信度>, <x>, <y>, <z>
    ```
    
    __Video-02_gt_fusion.txt__
    
    ```
    <秒>, <mmsi>, <边界框_左>, <边界框_上>, <边界框_宽度>, <边界框_高度>, <置信度>, <x>, <y>, <z>
    ```

* __V1.0 (26个视频)__

  

  |视频名称|视频时长|类型|天气|船舶遮挡次数|船舶总数|AIS船舶总数|
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  01|10m07s|桥区|弱光|2|5|4
  02|19m52s|桥区|晴天|6|7|6
  03|19m14s|江边|晴天|6|5|5
  04|06m10s|江边|晴天|0|1|1
  05|15m01s|江边|晴天|2|5|5
  06|12m49s|江边|晴天|2|4|4
  07|03m38s|江边|晴天|1|2|2
  08|16m05s|江边|晴天|3|6|5
  09|05m25s|江边|晴天|0|1|1
  10|11m17s|桥区|多云|2|3|1
  11|05m18s|江边|晴天|1|3|3
  12|07m19s|江边|晴天|1|4|4
  13|12m58s|江边|晴天|5|6|6
  14|03m58s|江边|晴天|3|4|4
  15|10m46s|江边|晴天|0|4|4
  16|05m05s|江边|晴天|0|1|1
  17|08m08s|江边|晴天|1|2|2
  18|23m57s|江边|晴天|10|10|6
  19|11m28s|江边|弱光|0|2|2
  20|14m10s|江边|弱光|0|3|3
  21|24m01s|江边|弱光|4|7|6
  22|02m40s|江边|弱光|0|2|1
  23|19m24s|江边|晴天|2|4|4
  24|08m39s|江边|晴天|2|3|3
  25|24m05s|江边|晴天|4|8|8
  26|07m26s|江边|晴天|0|5|5



### 02_Image+xml

`02_Image+xml`包含大量海事图像以及对应的用于目标检测网络训练的xml文件，该数据集只有一类"vessel"。

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

* __V1.0 (7625张图像)__

## 下载

FVessel_V1.0：[[MIPC](https://pan.baidu.com/s/19R1qSq0xTBmER8tj9WcRGA)] 

## AIS数据坐标转换

* 将数据复制到本项目的`01_demo_transform/data`路径下.

* 运行`01_demo_transformc/main.py`.

#### 坐标转换示例

案例：[[mipc](https://pan.baidu.com/s/1VBQc0QVNdOLGkpmqVZKSHg)]

#### 请注意: 与 FVessel 数据集中的 AIS 数据不同，示例中的 AIS 数据的已经被处理。

https://user-images.githubusercontent.com/48637474/220854656-97ddb185-e33c-44d6-9379-0a03c2418751.mp4

(蓝线是基于AIS数据的轨迹在图像中的投影，红色字母是对应的mmsi号。)

## 指标评估

* 安装[motmetrics](https://github.com/cheind/py-motmetrics)；

* 将此项目的`02_demo_metric/motmetrics`中的两个文件复制到已安装的motmetrics文件夹中；

* 将测试文件保存到`02_demo_metric/sample`文件夹；

* 选择评估类型`detection`, `tracking`, 和`fusion`；

* 运行`02_demo_metric/eval.py`。

## DeepSORVF: 基于深度学习的简单在线实时船舶数据融合方法

以下视频展示了我们提出的 DeepSORVF 数据融合结果。

https://user-images.githubusercontent.com/48637474/220344086-5684a8e8-cb73-4786-a8dc-bdc9f68b5a35.mp4

## 致谢

非常感谢武汉理工大学计算机与人工智能学院的**苏建龙**进行的数据采集和算法实现工作。

## 未来工作

我们将采集更多不同场景的数据以扩充数据集。

## 引用

```
@article{guo2023asynchronous,
  title={Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways},
  author={Guo, Yu and Liu, Ryan Wen and Qu, Jingxiang and Lu, Yuxu and Zhu, Fenghua, and Lv, Yisheng},
  journal={arXiv preprint arXiv:2302.11283},
  year={2023}
}
```

#### 如果您有更多问题，请联系我们(yuguo@whut.edu.cn & wenliu@whut.edu.cn)。
