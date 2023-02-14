from pyrogram import Client, filters, types, raw




bot = Client(
    "akk",
    api_id = 19896844,
    api_hash = "b65c54260c633112f396a8a8195713b9",
    
)




@bot.on_message(filters.regex("Гоу"))
async def prin(bot, message):
        for i in range(50, 600):
            await bot.send_message('xJetSwapBot', i)


bot.run()
