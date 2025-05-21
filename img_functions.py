from PIL import Image, ImageDraw, ImageFont



# image_path = './assets/image.jpg' # placeholder to input
# output_path = './assets/image_marked.jpg' # placeholder to input
# watermark_text = 'Watermark' # placeholder to input

def add_watermark(image_path, output_path, watermark_text, font_style, font_size):
    image = Image.open(image_path, mode='r')
    image = image.convert('RGBA')
    width, height = image.size

    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    watermark_lines_color = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line(((0, height -i), (i, height)),
                  fill=watermark_lines_color,
                  width=5)

    font_dict = {'Helvetica': 'Helvetica.ttc',
     'Times New Roman': 'Times New Roman.ttf',
     'Georgia': 'Georgia.ttf',
     'Comic Sans': 'Comic Sans MS.ttf',
     'Verdana': 'Verdana.ttf',
     'Arial': 'Arial.ttf',
     'Baskerville': 'Baskerville.ttc',
     'Futura': 'Futura.ttc',
     'Bodoni': 'Bodoni 72.ttc',
     'Rockwell': 'Rockwell.ttc'
                 }
    watermark_font = font_dict[font_style] # placeholder to input
    # font_size = 100 # placeholder to input

    font = ImageFont.truetype(watermark_font, font_size)
    text_width = font.getmask(watermark_text).getbbox()[2]
    text_height = font.getmask(watermark_text).getbbox()[3]

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_text_color = (255,255,255, 80)

    draw.text((x, y),
              watermark_text,
              fill=watermark_text_color,
              font=font)
    output_image = Image.alpha_composite(image, overlay)

    output_image.save(output_path)

if __name__ == "__main__":

    add_watermark(image_path=image_path, output_path= output_path, watermark_text=watermark_text)