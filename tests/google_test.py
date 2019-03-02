from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from googleapiclient import errors

ml = discovery.build('ml','v1')

print("Built discovery object!")


