from util.Util import try_send


class Kontribusi:
    def __init__(self):
        pass

    async def do_response(self, message, args):
        await try_send(message.channel, 'https://github.com/nugroho-s/jahyadi')