import os
from supabase import create_client, Client
from dotenv import load_dotenv
import uuid

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def upload_supabse(filepath = '/tmp/local_save.png'):
    print("Uploading to Supabase public bucket...")
    f_name = f"file-{uuid.uuid4().hex[-4:]}"
    response = supabase.storage.from_('test-bucket').upload(f_name, filepath)
    print(f'Image successfully uploaded!')
    res = supabase.storage.from_('test-bucket').get_public_url(f_name)
    print('Public URL fetched!')
    return res

# if __name__ == '__main__':
#     # res = supabase.storage.create_bucket('test2-bucket')
#     # print(supabase.list_buckets())
#     upload_supabse()

