from web3 import Web3

def check_eth_balance(address, rpc_url):
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        if w3.isConnected():
            balance_wei = w3.eth.get_balance(address)
            balance_eth = w3.fromWei(balance_wei, 'ether')
            return balance_eth
        else:
            return "Failed to connect to the Ethereum node"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    eth_rpc_url = input("Enter the Ethereum node's RPC URL: ")
    
    wallet_addresses = []
    while True:
        address = input("Enter an Ethereum wallet address to check (or 'q' to finish): ")
        if address.lower() == 'q':
            break
        wallet_addresses.append(address)

    for address in wallet_addresses:
        balance = check_eth_balance(address, eth_rpc_url)
        print(f"The balance of wallet address {address} is {balance} ETH")
