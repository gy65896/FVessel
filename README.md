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
|视频名称    Video|视频时长 <br> Video Length| 类型 Type| 天气 Weather| 船舶遮挡次数 Times of Occlusions| 船舶总数 Total Number of Vessels| AIS船舶总数 Number of Vessels with AIS|
| :----- | :----- | :----- | :----- | :----- | :----- | :----- |
video | 10m07s |  Bridge|Low-light|2|5|4



## Download
FVessel数据集可在百度网盘中下载。         
链接: https://pan.baidu.com/s/1jcheiu2jArDzmHX0RhK6Fg     
提取码: MIPC    

## Evaluation

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
