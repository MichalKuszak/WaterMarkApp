def get_full_output_path(self)
    input_path = "/Users/michalkuszak/PycharmProjects/Day 85 Image Watermarking Desktop App/assets/cool.new.image.jpg"
    output_path = "/Users/michalkuszak/PycharmProjects/Day 85 Image Watermarking Desktop App/assets/"
    file_name = input_path.split('/')[-1]
    file_name_elements = file_name.split(".")
    file_name_new = f'{".".join(file_name_elements[:-1])}_watermarked.png'
    full_output_path = f'{output_path}{file_name_new}'
    return full_output_path
