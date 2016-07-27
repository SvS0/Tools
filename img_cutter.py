from PIL import Image

im = Image.open("roguelikeCity_magenta.png")


tile_size = (17, 17)

x_tile = im.size[0] / tile_size[0]
y_tile = im.size[1] / tile_size[1]


for i in range(0, x_tile + 1):
	for j in range (0, y_tile + 1):
		
		rect_origin = (tile_size[0] * i,
					tile_size[1] * j,
					(tile_size[0] * (i + 1)),
					tile_size[1] * (j + 1) - 1)

		region = im.crop(rect_origin)
		
		rect_destiny = (tile_size[0] * i,
						((tile_size[1] - 1) * j),
						tile_size[0] * (i + 1),
						(tile_size[1] * (j + 1)) - j - 1)

		im.paste(region, rect_destiny)

	
	rect_origin = ((tile_size[0] * i),
				0,
				tile_size[0] * (i + 1),
				tile_size[1] * j)

	region = im.crop(rect_origin)

	rect_destiny = ((tile_size[0] * i) - i,
				0,
				(tile_size[0] * (i + 1)) - i,
				tile_size[1] * j)

	im.paste(region, rect_destiny)

im2 = Image.new("RGBA", (im.size[0] - x_tile, im.size[1] - y_tile))

rect_origin = (0, 0, im2.size[0], im2.size[1])
region = im.crop(rect_origin)

im2.paste(region, rect_origin)

im2.save("roguelikeCity_magenta2.png")
im2.show()