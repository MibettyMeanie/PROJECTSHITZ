import cv2
import numpy as np
import math

# IN KNUCKLES

def midpoint(a,b):
    return tuple(map(int,((a[0]+b[0])/2,(a[1]+b[1])/2)))

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return map(int,(x,y))
    else:
        return False

def drawline(img,pt1,pt2,color,thickness=1,style='dotted',gap=20):
    dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
    pts= []
    for i in  np.arange(0,dist,gap):
        r=i/dist
        x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
        y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
        p = (x,y)
        pts.append(p)

    if style=='dotted':
        for p in pts:
            cv2.circle(img,p,thickness,color,-1)
    else:
        s=pts[0]
        e=pts[0]
        i=0
        for p in pts:
            s=e
            e=p
            if i%2==1:
                cv2.line(img,s,e,color,thickness)
            i+=1

def distance2(a,b):
    dist = math.hypot(b[0] - a[0], b[1] - a[1])
    return dist


# IN VALLEY POINTS
def distance(a,b):
    if len(a)!=(len(b)):
        print ("a and b are not equal size")
    total=0
    for i in range(len(a)):
        total+=(a[i][0]-b[i][0])**2+(a[i][1]-b[i][1])**2
    return math.sqrt(total)

#IN TIPS

def unique(arr):
    arr=sorted(arr)
    xaxis=[i for (i,j) in arr]
    result=cluster(xaxis)
    mapx = {}
    for (i,j) in arr:
        mapx[i] = j
    mapy={}
    for (i,j) in arr:
        mapy[j]=i
    for i in range(0,len(result)):
        for j in range(0,len(result[i])):
            result[i][j]=mapx[result[i][j]]
    minimum=[]
    for i in result:
        minimum.append(min(i))
    ret=[]
    for i in minimum:
        ret.append((mapy[i],i))
    return ret

# IN FUNCTION UNIQUE

def cluster(xaxis):
    result=[]
    temp=[]
    temp.append(xaxis[0])
    d=50
    for i in range(1,len(xaxis)):
        if xaxis[i]-xaxis[i-1] < d:
            temp.append(xaxis[i])
        else:
            result.append(temp)
            temp=[]
            temp.append(xaxis[i])
    result.append(temp)
    return result

# PREPROCESSING AND GETTING IMAGE

img = cv2.imread("lala.jpg")
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

# this hull for drawing purpose

for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))


#  CREATING CANVAS FOR DRAWING CONTOURS

drawing = np.zeros((binary.shape[0], binary.shape[1], 3), np.uint8)

# old method for drawing contours

# for i in range(len(contours)):
#     color_contours = (0, 255, 0) # green - color for contours
#     color = (255, 0, 0) # blue - color for convex hull
#     # draw ith contour
#     cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
#     # draw ith convex hull object
#     cv2.drawContours(drawing, hull, i, color, 1, 8)

# DRAWING CENTROID 
cv2.circle(drawing,(cX,cY),7,(0,255,0),-1)

#  draw contours and hull points

cv2.drawContours(drawing,[cnt],0,(255,255,255),2)
for i in range(len(contours)):
    color = (255, 0, 0) 
    cv2.drawContours(drawing, hull, i, color, 1, 8)


#HULL OF MAXIMUM CONTOUR FOR FURTHER PROCESSING
hull = cv2.convexHull(cnt,returnPoints = False)


#VALLEY POINTS

defects = cv2.convexityDefects(cnt,hull)
    #convexityDefects is array of four values [start,end,far,approximate distance to farthest point]
far_points=[]

for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	far_points.append(far)
	
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

for (i,j) in valleys:
        cv2.circle(drawing,(i,j),7,[255,255,0],-1)


# TIP POINTS

arr=[]

for (i,j) in valleys:
    arr.append(j)

average=sum(arr)/len(arr)
corners=[]
tips=[]

for i in hull:
    corners.append((cnt[i[0]][0][0],cnt[i[0]][0][1]))

for (i,j) in corners:
    if j < average:
        tips.append((i,j))

arr=[j for (i,j) in tips]
average2=sum(arr)/len(arr)
average=(average+average2)/2
tips=[]

for (i,j) in corners:
    if j < average:
        tips.append((i,j))

corners=sorted(corners)
tips.append(corners[0])
tips=sorted(tips)
tips=unique(tips)

for (i,j) in tips:
    cv2.circle(drawing,(i,j),7,[0,255,255],-1)

#KNUCKLES

tips=sorted(tips)
valleys=sorted(valleys)
thumb_point=tips[0]
base=(cX,drawing.shape[0])
valley1=valleys[1]
valley0=valleys[0]
#cv2.line(drawing,valley1,valley0,[255,255,255],3)
knuckles=[]
dist=[]
line1=line(thumb_point,base)
line2=line(valley1,valley0)
thumb_base=intersection(line1,line2)
knuckles.append(tuple(thumb_base))


for i in range(1,len(valleys)):
    knuckles.append(midpoint(valleys[i],valleys[i-1]))

for i in knuckles:
    cv2.circle(drawing,i,7,[255,0,0],-1)
    
for i,j in zip(tips,knuckles):
    drawline(drawing,i,j,[255,0,0],3)
    dist.append(distance2(i,j))

#sixth distance
try:
    drawline(drawing,knuckles[0],knuckles[1],[255,0,0],3)
    dist.append(distance2(knuckles[0],knuckles[1]))
except:
    print ("all knuckles not detected")

#seventh distance
try:
    drawline(drawing,knuckles[1],knuckles[4],[255,0,0],3)
    dist.append(distance2(knuckles[1],knuckles[4]))
except:
    print ("all knuckles not detected")
   



# FINAL FUCK YEAH
cv2.imshow('FUCK YEAH',drawing)
cv2.waitKey(0)




