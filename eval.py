import motmetrics as mm
import numpy as np 
import os
import re

def detection(gt_file, ts_file):
    metrics = ['precision', 'recall']
    gt=mm.io.loadtxt(gt_file, fmt="mot15-2D")
    ts=mm.io.loadtxt(ts_file, fmt="mot15-2D")
    name=os.path.splitext(os.path.basename(ts_file))[0]
    acc=mm.utils.compare_to_groundtruth(gt, ts, 'iou', distth=0.7)
    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=metrics, name=name)
    return mm.io.render_summary(summary,namemap=mm.io.motchallenge_metric_names)
    
def tracking(gt_file, ts_file):
    metrics = ['mota','motp','idf1', 'idp', 'idr']
    gt=mm.io.loadtxt(gt_file, fmt="mot15-2D")
    ts=mm.io.loadtxt(ts_file, fmt="mot15-2D")
    name=os.path.splitext(os.path.basename(ts_file))[0]
    acc=mm.utils.compare_to_groundtruth(gt, ts, 'iou', distth=0.7)
    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=metrics, name=name)
    return mm.io.render_summary(summary,namemap=mm.io.motchallenge_metric_names)

def fusion(gt_file, ts_file):
    metrics = ['mota_fus','motp', 'idf1', 'precision', 'recall']
    gt=mm.io.loadtxt(gt_file, fmt="mot15-2D")
    ts=mm.io.loadtxt(ts_file, fmt="mot15-2D")
    name=os.path.splitext(os.path.basename(ts_file))[0]
    acc=mm.utils.compare_to_groundtruth_fus(gt, ts, 'iou', distth=0.7)
    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=metrics, name=name)
    return mm.io.render_summary(summary,namemap=mm.io.motchallenge_metric_names)


if '__main__':
    Type = 'fusion' # 'detection'|'tracking'|'fusion'
    
    if Type == 'detection':
        # 01 detection
        gt = './sample/Video-01_gt_detection.txt'
        ts = './sample/Video-01_re_detection.txt'
        result = detection(gt, ts)
        
    elif Type == 'tracking':
        # 02 tracking
        gt = './sample/Video-01_gt_tracking.txt'
        ts = './sample/Video-01_re_tracking.txt'
        result = tracking(gt, ts)
        
    elif Type == 'fusion':
        # 03 fusion
        gt = './sample/Video-01_gt_fusion.txt'
        ts = './sample/Video-01_re_fusion.txt'
        result = fusion(gt, ts)
    
    print(result)
