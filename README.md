# Dog_test

## Intreduction

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

Predict the class of a test image and compare it with images in _reference_ dataset, return top 15 images for show.



### gui_final.py

A GUI for test image selection and results presenting.

__Note:__ gui may look different due to computer resolution



## Usage

- Run gui_final.py
- Select image for testing
- Compute and wait for result
- Results presenting
- Select a new image...

