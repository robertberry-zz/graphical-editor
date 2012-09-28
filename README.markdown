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

### S

Show the contents of the image.

### X

Terminate the session.

## License

Copyright (c) 2012 Robert James Berry
