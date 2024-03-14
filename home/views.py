from django.shortcuts import render
import subprocess,pickle,cv2



def home(request):
    return render(request,'home/frontend.html')

def open_cam(request):
     print("start")
     subprocess.run(['python', 'new.py', '--source', '0'])
     return "done"


def open_camera(request):
      capture = cv2.VideoCapture(0)
      capture.set(3,640)
      capture.set(4,480)

      while capture.isOpened():
            ret,img = capture.read()
            cv2.imshow('Client',img)
            buffer = cv2.imencode('.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),30])
            img_as_bytes = pickle.dumps(buffer)
            detect(img_as_bytes)

            if cv2.waitKey(5) & 0xFF == 27:
                 break
      cv2.destroyAllWindows()


def detect(data):
     data = pickle.loads(data)
     print(data)

if __name__ == "__main__":
     data = open_camera()
     print(data)