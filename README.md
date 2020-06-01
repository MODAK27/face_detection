FACE_RECOGNITION
 
python video_hog_face_detect.py to detect face from HOG features(gradient)

python face_landmarks.py to detect facial landmarks by using facial_landmarks.dat file

python encodings_display.py to display 128 encodings that has been trained by resnet premodeled CNN

python create_facial_encodings.py -d location\dataset -e encodings\facial_encodings.pkl -r true

    	-d was used by arg passer for taking dataset from given input and form encodings in separate folder given by input -e

python calculate_encoding_distance.py -i location\my_photo.jpg -e encodings\facial_encodings.pkl

      to get a relative list of other images eucledian distance to given image
      
python video_facial_recognition.py -e encodings/facial_encodings.pkl --distance-tolerance 0.5
    
			to detect ur face and save it in mentioned folder
      
