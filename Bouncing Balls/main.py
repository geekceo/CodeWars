def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        look = 1
        bounce_height = h * bounce
        while bounce_height > window:
            look += 2
            h = bounce_height
            bounce_height = h * bounce

        return look
    return -1