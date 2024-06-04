
from .E5080B import VNA_E5080B
from .dummy import VNA_DUMMY
from .VNA import VNA

def get_VNA( address, model=None )->VNA:
    match model:
        case "E5080B":
            return VNA_E5080B(address)
        case _:
            return VNA_DUMMY(address)