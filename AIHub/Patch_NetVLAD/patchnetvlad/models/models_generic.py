'''
MIT License

Copyright (c) 2021 Stephen Hausler, Sourav Garg, Ming Xu, Michael Milford and Tobias Fischer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
from AIHub.Patch_NetVLAD.patchnetvlad.models.netvlad import NetVLAD
from AIHub.Patch_NetVLAD.patchnetvlad.models.patchnetvlad import PatchNetVLAD

# from patchnetvlad.models.netvlad import NetVLAD
# from patchnetvlad.models.patchnetvlad import PatchNetVLAD


class Flatten(nn.Module):
    def forward(self, input_data):
        return input_data.view(input_data.size(0), -1)


class L2Norm(nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

    def forward(self, input_data):
        return F.normalize(input_data, p=2, dim=self.dim)


def get_pca_encoding(model, vlad_encoding):
    pca_encoding = model.WPCA(vlad_encoding.unsqueeze(-1).unsqueeze(-1))
    return pca_encoding


def get_backend():
    enc_dim = 512
    enc = models.vgg16(pretrained=True)
    layers = list(enc.features.children())[:-2]
    # only train conv5_1, conv5_2, and conv5_3 (leave rest same as Imagenet trained weights)
    for layer in layers[:-5]:
        for p in layer.parameters():
            p.requires_grad = False
    enc = nn.Sequential(*layers)
    return enc_dim, enc


def get_model(encoder, encoder_dim, config, append_pca_layer=False):
    # config['global_params'] is passed as config
    nn_model = nn.Module()
    nn_model.add_module('encoder', encoder)

    if config['pooling'].lower() == 'netvlad':
        net_vlad = NetVLAD(num_clusters=int(config['num_clusters']), dim=encoder_dim,
                           vladv2=config.getboolean('vladv2'))              ##여기다 여기!!! 여기 코드가있어요!!!
        nn_model.add_module('pool', net_vlad)                               #현재의 모듈에 child module을 추가한다. 추가한 모듈은 주어진 이름을 이용하여 접근할 수 있다.
    elif config['pooling'].lower() == 'patchnetvlad':
        net_vlad = PatchNetVLAD(num_clusters=int(config['num_clusters']), dim=encoder_dim,
                                vladv2=config.getboolean('vladv2'),
                                patch_sizes=config['patch_sizes'], strides=config['strides'])
        nn_model.add_module('pool', net_vlad)
    elif config['pooling'].lower() == 'max':
        global_pool = nn.AdaptiveMaxPool2d((1, 1))
        nn_model.add_module('pool', nn.Sequential(*[global_pool, Flatten(), L2Norm()]))
    elif config['pooling'].pooling.lower() == 'avg':
        global_pool = nn.AdaptiveAvgPool2d((1, 1))
        nn_model.add_module('pool', nn.Sequential(*[global_pool, Flatten(), L2Norm()]))
    else:
        raise ValueError('Unknown pooling type: ' + config['pooling'].lower())

    if append_pca_layer:
        num_pcs = int(config['num_pcs'])
        netvlad_output_dim = encoder_dim
        if config['pooling'].lower() == 'netvlad' or config['pooling'].lower() == 'patchnetvlad':
            netvlad_output_dim *= int(config['num_clusters'])

        pca_conv = nn.Conv2d(netvlad_output_dim, num_pcs, kernel_size=(1, 1), stride=1, padding=0)          #여기다 여기!! 여기 pca코드 붙이는 곳이 있어요 !!
        nn_model.add_module('WPCA', nn.Sequential(*[pca_conv, Flatten(), L2Norm(dim=-1)]))

    return nn_model
