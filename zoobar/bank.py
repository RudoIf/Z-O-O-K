from zoodb import *
from debug import *

import time
import auth_client as auth

def register(username):
    if not auth.is_registered(username):
        raise ValueError("No such user to register a new bank")

    db = bank_setup()
    person = db.query(Bank).get(username)
    if (person):
        return None

    bank = Bank()
    bank.username = username
    db.add(bank)
    db.commit()

def transfer(sender, sender_token, recipient, zoobars):
    if not auth.check_token(sender, sender_token):
        raise ValueError("Sender token error2")
    if not auth.is_registered(recipient):
        raise ValueError("Receiver not exisi")

    bankdb = bank_setup()
    senderp = bankdb.query(Bank).get(sender)
    recipientp = bankdb.query(Bank).get(recipient)
    
    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderp.zoobars = sender_balance
    recipientp.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    person = db.query(Bank).get(username)
    if person:
        return person.zoobars

def get_log(username):
    db = transfer_setup()
    log = db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))
    def format_transfer(transfer):
        return {
                'time':transfer.time,
                'sender':transfer.sender,
                'recipient':transfer.recipient,
                'amount':transfer.amount}
    return [format_transfer(transfer) for transfer in log]
