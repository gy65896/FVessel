import pandas as pd
from geopy.distance import geodesic
import pyproj
from math import radians, cos, sin, asin, sqrt, tan, atan2, degrees
import math
import numpy as np
import cv2
from IPython import embed
import os

def count_distance(point1, point2, Type='m'):
    '''
    功能: 使用经纬度计算两点间的距离，单位m
    point1: 点1的经纬度（经度，纬度）
    point2: 点2的经纬度（经度，纬度）
    Type: nm——海里; m——米
    返回值: 二者之间的距离，单位为米
    '''
    # 计算两点间距离，单位m
    distance = geodesic(point1, point2).m  # 计算两经纬度之间的距离
    if Type == 'nm':
        # 将距离单位转换为nm
        distance = distance * 0.00054
    return distance


def getDegree(latA, lonA, latB, lonB):
    '''
    功能: 计算两点间方位角
    latA: 相机纬度
    LonA: 相机经度
    latB: 船舶纬度
    LonB: 船舶经度
    返回值: 方位角
    '''
    radLatA = radians(latA)
    radLonA = radians(lonA)
    radLatB = radians(latB)
    radLonB = radians(lonB)
    dLon = radLonB - radLonA
    y = sin(dLon) * cos(radLatB)
    x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLon)
    brng = degrees(atan2(y, x))
    brng = (brng + 360) % 360
    return brng

def visual_transform(lon_v, lat_v, camera_para, shape):
    '''
    功能: 计算两点间方位角
    lon_cam: 相机经度（单位）
    lat_cam: 相机纬度
    shoot_vdir： 相机垂直朝向向下倾斜多少度
    shoot_hdir: 水平朝向
    height_cam：相机距离水面高度
    width_pic：图片宽
    height_pic：图片高
    FOV_hor：水平视场角 55
    FOV_ver：垂直视场角
    返回值: 方位角
    '''
    # 初始化
    lon_cam = camera_para[0]
    lat_cam = camera_para[1]
    shoot_hdir = camera_para[2]
    shoot_vdir = camera_para[3]
    height_cam = camera_para[4]
    FOV_hor = camera_para[5]
    FOV_ver = camera_para[6]
    width_pic = shape[0]
    height_pic = shape[1]
    f_x = camera_para[7]
    f_y = camera_para[8]
    u0  = camera_para[9]
    v0  = camera_para[10]

    # 1.计算距离
    D_abs = count_distance((lat_cam, lon_cam), (lat_v, lon_v))
    
    # 2.计算水平夹角
    relative_angle = getDegree(lat_cam, lon_cam, lat_v, lon_v)
    Angle_hor = relative_angle - shoot_hdir
    if Angle_hor < -180:
        Angle_hor = Angle_hor + 360
    elif Angle_hor > 180:
        Angle_hor = Angle_hor - 360
    hor_rad = radians(Angle_hor)
    shv_rad = radians(-shoot_vdir)
    Z_w = D_abs*cos(hor_rad)
    X_w = D_abs*sin(hor_rad)
    Y_w = height_cam
    Z = Z_w/cos(shv_rad)+(Y_w-Z_w*tan(shv_rad))*sin(shv_rad)
    X = X_w
    Y = (Y_w-Z_w*tan(shv_rad))*cos(shv_rad)
    #print(X,Y,Z)
    target_x = int(f_x*X/Z+u0)
    target_y = int(f_y*Y/Z+v0)
    # 3.计算垂直夹角
    #Angle_ver = 90 + shoot_vdir - math.degrees(math.atan(D_abs / height_cam))
    #print(Angle_ver, shoot_vdir)
    # 4.计算坐标
    #target_x1 = int(width_pic // 2 + width_pic * Angle_hor / FOV_hor)
    #target_y1 = int(height_pic // 2 + height_pic * Angle_ver / FOV_ver)
    #print('new:')
    #print(target_x2, target_y2)
    #print('origion:')
    # print(Angle_hor)
    # print(target_x, target_y)
    return target_x, target_y

def data_filter(ais, camera_para):
    '''
    对推算后的数据进行筛选
    :param ais: 当前时刻的船舶数据
    :param lon_cam: 摄像头经度
    :param lat_cam: 摄像头纬度
    :param max_dis: 摄像头探测距离
    :return: 预处理后的当前时刻船舶数据
    '''
    # 初始化
    lon_cam = camera_para[0]
    lat_cam = camera_para[1]
    shoot_hdir = camera_para[2]
    shoot_vdir = camera_para[3]
    height_cam = camera_para[4]
    FOV_hor = camera_para[5]
    FOV_ver = camera_para[6]

    lon, lat = ais['lon'], ais['lat']
    D_abs = count_distance((lat_cam,lon_cam),(lat,lon))
    angle = getDegree(lat_cam, lon_cam, lat, lon)
    in_angle = abs(shoot_hdir - angle) if abs(shoot_hdir -
                        angle) < 180 else 360 - abs(shoot_hdir - angle)

    # 先进行相机垂直方向可视范围的判断，若垂直方向上在可视范围内，则再进行水平方向的判断
    if 90 + shoot_vdir - FOV_ver / 2 < math.degrees(math.atan(D_abs / height_cam)):
        # =============================================================================
        #         坐标转换及视觉轨迹筛选范围
        # =============================================================================
        # 相机水平方向可视范围判断，若在范围内，则返回1代表可进行坐标转换
        # 此处我们在相机水平方向的可视范围基础上适当增加相应角度
        # 处理船舶AIS数据位置相对船舶视频位置靠后的问题，以提高边缘船舶融合效果
        if in_angle <= (FOV_hor / 2 + 8):  # 此处“+x”为相应增加的角度
            return 'transform'
        # 若当前AIS数据超出设定的扇形角度(可视角度+相应增加的角度)，则不进行坐标转换。
        # 返回0,删除掉超出该范围的视觉轨迹
        elif in_angle > (FOV_hor / 2 + 8):
            return 'visTraj_del'
        # =============================================================================
        #         AIS数据筛选范围
        # =============================================================================
        # 如果当前AIS数据在更大范围的扇形范围内，则将此AIS数据删掉，不做考虑
        if in_angle > (FOV_hor / 2 + 12):
            return 'ais_del'


def transform(AIS_current, AIS_vis, camera_para, shape):
    '''
    功能: 将AIS数据转换至图像坐标系
    :param AIS_current: 当前AIS数据
    :param AIS_vis: 含有图像坐标的AIS数据
    :return: 当前处理后的AIS数据转换到图像坐标系中的AIS数据
    '''
    # 1.数据初始化
    
    AIS_visCurrent = pd.DataFrame(columns=['mmsi','lon',\
                                'lat','speed','course','heading','type','x','y','timestamp'])
    # 2.遍历所有数据
    for index, ais in AIS_current.iterrows():
        # 判断数据是否可以进行转换
        flag = data_filter(ais, camera_para)
        # 情况1: 坐标转换
        if flag == 'transform':
            x, y = visual_transform(ais['lon'], ais['lat'], camera_para, shape)
            ais['x'], ais['y'] = x, y
            AIS_visCurrent = AIS_visCurrent.append(ais, ignore_index=True)
            
        # 情况2: 数据删除
        elif flag == 'visTraj_del' or flag == 'ais_del':
            AIS_vis = AIS_vis.drop(AIS_vis[AIS_vis['mmsi'] == ais['mmsi']].index)
        AIS_vis = AIS_vis.append(AIS_visCurrent, ignore_index=True)
    return AIS_vis