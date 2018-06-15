import cv2 # computer vision library
import helpers # helper functions
import features # functions to determine features
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # for loading in images


def get_misclassified_images(test_images):
  '''Determines which images are misclassified from the estimate_label function'''

  # Track misclassified images by placing them into a list
  misclassified_images_labels = []

  # Iterate through all the test images
  # Classify each image and compare to the true label
  for image in test_images:

    # Get true data
    im = image[0]
    true_label = image[1]
    assert(len(true_label) == 3), "The true_label is not the expected length (3)."

    # Get predicted label from your classifier
    predicted_label = features.estimate_label(im)
    assert(len(predicted_label) == 3), "The predicted_label is not the expected length (3)."

    # Compare true and predicted labels
    if(predicted_label != true_label):
      # If these labels are not equal, the image has been misclassified
      misclassified_images_labels.append((im, predicted_label, true_label))

  # Return the list of misclassified [image, predicted_label, true_label] values
  return misclassified_images_labels

def calculate_accuracy(STANDARDIZED_TEST_LIST, MISCLASSIFIED):
  total = len(STANDARDIZED_TEST_LIST)
  num_correct = total - len(MISCLASSIFIED)
  accuracy = num_correct/total

  print('Accuracy: ' + str(accuracy))
  print("Number of misclassified images = " + str(len(MISCLASSIFIED)) +' out of '+ str(total))

  red_missclassified = []
  for image in MISCLASSIFIED:
    if image[2] == [1, 0, 0]:
      red_missclassified.append(image)
  print('Number of red images that were misclassified = ', len(red_missclassified))


if __name__ == '__main__':
  IMAGE_DIR_TRAINING = "traffic_light_images/training/"
  IMAGE_DIR_TEST = "traffic_light_images/test/"

  TEST_IMAGE_LIST = helpers.load_dataset(IMAGE_DIR_TEST)

  # Standardize the test data
  STANDARDIZED_TEST_LIST = helpers.standardize(TEST_IMAGE_LIST)
  # features.highest_sat_pixel(STANDARDIZED_TEST_LIST[2][0])

  # Shuffle the standardized test data
  random.shuffle(STANDARDIZED_TEST_LIST)
  image = STANDARDIZED_TEST_LIST[0][0]

  # Find all misclassified images in a given test set
  MISCLASSIFIED = get_misclassified_images(STANDARDIZED_TEST_LIST)
  calculate_accuracy(STANDARDIZED_TEST_LIST, MISCLASSIFIED)
