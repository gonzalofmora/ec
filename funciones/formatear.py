import re, unicodedata

def to_snake(name: str) -> str:
    s = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii') # drop accents
    s = s.strip().lower()
    s = re.sub(r'[%\.,]+', '', s)
    s = re.sub(r'\s+', '_', s)
    s = re.sub(r'[^a-z0-9_]+', '', s)
    s = re.sub(r'_+', '_', s).strip('_')
    return s