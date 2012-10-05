# Graphical Editor

Simulates a CLI graphical editor.

## Start up

```bash
  $ ./graphical_editor.py
```

## Commands

### I M N

Create a new M x N image with all pixels coloured white.

### C

Clear the image, setting all pixels to white.

### L X Y C

Colour the pixel (X, Y) with C.

### V X Y1 Y2 C

Draw a vertical segment of colour C in column X between Y1 and Y2 (inclusive).

### H X1 X2 Y C

Draw a horizontal segment of colour C in row Y between columns X1 and X2
 (inclusive).

### F X Y C

Fill the region of which X, Y forms a point with colour C. The region is
defined as the pixel at X, Y and any pixels of the initial colour of X, Y who
are adjacent to the initial pixels or other pixels in the set.

### S

Show the contents of the image.

### X

Terminate the session.

## License

Copyright (c) 2012 Robert James Berry
