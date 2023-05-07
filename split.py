import os
from PIL import Image
from tqdm import tqdm
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

def split_midjourney_image(input_path, filename, output_path):
    # Get input filename from paths
    input_file = os.path.join(input_path, filename)

    # Load the full image
    full_image = Image.open(input_file)

    # Define the size of each grid cell
    cell_size = 1024

    # Loop over each grid cell and save it as a separate file
    for i in range(2):
        for j in range(2):
            # Define the coordinates of the current cell
            left = j * cell_size
            upper = i * cell_size
            right = (j + 1) * cell_size
            lower = (i + 1) * cell_size

            # Extract the current cell as a new image
            cell_image = full_image.crop((left, upper, right, lower))

            # Generate the filename for the current cell
            out_filename = os.path.splitext(os.path.basename(input_file))[0]
            out_filename += f"_{i}{j}.png"
            output_file = os.path.join(output_path, out_filename)

            # Save the current cell as a separate file
            cell_image.save(output_file)


if __name__ == '__main__':
    # Specify the path to the folder containing the midjourney files
    input_path = os.environ.get('INPUT_PATH')
    
    # Specify the path to the folder where the output is generated
    output_path = os.environ.get('OUTPUT_PATH')

    # Loop over each file in the folder and split it into 4 cells
    for filename in tqdm(os.listdir(input_path)):
        if filename.endswith('.png'):
            split_midjourney_image(input_path, filename, output_path)
