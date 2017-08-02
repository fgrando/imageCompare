#thanks to http://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

IMG_A_OUTPUT_NAME="imgA.bmp"
IMG_B_OUTPUT_NAME="imgB.bmp"

def process(imageA, imageB, args):
        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        #print("SSIM: {}".format(score))
        print score

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,
                cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]


        # loop over the contours
        for c in cnts:
                # compute the bounding box of the contour and then draw the
                # bounding box on both input images to represent where the two
                # images differ
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if args["store"]:
                cv2.imwrite(IMG_A_OUTPUT_NAME, imageA);
                cv2.imwrite(IMG_B_OUTPUT_NAME, imageB);

        #last thing because it stops processing after waitkey
        if args["verbose"]:
                # show the output images
                cv2.imshow(IMG_A_OUTPUT_NAME, imageA)
                cv2.imshow(IMG_B_OUTPUT_NAME, imageB)
                cv2.imshow("Diff", diff)
                cv2.imshow("Thresh", thresh)
                cv2.waitKey(0)


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--imgA", required=True,
	help="first image")
ap.add_argument("-b", "--imgB", required=True,
	help="second image")
ap.add_argument("-v", "--verbose", action='store_true',
	help="display windows with intermediate images")
ap.add_argument("-s", "--store", action='store_true',
	help="save the comparison results")
args = vars(ap.parse_args())

# load the two input images
imageA = cv2.imread(args["imgA"])
imageB = cv2.imread(args["imgB"])

process(imageA, imageB, args)
