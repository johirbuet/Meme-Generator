from PIL import Image, ImageDraw, ImageFont


class MemeEngine:

    def __init__(self, root: str):
        self.root = root
        pass


    def make_meme(self, img_path, text, author, width = 500) -> str:
        name = img_path.split("/")[-1]
        img = Image.open(img_path)
        out_path = f'{self.root}/out_{name}'
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(img)
        #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((width/4, height/4), f'{text} - by {author}', fill='white')
        img.save(out_path)
        return out_path