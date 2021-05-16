import torch
from torch.utils.data import Dataset
import os
import io
import random



class DoodleDataset(Dataset):
    def __init__(self,root_dir,n_choices,transform=None,img_ext='.jpg'):
        super().__init__()
        self.n_choices= n_choices
        self.root_dir = root_dir
        self.paths = [path for path in os.walk(root_dir) if path.endswith(img_ext)]




    def __len__(self):
        return len(self.paths)

    def get_single_img(self,idx):

        image = io.imread(self.paths[idx])

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        to_be_drawn = self.get_single_img(idx)

        choices = [self.get_single_img(random.randint(0,self.__len__())) for x in range(self.n_choices)]

        #Inserted now so they get different transform
        insert_int = random.randint(0,self.n_choices)
        choices.insert(insert_int,to_be_drawn)


        if self.transform:
            to_be_drawn = self.transform(to_be_drawn)
            choices = [self.transform(x) for x in choices]
        
        return to_be_drawn,choices









