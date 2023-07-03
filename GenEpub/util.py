import re
import zlib
from os import path

def size_str_to_int(s):
    factor_map = {
        '' :   1,
        'k':   1 << 10,
        'm':   1 << 20,
        'g':   1 << 30,
        't':   1 << 40,
        'p':   1 << 50,
        'e':   1 << 60,
        'z':   1 << 60,
        'y':   1 << 70,
        'b':   1 << 80,
        'n':   1 << 90,
        'd':   1 << 100,
        'c':   1 << 110,
        'x':   1 << 120,
    }
    suf = ''.join(factor_map.keys())
    m = re.search(r'^(\d+(?:\.\d+)?)([' + suf + r']?)$', s.lower())
    if not m: return -1
    base = float(m.group(1))
    
    factor = factor_map[m.group(2)]
    return int(base * factor)
    
def comp_size(text):
    return len(zlib.compress(text.encode('utf8')))
    
d = lambda name: path.join(path.dirname(__file__), name) 

def fname_escape(name):
    return re.sub(r'\\|\/|:|\*|\?|"|<|>|\|', '-', name)

is_img = lambda s: re.search(r'\.(jpg|jpeg|gif|png|bmp|webp|tiff)$', s)
