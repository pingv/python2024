from PIL import Image, ImageOps
import sys
import os


def main():
    # Check command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Check if input file exists
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    try:
        # Open shirt image (overlay)
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        print("shirt_size : ", shirt_size)

        shirt_width = shirt_size[0]

        # Open input image
        with Image.open(input_path) as input_image:
            # Calculate the new height to maintain the aspect ratio
            aspect_ratio = input_image.height / input_image.width
            new_height = int(shirt_width * aspect_ratio)

            # Resize the input image to the new dimensions
            input_image = input_image.resize((shirt_width, new_height))

            # Crop the input image to a square size, removing 1.5 inches from the top and 1 inch from the bottom
            dpi = input_image.info.get('dpi', (72, 72))  # Default to 72 DPI if not available
            top_crop = int(1.5 * dpi[1])
            bottom_crop = int(1 * dpi[1])
            new_height = input_image.height - top_crop - bottom_crop
            if new_height > input_image.width:
                new_height = input_image.width
            left = 0
            top = top_crop
            right = input_image.width
            bottom = top_crop + new_height
            input_image = input_image.crop((left, top, right, bottom))

            # Calculate the position to paste the shirt at the bottom center
            position = (0, new_height - shirt_size[1])

            # Overlay shirt on input image
            input_image.paste(shirt, position, shirt)

            # Save result
            input_image.save(output_path)

    except Exception as e:
        sys.exit(f"Error: {str(e)}")

    except Exception as e:
        sys.exit(f"Error: {str(e)}")


if __name__ == "__main__":
    main()