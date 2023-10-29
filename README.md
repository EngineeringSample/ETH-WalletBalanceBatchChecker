# ETH-WalletBalanceBatchChecker
ETH WalletBalanceBatchChecker

## Ethereum Wallet Balance Batch Checker (Under Development)

Welcome to the Ethereum Wallet Balance Batch Checker! This Python script allows you to check the balances of multiple Ethereum wallet addresses in one go. Please keep in mind that this script is currently under development, and there may be improvements and updates in the future.

### Prerequisites

Before you get started, make sure you have the following:

- Python 3.x installed on your computer.
- The Web3.py library installed. You can install it using `pip`:
  ```
  pip install web3
  ```

### How to Use

1. **Run the Script**:

   Open a terminal or command prompt and run the script. You can use the following command to execute it:

   ```
   python ETH-WalletBalanceBatchChecker.py
   ```

2. **Enter Ethereum Node's RPC URL**:

   The script will ask you to provide the RPC URL of an Ethereum node. You can obtain an RPC URL by signing up for services like Infura or use the RPC URL of your Ethereum node if you have one.

   ```
   Enter the Ethereum node's RPC URL:
   ```

3. **Enter Wallet Addresses**:

   You will be prompted to enter the Ethereum wallet addresses you want to check, one address per line. Type 'q' when you've finished entering all the addresses you want to check.

   ```
   Enter an Ethereum wallet address to check (or 'q' to finish):
   ```

4. **Check Balances**:

   The script will use the provided RPC URL to query the Ethereum blockchain for the balances of the entered wallet addresses. It will then display the balance of each address in Ether (ETH).

   ```
   The balance of wallet address 0xAddress1 is 1.23456789 ETH
   The balance of wallet address 0xAddress2 is 2.34567891 ETH
   The balance of wallet address 0xAddress3 is 3.45678912 ETH
   ```

### Important Note

Please note that this script is still under development, which means it may have limitations and potential bugs. If you encounter any issues or have suggestions for improvement, we welcome your feedback to make this tool more robust and user-friendly.

---

This tutorial explains how to use the script while considering that it's still in development and open to future enhancements.
