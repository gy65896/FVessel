import os, time, imutils, cv2, argparse
import pandas as pd
import numpy as np
from utils.file_read import read_all, ais_initial, update_time, time2stamp
from utils.AIS_utils import transform
from utils.draw_org import draw_traj
sum_t = []

def main(arg):
    # 输出ais文件列表，从第几个开始数，时间戳，时间
    ais_file, timestamp0, time0 = ais_initial(arg.ais_path,arg.initial_time)
    Time = arg.initial_time.copy()
    # =============================================================================
    # 其他参数初始化
    # cap: 视频读取
    # fps: 帧率
    # t: 每帧持续时间
    # AIS: AIS处理初始化
    # VIS: VIS处理初始化
    # FUS: FUS处理初始化
    # name: 显示视频框的名称
    # show_size: 视频展示时的图像尺寸
    # videoWriter: 保存视频（None）
    # time_long: 视频运行时间
    # bin_inf: 绑定数据
    # =============================================================================
    
    cap = cv2.VideoCapture(arg.video_path)
    im_shape = [cap.get(3), cap.get(4)]
    max_dis = min(im_shape)//2
    fps = int(cap.get(5))
    t = int(1000/fps)
    
    name = 'demo'
    show_size = 1000
    videoWriter = None
    bin_inf = pd.DataFrame(columns=['ID', 'mmsi', 'timestamp', 'match'])
    AIS_vis = pd.DataFrame(columns=['mmsi','lon',\
                                'lat','speed','course','heading','type','x','y','timestamp'])

    # =============================================================================
    #  视频读取
    # =============================================================================
    print('Start Time: %s || Stamp: %d || fps: %d' % (time0, timestamp0, fps))
    pp = 0
    sum_time = 0
    if not os.path.exists(arg.result_video.split('/')[1]):
        os.mkdir(arg.result_video.split('/')[1])
    global sum_t
    
    while True:
        # 逐帧读取
        _, im = cap.read()
        if im is None:
            break
        start = time.time()
        
        # 更新时间戳
        Time, timestamp, Time_name = update_time(Time, t)
        
        # 读取ais数据
        try:
            path = arg.ais_path + '/' + Time_name[:-4] + '.csv'
            ais_data = pd.read_csv(path, usecols=[1, 2, 3, 4, 5, 6, 7, 8], header=0)
        except:
            ais_data = pd.DataFrame(columns=['mmsi','lon',\
                                    'lat','speed','course','heading','type','timestamp'])

        # 坐标转换
        AIS_vis = transform(ais_data,AIS_vis,arg.camera_para,im_shape)
        end = time.time() - start
        sum_time = sum_time + end

        if timestamp % 1000 < t:
            pp = pp+1
            sum_t.append(sum_time)
            print('Time: %s || Stamp: %d || Process: %.6f || Average: %.6f +- %.6f'%(Time_name, timestamp, sum_time,np.mean(sum_t),np.std(sum_t)))
            sum_time = 0
        # 绘制
        im = draw_traj(im, AIS_vis, timestamp)
        
        # =============================================================================
        #  视频展示
        # =============================================================================
        result = im
        result = imutils.resize(result, height=show_size)
        if videoWriter is None:
            fourcc = cv2.VideoWriter_fourcc(
                'm', 'p', '4', 'v')
            videoWriter = cv2.VideoWriter(
                arg.result_video, fourcc, fps, (result.shape[1], result.shape[0]))
        videoWriter.write(result)
        # if timestamp % 1000 < t:
        #     cv2.imwrite(arg.result_video[:-4]+'_'+Type+'/%04d_%s.png'%(pp,Type),im)
        cv2.imshow(name, result)
        cv2.waitKey(1)
        if cv2.getWindowProperty(name, cv2.WND_PROP_AUTOSIZE) < 1:
        # 点x退出
            break   
    cap.release()
    videoWriter.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    path = './data/clip-%02d'%(1)
    print(path)
    video_path, ais_path, result_video, initial_time, camera_para = read_all(path)
    # =============================================================================
    #     该开关定义了所有需要修改的参数
    # =============================================================================
    parser = argparse.ArgumentParser(description = "VesselSORT")
    
    parser.add_argument("--prepare_time", type=int, default = 1) # 准备时间
    parser.add_argument("--anti", type=int, default = 1) # 是否抗遮挡
    parser.add_argument("--val", type=int, default = 0) # 遮挡系数
    
    parser.add_argument("--video_path", type=str, default = video_path) # 视频路径
    parser.add_argument("--ais_path", type=str, default = ais_path) # ais路径
    parser.add_argument("--result_video", type=str, default = result_video) #视频保存名称
    parser.add_argument("--initial_time", type=list, default = initial_time) #初始时间
    parser.add_argument("--camera_para", type=list, default = camera_para) # 相机参数

    argspar = parser.parse_args()
    
    print("\nVesselSORT")
    for p, v in zip(argspar.__dict__.keys(), argspar.__dict__.values()):
        print('\t{}: {}'.format(p, v))
    print('\n')
    arg = parser.parse_args()
    
    main(arg)
