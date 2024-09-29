# 导入opencv
import cv2
import matplotlib.pyplot as plt

# 读入原始图像，使用cv2.IMREAD_UNCHANGED
img = cv2.imread("images/girl.jpg", cv2.IMREAD_UNCHANGED)
# 查看打印图像的shape
shape = img.shape
print(shape)
# 判断通道数是否为3通道或4通道
# create figure
fig = plt.figure(figsize=(10, 7))
# setting values to rows and column variables
rows = 1
columns = 2


if shape[2] == 3 or shape[2] == 4:
    # 将彩色图转化为单通道图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像变量 转化模式
    # cv2.imshow("gray_image", img_gray)
    fig.add_subplot(rows, columns, 2)
    plt.imshow(img_gray)

fig.add_subplot(rows, columns, 1)
plt.imshow(img)
plt.show()
# cv2.imshow("images2", img)
# cv2.waitKey(1000)  # 停顿 1000ms 后执行下面的
# cv2.destroyAllWindows()