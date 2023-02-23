from azure.storage.blob import BlobServiceClient, BlobClient


blob_service_client = BlobServiceClient.from_connection_string("[YOUR_CONNECTION_STRING]")
# Instantiate a new ContainerClient
container_client = blob_service_client.get_container_client("myappendcontainer")

# Instantiate a new BlobClient
blob_client = container_client.get_blob_client("myappendblob")

# Define the text to be uploaded
text = "This is some sample text to be uploaded to the append blob."

# Convert the text to bytes
data = text.encode("utf-8")

blob_client.upload_blob(data, blob_type="AppendBlob")