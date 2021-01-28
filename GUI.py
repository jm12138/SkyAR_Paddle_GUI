'''4.使用回调函数打印当前的值'''
# -*- coding: utf-8 -*-
from tkinter import Tk, Button, StringVar, IntVar, Radiobutton, Checkbutton, Scale, HORIZONTAL
 
from SkyAR import SkyAR
from os.path import abspath, split, join
import sys
try:
    base_path = sys._MEIPASS
except:
    base_path = split(abspath(__file__))[0]

global config_list
config_list = [
    'rainy', 'sunny', 'cloudy', 'galaxy', 'jupiter', 'sunset', 
    'supermoon', 'district9ship', 'floatingcastle', 'thunderstorm'
]
root = Tk()
 
root.title('SkyAR GUI')


root.iconbitmap(join(base_path, 'favicon.ico'))

root.geometry('300x800')
from tkinter.filedialog import askopenfilename, asksaveasfilename

def file_select(item, types, is_save=False):
    if not is_save:
        item.set(askopenfilename(title='choose an video', filetypes=types))
    else:
        item.set(asksaveasfilename(title='save result', filetypes=types))

def start():
    configs = {
        'video_path': str(video_path.get()),
        'save_path': str(save_path.get()),
        'config': config_list[int(config_choose.get())],
        'is_rainy': bool(int(is_rainy.get())),
        'preview_frames_num': 0,
        'is_video_sky': None,
        'is_show': bool(int(preview.get())),
        'skybox_img': None,
        'skybox_video': None,
        'rain_cap_path': None,
        'halo_effect': bool(int(halo_effect.get())),
        'auto_light_matching': bool(int(auto_light_matching.get())),
        'relighting_factor': float(relighting_factor.get()),
        'recoloring_factor': float(recoloring_factor.get()),
        'skybox_center_crop': float(skybox_center_crop.get())
    }
    print(configs)
    skyar = SkyAR()
    skyar.MagicSky(**configs)

video_path = StringVar() 
Button(root, text='video_path', command=lambda: file_select(video_path, (("image", "*.mp4"), ("all", "*")))).pack()
save_path = StringVar()
save_path.set('save_videos/result.mp4')
Button(root, text='save_path', command=lambda: file_select(save_path, (("image", "*.mp4"), ("all", "*")), True)).pack()
skybox_img = StringVar() 
Button(root, text='skybox_img', command=lambda: file_select(skybox_img, (("image", "*.jpg; *.png; *.bmp; *.jpeg"), ("all", "*")))).pack()
skybox_video = StringVar() 
Button(root, text='skybox_video', command=lambda: file_select(skybox_video, (("image", "*.mp4"), ("all", "*")))).pack()
rain_cap_path = StringVar() 
Button(root, text='rain_cap_path', command=lambda: file_select(rain_cap_path, (("image", "*.mp4"), ("all", "*")))).pack()


config_choose = IntVar()
config_choose.set(4)
for i, value in enumerate(config_list):
    b = Radiobutton(root, text=value, variable=config_choose, value=i)
    b.pack()

is_rainy = StringVar()
is_rainy.set(0)
br = Checkbutton(root, text='is_rainy', variable=is_rainy)
br.pack()
halo_effect = StringVar()
halo_effect.set(1)
bh = Checkbutton(root, text='halo_effect', variable=halo_effect)
bh.pack()
auto_light_matching = StringVar()
auto_light_matching.set(0)
ba = Checkbutton(root, text='auto_light_matching', variable=auto_light_matching)
ba.pack()
preview = StringVar()
preview.set(1)
ba = Checkbutton(root, text='preview', variable=preview)
ba.pack()


relighting_factor = StringVar()
relighting_factor.set(0.8)
Scale(root,
      label='relighting_factor',
      length=200,
      from_=0.,  # 设置最小值
      to=1.0,  # 设置最大值
      resolution=0.001,  # 设置步距值
      orient=HORIZONTAL,  # 设置水平方向
      variable=relighting_factor,  # 绑定变量
      digits=3,  # 设置显示的位数为8
      ).pack()


recoloring_factor = StringVar()
recoloring_factor.set(0.5)
Scale(root,
      label='recoloring_factor',
      length=200,
      from_=0.,  # 设置最小值
      to=1.0,  # 设置最大值
      resolution=0.001,  # 设置步距值
      orient=HORIZONTAL,  # 设置水平方向
      variable=recoloring_factor,  # 绑定变量
      digits=3,  # 设置显示的位数为8
      ).pack()


skybox_center_crop = StringVar()
skybox_center_crop.set(0.5)
Scale(root,
      label='skybox_center_crop',
      length=200,
      from_=0.,  # 设置最小值
      to=1.0,  # 设置最大值
      resolution=0.001,  # 设置步距值
      orient=HORIZONTAL,  # 设置水平方向
      variable=skybox_center_crop,  # 绑定变量
      digits=3,  # 设置显示的位数为8
      ).pack()
Button(root, text='start', command=start).pack()
root.mainloop()