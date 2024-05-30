import numpy as np
import nibabel as nib

def get_transpose(image,x=0,y=1,z=2):
    return image.transpose(x,y,z)

def get_slices_nii(image):
    images_slices = list()
    
    image_nii = nib.load(image).get_fdata()    
    image_nii = get_transpose(image_nii,2,1,0)

    for im in image_nii:
        images_slices.append(im.astype('float32'))
    
    return images_slices
    
def preprocessing_nii(images):
    for i in range(len(images)):
        images[i][images[i] < 0] = 0
        images[i] = images[i]/np.max(images[i])
        
    return images

