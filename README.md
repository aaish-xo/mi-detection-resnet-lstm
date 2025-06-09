# mi-detection-resnet-lstm
MI Classification from Echocardiographic Videos (A4C & A2C Views)
This project builds deep learning models to detect myocardial infarction using echocardiographic videos from the HMC-QU dataset.
We use ResNet18 + LSTM to model both spatial patterns and temporal dynamics in the video sequences.

Note: The dataset is not included due to license restrictions. Please request access from the original authors at HMC-QU dataset page.


This repository includes adapted code from the following sources:

# Acknowledgements

This repository reuses and adapts components from the excellent open-source work by [UtopAIBuilder/Grad-CAM-for-video-and-regression-task](https://github.com/UtopAIBuilder/Grad-CAM-for-video-and-regression-task).

- The Grad-CAM logic used to visualise attention in hybrid models (e.g., ResNet-LSTM) for video-based classification was adapted from their implementation.
- Components of the training loop and model architecture for spatiotemporal modeling were also influenced by their example notebooks.

I am grateful to the authors for making their work publicly available.



