import argparse
import torch
import transformers

import os.path

from google_drive_downloader import GoogleDriveDownloader as gdd

from transformers import BertTokenizer
from transformers import AdamW
from transformers import BertForSequenceClassification

import numpy as np
import torch

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--title')
    parser.add_argument('--description')

    args = vars(parser.parse_args(argv))

    if 'title' in args and 'description' in args:
        print(f'Title and description are present')

    if len(args) == 2:
        print(f'Correct number of arguments')
    
    if (1 < len(args['title']) < 30) and (1 <= len(args['title'].split()) < 30):
        print(f'Title argument has words and characters in range')

    if (1 < len(args['description']) < 500) and (1 <= len(args['description'].split()) < 250):
        print(f'Description argument has words and characters in range')

    if (any(not c.isalnum() for c in args['title'].split()) == False) and (any(not c.isalnum() for c in args['description'].split()) == False):
        print(f'Title and description have only alphanumeric characters')

    if os.path.exists('./src/model.pt') == False:
        print('Weights file is not present, downloading')
        gdd.download_file_from_google_drive(file_id='1lMjuBZ161egqHAnBtwNDHzv5hkzh4G26', dest_path='./model.pt')
        print('Model is downloaded.')

    # Load BERT model from Huggingface library, and load the trained weights.
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=20)
    model.load_state_dict(torch.load('./model.pt'))
    model.eval()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    max_length = 100
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True) # tokenizer
    encoded = tokenizer.encode_plus(args['description'], max_length=100, pad_to_max_length = True)

    # Extract data from encoded array.
    seed_ids = encoded['input_ids']
    seed_token_type_ids = encoded['token_type_ids']
    seed_masks = encoded['attention_mask']

    # Convert numpy data to Tensors
    inp = torch.tensor(seed_ids)
    msk = torch.tensor(seed_masks)
    tok = torch.tensor(seed_token_type_ids)

    # Reshape to [1,100] shape
    inp = inp.unsqueeze(0)
    msk = msk.unsqueeze(0)

    # Put input and masks to GPU
    inp = inp.to(device)
    msk = msk.to(device)

    # Put model to GPU
    model = model.to(device)

    # Perform forward pass
    ot = model(inp, token_type_ids=None, attention_mask=msk)

    # Get logits from output
    b_logit_pred = ot[0]

    # Put through Sigmoid function
    pred_label = torch.sigmoid(b_logit_pred)

    # If a individual logit is higher than 0.5, take as predicted.
    pred_bools = [pl>0.50 for pl in pred_label]

    ar = pred_bools[0].cpu().detach().numpy()

    # Match binary vector with column values
    t = np.where(ar)[0]

    # Get column values
    label_cols = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Foreign', 'History','Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction','TV Movie', 'Thriller', 'War', 'Western']
    label_cols = np.array(label_cols)
    t = np.array(t)
    genres = label_cols[t]
    
    print('\n \n \n \n')
    print({"title": args['title'], "description": args['description'],"genre": genres})

if __name__ == "__main__":
    main()
