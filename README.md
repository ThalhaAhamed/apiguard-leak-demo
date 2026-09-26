# apiguard leak demo

A throwaway repository for demonstrating [apiguard](https://github.com/ThalhaAhamed/apiguard),
which detects leaked API keys, identifies whose key it is, and checks whether it is being abused.

`app/config.py` deliberately contains **fake** keys for a fictional API ("MeetStream").
They grant access to nothing: they only work against a local test server on the presenter's laptop.
