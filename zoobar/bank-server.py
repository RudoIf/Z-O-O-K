#!/usr/bin/python
#
# Insert bank server code here.
#
import rpclib
import sys
import os
from debug import *
 class BankRpcServer(rpclib.RpcServer):
     def rpc_register(self, username):
         return bank.register(username)
     def rpc_transfer(self, sender, sender_token, recipient, zoobars):
         return bamk.transfer(sender, sender_token, recipient, zoobars)
     def rpc_balance(self, username):
         return bank.balance(username)
     def rpc_get_log(self, username):
         return bank.get_log(username)

(_, dummy_zoold_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)

