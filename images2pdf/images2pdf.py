import os
import sys
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.units import cm
from os.path import basename

# -----------------------------------------------------------------------------
def conv_directories_to_pdf(path):
    for dir in os.listdir(path):
        print(dir)
        dir_path = '{}/{}'.format(path, dir)
        conv_images_to_pdf(dir_path, '{}.pdf'.format(dir_path))

# -----------------------------------------------------------------------------
def conv_images_to_pdf(input_path, output):
    c = canvas.Canvas(output, pagesize=A4)
    print('directory:{}'.format(input_path))
    for img_file in os.listdir(input_path):
        base, ext = os.path.splitext(img_file)
        if ext == '.png' or ext == '.jpg' or ext == '.jpeg':
            __drawImage(c, '{}/{}'.format(input_path, img_file))
            c.showPage()
    c.save()
    print ("finish")

# -----------------------------------------------------------------------------
def __drawImage(c, img_file):
    img = Image.open(img_file).convert('RGB')
    img_w, img_h = img.size
    page_w, page_h = A4

    if (float(img_w) / img_h) < (float(page_w) / page_h):
        dest_h = page_h
        dest_w = img_w * (page_h / img_h)
        x = (page_w - dest_w) / 2
        y = 0
    else:
        dest_w = page_w
        dest_h = img_h * (page_w / img_w)
        y = (page_h - dest_h) / 2
        x = 0

    c.setPageSize((img_w, img_h))
    c.drawImage(img_file, 0, 0, mask='auto')

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    conv_directories_to_pdf(sys.argv[1])
