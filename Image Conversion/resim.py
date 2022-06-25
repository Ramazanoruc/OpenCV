import cv2

def nothing(x):#Trackbar oluştururken hata almamamız için
    pass


img1=cv2.imread("1.jpg")
img1=cv2.resize(img1,(640,480))

img2=cv2.imread("2.jpg")
img2=cv2.resize(img2,(640,480))

output=cv2.addWeighted(img1,0.5,img2,0.5,0)
windowname="Donusum"
cv2.namedWindow(windowname)

cv2.createTrackbar("Alpha/Beta",windowname,0,500,nothing)

while True:
    cv2.imshow(windowname,output)
    alpha=cv2.getTrackbarPos("Alpha/Beta",windowname)/500
    beta=1-alpha
    output=cv2.addWeighted(img1,alpha,img2,beta,0)
    print(alpha,beta)

    if cv2.waitKey(1) ==27:
        break


cv2.destroyAllWindows()
