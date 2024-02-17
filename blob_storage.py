from azure.storage.blob import BlobServiceClient, BlobClient
import os

Azure_Storage_Blob_Connection_String = 'DefaultEndpointsProtocol=https;AccountName=personal922;AccountKey=F+ZQP/ljFP8D80d7P10tAft6H9jJoZ/0B0Swayst8eGg4DUOUW3vUUK655hNS0nv5qTimgk8bV3E+AStDdNaJA==;EndpointSuffix=core.windows.net'
Container_Name = 'webapp'
Blob_Folder = 'uploaded_imgs'



def file_storage_blob(bin_file,filename):
    """
    This function upload the binary file to Azure_Storage/Container/Blob
    bin_file: the binary file you want to upload
    filename: the path that will the binary file
    """
    try:
        blob_name = os.path.join(Blob_Folder,filename)  # set the blob name (path + filename)
        blob_server_client = BlobServiceClient.from_connection_string(Azure_Storage_Blob_Connection_String) #connect to your Azure storage resource
        blob_client = blob_server_client.get_blob_client(container = Container_Name, blob = blob_name)  #connect to the container and the underlying blob

        blob_client.upload_blob(bin_file,blob_type='BlockBlob',overwrite = True)
        print('Blob Upload Success!')
    except:
        print('Blob Upload Failure.')
    
