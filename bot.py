from discord_webhook import DiscordWebhook

# this calls to the discord channel
WEBHOOK_URL = 'https://discordapp.c' # ur webhook url goes here


def send_to_discord(trades):
    """
    Send trade data to a Discord server using a webhook.
    """
    # Convert the trades data into a string format suitable for sending
    message = '\n'.join([', '.join(trade) for trade in trades])

    # Create a new DiscordWebhook instance
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=message)

    # Send the webhook
    response = webhook.execute()
