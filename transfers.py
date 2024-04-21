import time
from web3 import Web3
import pandas as pd

# Connect to an Ethereum node (replace with your provider)
infura_url = "YOUR_INFURA_URL"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Contract ABI (replace with the ABI of the contract you're interested in)
contract_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'

# Contract address
contract_address = "YOUR_CONTRACT_ADDRESS"

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Define a function to handle events and provide insights
def handle_event(event):
    event_data = dict(event)
    df = pd.DataFrame([event_data['args']])
    
    # Basic insights - you can expand on this
    print(f"Event: {event['event']}")
    print(df.describe())

# Subscribe to new blocks
def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

# Create a filter for the 'Transfer' and 'Approved' events
event_filter = contract.events.Transfer.createFilter(fromBlock='latest')
event_filter2 = contract.events.Approval.createFilter(fromBlock='latest')

# Run the log loop with a polling interval of 1 second
log_loop(event_filter, 1)
log_loop(event_filter2, 1)