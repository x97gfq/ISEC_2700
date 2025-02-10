import matplotlib.pyplot as plt
from PIL import Image
import os

def extract_lsb(image_path):
    # Open the image
    img = Image.open(os.getcwd() + "\\Steganography\\" + image_path)
    pixels = list(img.getdata())
    
    # Extract the LSB from each pixel
    lsb_bits = []
    for pixel in pixels:
        for color in pixel:
            lsb_bits.append(color & 1)
    
    return lsb_bits

def analyze_lsb_distribution(lsb_bits):
    # Calculate the frequency of 0s and 1s in the LSB bits
    zero_count = lsb_bits.count(0)
    one_count = lsb_bits.count(1)
    
    # Print the counts
    print(f"Number of 0s: {zero_count}")
    print(f"Number of 1s: {one_count}")
    
    # Plot the distribution
    labels = ['0', '1']
    counts = [zero_count, one_count]
    
    plt.bar(labels, counts, color=['blue', 'orange'])
    plt.xlabel('LSB Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of LSB Bits')
    plt.show()
    
    # Perform a chi-square test to check for uniformity
    expected_count = len(lsb_bits) / 2
    chi_square_stat = ((zero_count - expected_count) ** 2 / expected_count) + ((one_count - expected_count) ** 2 / expected_count)
    
    print(f"Chi-square statistic: {chi_square_stat}")

# Example usage
image_path = 'picture_none.bmp'  # Replace with the path to your image
lsb_bits = extract_lsb(image_path)
analyze_lsb_distribution(lsb_bits)
