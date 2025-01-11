%%writefile countryshape/data_setup.py
"""
Contains the functionality for creating PyTorch DataLoades for 
Image classification data.
"""
# import libraries
import os
from torchvision import transforms
from torch.utils.data import DataLoader

# Set constants
NUM_WORKERS = os.cpu_count()

# Functions
def create_dataloaders(
    train_dir: str, 
    test_dir: str,
    transform: transforms.Compose,
    batch_size: int,
    num_workers: int=NUM_WORKERS
):
    """
    Creates training and testing DataLoaders.

    Takes in a training directory and testing directory path and turns
    them into PyTorch Datasets and then into PyTorch DataLoaders

    Args:
        train_dir: Path to training directory
        test_dir: Path to testing directory
        transform: torchvision transforms to perform on training and testing data.
        batch_size: Number of samples per batch in each of the DataLoaders
        num_workers: An integer for number of workers per DataLoader.

    Returns:
        A tuple of (train_dataloader, test_dataloader, class_names).
        Where class_names is a list of the target classes.
        Example usage: 
            train_dataloader, test_dataloader, class_names = \
                = create_dataloaders(train_dir)
    """
