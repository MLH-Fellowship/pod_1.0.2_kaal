import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
# Use a service account
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
user_ref = db.collection(u'users')
batch = db.batch()


def upload(userID, roles):
    print('working')
    userHash = uuid.uuid4()
    doc_ref = user_ref.document(f'{userHash}')
    doc_ref.set({
        u'roles': roles,
        u'discordId': userID
    })
    return userHash


def get_user(userHash):
    print("getting user")
    users = user_ref.stream()
    for user in users:
        if(user.id == userHash):
            print(user.to_dict())
            return user.to_dict()
        else:
            return 'User not found'


def store_activity(userHash, activity):
    print('storing activity')
    doc_ref = user_ref.document(f'{userHash}').collection('activity')
    for i in range(len(activity)):
        doc_ref.document().set(activity[i])

    print('done')
    return "working"


def update(userHash, status):
    print('updating status')
    doc_ref = user_ref.document(f'{userHash}')
    doc_ref.update({
        u'status': status,
    })
    return 'successful'
