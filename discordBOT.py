import os
from dhooks import Webhook, Embed, File

image2_path = 'sakamoto.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[Sakamoto days link - click here -](https://www.sakamotodayschapters.com/)**",
        color=0xF0B232
    )
    
    embed.set_image(url="attachment://sakamoto.png")
    file = File(image2_path, name="sakamoto.png")
    hook.send("@everyone 📢 Sakamoto days", embed=embed, file=file)
