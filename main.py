import scrape
import bot

if __name__ == '__main__':
    print('test')
    # Scrape the data
    trades = scrape.scrape_trades()

    # Print the data
    # Print the data
    for trade in trades:
        formatted_trade = '**' + ' - '.join(trade) + '**'  # This will make the text bold.
        print(formatted_trade)

        print(trade)

    # Send the data to your Discord server
    bot.send_to_discord(trades)
