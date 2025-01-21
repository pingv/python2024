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

        # Open input image
        with Image.open(input_path) as input_image:
            # Resize and crop input to match shirt size
            input_image = ImageOps.fit(input_image, shirt_size)

            # Overlay shirt on input image
            input_image.paste(shirt, (0, 0), shirt)

            # Save result
            input_image.save(output_path)

    except Exception as e:
        sys.exit(f"Error: {str(e)}")


if __name__ == "__main__":
    main()