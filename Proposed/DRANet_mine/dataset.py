import torch
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms

## Import Data Loaders ##
from dataloader import *


def get_dataset_NB(dataset, batch, imsize, workers):
    if dataset == 'G':
        train_dataset = GTA5(list_path='./data_list/GTA5', split='train', crop_size=imsize)
        test_dataset = None

    elif dataset == 'C':
        train_dataset = Cityscapes(list_path='./data_list/Cityscapes', split='train', crop_size=imsize)
        test_dataset = Cityscapes(list_path='./data_list/Cityscapes', split='val', crop_size=imsize, train=False)

    elif dataset == 'M':
        train_dataset = dset.MNIST(root='D:\\UDA_research\\Dataset', train=True, download=True,
                                   transform=transforms.Compose([
                                       transforms.Resize(imsize),
                                       transforms.Grayscale(3),
                                       transforms.ToTensor(),
                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                   ]))
        test_dataset = dset.MNIST(root='D:\\UDA_research\\Dataset', train=False, download=True,
                                  transform=transforms.Compose([
                                      transforms.Resize(imsize),
                                      transforms.Grayscale(3),
                                      transforms.ToTensor(),
                                      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                  ]))
    elif dataset == 'U':
        train_dataset = dset.USPS(root='D:\\UDA_research\\Dataset\\usps', train=True, download=True,
                                   transform=transforms.Compose([
                                       transforms.Resize(imsize),
                                       transforms.Grayscale(3),
                                       transforms.ToTensor(),
                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                   ]))
        test_dataset = dset.USPS(root='D:\\UDA_research\\Dataset\\usps', train=False, download=True,
                                  transform=transforms.Compose([
                                      transforms.Resize(imsize),
                                      transforms.Grayscale(3),
                                      transforms.ToTensor(),
                                      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                  ]))
    elif dataset == 'MM':
        train_dataset = MNIST_M(root='D:\\UDA_research\\Dataset\\mnist_m', train=True,
                                transform=transforms.Compose([
                                    transforms.Resize(imsize),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                ]))
        test_dataset = MNIST_M(root='D:\\UDA_research\\Dataset\\mnist_m', train=False,
                               transform=transforms.Compose([
                                   transforms.Resize(imsize),
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                               ]))
    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch,
                                                   shuffle=True, num_workers=int(workers), pin_memory=True)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=batch*4,
                                                   shuffle=False, num_workers=int(workers))
    return train_dataloader, test_dataloader


def get_dataset_OH(dataset, batch, imsize, workers):
    cls_dict = {'A':'Art', 'CA':'Clipart', 'P':'Product', 'R':'Real World'}
    root      = 'D:\\UDA_research\\Dataset\\OfficeHomeDataset'
    path      = os.path.join(root, cls_dict[dataset])
    transform = transforms.Compose([
                                   transforms.Resize(imsize),
                                   transforms.ToTensor()
                                   ])

    train_dataset = OfficeHome(path, 'train', transform=transform)
    test_dataset  = OfficeHome(path, 'test', transform=transform)

    '''
    dataset Normalize 추가
    if dataset == 'A':
        pass
    elif dataset == 'CA':
        pass
    elif dataset == 'P':
        pass
    else:
        pass
    '''
    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch,
                                                   shuffle=True, num_workers=int(workers), pin_memory=True)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=batch*2,
                                                   shuffle=False, num_workers=int(workers))

    return train_dataloader, test_dataloader