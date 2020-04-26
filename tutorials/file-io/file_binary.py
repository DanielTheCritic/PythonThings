# Opening a new binary file for write with wb = write binary
width = 100
height = 100

with open("mybinaryfile.bmp", mode="wb") as b:
    # BMP header
    b.write(b'BM')
    size_bookmark = b.tell()  # The next four bytes hold the filesize as a 32bit
    b.write(b'\x00\x00\x00\x00') # little-endian integer. Zero placeholder for now.

    b.write(b'\x00\x00') #Unused 16bit integer - should be zero
    b.write(b'\x00\x00') #Unused 16bit integer - should be zero

    pixel_offset_bookmark = b.tell()  # The next four bytes hold the integer offset o the pixel data.
    b.write(b'\x00\x00\x00\x00') # Zero placeholder for now.

    #Img header
    b.write(b'\x28\x00\x00\x00') # Image header size in bytes - 40 decimal
    # etc etc etc
    
# Check online for how to create BMP files