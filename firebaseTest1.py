from firebase import firebase

firebase = firebase.FirebaseApplication('https://kbms-bot.firebaseio.com/')
result = firebase.get('/firstChild',None)
print (result)
