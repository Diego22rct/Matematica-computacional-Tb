import cv2
import matplotlib.pyplot as plt
import PIL as pil

# constants for the image
picture = cv2.imread("image4.jpg")


def Equialization():
    img = picture
    cv2.imshow("Imagen inicial", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.hist(img.ravel(), 256, [0, 256], color="black", histtype="bar")
    plt.savefig("histogram/normal/hist.png")
    plt.show()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    # Apply histogram equalization
    gray = cv2.equalizeHist(gray)

    # Show the image with 400x400 size
    cv2.imshow("Imagen equalizada", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # draw the histogram of the grayscale image with matplotlib in 0 to 7 range
    plt.hist(gray.ravel(), 256, [0, 256], color="black", histtype="bar", ec="black")
    plt.savefig("histogram/equalized/hist.png")
    plt.show()

    # Save the image
    cv2.imwrite("image_p/equa/pictureEqua.jpg", gray)


def Expantion(x, y):
    img = picture
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # draw the histogram of the grayscale image with matplotlib
    plt.hist(img.ravel(), 256, [0, 256], color="black", histtype="bar", ec="black")
    plt.show()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    # Apply histogram exapantion
    gray = cv2.normalize(gray, None, x, y, cv2.NORM_MINMAX)

    # Show the image with 400x400 size
    cv2.imshow("image", gray)
    cv2.waitKey(0)

    # draw the histogram of the grayscale image with matplotlib in 0 to 7 range
    plt.hist(gray.ravel(), 256, [0, 256], color="black", histtype="bar", ec="black")
    plt.show()

    # Save the image
    cv2.imwrite("imageexpan2.jpg", gray)


def equa2():
    img = picture

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:, :, 1] = cv2.equalizeHist(img_yuv[:, :, 1])

    plt.hist(img_yuv.ravel(), 256, [0, 256], color="black", histtype="bar", ec="black")
    plt.show()

    # convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    cv2.imshow("Color input image", img)
    cv2.imshow("Histogram equalized", img_output)

    cv2.waitKey(0)


def equa3():
    rgb_img = picture

    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 2] = cv2.equalizeHist(ycrcb_img[:, :, 2])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    cv2.imshow("equalized_img", equalized_img)
    cv2.waitKey(0)
