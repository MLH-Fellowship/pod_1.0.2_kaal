import uuid

import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
user_ref = db.collection(u'users')
batch = db.batch()


def upload(userID, roles, userName):
    userHash = uuid.uuid4()
    doc_ref = user_ref.document(f"{userHash}")
    doc_ref.set(
        {
            u'roles': roles,
            u'discordId': userID,
            u'userName': userName,
            u'status': 'Away',
        }
    )
    return userHash


def get_user(userHash):
    users = user_ref.stream()
    for user in users:
        if user.id == userHash:
            return user.to_dict()
    return 'User not found'


def store_activity(userHash, activity):
    doc_ref = user_ref.document(f'{userHash}').collection('activity')
    for i in range(len(activity)):
        doc_ref.document().set(activity[i])
    return "working"


def update(userHash, status):
    doc_ref = user_ref.document(f'{userHash}')
    doc_ref.update(
        {
            u'status': status,
        }
    )
    return 'successful'


def updateWebhooks(userHash, webhookUrls):
    doc_ref = user_ref.document(f'{userHash}')
    upload = []
    for j in webhookUrls:
        for x in j.values():
            upload.append(x)
    doc_ref.update({
        u'webhookUrls': upload
    })
    channel_ref = db.collection(u'channels')
    for i in webhookUrls:
        channel_ref.document().set(i)

    return True
