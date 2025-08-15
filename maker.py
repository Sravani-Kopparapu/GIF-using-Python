import imageio as iio
files = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []
for file in files:
    images.append(iio.imread(file))
iio.mimsave('cat.gif', images, duration=0.5,loop=0)