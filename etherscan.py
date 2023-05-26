import requests

def get_wallet_transactions(wallet_address):
    url = f"https://api.blockchair.com/Ethereum/dashboards/address/{wallet_address}"
    response = requests.get(url)
    data = response.json()
    print(data)
    if data.get('data'):
        transactions = data['data'][wallet_address]['transactions']
        for transaction in transactions:
            # Extract relevant transaction details
            transaction_hash = transaction['hash']
            block_time = transaction['time']
            block_height = transaction['block_id']
            sender_address = transaction['inputs'][0]['recipient']
            recipient_address = transaction['outputs'][0]['recipient']
            amount = transaction['outputs'][0]['value']

            # Print or process the transaction details
            print(f"Transaction Hash: {transaction_hash}")
            print(f"Block Time: {block_time}")
            print(f"Block Height: {block_height}")
            print(f"Sender Address: {sender_address}")
            print(f"Recipient Address: {recipient_address}")
            print(f"Amount: {amount}")
            print('---------------------------------')
    else:
        print("No transactions found for the wallet.")

# Replace 'your_wallet_address' with the actual Bitcoin wallet address
wallet_address = '0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5'

get_wallet_transactions(wallet_address)