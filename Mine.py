from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path, output_path, text, position=(10, 10),
                      font_size=20, text_color=(255, 255, 255)):
    """
    Add text to an image and save the result

    Args:
        image_path (str): Path to input image
        output_path (str): Path to save the modified image
        text (str): Text to add to the image
        position (tuple): (x, y) coordinates for text position
        font_size (int): Size of the font
        text_color (tuple): RGB color for the text
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Load a font (you can also specify a custom font file)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Fallback to default font if arial isn't available
            font = ImageFont.load_default()
            print("Using default font as arial.ttf not found")

        # Add text to image
        draw.text(position, text, font=font, fill=text_color)

        # Save the image
        img.save(output_path)
        print(f"Image with text saved to: {output_path}")

        # Optionally show the image
        img.show()

    except FileNotFoundError:
        print(f"Error: The file was not found at {image_path}")
    except Exception as e:
        print(f"Error processing image: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Input and output paths
    input_image = r'C:\Users\Jeya Janilakshmanan\OneDrive\Desktop\mine\Nature.jpeg'  # Replace with your image path
    output_image = r'C:\Users\Jeya Janilakshmanan\OneDrive\Desktop\mine\our_nature.jpg'

    # Text settings
    text_to_add = "The best way to predict your future is to create it."
    text_position = (50, 50)  # (x, y) coordinates from top-left corner
    text_size = 55
    text_color = (0, 0, 0)  # Black color

    # Add text to image
    add_text_to_image(input_image, output_image, text_to_add,
                      text_position, text_size, text_color)