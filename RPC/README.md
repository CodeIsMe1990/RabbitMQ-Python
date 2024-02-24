Our RPC service is now ready. We can start the server:
    python rpc_server.py
    # => [x] Awaiting RPC requests
To request a fibonacci number run the client:
    python rpc_client.py
    # => [x] Requesting fib(30)
    
The presented design is not the only possible implementation of an RPC service, but it has some important advantages:

If the RPC server is too slow, you can scale up by just running another one. Try running a second rpc_server.py in a new console.
On the client side, the RPC requires sending and receiving only one message. No synchronous calls like queue_declare are required. As a result the RPC client needs only one network round trip for a single RPC request.
Our code is still pretty simplistic and doesn't try to solve more complex (but important) problems, like:

How should the client react if there are no servers running?
Should a client have some kind of timeout for the RPC?
If the server malfunctions and raises an exception, should it be forwarded to the client?
Protecting against invalid incoming messages (e.g. checking bounds) before processing.