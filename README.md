# SourceRestorer

SourceRestorer is a tool designed to recover lost code from `.pye` files
encrypted using [SOURCEdefender](https://www.sourcedefender.co.uk). It provides
a means to decrypt and analyze otherwise unreadable Python source code, which
can be particularly useful in several scenarios such as:

- **Malware analysis:** Analyzing potentially harmful code without having access
  to its original sources
- **Forensic investigation of unknown code:** Gaining insights into third-party
  scripts with no available documentation
- **Code recovery:** Restoring your own code when you've accidentally lost the
  original source files

It has been tested with version 11.0 of the library.


## How does it work?

SOURCEdefender uses `TgCrypto` and `msgpack` under the hood. We simply need to
wrap the `tgcrypto.ctr256_decrypt` function [so that it prints the decrypted
code](https://stackoverflow.com/a/78422120/1101509).

Finally, we make it return an empty value instead. This last step is performed
to ensure no harmful code is ever executed.


## Usage

Firstly, you should install the original SOURCEdefender library:

```bash
pip install -r requirements.txt
```

To use the program **place the encrypted file in the same directory as the
script,** then simply call it by passing the file name as the only parameter:

```bash
python sourcerestorer.py input.pye
```

The code will be printed out on screen.


## License

This software is released in the public domain under _The Unlicense_. It comes
without warrant of any kind and no support will be provided.
