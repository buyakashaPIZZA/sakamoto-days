import os
from dhooks import Webhook, Embed, File

image2_path = 'kaiju.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[Kaiju no.8 link - click here -](https://kaijunomanga.online/)**",
        color=0x3498DB
    )
    
    embed.set_image(url="attachment://sakamoto.png")
    file = File(image2_path, name="sakamoto.png")
    hook.send("@everyone 📢 Sakamoto days", embed=embed, file=file)
