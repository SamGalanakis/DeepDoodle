import torch
import torch.nn as nn
import einops
from models import MLP










line(torch.tensor([0.,0.]),torch.tensor([0.,10.]))
class Painter(nn.Module):
    def __init__(self,image_embedder,img_emb_dim,chooser_dims,budget):
        super().__init__()
        self.budget = budget

        self.image_embedder = image_embedder
        self.action_chooser = MLP(img_emb_dim+1,chooser_dims,7)




    def forward(self,image):
        latent_0 = self.image_embedder(image)
        budget_count = torch.ones(latent_0.shape[0])*self.budget
        x = torch.cat((latent_0,budget_count),dim=-1)
        for act_ind in range(self.budget):
            chooser_out = self.chooser(x)

            
            

            



