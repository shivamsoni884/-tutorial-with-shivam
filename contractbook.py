# contract book
import json
import os

# File to store contracts data
contracts_file = 'contracts.json'

# Function to load existing contracts from the file
def load_contracts():
    if os.path.exists(contracts_file):
        with open(contracts_file, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save contracts to the file
def save_contracts(contracts):
    with open(contracts_file, 'w') as file:
        json.dump(contracts, file, indent=4)

# Function to display contract details
def display_contract(contract):
    print(f"Contract ID: {contract['id']}")
    print(f"Party 1: {contract['party_1']}")
    print(f"Party 2: {contract['party_2']}")
    print(f"Contract Date: {contract['contract_date']}")
    print(f"Contract Terms: {contract['terms']}")
    print(f"Status: {contract['status']}")
    print("-" * 40)

# Function to add a new contract
def add_contract(contracts):
    contract_id = len(contracts) + 1
    party_1 = input("Enter the first party name: ")
    party_2 = input("Enter the second party name: ")
    contract_date = input("Enter the contract date (e.g., YYYY-MM-DD): ")
    terms = input("Enter the contract terms: ")
    status = input("Enter the status of the contract (Active/Inactive): ")

    contract = {
        'id': contract_id,
        'party_1': party_1,
        'party_2': party_2,
        'contract_date': contract_date,
        'terms': terms,
        'status': status
    }

    contracts.append(contract)
    save_contracts(contracts)
    print("Contract added successfully!")

# Function to view all contracts
def view_contracts(contracts):
    if contracts:
        for contract in contracts:
            display_contract(contract)
    else:
        print("No contracts found.")

# Function to search for a contract by ID
def search_contract_by_id(contracts, contract_id):
    for contract in contracts:
        if contract['id'] == contract_id:
            display_contract(contract)
            return
    print("Contract not found.")

# Function to display the menu and handle user input
def display_menu():
    print("Contract Book Menu:")
    print("1. Add a new contract")
    print("2. View all contracts")
    print("3. Search contract by ID")
    print("4. Exit")

# Main program loop
def contract_book():
    contracts = load_contracts()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contract(contracts)
        elif choice == '2':
            view_contracts(contracts)
        elif choice == '3':
            contract_id = int(input("Enter the contract ID to search: "))
            search_contract_by_id(contracts, contract_id)
        elif choice == '4':
            print("Exiting Contract Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contract_book()
