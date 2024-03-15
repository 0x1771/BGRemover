from networks.models import build_model


class Args:
    def __init__(self):
        self.encoder = 'resnet50_GN_WS'
        self.decoder = 'bgr_decoder'
        self.weights = 'BGR.pth'
    
args = Args()
Model = build_model(args)
