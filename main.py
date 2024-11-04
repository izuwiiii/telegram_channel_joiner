import os
from pyrogram import Client

session_folder = "path/to/session_folder"
api_id = 123456  # API ID
api_hash = 'your_api_hash'  # API Hash

session_files = [f for f in os.listdir(session_folder) if f.endswith('.session')]

app = Client(session_file, api_id=api_id, api_hash=api_hash)

for session_file in session_files:
    session_name = os.path.splitext(session_file)[0]
    session_path = os.path.join(session_folder, session_name)

    app = Client(session_path, api_id=api_id, api_hash=api_hash)

    with app:
        channel_username = "@test" #channel name or link
        try:
            chat = app.get_chat(channel_username)
            print(f"Канал найден: {chat.title}")
            app.join_chat(chat.id)
            print(f'Успешно присоединились к {chat.title}')
        except Exception as e:
            print(f'Не удалось присоединиться: {e}')