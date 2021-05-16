import torch
import einops
import matplotlib.pyplot as plt






def line(a,b,inter_dist = 0.5):
    dist = torch.linalg.norm(a-b)
    inter_dist= inter_dist/dist


    interp_vals = torch.arange(0,1,inter_dist)
    interp_vals = einops.repeat(interp_vals,"i -> i j",j=2)
    return interp_vals*a+(1-interp_vals)*b




def grid(h,w):
    return torch.stack(torch.meshgrid(torch.arange(0,h),torch.arange(0,w)))


if __name__ ==  '__main__':
    line_points = line(torch.tensor([0.,0.]),torch.tensor([30.,35.])).floor().long()
    img = torch.zeros((100,100))
    img[line_points[:,0],line_points[:,1]] = 1
    plt.imshow(img.numpy())
    grid_vals = grid(100,100)
    pass