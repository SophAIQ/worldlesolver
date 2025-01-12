%%writefile countryshape/model_builder.property
"""
Contains PyTorch model code to instantiate a TinyVGG model
"""

# Import libraries
import torch
from torch import nn

class TinyVGG(nn.Module):
    """
    Creates the TinyVGG architecture.

    Replicates the TIny VGG architecture from the CNN explainer website in PyTorch.
    Original: https://poloclub.github.io/cnn-explainer/
    I have changed it by adding conv_output_size so that any image size can be an input (not just 64x64)

    Args:
        input_shape: An integer indicating number of input channels.
        hidden_inputs: An integer indicating number of hidden units between layers
        output_shape: An integer indicating number of output units
    """    
    def __init__(self, input_shape: int, hidden_units: int, output_shape: int, input_image_size: int) -> None:
        super().__init__()
        self.conv_block_1 = nn.Sequential(
            nn.Conv2d(in_channels=input_shape, 
                      out_channels=hidden_units, 
                      kernel_size=3, 
                      stride=1, 
                      padding=1), 
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_units, 
                      out_channels=hidden_units,
                      kernel_size=3,
                      stride=1,
                      padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.conv_block_2 = nn.Sequential(
            nn.Conv2d(hidden_units, hidden_units, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_units, hidden_units, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        
        # Calculate the output size after the convolutional blocks
        conv_output_size = input_image_size // (2 ** 2)  # Dividing by 2 for each MaxPool2d
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=hidden_units * conv_output_size * conv_output_size,
                      out_features=output_shape)
        )
    
    def forward(self, x: torch.Tensor):
        x = self.conv_block_1(x)
        x = self.conv_block_2(x)
        x = self.classifier(x)
        return x
