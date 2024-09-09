import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

# El işi fikirleri listesi
plastic_craft_ideas = [
    "Plastik şişelerden saksı yapabilirsiniz.",
    "Eski plastik kapaklardan mozaik tablo yapabilirsiniz.",
    "Plastik kutulardan kalemlik yapmayı deneyin."
]

# Geri dönüşüm için bilgi listesi
recycling_info = {
    "plastik şişe": "Geri dönüştürülebilir. Plastik atık kutusuna atmalısınız.",
    "cam şişe": "Geri dönüştürülebilir. Cam atık kutusuna atmalısınız.",
    "kağıt": "Geri dönüştürülebilir. Kağıt atık kutusuna atmalısınız.",
    "alüminyum kutu": "Geri dönüştürülebilir. Metal atık kutusuna atmalısınız.",
    "piller": "Piller tehlikeli atık grubuna girer, özel atık toplama noktalarına götürmelisiniz."
}

# Ayrışma süreleri
decomposition_times = {
    "plastik şişe": "450 yıl",
    "cam şişe": "1 milyon yıl",
    "kağıt": "2-6 hafta",
    "alüminyum kutu": "200-500 yıl",
    "piller": "100 yıl"
}

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam! Size nasıl yardımcı olabilirim?")

    # El işi fikirleri
    elif message.content.startswith('$elisi'):
        await message.channel.send("İşte plastikten yapabileceğiniz birkaç el işi fikri:")
        for idea in plastic_craft_ideas:
            await message.channel.send(f"- {idea}")

    # Geri dönüşüm rehberi
    elif message.content.startswith('$geri_donusum'):
        item = message.content[len('$geri_donusum '):].strip().lower()
        response = recycling_info.get(item, "Bu eşya hakkında bilgi bulamadım.")
        await message.channel.send(response)

    # Ayrışma süreleri
    elif message.content.startswith('$ayrismasüresi'):
        item = message.content[len('$ayrismasüresi '):].strip().lower()
        response = decomposition_times.get(item, "Bu eşyanın ayrışma süresi hakkında bilgi bulamadım.")
        await message.channel.send(response)

    else:
        await message.channel.send("Komut listesi:\n- $merhaba\n- $elisi\n- $geri_donusum <eşya>\n- $ayrismasüresi <eşya>")

client.run("TOKEN")
