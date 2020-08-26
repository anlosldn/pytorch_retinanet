from typing import *

# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# `Generalized RCNN` Input  Transformation Options
# -----------------------------------------------------------------------------
MEAN: List[float] = [0.485, 0.456, 0.406]
# `Mean values` used for input normalization.
STD: List[float] = [0.229, 0.224, 0.225]
# `STD values` used for input normalization.
MIN_IMAGE_SIZE: int = 600
# `Minimum size` of the image to be rescaled before feeding it to the backbone
MAX_IMAGE_SIZE: int = 1333
# `Maximum` size of the image to be rescaled before feeding it to the backbone


# -----------------------------------------------------------------------------
# `Anchor Generator` Flags
# -----------------------------------------------------------------------------
ANCHOR_SIZES: List[float] = [
    [x, x * 2 ** (1 / 3), x * 2 ** (2 / 3)] for x in [32, 64, 128, 256, 512]
]
# Anchor sizes (i.e. sqrt of area) in absolute pixels w.r.t. the network input.
ANCHOR_STRIDES: List[int] = [8, 16, 32, 64, 128]
# A list of float value representing the strides for each feature
# map in the feature pyramid.
ANCHOR_OFFSET: float = 0.0
# Relative offset between the center of the first anchor and the top-left corner of the image
# Value has to be in [0, 1). Recommend to use 0.5, which means half stride.
# The value is not expected to affect model accuracy.
ANCHOR_ASPECT_RATIOS: List[float] = [0.5, 1.0, 2.0]
# Anchor aspect ratios. For each area given in `SIZES`, anchors with different aspect
# ratios are generated by an anchor generator.
IOU_THRESHOLDS_FOREGROUND: float = 0.5
IOU_THRESHOLDS_BACKGROUND: float = 0.4

# -----------------------------------------------------------------------------
# `RetinaNet` Options
# -----------------------------------------------------------------------------
NUM_CLASSES: int = 80
# This is the number of foreground classes.

# The network used to compute the features for the model.
# Should be one of ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet101', 'resnet152'].
BACKBONE: str = "resnet18"

# Prior prob for rare case (i.e. foreground) at the beginning of training.
# This is used to set the bias for the logits layer of the classifier subnet.
# This improves training stability in the case of heavy class imbalance.
PRIOR: float = 0.01

# Wether the backbone should be pretrained or not,. If true loads `pre-trained`
# weights from `Imagenet`
PRETRAINED_BACKBONE: bool = True

# Inference cls score threshold, only anchors with score > INFERENCE_TH are
# considered for inference (to improve speed)
SCORE_THRES: float = 0.05
MAX_DETECTIONS_PER_IMAGE: int = 1000
NMS_THRES: float = 0.5

# Wether to freeze `BatchNormalization` layers of `backbone`
FREEZE_BN: bool = True

# Loss parameters
FOCAL_LOSS_GAMMA: float = 2.0
FOCAL_LOSS_ALPHA: float = 0.25
SMOOTH_L1_LOSS_BETA: float = 0.1