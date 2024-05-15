import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# Function to apply an adaptive Gaussian filter to the image
def apply_adaptive_gaussian_filter(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not open the image file.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive Gaussian filter
    filtered_image1 = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    kernel_size = 2
    # Define the parameters for the bilateral filter
    diameter = 9  # Diameter of pixel neighborhood
    sigma_color = 75  # Sigma for color space
    sigma_space = 75  # Sigma for coordinate space

    # Find connected components in the binary image
    filtered_image1=cv2.bitwise_not(filtered_image1)
    num_labels, labeled_image, stats, centroids = cv2.connectedComponentsWithStats(filtered_image1, connectivity=8)
    min_blob_size = 100  # Set your desired minimum blob size

    for label in range(1, num_labels):  # Skip label 0 (background)
        if stats[label, cv2.CC_STAT_AREA] < min_blob_size:
            filtered_image1[labeled_image == label] = 0
    # Perform dilation
    filtered_image1=cv2.bitwise_not(filtered_image1)

    _, filtered_image2 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    filtered_image = cv2.bitwise_and(filtered_image1, filtered_image2)
    #filtered_image= cv2.bitwise_not(filtered_image)
    # Define the kernel for erosion and dilation
    
    # Show the filtered image
    """cv2.imshow("Adaptive Gaussian Filter", filtered_image2)
    cv2.imshow("Binary", filtered_image1)#"""
    cv2.imshow("Both", filtered_image)
    cv2.waitKey(0)

    # Save the filtered image
    cv2.imwrite(output_path, filtered_image)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

def convert_to_greyscale_with_alpha(input_path, output_path):
    try:
        # Read the image
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        #blank
        # Create a 4-channel image (RGBA)
        img_p=img.copy()
        img_with_alpha = cv2.merge((np.ones_like(img)*255, np.ones_like(img)*255,
                                     np.ones_like(img)*255, cv2.bitwise_not(img)))
        
        plt.imshow(img_with_alpha)
        plt.show()
        # Save the image with alpha channel
        cv2.imwrite(output_path, img_with_alpha)
        print(f"Image converted and saved to {output_path}")
    except Exception as e:
        print("An error occurred:", e)

input_image_path = "/its/home/drs25/Pictures/diagram.png"
output_image_path = "/its/home/drs25/Pictures/output_image.png"
#apply_adaptive_gaussian_filter(input_image_path, output_image_path.replace(".png",".jpg"))
convert_to_greyscale_with_alpha(input_image_path, output_image_path)
input_image_path = "/its/home/drs25/Pictures/walker1.png"
output_image_path = "/its/home/drs25/Pictures/output_image1.png"
#apply_adaptive_gaussian_filter(input_image_path, output_image_path.replace(".png",".jpg"))
convert_to_greyscale_with_alpha(input_image_path, output_image_path)
input_image_path = "/its/home/drs25/Pictures/walker2.png"
output_image_path = "/its/home/drs25/Pictures/output_image2.png"
#apply_adaptive_gaussian_filter(input_image_path, output_image_path.replace(".png",".jpg"))
convert_to_greyscale_with_alpha(input_image_path, output_image_path)