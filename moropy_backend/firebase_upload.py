import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
# Use a service account
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def upload(userID, roles):
    print('working')
    userHash = uuid.uuid4()
    doc_ref = db.collection(u'users').document(f'{userHash}')
    doc_ref.set({
        u'roles': roles,
        u'discordId': userID
    })
    return userHash
