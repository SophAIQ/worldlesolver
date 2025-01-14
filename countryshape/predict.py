## To import .pth file

import torchvision
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from pathlib import Path
from torchvision import transforms

game_images_path = Path(r'C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\')
todays = game_images_path / "worldle-2025-01-13.png"

custom_image = torchvision.io.read_image(todays)

# Divide the image pixel values by 255 to get them between [0, 1]
custom_image = (custom_image.float() / 255.0).repeat(3, 1, 1)

# Create transform pipleine to resize image
custom_image_transform = transforms.Compose([
    transforms.Resize((64, 64)),
])

# Transform target image
custom_image_transformed = custom_image_transform(custom_image)
custom_image_transformed = custom_image_transformed[:3]


# Print out original shape and new shape
plt.imshow(custom_image_transformed.permute(1, 2, 0))
plt.title(f"Image shape: {custom_image_transformed.shape}")
plt.axis(False)

# print(custom_image_transformed.shape)

# Create an instance of your model
modelx = model_0

# Load the saved state_dict into the model
modelx.load_state_dict(torch.load('countryshape/models/Countryshape64_VGG_model.pth'))

# Switch the model to evaluation mode
modelx.eval()

with torch.inference_mode():
    # Add an extra dimension to image
    custom_image_transformed_with_batch_size = custom_image_transformed.unsqueeze(dim=0)
    
    # Make a prediction on image with an extra dimension
    custom_image_pred = modelx(custom_image_transformed.unsqueeze(dim=0).to(device))

    # Print out prediction logits
# print(f"Prediction logits: {custom_image_pred}")

# Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
custom_image_pred_probs = torch.softmax(custom_image_pred, dim=1)

# Convert prediction probabilities -> prediction labels
custom_image_pred_label = torch.argmax(custom_image_pred_probs, dim=1)
# print(custom_image_pred_label)

# Find the predicted label
custom_image_pred_class = class_names[custom_image_pred_label.cpu()] # put pred label to CPU, otherwise will error
custom_image_pred_class
predicted_probability = custom_image_pred_probs[0, custom_image_pred_label].item()
print(custom_image_pred_class)
print(predicted_probability)

# # top K probs
# topk_probs, topk_indices = torch.topk(custom_image_pred_probs, k=5, dim=1)
# top2_index = topk_indices[0, 1].item()
# top2_prob = topk_probs[0, 1].item()
# top2_class = class_names[top2_index]
# print(f"Top 2 Prediction: {top2_class} with probability {top2_prob:.4f}")

# top3_index = topk_indices[0, 2].item()
# top3_prob = topk_probs[0, 2].item()
# top3_class = class_names[top3_index]
# print(f"Top 3 Prediction: {top3_class} with probability {top3_prob:.4f}")

# top4_index = topk_indices[0, 3].item()
# top4_prob = topk_probs[0, 3].item()
# top4_class = class_names[top4_index]
# print(f"Top 4 Prediction: {top4_class} with probability {top4_prob:.4f}")

# top5_index = topk_indices[0, 4].item()
# top5_prob = topk_probs[0, 4].item()
# top5_class = class_names[top5_index]
# print(f"Top 5 Prediction: {top5_class} with probability {top5_prob:.4f}")
