import os
from supabase import create_client, Client
from dotenv import load_dotenv
import uuid

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def upload_supabse(filepath = 'local_save.png'):
    f_name = f"file-{uuid.uuid4().hex[-4:]}"
    response = supabase.storage.from_('test-bucket').upload(f_name, filepath)
    res = supabase.storage.from_('test-bucket').get_public_url(f_name)
    return res

# if __name__ == '__main__':
#     # res = supabase.storage.create_bucket('test2-bucket')
#     # print(supabase.list_buckets())
#     upload_supabse()

