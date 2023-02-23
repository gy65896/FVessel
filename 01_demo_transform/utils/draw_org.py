import pandas as pd
import cv2
from IPython import embed

def draw_traj(pic, AIS_vis, timestamp):
    add_img = pic.copy()
    tl = None or round(
        0.002 * (pic.shape[0] + pic.shape[1]) / 2) + 1
    tf = max(tl - 1, 1)  # font thickness
    mmsi_list = AIS_vis['mmsi'].unique()
    # 画ais线
    for k in range(len(mmsi_list)):
        ais_current = AIS_vis[AIS_vis['mmsi'] == mmsi_list[k]].reset_index(drop=True)
        for i in range(ais_current.shape[0] - 1):
            cv2.line(add_img, (int(ais_current['x'][i]), int(ais_current['y'][i])),\
                (int(ais_current['x'][i+1]), int(ais_current['y'][i+1])), (255,0,0), 3)   
        cv2.putText(add_img, 'MMSI:{}'.format(int(ais_current['mmsi'][ais_current.shape[0] - 1])),\
                            (int(ais_current['x'][ais_current.shape[0] - 1]), int(ais_current['y'][ais_current.shape[0] - 1]) - 2), 0, tl / 6,\
                                [0, 0, 255], thickness=tf, lineType=cv2.LINE_AA)
    # 画vis框和匹配信息
    # id_list = Vis_cur['ID'].unique()
    # for k in range(len(id_list)):
    #     id_current = Vis_tra[Vis_tra['ID'] == id_list[k]].reset_index(drop=True)
    #     last = len(id_current)-1
    #     if last != -1:
    #         if id_current['timestamp'][last] == timestamp//1000:
    #             cv2.rectangle(add_img, (id_current['x1'][last],id_current['y1'][last]),\
    #                           (id_current['x2'][last],id_current['y2'][last]), (0,0,255), thickness=2, lineType=cv2.LINE_AA)
    #             cv2.putText(add_img, 'ID:{}'.format(int(id_current['ID'][last])), \
    #                     (id_current['x1'][last], id_current['y2'][last] + 25), 0, tl / 8, \
    #                     [0, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
    #             if len(fusion_list) != 0:
    #                 fusion_current = fusion_list[fusion_list['ID'] == id_current['ID'][last]].reset_index(drop=True)
    #                 if len(fusion_current) != 0:
    #                     cv2.putText(add_img, 'MMSI:{}'.format(int(fusion_current['mmsi'][0])),\
    #                         (id_current['x1'][last], id_current['y1'][last] - 2), 0, tl / 8,\
    #                             [0, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
    #                     cv2.putText(add_img, 'ID:{}'.format(int(fusion_current['ID'][0])),\
    #                         (id_current['x1'][last], id_current['y1'][last] - 25), 0, tl / 8,\
    #                             [0, 0, 0], thickness=tf, lineType=cv2.LINE_AA)

    #             for i in range(id_current.shape[0] - 1):
    #                 cv2.line(add_img, (int(id_current['x'][i]), int(id_current['y'][i])),\
    #                          (int(id_current['x'][i+1]), int(id_current['y'][i+1])), (0,255,0), 3) 
    #             cv2.putText(add_img, 'ID:{}'.format(int(id_current['ID'][0])),\
    #                         (int(id_current['x'][id_current.shape[0] - 1]), int(id_current['y'][id_current.shape[0] - 1]) - 2), 0, tl / 6,\
    #                             [0, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
    return add_img