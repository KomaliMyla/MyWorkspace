import qrcode
song = "https://www.youtube.com/watch?v=wdHeiVf0mds"
img = qrcode.make(song)
img.save('myQR.png')
img.show()