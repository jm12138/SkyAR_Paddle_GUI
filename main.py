import argparse
from SkyAR import SkyAR


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model_path', type=str,
                        required=False, default=None, help='model path')
    parser.add_argument('-v', '--video_path', type=str,
                        required=True, default=None, help='video path')
    parser.add_argument('-s', '--save_path', type=str,
                        required=True, default=None, help='save path')
    parser.add_argument('-c', '--config', type=str,
                        required=False, default='jupiter', help='save path')

    parser.add_argument('-p', '--preview_frames_num', type=int,
                        required=False, default=0, help='preview frames num')

    parser.add_argument('--skybox_img', type=str,
                        required=False, default=None, help='skybox img path')
    parser.add_argument('--skybox_video', type=str,
                        required=False, default=None, help='skybox video path')
    parser.add_argument('--rain_cap_path', type=str,
                        required=False, default=None, help='rain cap path')

    parser.add_argument('--is_show', action='store_true',
                        required=False, default=False, help='is show')
    parser.add_argument('--is_rainy', action='store_true',
                        required=False, default=False, help='is rainy')
    parser.add_argument('--is_video_sky', action='store_true',
                        required=False, default=False, help='is video skybox')
    parser.add_argument('--disable_halo_effect', action='store_true',
                        required=False, default=False, help='disable halo effect')
    parser.add_argument('--auto_light_matching', action='store_true',
                        required=False, default=False, help='is auto light matching')

    parser.add_argument('--relighting_factor', type=float,
                        required=False, default=0.8, help='relighting factor')
    parser.add_argument('--recoloring_factor', type=float,
                        required=False, default=0.5, help='recoloring factor')
    parser.add_argument('--skybox_center_crop', type=float,
                        required=False, default=0.5, help='skybox center crop')

    args = parser.parse_args()

    for k, v in sorted(vars(args).items()):
        print(k, '=', v)
    return args


def main(args):
    skyar = SkyAR(args.model_path)

    skyar.MagicSky(
        video_path=args.video_path,
        save_path=args.save_path,
        config=args.config,
        is_rainy=args.is_rainy,
        preview_frames_num=args.preview_frames_num,
        is_video_sky=args.is_video_sky,
        is_show=args.is_show,
        skybox_img=args.skybox_img,
        skybox_video=args.skybox_video,
        rain_cap_path=args.rain_cap_path,
        halo_effect=(not args.disable_halo_effect),
        auto_light_matching=args.auto_light_matching,
        relighting_factor=args.relighting_factor,
        recoloring_factor=args.recoloring_factor,
        skybox_center_crop=args.skybox_center_crop
    )


if __name__ == "__main__":
    args = get_args()
    main(args)
