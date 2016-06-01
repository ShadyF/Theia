# Theia
An image processing tool made using Python 3.4. Demonstrates how images can be manipulated via Pillow and displayed via Tkinter's canvas widget.

### Supported Manipulations
1. Geometric Transformations
  * Translation
  * Rotation
  * Scaling
  * Shearing
  
2. Image Filtering using a user-defined 3x3 kernel.

### Compatibility
Tested on Ubuntu 14.04 and Windows 7/8/10

### Dependencies
1. Tkinter (GUI Interface)
  *Comes pre-installed with python
2. Pillow (Image Library)
  *``` sudo pip3 install Pillow
  
### Building
```python3 Theia.py```

Theia can also be **compiled** using [Nuitka](https://github.com/kayhayen/Nuitka)
```nuitka --recurse-all Theia.py```
