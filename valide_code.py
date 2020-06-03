#coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import random
import string

WIDTH = 220  # 验证码图片宽度
HEIGHT = 40  # 验证码图片长度
RANDOM_WORLD_NUMBER = 5  # 随机字母数
POINT_NUMBER = 100  # 噪点数
LINE_NUMBER = 5  # 噪点直线数


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_validCode_img():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=get_random_color())
    myfont = ImageFont.truetype( font='arial.ttf',size=30)
    draw = ImageDraw.Draw(img)
    code=''
    # 生成验证码中的随机字母
    for i in range(RANDOM_WORLD_NUMBER):
        alphant = random.choice(string.digits + string.ascii_letters)
        code+=alphant
        distance_x = random.randint(40 * i, 40 * i + 20)  # [0,10]
        distance_y = random.randint(0, 10)
        draw.text((distance_x, distance_y), alphant, get_random_color(), font=myfont)

    # 生成验证码中的噪点
    for i in range(POINT_NUMBER):
        draw.point([random.randint(0, WIDTH), random.randint(0, HEIGHT)], fill=get_random_color())  # fill为颜色
        x = random.randint(0, WIDTH)
        y = random.randint(0, WIDTH)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random.randint(0, 10))  # fill为弧长

    # 生成验证码中的直线
    for i in range(LINE_NUMBER):
        x1 = random.randint(0, WIDTH)
        x2 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        y2 = random.randint(0, HEIGHT)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    with open("static/validCode.png", "wb") as f:
        img.save(f, "png")
    return code

get_validCode_img()
