from graphics import Point, GraphWin, Text
from tri_drawing import draw


def main():
    win = GraphWin('Smartass Buster', 600, 800)
    exit_txt = Text(Point(win.getWidth() - 60, win.getHeight() - 15), 'COMPUTE')
    exit_txt.draw(win)

    tri_thing = draw(win)

    if tri_thing:
        result = tri_thing.triangles()
    else:
        result = 0

    result1_txt = Text(Point(100, win.getHeight() - 45), 'This figure contains')
    result2_txt = Text(Point(100, win.getHeight() - 15), '{} triangles'.format(result))
    result1_txt.draw(win)
    result2_txt.draw(win)
    win.getMouse()


if __name__ == '__main__':
    main()
