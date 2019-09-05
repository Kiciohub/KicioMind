from PyQt5.QtGui import QImage, QPainter, QPixmap, QColor


def merge_result_image(result, length, style):
    width = 20
    total_width = width * length
    correct, close = result
    incorrect = length - correct - close
    painter = QPainter()
    res_img = QImage(total_width, width, QImage.Format_RGBA64_Premultiplied)
    res_img.fill(QColor(0, 0, 0, 0))

    painter.begin(res_img)
    x_offset = draw_image_n_times(QImage('../img/' + style + '/Correct.png'), painter, correct, width, 0)
    x_offset = draw_image_n_times(QImage('../img/' + style + '/Close.png'), painter, close, width, x_offset)
    x_offset = draw_image_n_times(QImage('../img/' + style + '/InCorrect.png'), painter, incorrect, width, x_offset)
    painter.end()

    return QPixmap.fromImage(res_img)


def draw_image_n_times(image, painter, times, width, x_offset):
    for i in range(times):
        painter.drawImage(x_offset, 0, image)
        x_offset += width
    return x_offset
