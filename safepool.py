import math
from google.cloud import storage
from firebase import firebase
import os

FIREBASE_URL = 'https://safepool-b1b19.firebaseio.com/'

# INDEXS_OF_PEOPLE
CORD_OF_FACE = 0
AGE = 1


def upload_image_to_firebase(file_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<add your credentials path>"
    f = firebase.FirebaseApplication(FIREBASE_URL)
    client = storage.Client()
    bucket = client.get_bucket(FIREBASE_URL)
    # posting to firebase storage
    imageBlob = bucket.blob("/")
    # imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
    imagePath = file_path
    imageBlob = bucket.blob(file_path.split('/')[-1])
    imageBlob.upload_from_filename(imagePath)


def get_peoples_in_area(peoples):
    for i in peoples:
        face1 = i[CORD_OF_FACE]  # tuple of 4 corddient (x1, x2, y1, y2)
        size_of_face = math.fabs(face1[0] - face1[1]) * math.fabs(face1[2] - face1[3])
        age = i[AGE]


def safepool(dict1, dict2, key):
    base = firebase.FirebaseApplication(FIREBASE_URL, None)
    if dict1['Adults'] == dict2['Adults'] and dict1['Kids'] == dict2['Kids'] or dict1['Adults'] == dict2['Adults']:
        pass
    if dict2['pop']:
        base.put('/users/{}'.format(key), 'buoysRelease', 'true')
    elif dict1['Adults'] == 0 and dict2['Adults'] > 0 and dict1['Kids'] == 0 and dict2['Kids'] > 0:
        base.put('/users/{}'.format(key), 'notice', 'true')
    elif dict1['Adults'] == 0 and dict2['Adults'] > 0 and dict2['Kids'] > 0:
        base.put('/users/{}'.format(key), 'notice', 'true')
    elif dict1['Adults'] > 0 and dict2['Adults'] == 0 and dict2['Kids'] > 0:
        base.put('/users/{}'.format(key), 'dangerous', 'true')

# def main():
#   dict1 = {'Adults': 1, 'Kids': 0}
#  dict2 = {'Adults': 0, 'Kids': 1}
# safepool(dict1, dict2,"001")
