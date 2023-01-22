# dogdown

*A Python script for sending a large quantity of a given payload to a HTTP(S) server.*

Put your payload information in a JSON file (e.g. `payload.json`). Make sure it is in the same directory as where the script is being ran. When ran, the script will give you a selection of the JSON files (that it finds in the same directory) to choose from as your payload.

Proxy providers can be found in `proxies.json`. Extra configuration can be modified **at the top of `dogdown.py`**.
