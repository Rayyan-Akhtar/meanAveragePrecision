# Function to compute IoU
def compute_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1g, y1g, x2g, y2g = box2

    xi1 = max(x1, x1g)
    yi1 = max(y1, y1g)
    xi2 = min(x2, x2g)
    yi2 = min(y2, y2g)
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2g - x1g) * (y2g - y1g)
    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area


# Function to compute precision, recall, F1 score, and IoU
def compute_metrics(detections, annotations, iou_threshold=0.5):
    print(detections, annotations)
    """_summary_

    Args:
        detections (_type_): list of lists, [[class id or classname score x1 y1 x2 y2], [class id or classname score x1 y1 x2 y2], ...]
        annotations (_type_): list of lists, [[class id or classname x1 y1 x2 y2], [class id or classname x1 y1 x2 y2], ...]
        iou_threshold (float, optional):. Defaults to 0.5.

    Returns:
        _type_: _description_
    """
    y_true = []
    y_pred = []

    for det, ann in zip(detections, annotations):
        print(det, ann)
        detected = [False] * len(det)
        true_positive = 0
        false_positive = 0
        false_negative = len(ann)

        for a in ann:
            matched = False
            for d in det:
                iou = compute_iou(d[2:], a[1:])
                if iou >= iou_threshold and d[0] == a[0]:
                    matched = True
                    break
            if matched:
                true_positive += 1
                false_negative -= 1
            else:
                false_positive += 1

        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        recall = true_positive / len(ann) if len(ann) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    average_precision = precision * recall

    return average_precision


def compute_mAP(AP: list, num_tasks: int):
    return (1/num_tasks) * sum(AP)