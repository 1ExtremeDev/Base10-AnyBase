def base(num, base=2, binary=""):
    while num > 0 and base <= 62: binary += "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[num % base]; num //= base
    return binary[::-1] if not(len(binary) == 0) else "0"
