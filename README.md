# README

### How to Run it (Dont assume everything is installed) ?

    The docker image was succesfuly deployed and tested on a GCP instance on Nvidia T4 GPU.
    The image consists of Pytorch-gpu-devel and Python3.7.5-slim.

    To run the application, run the docker container on a machine with CUDA support.

    Command used for starting the container. 
    1. sudo docker run -d --gpus all -p <IMAGE ID>

    Command used for getting to the image.
    2. sudo docker exec -it <CONTAINER ID> /bin/bash

    Command used for performing the inference.
    3. python3 src/inference.py --title "Othello" --description "The evil iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of the Shakespeare classic"

    Command used for performing the tests.
    4. pytest -v src/test.py

### What Libraries/ Programming languages/Algorithms you used and why?

    Libraries: Pandas - Numpy - PyTorch - Huggingface. Reason for PyTorch is its ease of use with Transformers.
    Algorithms: Bert Transformer. The reason for this is that BERT proves to be very effective in NLP classification tasks.
    I could have used different transformers such as distilbert or RoBERTa but the original BERT has a good tradeoff between performance and model size.

### How to reproduce your work? (training included)

    I attach a jupyter notebook with entire pipeline (Load Data, EDA, Preprocessing, Training, Testing, and performing Inference.)

    To reproduce my work upload the dataset and Jupyter notebook to google colab GPU instance.
    Run all cells including training (should take around 40 minutes).