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
    metrics = ['mota','idf1', 'idp', 'idr']
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
    # detection
    gt = './Video-01_gt_fusion.txt'
    ts = './Video-01_re_fusion.txt'
    result = fusion(gt, ts)
    print(result)
