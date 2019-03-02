from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from googleapiclient import errors

project_id = "projects/leafy-clone-233310"
ml = discovery.build('ml','v1')

print("Built discovery object!")

# request_dict = {'name': 'your_model_name',
#                       'description': 'your_model_description'}

request_dict = {
                "features": [
                    {"type": "DOCUMENT_TEXT_DETECTION"}
                    ],
                "image": {
                    "source": {
                                  "imageUri": "gs://vision-api-handwriting-ocr-bucket/handwriting_image.png"
                        }

                    }


}


response = ml.projects().models().create(parent=project_id, body=request_dict).execute()
print(response)


