# Appendixes

## Hardware wallet and 2 factor support

Since the signing is done using the underlying chains mechanisms, their support for hardware wallets is used. Wherever possible, those supports will be used.

Examples:

- NULS has hardware wallet support done on ledger, we use the built-in signing mechanism to sign the messages.
- Ethereum supports Ledger and Trezor, we use their support and signing mechanism.

Another way to go is using the webauthn standard, that will use whatever hardware support is available (built-in crypto chip in mobile device as 2 factor auth, usb u2f key), specific to used website. Wherever possible, webauthn support will be added (generating NULS addresses using secp256k1 support). An exception to the underlying protocol signing mechanism can be done to support json object signing specific to webauthn.