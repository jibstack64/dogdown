# dogdown

![GitHub](https://img.shields.io/github/license/jibstack64/dogdown) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/jibstack64/dogdown)

*A Python script for sending a large quantity of a given payload to a HTTP(S) server.*

Put your payload information in a JSON file (e.g. `payload.json`). Make sure it is in the same directory as where the script is being ran. When ran, the script will give you a selection of the JSON files (that it finds in the same directory) to choose from as your payload.

Proxy providers can be found in `proxies.json`. Extra configuration can be modified **at the top of `dogdown.py`**.

---

![screenshot-2023-01-22-14:32:10](https://user-images.githubusercontent.com/107510599/213921558-9ea1f459-d5b8-4f57-a391-03ff9b53b33e.png)
> ### You can change the number of threads in `dogdown.py`. I chose two for this example.

![screenshot-2023-01-22-14:33:18](https://user-images.githubusercontent.com/107510599/213921565-8f4f9e86-f4e0-4893-89c9-d66e6d1ee78d.png)
