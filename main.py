import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

response = supabase.auth.sign_in_with_password(
    {
        "email": "matheusfranco2323@gmail.com",
        "password": "32174353"
    }
)

print("Login successful")

user = response.session.user
if user:
    user_id = user.id  # This is the UUID of the logged-in user

    data_bot = {
        "user_id": user_id,  # Use the logged-in user's UUID
        "name": "Example Name",
        "cliente_server_id": 123,
    }

    result = supabase.table("bot").insert(data_bot).execute()
