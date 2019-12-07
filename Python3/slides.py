"""
@file           slides.py
@brief          Display images using PyGame
@author         Stephen Longofono

@Notes          Credit to Github user bradmontgomery for the skeleton code I
                used to stand this up.  Retrieved Dec. 2019 from:
                https://github.com/bradmontgomery/pgSlideShow
"""

import argparse
import os
import stat
import sys
import time
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


def walktree(root, depth, curDepth):
    """
    Starting at directory root, recursively descend the directory tree and
    retrieve files of interest up to depth levels of recursion
    """
    if curDepth == depth:
        return []

    files = []
    for f in os.listdir(root):
        pathname = os.path.join(root, f)
        mode = os.stat(pathname)[stat.ST_MODE]
        if stat.S_ISDIR(mode):
            # It's a directory, recurse into it
            files.extend(walktree(pathname, depth, curDepth + 1))
        elif stat.S_ISREG(mode):
            # It's a file, store it
            f, e = os.path.splitext(pathname)
            if e.lower() in ['.png','.jpg','.jpeg','.gif','.bmp']:
                files.append(pathname)
    return files


def eventHandler(events):
    """
    Handle keyboard/mouse/device input events
    """
    for event in events:  # Hit the ESC key to quit the slideshow.
        if event.type in [QUIT, KEYDOWN]:
            pygame.quit()
            exit()


def main(root, waittime, depth, fancy):
    """
    Main loop to display images via pygame
    """
    pygame.init()

    # Test for image support
    if not pygame.image.get_extended():
        sys.exit(1)

    files = walktree(root, depth, 0)
    if len(files) == 0:
        sys.exit(1)

    modes = pygame.display.list_modes()
    SCRNWIDTH, SCRNHEIGHT = max(modes)
    pygame.display.set_mode((SCRNWIDTH, SCRNHEIGHT))
    screen = pygame.display.get_surface()
    pygame.display.toggle_fullscreen()

    while(True):
        try:
            img = pygame.image.load(random.choice(files))
            img = img.convert()
            xpos, ypos, xdim, ydim = img.get_rect()

            # Handle mismatched image sizes
            if ydim > xdim:
                if ydim > SCRNHEIGHT:
                    scalefac = float(ydim) / SCRNHEIGHT
                    img = pygame.transform.smoothscale(img, (int(xdim/scalefac),int(ydim/scalefac)))
            elif xdim > ydim:
                if xdim > SCRNWIDTH:
                    scalefac = float(xdim) / SCRNWIDTH
                    img = pygame.transform.smoothscale(img, (int(xdim/scalefac),int(ydim/scalefac)))
            else:
                if ydim > SCRNHEIGHT:
                    scalefac = float(xdim) / SCRNHEIGHT
                    img = pygame.transform.smoothscale(img, (int(xdim/scalefac),int(ydim/scalefac)))

            # Add a little variety for images of different sizes ( and sidestep
            # the problem of centering them...)
            xdiff = SCRNWIDTH - xdim
            ydiff = SCRNHEIGHT - ydim

            if xdiff > 10:
                xpos = random.randint(0, xdiff)
            if ydiff > 10:
                ypos = random.randint(0, ydiff)

            bound = waittime * 1000
            screen.fill((0,0,0))
            screen.blit(img, (xpos, ypos))
            pygame.display.flip()

            if fancy: # oh my
                for i in range(waittime * 1000):
                    if i > 0.75 * bound:
                        screen.fill((0,0,0))
                        img.set_alpha(bound-i)
                        screen.blit(img, (xpos, ypos))
                        pygame.display.flip()
                    eventHandler(pygame.event.get())
            else:
                eventHandler(pygame.event.get())
                time.sleep(waittime)

        except KeyboardInterrupt:
            pygame.quit()
            exit()
        except pygame.error as err:
            print(err)
            pygame.quit()
            exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recursively loads images from a directory, then displays them in a slideshow.')
    parser.add_argument('--path', type=str, default='.', nargs="?", help='Path(s) that contains images, default CWD')
    parser.add_argument('--waittime', type=int, default=3, help='Amount of time to wait before showing the next image.')
    parser.add_argument('--maxdepth', type=int, default=4, help='Maximum depth of recursion when searching for files relative to the root directory')
    parser.add_argument('--nofade', default=True, action='store_false', help='Disable image fade for slower machines') # action means only set to false if present
    args = parser.parse_args()
    print("\033[91m {}\033[00m".format(
        "[ WARNING ] Take care that the directory you provide (CWD by default) does not\n"
        " have too many image files for your system memory to readily handle.  This\n"
        " script will recursively walk directories to assemble a list of images to\n"
        " display."))
    if input('OK to proceed? (y/n):\t') in ['y','Y']:
        main(args.path, args.waittime, args.maxdepth, args.nofade)
