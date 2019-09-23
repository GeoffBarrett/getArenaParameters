from core.Tint_Matlab import getpos, centerBox
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime


def print_msg(self, msg):
    if self is not None:
        self.LogAppend.myGUI_signal.emit(msg)
    else:
        print(msg)


def getParameters(posfile, arena_length_meters, arena_width_meters, plot_arena=False, ax=None, self=None):
    """
    This function will acquire th

    :param posfile: the filename of the session's .pos file
    :param arena_length_meters: the length the arena in meters
    :param arena_width_meters: the width of the arena in meters
    :param plot_arena: set this value to True if you want to plot the arena position
    :param ax: the axis of the arena you want to plot the arena on
    :param self: used for printing the message to a GUI (self is used in object-oriented-programming)
    :return: ppm (pixels per meter), center (a list of values for the center point of the arena: [x,y])
    """

    if not os.path.exists(posfile):
        msg = '[%s %s]: the following position file does not exist, skipping: %s.' % (
            str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time())[:8], posfile)
        print_msg(self, msg)
        raise FileNotFoundError

    msg = '[%s %s]: Loading position data.' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8])
    print_msg(self, msg)

    posx, posy, post, Fs_pos = getpos(posfile, method='raw')  # getting the mouse position

    posx[np.where(posx == 1023)] = np.nan
    posy[np.where(posy == 1023)] = np.nan

    nonNanValues = np.where(np.isnan(posx) == False)[0]
    # removing any NaNs
    # post = post[nonNanValues]
    posx = posx[nonNanValues]
    posy = posy[nonNanValues]

    if plot_arena:
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)
        ax.plot(posx, posy)
        ax.set_xlabel("X Position (pix)")
        ax.set_ylabel("Y Position (pix)")
        ax.set_title("X vs Y Position")

    msg = '[%s %s]: Calculating arena center.' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8])
    print_msg(self, msg)

    # calculating the center of the arena
    centerX, centerY = centerBox(posx, posy)

    msg = '[%s %s]: Calculating ppm value.' % (
        str(datetime.datetime.now().date()),
        str(datetime.datetime.now().time())[:8])
    print_msg(self, msg)

    # calculating the length and width of the arena boundaries
    arena_length_pixels = np.amax(posx) - np.amin(posx)  # units - pixels
    arena_width_pixels = np.amax(posy) - np.amin(posy)  # units - pixels

    # calculating the pixels-per-meter (ppm) by normalizing the pixel values by the arena boundaries (in meters)
    ppm = np.mean([arena_length_pixels / arena_length_meters, arena_width_pixels / arena_width_meters])

    return ppm, [centerX, centerY]
