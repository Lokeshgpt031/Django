from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('github.png')
img = img.resize((48,48))
print(img)
img.save('github.png')
plt.imshow(img)