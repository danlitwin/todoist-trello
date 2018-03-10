from box        import SBox
from _app_keys  import api_keys

keybox = SBox(api_keys, frozen_box=True, box_it_up=True)
