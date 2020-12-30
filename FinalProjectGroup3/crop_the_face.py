import cv2

IMAGE = "img/girl.jpg"
OUT_IMAGE = "img/girl_ellipse.jpg"


def draw_ellipse(image,
                 center_x,
                 center_y,
                 width_px,
                 height_px,
                 angle=0,
                 start_angle=0,
                 end_angle=360,
                 color_bgr=[255, 0, 0],
                 size=0.01,  # -1: filled
                 line_type=cv2.LINE_AA,
                 is_copy=True):
    image = image.copy() if is_copy else image  # copy/clone a new image

    # calculate thickness
    h, w = image.shape[:2]
    if size > 0:
        short_edge = min(h, w)
        thickness = int(short_edge * size)
        thickness = 1 if thickness <= 0 else thickness
    else:
        thickness = -1

    # calc x,y in absolute coord
    x_abs = int(center_x * w)
    y_abs = int(center_y * h)

    cv2.ellipse(img=image,
                center=(x_abs, y_abs),
                axes=(width_px, height_px),
                angle=angle,
                startAngle=start_angle,
                endAngle=end_angle,
                color=color_bgr,
                thickness=thickness,
                lineType=line_type,
                shift=0)
    return image


def main():
    """
    - center_x, center_y: tọa độ (x, y) theo %. Miền giá trị [0, 1]
    - angle: góc của ellipse so với trục X. Chiều tính theo chiều kim đồng hồ
    - width_px: độ rộng của ellipse trải dài theo hướng angle
    - height_px: độ cao của ellipse theo phương vuông góc
    - start_angle, end_angle: đặc tả cung ellipse sẽ vẽ. start_angle là góc tính từ angle trở đi. start_angle=0, end_angle=360 tức ta sẽ vẽ toàn đường ellipse
    - size: đơn vị theo % cạnh ngắn của ảnh để tính tự động thickness. size <= 0 để vẽ ellipse đặc.
    - color: màu sắc của ellipse
    - is_copy: clone ảnh gốc ra để vẽ (True) hoặc vẽ trực tiếp lên ảnh gốc (False)
    """
    img = cv2.imread(IMAGE)
    img_ellipse = draw_ellipse(image=img,
                               center_x=0.45,
                               center_y=0.45,
                               angle=-20,
                               width_px=200,
                               height_px=400,
                               start_angle=0,
                               end_angle=360,
                               color_bgr=[0, 0, 255],
                               size=0.01,  # -1: filled
                               line_type=cv2.LINE_AA,
                               is_copy=True)
    cv2.imwrite(OUT_IMAGE, img_ellipse)
    print("Done drawing ellipse @ %s" % OUT_IMAGE)


if __name__ == "__main__":
    main()