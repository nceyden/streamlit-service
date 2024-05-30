import preprocessing
import model


def main(image):

    ims = preprocessing.get_slices_nii(image) 
    ims = preprocessing.preprocessing_nii(ims)

    out = model.interference(ims)

    print(out.shape)