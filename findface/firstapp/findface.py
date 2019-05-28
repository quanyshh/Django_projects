import cv2
import os

class FaceControl():

    def faces(self, url):
        print(url)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cascade_url = BASE_DIR+ '/static/' +'haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(cascade_url)
        dic_to_url = url['model_pic']
        url_path = dic_to_url.split('/')[0]
        url_file_type = dic_to_url.split('/')[1].split('.')[1]
        print(url_file_type)
        image_path = BASE_DIR+ '/media/' +dic_to_url
        image = cv2.imread(image_path)
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        count=0
        count_arr=[]
        for (x,y,w,h) in faces:
            count_arr.append(count)
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            crop_image = image[y:y+h, x:x+w]
            imwrite_url = BASE_DIR+ '/media/'+ url_path + '/' +'face-'+str(count)+ '.' +url_file_type
            print(imwrite_url)
            count+=1
            cv2.imwrite(imwrite_url, crop_image)
            cv2.imwrite(BASE_DIR+'/media/'+url_path+'/rectangle.'+url_file_type, image)
        return count_arr
