import cv2
import numpy as np
import math


def distance(a,b):
    if len(a)!=(len(b)):
        print ("a and b are not equal size")
    total=0
    for i in range(len(a)):
        total+=(a[i][0]-b[i][0])**2+(a[i][1]-b[i][1])**2
    return math.sqrt(total)


img = cv2.imread("lala.jpg")
# img = img.astype('uint8')
img=cv2.resize(img,(1200,700))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
binary = cv2.inRange(gray,65,255)
image,contours,hierarchy = cv2.findContours(binary.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = max(contours, key= lambda x: cv2.contourArea(x))

epsilon = 0.0005*cv2.arcLength(cnt,True)
cnt = cv2.approxPolyDP(cnt,epsilon,True)

M = cv2.moments(cnt)
cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])

hull = []
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
drawing = np.zeros((binary.shape[0], binary.shape[1], 3), np.uint8)
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)

cv2.circle(drawing,(cX,cY),7,(0,255,0),-1)

hull = cv2.convexHull(cnt,returnPoints = False)

color_contours = (0, 255, 0) # green - color for contours
color = (255, 0, 0) # blue - color for convex hull

# cv2.drawContours(drawing, cnt,0, color_contours, 1, 8, hierarchy)
# cv2.drawContours(drawing, hull, 0, color, 1, 8)

defects = cv2.convexityDefects(cnt,hull)
    #convexityDefects is array of four values [start,end,far,approximate distance to farthest point]
far_points=[]
for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	far_points.append(far)
	#cv2.line(drawing,start,end,[255,255,255],3)   
    #obtain four valleys
    #far_points contains all convexity defects
    #return far_points
centroid=[(cX,cY) for i in range (len(far_points))]
dist=[]
for i in far_points:
	dist.append(distance([i],[(cX,cY)]))
z=zip(dist,far_points)
z=sorted(z)
z=z[:5]
valleys=[]
for i,j in z:
	valleys.append(j)
print(valleys)

for i in range(4):
	for j in range(1):
		print(valleys[i][j])
		cv2.circle(drawing,(valleys[i][j],valleys[i][j+1]),7,(255,255,0),-1)
cv2.imshow('FUCK YEAH',drawing)
cv2.waitKey(0)




