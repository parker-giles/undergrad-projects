import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

original_image = Image.open(r"C:\Users\parke\Desktop\svd_project\_nighthawks.jpg")

original_image = np.array(original_image).astype(np.float32)

#Normalize b/c JPG which are in [0, 255] which is fine, but for better results we want [0, 1] which is what PNGs are in. 
#If this is not performed some singular values may become more important than they actually are and mess with the output. 
if original_image.max() > 1:
    original_image = original_image / 255.0

#Split channels, recall: A[height, width, channel]
r = original_image[:, :, 0]
g = original_image[:, :, 1]
b = original_image[:, :, 2]

# SVD for each color channel, 'full_matrices=False' gives us the faster/reduced verison of the SVD
# Also gives the relative, cumulative sums of each
U_r, S_r, VT_r = np.linalg.svd(r, full_matrices=False)
relative_r = S_r / S_r.sum()
cumulative_r = np.cumsum(relative_r)
print (f"cumulative_r: {cumulative_r}\n")

U_g, S_g, VT_g = np.linalg.svd(g, full_matrices=False)
relative_g = S_g / S_g.sum()
cumulative_g = np.cumsum(relative_g)
print (f"cumulative_g: {cumulative_g}\n")

U_b, S_b, VT_b = np.linalg.svd(b, full_matrices=False)
relative_b = S_b / S_b.sum()
cumulative_b = np.cumsum(relative_b)
print (f"cumulative_b: {cumulative_b}")

#Plotting the various channels a la semilog.
plt.figure(figsize=(7,5))
plt.semilogy(S_r, 'r', label='Red Channel')
plt.semilogy(S_g, 'g', label='Green Channel')
plt.semilogy(S_b, 'b', label='Blue Channel')
plt.title("Singular Values")
plt.xlabel("Index")
plt.ylabel("singular Value in log scale")
plt.legend()
plt.grid(True)
plt.show()

#Reconstruction machine
def reconstruct(U, S, VT, k):
    return U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

ranks = [5, 20, 50, 100]

plt.figure(figsize=(10,9))

for i, k in enumerate(ranks):
    rk = reconstruct(U_r, S_r, VT_r, k)
    gk = reconstruct(U_g, S_g, VT_g, k)
    bk = reconstruct(U_b, S_b, VT_b, k)

    #This puts the channels backtogether 
    new_image_k = np.stack((rk, gk, bk), axis = 2)

    plt.subplot(2, 2, i+1)
    plt.imshow(new_image_k)
    plt.title(f"Rank = {k}")
    plt.axis('off')

plt.tight_layout()
plt.show()



