ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def to_base64(raw_input: bytes) -> bytes:
    padding_len = 3 - len(raw_input) % 3 if len(raw_input) % 3 != 0 else 0
    bytes_to_encode = raw_input + b'0' * padding_len
    encoded = bytes()
    for i in range(0, len(bytes_to_encode), 3):
        num_container = sum(
            bytes_to_encode[i + 2 - byte_pos] << (8 * byte_pos)
            for byte_pos in (2, 1, 0)
        )
        alphabet_keys = [
            (num_container >> pos) & 63
            for pos in (18, 12, 6, 0)
        ]
        encoded += bytes(ALPHABET[k] for k in alphabet_keys)
    return encoded[0:len(encoded) - padding_len] + b'=' * padding_len


def base64_decode(raw_input: bytes) -> bytes:
    allowed_chars = ALPHABET + b'='
    valid_input = bytes(char for char in raw_input if char in allowed_chars)
    padding_len = valid_input[-2:].count(b'=')
    without_padding = (
        valid_input[0:len(valid_input)-padding_len] + b'0' * padding_len
    )
    decoded = bytes()
    for i in range(0, len(without_padding), 4):
        num_container = sum(
            ALPHABET.index(without_padding[i + 3 - byte_pos]) << (6 * byte_pos)
            for byte_pos in (3, 2, 1, 0)
        )
        decoded += bytes(
            (num_container >> byte_pos) & 0xFF
            for byte_pos in (16, 8, 0)
        )
    return decoded[0:len(decoded) - padding_len]
