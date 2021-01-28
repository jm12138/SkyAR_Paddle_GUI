# SkyAR_Paddle
* A Paddle implementation of SkyAR.
* Base repo： [jiupinjia/SkyAR](https://github.com/jiupinjia/SkyAR)
* Paper：Zhengxia Zou. [Castle in the Sky: Dynamic Sky Replacement and Harmonization in Videos](https://arxiv.org/abs/2010.11800). CoRR, abs/2010.118003, 2020.
# Examples
* raw video：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126142046572.gif)

* jupiter：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211435619.gif)
* rainy：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012521152492.gif)
* galaxy：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211523491.gif)
* district9ship：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211520955.gif)
* raw video：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210126142038716.gif)
* floatingcastle：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211514997.gif)
* thunderstorm：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211433591.gif)
* supermoon：

	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210125211417524.gif)

# License
![Creative Commons License](https://camo.githubusercontent.com/f05d4039b67688cfdf339d2a445ad686a60551f9891734c418f7096184de5fac/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d6e632d73612f342e302f38387833312e706e67) [SkyAR](https://github.com/jiupinjia/SkyAR) by [Zhengxia Zou](http://www-personal.umich.edu/~zzhengxi/) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

# Quick Start
* clone or download the code

* download the pretrained model：[link](https://bj.bcebos.com/v1/ai-studio-online/232021343ede409f92d512707c04d870f8b267035e86412084cf838f83afc6cb?responseContentDisposition=attachment%3B%20filename%3DResNet50FCN.zip&authorization=bce-auth-v1%2F0ef6765c1e494918bc0d4c3ca3e5c6d1%2F2021-01-25T08%3A44%3A17Z%2F-1%2F%2F7afd50b9b0d15e6eec3cac9ca3c213d33695474539b9fdc6cfe8d1a8d8525909)

* unpack the pretrained model

* run main.py
```shell
$ python main.py -v [video_path] -s [save_path] -m [model_path]
```

# Configs
```
optional arguments:
  -h, --help  show this help message and exit

  -m MODEL_PATH, --model_path MODEL_PATH
  -v VIDEO_PATH, --video_path VIDEO_PATH
  -s SAVE_PATH,  --save_path  SAVE_PATH

  -c CONFIG, --config CONFIG
  All Choices：[
    'rainy', 'sunny', 'cloudy', 'galaxy', 'jupiter', 'sunset', 
    supermoon', 'district9ship', 'floatingcastle', 'thunderstorm'
  ]
  Please set --config to None if use custom skybox

  -p PREVIEW_FRAMES_NUM, --preview_frames_num PREVIEW_FRAMES_NUM

  --skybox_img SKYBOX_IMG
  --skybox_video SKYBOX_VIDEO
  --rain_cap_path RAIN_CAP_PATH

  --is_show              to visual result 
  --is_rainy             is rainy
  --is_video_sky         is video skybox

  More configs to tune the result:
  --disable_halo_effect  disable halo effect
  --auto_light_matching  is auto light matching
  --relighting_factor    RELIGHTING_FACTOR
  --recoloring_factor    RECOLORING_FACTOR
  --skybox_center_crop   SKYBOX_CENTER_CROP
```

# Citation
```
@inproceedings{zou2020skyar,
    title={Castle in the Sky: Dynamic Sky Replacement and Harmonization in Videos},
    author={Zhengxia Zou},
    year={2020},
    journal={arXiv preprint arXiv:2010.11800},
}
```