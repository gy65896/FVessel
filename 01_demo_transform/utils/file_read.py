import os, time, glob, re
from datetime import datetime

def time2stamp(Time):
    name = "%d_%02d_%02d_%02d_%02d_%02d_%03d"%(Time[0],Time[1],Time[2],Time[3],Time[4],Time[5],Time[6])
    datetime_obj = datetime.strptime(name, "%Y_%m_%d_%H_%M_%S_%f")
    timeStamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return timeStamp, name

def update_time(Time, t):
    Time[6] = Time[6] + t
    if Time[6]>=1000:
        Time[5] = Time[5] + 1
        Time[6] = Time[6] - 1000
        if Time[5]>=60:
            Time[4] = Time[4] + 1
            Time[5] = Time[5] - 60
            if Time[4]>=60:
                Time[3] = Time[3] + 1
                Time[4] = Time[4] - 60
    timeStamp, name = time2stamp(Time)
    return Time, timeStamp, name


def read_all(path):
    name = path.split('/')[-1]
    video_path = glob.glob(path+'/*.mp4') + glob.glob(path+'/*.avi')
    print(video_path)
    video_path = video_path[0]
    v_p = re.split('[\.\-\_\\\]',video_path)
    print(v_p)
    ais_path = path+'/ais'
    result_video = './result/out_%s.mp4'%(name)

    initial_time = [int(v_p[-11]), int(v_p[-10]), int(v_p[-9]),\
                        int(v_p[-8]), int(v_p[-7]), int(v_p[-6]), 0]

    
    with open(glob.glob(path+'/*.txt')[0], "r") as f:
        camera_para = f.readlines()[0][1:-2]
        camera_para = camera_para.split(',')
        camera_para = list(map(float,camera_para))
    
    return video_path, ais_path, result_video, initial_time, camera_para

def ais_initial(ais_path, initial_time):
    ais_file = os.listdir(ais_path)
    timestamp0, time0 = time2stamp(initial_time)

    return ais_file, timestamp0, time0