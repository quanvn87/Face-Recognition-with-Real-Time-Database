import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendentrealtime-default-rtdb.firebaseio.com/"
})

ref = db.reference("people")

data = {
    "1234":
        {
            "name": "Keanu Reeves",
            "major": "actor",
            "total_attendance": 6,
            "standing": "G",
            "last_attendance_time": "2023-6-13, 11:53:00"
        },
    "3312":
        {
            "name": "Huge Jackman",
            "major": "actor",
            "total_attendance": 7,
            "standing": "G",
            "last_attendance_time": "2023-6-13, 11:53:00"
        },
    "4231":
        {
            "name": "Ju Jingyi",
            "major": "actor",
            "total_attendance": 6,
            "standing": "B",
            "last_attendance": "2023-6-13, 11:53:00"
        },
    "4321":
        {
            "name": "Ju Jingyi",
            "major": "actor",
            "total_attendance": 6,
            "standing": "B",
            "last_attendance_time": "2023-6-13, 11:53:00"
        },
    "1233":
        {
            "name": "Lai Anh Quan",
            "major": "Programmer",
            "total_attendance": 6,
            "standing": "B",
            "last_attendance_time": "2023-6-13, 11:53:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)