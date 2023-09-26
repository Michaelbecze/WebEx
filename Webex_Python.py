import requests
import json


token = 'ZjQ4NTk4MjUtZjJkMy00YTkzLWExNzEtYmM4MGM3YTI4YTg4NzUyYzE0OGItYWFh_P0A1_b8079746-d12d-4e32-84b4-28a78b9419d8'


headers = {'Authorization' : f'Bearer {token}',
           'Content-Type' : 'application/json'}

def Create_Room(*arg):
    body = {
    "title": str(arg)}
    post_room = requests.post(url='https://webexapis.com/v1/rooms', headers=headers, data=json.dumps(body))
    print(post_room)
    
                              
                            
#Create_Room()

list_rooms = requests.get(url='https://webexapis.com/v1/rooms', headers=headers)
print(list_rooms.text)
