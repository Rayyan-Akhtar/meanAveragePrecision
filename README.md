<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://techpilot.ai/wp-content/uploads/2023/06/Open-Source-AI.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Mean Average Precision (mAP)</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This repository is to calculate mean Average Precision using the annotations and ground-truth from the object detection model. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

The following python packeges need to be installed.
```
tqdm
numpy
requests
yaml
```

### Installing

A step by step series of examples that tell you how to get a development env running.
```
Create .txt file for each input image and put it into the "cocodataset/detection-results". Similarly, make a .txt file with the same name and save it in the "cocodataset/ground-truth"

Content of these files:
"cocodataset/detection-results"
    00001.txt
    00002.txt
    .
    .
    .
    0000100.txt or whatever the name you like to give your files.

"cocodataset/ground-truth"
    00001.txt
    00002.txt
    .
    .
    .
    0000100.txt or whatever the name you like to give your files but the names should be same as in detection-results folder.
```

```
content of "cocodataset/detection-results" .txt file:
classname score x1 y1 x2 y2

content of "cocodataset/ground-truth" .txt file:
classname x1 y1 x2 y2

by running main.ipynb, the script will download COCO2017 val dataset images. Use these images to test your object detection model.
```

And repeat

```
until finished
```


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

Tsung-Yi Lin et al., 2014. Microsoft COCO: Common Objects in Context. CoRR, abs/1405.0312. Available at: http://arxiv.org/abs/1405.0312.

If this repository is helpful to you, please consider giving it a star and citing it in your own repository.
