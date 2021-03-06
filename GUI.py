import sys
from os.path import abspath, split, join
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk, Button, StringVar, IntVar, Radiobutton, Checkbutton, Scale, HORIZONTAL, BooleanVar, DoubleVar
from tkinter.ttk import Progressbar
from threading import Thread
from SkyAR import SkyAR


def file_select(item, types, is_save=False):
    if not is_save:
        item.set(askopenfilename(title='choose an video', filetypes=types))
        if item == skybox_img:
            skybox_video.set('')
        elif item == skybox_video:
            skybox_img.set('')
    else:
        item.set(asksaveasfilename(title='save result', filetypes=types))


def run(configs):
    skyar = SkyAR()
    skyar.MagicSky(**configs)
    bar.stop()
    start_button['bg'] = 'SystemButtonFace'
    start_button['state'] = 'normal'
    start_button['text'] = 'start'


def start():
    if skybox_video.get():
        is_video_sky = True
    else:
        is_video_sky = False
    configs = {
        'video_path': video_path.get(),
        'save_path': save_path.get(),
        'config': config_list[config_choose.get()],
        'is_rainy': is_rainy.get(),
        'preview_frames_num': 0,
        'is_video_sky': is_video_sky,
        'is_show': preview.get(),
        'skybox_img': skybox_img.get(),
        'skybox_video': skybox_video.get(),
        'rain_cap_path': rain_cap_path.get(),
        'halo_effect': halo_effect.get(),
        'auto_light_matching': auto_light_matching.get(),
        'relighting_factor': relighting_factor.get(),
        'recoloring_factor': recoloring_factor.get(),
        'skybox_center_crop': skybox_center_crop.get()
    }
    print(configs)
    start_button['bg'] = 'red'
    start_button['text'] = 'wait'
    start_button['state'] = 'disabled'
    bar.start()
    t = Thread(target=run, args=(configs,))
    t.start()


def reset():
    video_path.set('')
    save_path.set('result.mp4')
    skybox_img.set('')
    skybox_video.set('')
    rain_cap_path.set('')
    config_choose.set(4)
    is_rainy.set(False)
    halo_effect.set(True)
    preview.set(True)
    auto_light_matching.set(False)
    relighting_factor.set(0.8)
    recoloring_factor.set(0.5)
    skybox_center_crop.set(0.5)


if __name__ == "__main__":
    try:
        base_path = sys._MEIPASS
    except:
        base_path = split(abspath(__file__))[0]

    global config_list
    config_list = [
        'rainy', 'sunny', 'cloudy', 'galaxy', 'jupiter', 'sunset',
        'supermoon', 'floatingcastle', 'thunderstorm', 'district9ship', None
    ]

    root = Tk()
    root.title('SkyAR Paddle GUI')
    root.iconbitmap(join(base_path, 'favicon.ico'))
    root.geometry('300x850')

    video_path = StringVar()
    Button(root, text='video path', command=lambda: file_select(
        video_path, (("image", "*.mp4"), ("all", "*")))).pack()

    save_path = StringVar()
    save_path.set('result.mp4')
    Button(root, text='save path', command=lambda: file_select(
        save_path, (("image", "*.mp4"), ("all", "*")), True)).pack()

    skybox_img = StringVar()
    Button(root, text='custom skybox img', command=lambda: file_select(
        skybox_img, (("image", "*.jpg; *.png; *.bmp; *.jpeg"), ("all", "*")))).pack()

    skybox_video = StringVar()
    Button(root, text='custom skybox video', command=lambda: file_select(
        skybox_video, (("image", "*.mp4"), ("all", "*")))).pack()

    rain_cap_path = StringVar()
    Button(root, text='custom rain effect video', command=lambda: file_select(
        rain_cap_path, (("image", "*.mp4"), ("all", "*")))).pack()

    config_choose = IntVar()
    config_choose.set(4)
    for i, value in enumerate(config_list):
        if not value:
            value = 'custom'
        b = Radiobutton(root, text=value, variable=config_choose, value=i)
        b.pack()

    is_rainy = BooleanVar()
    is_rainy.set(False)
    br = Checkbutton(root, text='rainy', variable=is_rainy)
    br.pack()

    halo_effect = BooleanVar()
    halo_effect.set(True)
    bh = Checkbutton(root, text='halo effect', variable=halo_effect)
    bh.pack()

    preview = BooleanVar()
    preview.set(True)
    ba = Checkbutton(root, text='preview', variable=preview)
    ba.pack()

    auto_light_matching = BooleanVar()
    auto_light_matching.set(False)
    ba = Checkbutton(root, text='auto light matching',
                     variable=auto_light_matching)
    ba.pack()

    relighting_factor = DoubleVar()
    relighting_factor.set(0.8)
    Scale(root,
          label='relighting factor',
          length=200,
          from_=0.,
          to=1.0,
          resolution=0.001,
          orient=HORIZONTAL,
          variable=relighting_factor,
          digits=3,
          ).pack()

    recoloring_factor = DoubleVar()
    recoloring_factor.set(0.5)
    Scale(root,
          label='recoloring factor',
          length=200,
          from_=0.,
          to=1.0,
          resolution=0.001,
          orient=HORIZONTAL,
          variable=recoloring_factor,
          digits=3,
          ).pack()

    skybox_center_crop = DoubleVar()
    skybox_center_crop.set(0.5)
    Scale(root,
          label='skybox center crop',
          length=200,
          from_=0.,
          to=1.0,
          resolution=0.001,
          orient=HORIZONTAL,
          variable=skybox_center_crop,
          digits=3,
          ).pack()

    Button(root, text='reset', command=reset).pack()

    start_button = Button(root, text='start', command=start)
    start_button.pack()

    bar = Progressbar(root, length=200, value=0, mode="indeterminate")
    bar.pack(pady=10)

    root.mainloop()
