from PIL import Image
import math

def remove_gray_bg(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # The background is a dark gray gradient
            # Red text is high in R, Blue text is high in B
            # Calculate colorfulness
            rg = abs(r - g)
            gb = abs(g - b)
            rb = abs(r - b)
            colorfulness = max(rg, gb, rb)
            
            brightness = (r + g + b) / 3
            
            if colorfulness < 30 and brightness < 100:
                # Pure background
                pixels[x, y] = (r, g, b, 0)
            elif colorfulness < 60 and brightness < 120:
                # Edge pixel - soft alpha based on colorfulness
                # Map colorfulness 30->60 to alpha 0->255
                alpha = int(((colorfulness - 30) / 30.0) * 255)
                pixels[x, y] = (r, g, b, alpha)

    img.save(out_path, "PNG")

remove_gray_bg("logo.png", "logo.png")
