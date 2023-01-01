from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23980613"))
    API_HASH = getenv("API_HASH", "b54b7945e223bded6baa22d0a7c72884")
    BOT_TOKEN = getenv("BOT_TOKEN", "5685807128:AAFoTlc7eVbyQFyRRuZ_PpXF8Kmiz9weB8U")
    FSUB = getenv("FSUB", "ndjdmdjdjdndn")
    CHID = int(getenv("CHID", "-1001894487652")
    SUDO = list(map(int, getenv("SUDO", "5531461861").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://evatgbottelegram:evatgbottelegram@cluster0.hckeuhb.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
