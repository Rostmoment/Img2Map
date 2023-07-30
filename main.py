from PIL import Image
import time
chars = ["T", ".", "B", "C", "M", "N", "R", "W"]
file = input("Enter image name: ")
start = time.time()
image = Image.open(file).convert("L") 
text = ""
x, y = 0, 0
width, height = image.size
for y in range(height):
	for x in range(width):
		pixel_value = image.getpixel((x, y))
		char_index = int((pixel_value / 255) * (len(chars) - 1))
		text+=(chars[char_index])
	text+="A"
res = Image.new('RGB', (width*20, height*20))
for i in text:
	if i == "A":
		x = 0
		y += 20
	else:
		res.paste(Image.open(f"block/block_{i}.png"), (x , y))
		x += 20
name = f"{time.time()}.png"
res.save(name)
end = time.time()
print(f"Saved in {name}\nTotal time: {round((end-start),3)} seconds!")