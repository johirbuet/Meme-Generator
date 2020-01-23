from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """
        This is the meme generator module. This module includes a class MemeEngine that defines a MemeEngine object
        which contains an output_dir field, to store memes.

        The class MemeEngine also contains methods:
        1. url_to_string : that converts a HttpResponse object to a string
        2. check_path: extracts raw form of an HttpResponse object
        3. make_meme: reads in an image, transforms and adds a caption to the image (body and author)

        Example:
        meme = MemeEngine("./tmp")
        output_path = meme.make_meme("path to image", "body of quote", "author of quote")

        The output_path is the that path to the saved image which has been mememified.
    """

    def __init__(self, root: str):
        self.root = root
        pass


    def make_meme(self, img_path, text, author, width = 500) -> str:
        """
        This method creates meme and stores in a path.
        :param img_path:
        :param text:
        :param author:
        :param width:
        :return: out_path
        """
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