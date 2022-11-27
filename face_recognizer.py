from time import sleep
import cv2
import face_recognition
import os
import numpy as np

def find_face():
    images = []
    known_face_names = []
    mylist = os.listdir(os.path.dirname(os.path.realpath(__file__))+"\\face_storage")
    for cl in mylist:
        curImg = cv2.imread(os.path.dirname(os.path.realpath(__file__))+f'\\face_storage\\{cl}')
        images.append(curImg)
        known_face_names.append(os.path.splitext(cl)[0])
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    known_face_encodings = encodeList
# Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    video_capture = cv2.VideoCapture(0)

    flag_unknown=0
    name_count=0
    name=""
    pos_name=""

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Only process every other frame of video to save time
        if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
        
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.5)
                name = "unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame
    

        if (name!="unknown" and name!="") or (name_count<6 and name!=""):
            pos_name=name
            name_count+=1
            return pos_name

        elif flag_unknown>=30 or name_count >=6:
            if flag_unknown>=30:
             flag_unknown=0
             return "unknown"
            return pos_name
        elif flag_unknown<30 and name!="":
            flag_unknown+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


