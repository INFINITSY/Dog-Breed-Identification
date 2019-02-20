# Dog_test

## Introduction

This is a __Dog Breed Identification__ App.
Input an image, and it will tell you the type of dog in it. 15 most similar images are shown in the meantime.

### Demo
The cropped image of the original input is shown on the up-left with the predicted type. The rest are the output images that are most similar to the input.

The input is a __Golden Retriever__. The predicted type is __CORRECT__. Most similar images belong to the right type of dogs, but some of them don't, e.g., Labrador.
![test1](https://github.com/INFINITSY/dog_test/blob/master/test1.jpg)
The input is a __Siberian Husky__. The predicted type is __CORRECT__. Most similar images again belong to the same kind, yet some Malamutes are included.
![test2](https://github.com/INFINITSY/dog_test/blob/master/test2.jpg)
Experiments show that this App can always predict the right type and most of the output  images belong to the same kind of dog as the input. It does make some mistakes when two types of dogs are similar to each other, e.g., __Husky vs Malamute__, which is hard even for human eyes:). 

### detect.py

A YOLO algorithm to detect and crop dog in images.

__Input:__ origin image

__Output:__ cropped image

__Note:__ download yolov3.weights to this directory first

```shell
$ wget https://pjreddie.com/media/files/yolov3.weights
```



### ResNet50_train_model.py

A ResNet50 model for training.

__Data:__ _training data_ is in `/train` and _validation data_ is in `/validation`



### ResNet50_test_model.py

Predict the class of a test image and compare it with _reference_ images in `/retrival`, return top 15 images for show.



### gui_final.py

A GUI for test image selection and results presenting.

__Note:__ gui may look different due to computer resolution



## Usage

- Run gui_final.py
- Select image for testing
- Compute and wait for result
- Results presenting
- Select a new image...

