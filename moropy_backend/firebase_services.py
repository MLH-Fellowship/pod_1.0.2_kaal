import uuid

import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
batch = db.batch()


def upload(userID, roles, userName):
    user_ref = db.collection(u'users')

    userHash = uuid.uuid4()
    doc_ref = user_ref.document(f"{userHash}")
    doc_ref.set(
        {
            u'roles': roles,
            u'discordId': str(userID),
            u'userName': userName,
            u'status': 'Away',
        }
    )
    return userHash


def get_user(userHash):
    user_ref = db.collection(u'users')

    users = user_ref.stream()
    for user in users:
        if user.id == userHash:
            return user.to_dict()
    return 'User not found'


def validate_user(userID):
    duplicates = db.collection(u'users').where(u'discordId', u'==', (userID)).stream()

    print('here ' + userID)
    # duplicates = user_ref.stream()
    for duplicate in duplicates:
        print(duplicate.to_dict()['discordId'])
        if str(userID) == str(duplicate.to_dict()['discordId']):
            return duplicate.id
    return 'User not found'


def store_activity(userHash, activity):
    user_ref = db.collection(u'users')

    doc_ref = user_ref.document(f'{userHash}').collection('activity')
    for i in range(len(activity)):
        doc_ref.document().set(activity[i])
    return "working"


def update(userHash, status):
    user_ref = db.collection(u'users')

    doc_ref = user_ref.document(f'{userHash}')
    doc_ref.update(
        {
            u'status': status,
        }
    )
    return 'successful'


def updateWebhooks(userHash, webhookUrls):
    user_ref = db.collection(u'users')

    doc_ref = user_ref.document(f'{userHash}')
    doc_ref.update({u'webhookUrls': webhookUrls})
    return True


def makeChannel(channel_id, url):
    channel_ref = db.collection(u'channels')
    channel_ref.document(channel_id).set({"url": url})
    return True


def getChannel(channel_id):

    channel_ref = db.collection(u'channels')
    res = channel_ref.stream()
    for r in res:
        if r.id == channel_id:
            print(True)
            return r.to_dict()

    return ''
