from PIL import Image
import matplotlib.pyplot as plt


def merge_result_image(result, length):

    images = [Image.open('../img/Correct.png'), Image.open('../img/Close.png'), Image.open('../img/InCorrect.png')]
    widths, heights = zip(*(i.size for i in images))

    total_width = 20*length
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    correct, close = result
    incorrect = length-correct-close

    for i in range(correct):
        new_im.paste(images[0], (x_offset, 0))
        x_offset += images[0].size[0]

    for i in range(close):
        new_im.paste(images[1], (x_offset, 0))
        x_offset += images[1].size[0]

    for i in range(incorrect):
        new_im.paste(images[2], (x_offset, 0))
        x_offset += images[2].size[0]

    new_im.save('../img/test.png')
    plt.imshow(Image.open('../img/test.png'))
    plt.show()


if __name__ == '__main__':
    merge_result_image((2, 1), 6)
