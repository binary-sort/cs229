from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/numbers/y0.4.png')
iar = np.asarray(i)

print iar
plt.imshow(iar)
plt.show()
