* I have been having tremendous troubles setting up the dev environment in other machines. Just making a note of python and pygame versions.
* I m guessing there are some more dependencies with mac os , xcode , nsdraw and other audio packages which is making it harder to set this up again elsewhere.Will have those errors documented as well here.

```
$ python -V
Python 2.7.6
$ python
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pygame
>>> pygame.version.ver
'1.9.2pre'
```
* Ran into this error while trying to run platform_basic.py
* 2016-09-27 11:21:12.330 X11[14262:2659500] Failed to connect (primary_text_field_cell) outlet from (AppDelegate) to (NSTextFieldCell): missing setter or instance variable
* Installed XQuartz 2.7.9

* Uninstalling pygame
```
pip uninstall pygame
Uninstalling pygame-1.9.1release:
  /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pygame
  /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pygame-1.9.1release-py2.7.egg-info
Proceed (y/n)? y
  Successfully uninstalled pygame-1.9.1release
You are using pip version 8.1.1, however version 8.1.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
* Mucked around with Homebrew (to install and uninstall pygame , moved away from using pip).
* [This](https://bitbucket.org/pygame/pygame/issues/284/max-osx-el-capitan-using-the-deprecated) thread mentioned that the problem could actually be with the sdl_image version 1.2.12. I downgraded it to 1.2.10 and the problem still persists , may be its due to the way I brewed my formula.[Here] is the formula I wrote by referring to the old sdl_image formula. For some reason , the suggested fix still doesnt work.I m just going to give up trying on El Capitan.

*  My guess it that the solution for this problem lies in the patcha and its not gettin Installed for some reason, here is the installation trace ( which also turned out to be the wrong diagnosis)

```
==> Pouring pkg-config-0.29.1.el_capitan.bottle.tar.gz
🍺  /usr/local/Cellar/pkg-config/0.29.1: 10 files, 627.2K
==> Downloading https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.10.tar.gz
Already downloaded: /Users/pdhanapal/Library/Caches/Homebrew/sdl_image-1.2.10.tar.gz
==> Downloading https://raw.githubusercontent.com/Homebrew/formula-patches/41996822/sdl_image/IMG_ImageIO.m.patch
######################################################################## 100.0%
==> Patching
==> Applying IMG_ImageIO.m.patch
can't find file to patch at input line 3
Perhaps you used the wrong -p or --strip option?
The text leading up to this was:
--------------------------
|--- IMG_ImageIO.m.orig	2012-01-21 12:51:33.000000000 +1100
|+++ IMG_ImageIO.m	2016-04-29 22:48:02.000000000 +1000
--------------------------
No file to patch.  Skipping patch.
1 out of 1 hunk ignored
Error: Failure while executing: /usr/bin/patch -g 0 -f -p0 -i /private/tmp/sdl_image--patch-20160927-21193-hvpvey/IMG_ImageIO.m.patch
pdhanapal:Formula pdhanapal$ brew install
```

* I still see the following error

```
$ python platformer_basic.py
2016-09-27 12:51:09.963 Python[27722:3247809] 12:51:09.962 WARNING:  140: This application, or a library it uses, is using the deprecated Carbon Component Manager for hosting Audio Units. Support for this will be removed in a future release. Also, this makes the host incompatible with version 3 audio units. Please transition to the API's in AudioComponent.h.
Traceback (most recent call last):
  File "platformer_basic.py", line 442, in <module>
    main()
  File "platformer_basic.py", line 354, in main
    player = Player()
  File "platformer_basic.py", line 57, in __init__
    sprite_sheet = SpriteSheet("p1_walk.png")
  File "/Users/pdhanapal/developer/pygame_examples/pygame_platform/spritesheet_function.py", line 7, in __init__
    self.sprite_sheet = pygame.image.load(file_name).convert()
pygame.error: File is not a Windows BMP file
```
