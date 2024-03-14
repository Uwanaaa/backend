from channels.generic.websocket import AsyncWebsocketConsumer
import base64,json,numpy as np,cv2
from model.count_and_track import Chicken,Cow,Sheep,Pig,Goat
from model.new import Animal
import cv2,pickle
import subprocess

class Streams(AsyncWebsocketConsumer):
     async def connect(self):
        await self.accept()

     async def disconnect(self,close_code):
        pass

     async def receive(self,text_data):

        data = pickle.loads(text_data)
        print(text_data)

        img = cv2.imdecode(data,cv2.IMREAD_COLOR)

        print(img)

        cv2.imshow('Server:',img)

        if cv2.waitKey(5) & 0xFF == 27:
            cv2.destroyAllWindows()

        #data = json.loads(text_data)
        #selectedAnimal = data.get('selectedAnimal',[])
        #message = data.get('imageData',[])
        #imageMessage = message

        #animal = {selectedAnimal}()

        capture = cv2.VideoCapture(0)
        while True:
            ret,frame = capture.read()
            frame = np.array(frame)
            height,width = frame.shape
     
             
            #logic for the model
            class_index = animal.class_index
            capture = animal.setup_capture((width,height))
            model = animal.setup_model()
            animal.setup_zone_annotator()
            frame = animal.process_frame(model,frame,class_index)
            animal.run(class_index)


            if not ret:
                print('There was an error capturing the frame')
                exit()

            cv2.imshow('Result', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            capture.release()
            cv2.destroyAllWindows()

        await self.send(text_data=json.dumps({
            'message': imageMessage
        }))

