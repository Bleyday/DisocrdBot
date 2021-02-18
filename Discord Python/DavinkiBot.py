import discord
import datetime

gif_token = 811729657249398785
class MyClient(discord.Client):

    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        channel = 811607792389587028
        if message.author == client.user:
            return

        if message.content.startswith("$jujutsu"):
            jetzt = datetime.datetime.now()
            jujufriday = datetime.datetime(2021,2,19,19,45)

            left_time = jujufriday - jetzt
            if left_time.days == 0:
                print(left_time.total_seconds())
                await message.channel.send(file=discord.File("tenor.gif"))
            else:
                print(int(left_time.total_seconds() / 86400)) #Tage
                print(int(left_time.total_seconds() / 3600)) #Stunden
                await message.channel.send(left_time)

            if left_time == 0:
                jujufriday = jujufriday.day + 7

client = MyClient()
client.run("ODExNjEwNjU4MDM3OTU2NjE4.YC0tUw.TyCwh2auL9dzidzGyKoowlV1jgo")
channel = client.get_channel(811607792389587028)

