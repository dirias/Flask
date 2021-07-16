from typing import Collection
import firebase_admin
from firebase_admin import credentials, firestore

#Alternative a  export GOOGLE_CLOUD_PROJECT='PlatziFlask'
# project_id = 'PlatziFlask'
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': project_id,
# })

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_todos(user_id):
    return db.collection('users')\
    .document(user_id)\
    .collection('todos').get()