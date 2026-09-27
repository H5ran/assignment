import jetson.inference
import jetson.utils
import sys

IMAGE_PATH = r"/home/nvidia/Desktop/000.jpg"
MODEL = "ssd-mobilenet-v2"
THRESHOLD = 0.62

net = jetson.inference.detectNet(MODEL, threshold=THRESHOLD)

img = jetson.utils.loadImage(IMAGE_PATH)
if img is None:
    print("无法读取图片")
    sys.exit(1)

print("图片尺寸:", img.width, "x", img.height)
print("模型:", MODEL, "阈值:", THRESHOLD)
print("=" * 60)

detections = net.Detect(img)

print("共检测到", len(detections), "个目标")
print("=" * 60)

for i, det in enumerate(detections):
    print("Target #" + str(i + 1))
    print("  classID   :", det.ClassID)
    print("  Classname :", net.GetClassDesc(det.ClassID))
    print("  Confidence   :", det.Confidence)
    print("  Left  :", det.Left)
    print("  Top   :", det.Top)
    print("  Right   :", det.Right)
    print("  Right   :", det.Bottom)
    print("  Width     :", det.Width)
    print("  Height     :", det.Height)
    print("  Area    :", det.Area)
    print("  Center   :", det.Center[0], det.Center[1])
    print("-" * 60)

print("推理耗时:", net.GetNetworkTime(), "ms")

display = jetson.utils.videoOutput("display://0")
display.Render(img)
display.SetStatus("Detected " + str(len(detections)) + " objects")

while display.IsStreaming():
    pass