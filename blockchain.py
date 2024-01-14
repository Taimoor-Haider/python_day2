#javascript (push() , pop())    Python(append(), pop())
from itertools import chain
MINING_REWARD=10
genesis_block={
        "previous_hash":"",
        "index":0,
        "transactions":[]
}
blockchain=[genesis_block]
open_transactions=[]
owner="Taimoor Haider"
participants={"Taimoor Haider"}

def get_last_blockchain_element():
    if(len(blockchain) < 1):
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance=get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """Function to add the transaction value and also to 
    store the last transaction

    Args:
    sender: Sender of the coins.
    recipient: Recipient of the coins.
    amount: Amount of coins sent by the sender
    """
    
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount}
    
    if not verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    else:
        return False

 
def get_balance(participant):
    tx_sender=[[el['amount'] for el in block['transactions'] if el['sender'] == participant ] for block in blockchain]
    open_tx_sender=[trans['amount'] for trans in open_transactions if trans["sender"]==participant]
    tx_sender.append(open_tx_sender)
    send_amount=0
    for el in tx_sender:
         if(len(el) >=1):
           send_amount += el[0]
    tx_receiver=[[el['amount'] for el in block['transactions'] if el['recipient'] == participant ] for block in blockchain]
    received_amount=0
    for el in tx_receiver:
       if(len(el) >=1):
           received_amount += el[0]
    return received_amount - send_amount
def has_block(block):
    return '-'.join([str(block[key]) for key in block])


def mine_block():
    last_block=blockchain[-1]
    hashed_block= has_block(last_block)
    #print(hashed_block)
    reward_transaction={
        'sender':"MINIG",
        'recipient':owner,
        'amount':MINING_REWARD,
    }
    copied_transaction=open_transactions[:]

    copied_transaction.append(reward_transaction)
    block={
        "previous_hash":hashed_block,
        "index":len(blockchain),
        "transactions":copied_transaction
    }
    #print(block)
    blockchain.append(block)
    return True

def get_transactional_value():
    """Taking the user input for the amount"""
    tx_recipient=input("Enter the recipient name:- ")
    tx_amount=float(input("Enter the amount:- "))
    return (tx_recipient,tx_amount)


def get_user_input():
    userInput=input("Your choice: ")
    return userInput


def print_blockchain():
    #Printing the blocks of the blockchain
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
  for (index,data) in enumerate(blockchain):
      if(index == 0):
          continue
      elif(data["previous_hash"] != has_block(blockchain[index-1])):
          return False
  return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input=True
while waiting_for_input:
    print("Please choose!")
    print("1. Enter a new transaction value")
    print("2. Display blockchain blocks")
    print("3. Mine a block")
    print("4. Output participants")
    print("5. Manipulate the blockchain")
    print("6. Verify Transaction")
    print("7. Quit")


    userInput=get_user_input()

    if(userInput == '1'):
        tx_data=get_transactional_value()
        recipient,amount=tx_data
        if add_transaction(recipient,amount=amount):
            print("Transaction Added!")
        else:
            print("Transaction Failed!")
        #print(open_transactions)
    elif(userInput == '2'):
        print_blockchain()
    elif(userInput=='3'):
      if  mine_block() is True:
          open_transactions=[]
    elif (userInput == '4'):
        print(participants)
    elif (userInput == '5'):
        if(len(blockchain) >=1):
            blockchain[0]={
            "previous_hash":"",
            "index":0,
            "transactions":[{'sender':"Taimoor Haider", "recipient":"Usama", 'amount':100.0}]
            }
    elif(userInput == '6'):
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("Some transactions are invalid")
    elif(userInput == '7'):
       waiting_for_input=False    
    else:
        print("Input is invalid please select the right option!!!") 
    if not verify_chain():
        print_blockchain()
        print("Invlaid blockchain!!!")
        break 
    print(get_balance("Taimoor Haider"))
     

print("Done")