# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import argparse
import time


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--display-time", type=int, required=False, default=-1,
                    help="Amount of time to display the image.  Sometimes 'q' does not work right away")
    args = vars(ap.parse_args())
    start = time.time()

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    p = "H:\\jupyter_projects\\face_detection\\github_uploaded\\shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)

    cap = cv2.VideoCapture(0)
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("H:\\jupyter_projects\\face_detection\\github_uploaded\\videos\\cam_video.mp4", vid_cod, 20.0, (640,480))
    while True:
        # load the input image and convert it to grayscale
        _, image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale image
        rects = detector(gray, 0)

        # loop over the face detections
        for (i, rect) in enumerate(rects):
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # loop over the (x, y)-coordinates for the facial landmarks
            # and draw them on the image
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

        # show the output image with the face detections + facial landmarks
        cv2.imshow("Output", image)
        output.write(image)
        key = cv2.waitKey(5) & 0xFF
        if key == ord("q"):
            break

        if args['display_time'] > 0 and (time.time() - start) > args['display_time']:
            break

    cv2.destroyAllWindows()
    cap.release()
    output.release()
