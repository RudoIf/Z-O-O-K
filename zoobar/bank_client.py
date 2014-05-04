from debug import *
from zoodb import *
import rpclib

def register( username ):
    with rpclib.client_connect('/banksvc/sock') as rpc_client:
        kwargs = {'username':username}
        return rpc_client.call('register', **kwargs )
            
def transfer( sender, sender_token, recipient, zoobars ):
    with rpclib.client_connect('/banksvc/sock') as rpc_client:
        kwargs = {'sender':sender, 'sender_token':sender_token, 'recipient':recipient, 'zoobars':zoobars}
        return rpc_client.call('transfer', **kwargs )

def balance( username ):
    with rpclib.client_connect('/banksvc/sock') as rpc_client:
        kwargs = {'username':username}
        return rpc_client.call('balance', **kwargs )

def get_log( username ): 
    with rpclib.client_connect('/banksvc/sock') as rpc_client:
        kwargs = {'username':username}
        return rpc_client.call('get_log', **kwargs )
