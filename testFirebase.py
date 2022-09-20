import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

email = input('email:')
# password = input('password:')

user = auth.get_user_by_email(email=email)

print(user.display_name)

docs = db.collection('weights').get()

for doc in docs:
    print(doc.to_dict())
