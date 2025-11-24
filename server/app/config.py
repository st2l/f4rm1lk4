def _default_teams():
    return {f"Team #{i}": f"10.60.{i}.3" for i in range(0, 10)}


# === Protocol: RuCTF TCP ===
RUCTF_TCP_CONFIG = {
    "SYSTEM_PROTOCOL": "ructf_tcp",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "10.10.10.10",
    "SYSTEM_PORT": 31337,
}


# === Protocol: CTF Cup TCP ===
CTFCUP_TCP_CONFIG = {
    "SYSTEM_PROTOCOL": "ctfcup_tcp",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "10.10.10.10",
    "SYSTEM_PORT": 31337,
}


# === Protocol: Faust TCP ===
FAUST_CONFIG = {
    "SYSTEM_PROTOCOL": "faust",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "10.10.10.10",
    "SYSTEM_PORT": 31337,
}


# === Protocol: RuCTF HTTP ===
RUCTF_HTTP_CONFIG = {
    "SYSTEM_PROTOCOL": "ructf_http",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_URL": "https://monitor.ructfe.org/flags",
    "SYSTEM_TOKEN": "275_17fc104dd58d429ec11b4a5e82041cd2",
}


# === Protocol: VolgaCTF v2 ===
VOLGACTF_CONFIG = {
    "SYSTEM_PROTOCOL": "volgactf",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "final.volgactf.ru",
    "INFO_FLAG_LIMIT": 150,
    "SYSTEM_VALIDATOR": "volgactf",
    "SYSTEM_SERVER_KEY": None,  # Set cached key if validators.volgactf is unavailable.
}


# === Protocol: VolgaCTF legacy ===
VOLGACTF_OLD_CONFIG = {
    "SYSTEM_PROTOCOL": "volgactf_old",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "final.volgactf.ru",
}


# === Protocol: CTF Moscow ===
CTF_MOSCOW_CONFIG = {
    "SYSTEM_PROTOCOL": "ctf_moscow",
    "DEBUG": True,
    "SERVER_PASSWORD": "1234",
    "TEAMS": _default_teams(),
    "FLAG_FORMAT": r"[A-Z0-9]{31}=",
    "TIMEZONE": "Europe/Moscow",
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 5 * 60,
    "SYSTEM_HOST": "final.ctf.moscow",
}


# --- Pick the active block below ---
PROTOCOL_NAME = "ructf_tcp"
PROTOCOLS = {
    "ructf_tcp": RUCTF_TCP_CONFIG,
    "ctfcup_tcp": CTFCUP_TCP_CONFIG,
    "faust": FAUST_CONFIG,
    "ructf_http": RUCTF_HTTP_CONFIG,
    "volgactf": VOLGACTF_CONFIG,
    "volgactf_old": VOLGACTF_OLD_CONFIG,
    "ctf_moscow": CTF_MOSCOW_CONFIG,
}

if PROTOCOL_NAME not in PROTOCOLS:
    raise RuntimeError(f"Unknown protocol selected: {PROTOCOL_NAME}")

CONFIG = PROTOCOLS[PROTOCOL_NAME]
