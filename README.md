# Ethereum-Event-Tracker

One-line description: Python script to track and analyze Ethereum blockchain events using Web3.py.

Summary: This Python script uses Web3.py to connect to an Ethereum node, utilizing an Infura URL for access. It defines interactions with a smart contract using a specified ABI and contract address. The script creates instances of contract events and monitors them in real-time by polling new blockchain entries. Events are handled by converting event data into a Pandas DataFrame for basic analysis and insight extraction, displayed in the console. The script tracks 'Transfer' and 'Approval' events specifically, providing updates every second to capture the latest on-chain activities.
