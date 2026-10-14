# Issues Identified in `digital_wallet.py`

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
|---|---|---|---|---|
| Hardcoded Gateway Secret | Security – High | 6 | Gateway secret is directly stored in the source code, exposing sensitive information. | Store the secret in an environment variable. |
| Hardcoded Wallet PIN | Security – High | 7 | Wallet PIN is hardcoded in the source code and can be exposed to anyone accessing the file. | Use secure credential storage and avoid hardcoding the PIN. |
| Weak Hashing Algorithm | Security – High | 13–14 | SHA-1 is used to hash the wallet PIN, which is not suitable for secure PIN storage. | Use a password-hashing algorithm such as Argon2 or PBKDF2 with a salt. |
| Insecure Temporary File Creation | Security – High | 60 | `tempfile.mktemp()` can introduce a race condition when creating temporary files. | Use a secure API such as `tempfile.NamedTemporaryFile()`. |
| Mutable Default Argument | Code Quality – Medium | 17 | The `addMoney()` function uses an empty list as a default argument, so the same list is reused across calls. | Set the default to `None` and initialize a new list inside the function. |
| Unused Function Parameter | Code Quality – Low | 50 | The `merchantType` parameter in `cashbackFor()` is not used. | Use the parameter in cashback calculations or remove it. |
| Inconsistent Function Naming | Code Style – Low | 13, 17, 24, 30, 38, 50, 54, 58 | Function names use camelCase instead of Python's conventional snake_case style. | Rename functions, for example, `hashPin()` to `hash_pin()`. |
| Inconsistent Spacing and Formatting | Code Style – Low | 78–79 | Missing spaces around assignment and function arguments reduce readability and violate common Python style conventions. | Apply consistent spacing and follow PEP 8 formatting guidelines. |