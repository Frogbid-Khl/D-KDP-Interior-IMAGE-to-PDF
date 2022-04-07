import os
import natsort
from fpdf import FPDF

page_format = 'letter'
page_width_in_mm = 215.9
page_height_in_mm = 279.4
image_width_in_pixel = 2500
image_height_in_pixel = 3300

directory_name_list = os.listdir('INPUT')

for directory_name in directory_name_list:
    pdf = FPDF(orientation='P', unit='mm', format=page_format)
    pdf.set_auto_page_break(0)
    imagelist = [i for i in os.listdir('INPUT/' + directory_name) if i.endswith('jpg')]

    for image in natsort.natsorted(imagelist):
        width, height = float(image_width_in_pixel * 0.264583), float(image_height_in_pixel * 0.264583)

        # given we are working with A4 format size
        pdf_size = {'P': {'w': page_width_in_mm, 'h': page_height_in_mm},
                    'L': {'w': page_height_in_mm, 'h': page_width_in_mm}}

        # get page orientation from image size
        orientation = 'P' if width < height else 'L'

        #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']
        pdf.add_page(orientation=orientation)

        pdf.set_left_margin(0.38)
        pdf.set_right_margin(0.38)

        pdf.image('INPUT/' + directory_name + '/' + image, 0, 0, width, height)

    pdf.output("OUTPUT/" + directory_name + ".pdf", "F")
    print(directory_name + ".pdf Ready")
