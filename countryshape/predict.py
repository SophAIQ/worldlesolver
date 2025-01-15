"""
Predicts input image from Worldle website using countryshape_solver.py to snip image.
"""

# Import libraries
import torchvision
import matplotlib.pyplot as plt
import torch
from pathlib import Path
from torchvision import transforms
import argparse
import model_builder, data_setup

# Setup hyperparameters
HIDDEN_UNITS = 10

def predict64(image_name):

    # Setup target device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Setup image directoy and train directory
    # game_images_path = Path(r'path to images')
    data_path = Path(r'path to data')
    model_path = 'path to model'
    train_dir = data_path / "train"

    # Get path to import image
    # todays = game_images_path / image_name

    # Read image
    custom_image = torchvision.io.read_image(image_name)

    # Divide the image pixel values by 255 to get them between [0, 1]
    custom_image = (custom_image.float() / 255.0).repeat(3, 1, 1)

    # Create transform pipleine to resize input image and data image
    custom_image_transform = transforms.Compose([
        transforms.Resize((64, 64)),
    ])
    data_transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor()
    ])

    # Transform target image
    custom_image_transformed = custom_image_transform(custom_image)
    custom_image_transformed = custom_image_transformed[:3]

    # Get class names
    class_names = data_setup.return_classes(
        train_dir=train_dir,
        transform=data_transform
    )
    
    # Create model with help from model_builder.py
    model = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=HIDDEN_UNITS,
        output_shape=len(class_names),
        input_image_size=64
    ).to(device)

    # Load the saved state_dict into the model
    model.load_state_dict(torch.load(model_path + 'Countryshape64_VGG_model.pth',weights_only=True))

    # Switch the model to evaluation mode
    model.eval()

    with torch.inference_mode():
        # # Add an extra dimension to image
        # custom_image_transformed_with_batch_size = custom_image_transformed.unsqueeze(dim=0)
        
        # Make a prediction on image with an extra dimension
        custom_image_pred = model(custom_image_transformed.unsqueeze(dim=0).to(device))

    # Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
    custom_image_pred_probs = torch.softmax(custom_image_pred, dim=1)

    # Convert prediction probabilities -> prediction labels
    custom_image_pred_label = torch.argmax(custom_image_pred_probs, dim=1)

    # Find the predicted label
    custom_image_pred_class = class_names[custom_image_pred_label.cpu()] # put pred label to CPU, otherwise will error
    # predicted_probability = custom_image_pred_probs[0, custom_image_pred_label].item()
    # print(custom_image_pred_class)
    return custom_image_pred_class

    # # # top K probs
    # # topk_probs, topk_indices = torch.topk(custom_image_pred_probs, k=5, dim=1)
    # # top2_index = topk_indices[0, 1].item()
    # # top2_prob = topk_probs[0, 1].item()
    # # top2_class = class_names[top2_index]
    # # print(f"Top 2 Prediction: {top2_class} with probability {top2_prob:.4f}")

    # # top3_index = topk_indices[0, 2].item()
    # # top3_prob = topk_probs[0, 2].item()
    # # top3_class = class_names[top3_index]
    # # print(f"Top 3 Prediction: {top3_class} with probability {top3_prob:.4f}")

    # # top4_index = topk_indices[0, 3].item()
    # # top4_prob = topk_probs[0, 3].item()
    # # top4_class = class_names[top4_index]
    # # print(f"Top 4 Prediction: {top4_class} with probability {top4_prob:.4f}")

    # # top5_index = topk_indices[0, 4].item()
    # # top5_prob = topk_probs[0, 4].item()
    # # top5_class = class_names[top5_index]
    # # print(f"Top 5 Prediction: {top5_class} with probability {top5_prob:.4f}")

# Lets it take command line arguments
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Predict image from file")
    parser.add_argument('image_name', type=str, help='Path to the image file')

    # Parse arguments
    args = parser.parse_args()

    # Call the predict64 function with the provided image_name
    predict64(args.image_name)
