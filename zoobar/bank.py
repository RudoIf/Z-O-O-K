from zoodb import *
from debug import *

import time

def register(username):
    if not auth.is_registered(username):
        raise ValueError("No such user to register a new bank")

    db = bank_setup()
    pserson = db.query(Bank).get(username)
    if (person):
        return None

    bank = Bank()
    bank.username = username
    db.add(bank)
    db.commit()

def transfer(sender, recipient, zoobars, sender_token):
    if not auth.check_token(sender, sender_token):
        raise ValueError("Sender token error")
    if not auth.is_registered(recipientp):
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
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

