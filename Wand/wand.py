from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display

background ="./scorebola.jpg"
font = "./overpass-regular.otf"

with Image(filename=background) as img_background:
    with Drawing() as context:
        context.font = font
        context.fill_color = Color('white')
        context.font_size = 60
        context.text(x=0,y=0,body="bola")
        context(img_background)
    display(img_background)