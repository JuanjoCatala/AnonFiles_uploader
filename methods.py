# coding: UTF-8
import sys
l1l11JuanjoCG = sys.version_info [0] == 2
l11JuanjoCG = 2048
l1lJuanjoCG = 7
def l11lJuanjoCG (l1llJuanjoCG):
    global l1JuanjoCG
    l111JuanjoCG = ord (l1llJuanjoCG [-1])
    l1l1JuanjoCG = l1llJuanjoCG [:-1]
    l1l1lJuanjoCG = l111JuanjoCG % len (l1l1JuanjoCG)
    l1ll1JuanjoCG = l1l1JuanjoCG [:l1l1lJuanjoCG] + l1l1JuanjoCG [l1l1lJuanjoCG:]
    if l1l11JuanjoCG:
        l1lllJuanjoCG = unicode () .join ([unichr (ord (char) - l11JuanjoCG - (llJuanjoCG + l111JuanjoCG) % l1lJuanjoCG) for llJuanjoCG, char in enumerate (l1ll1JuanjoCG)])
    else:
        l1lllJuanjoCG = str () .join ([chr (ord (char) - l11JuanjoCG - (llJuanjoCG + l111JuanjoCG) % l1lJuanjoCG) for llJuanjoCG, char in enumerate (l1ll1JuanjoCG)])
    return eval (l1lllJuanjoCG)
import os
import sys
from colorama import Fore, Style
def clean():
	if os.name == l11lJuanjoCG (u"ࠦࡵࡵࡳࡪࡺࠥࠀ"):
		os.system (l11lJuanjoCG (u"ࠧࡩ࡬ࡦࡣࡵࠦࠁ"))
	elif os.name == l11lJuanjoCG (u"ࠨࡣࡦࠤࠂ") or os.name == l11lJuanjoCG (u"ࠢ࡯ࡶࠥࠃ") or os.name == l11lJuanjoCG (u"ࠣࡦࡲࡷࠧࠄ"):
		os.system (l11lJuanjoCG (u"ࠤࡦࡰࡸࠨࠅ"))
def code_check(str_json_recived, request):
	if l11lJuanjoCG (u"ࠥ࠵࠵ࠨࠆ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠦࡊࡸ࡯ࡳ࠮ࠣࡲࡴࠦࡦࡪ࡮ࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠨࠇ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠧ࠷࠱ࠣࠈ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠨࡅࡳࡴࡲࡶ࠱ࠦࡦࡪ࡮ࡨࠤࡪࡳࡰࡵࡻࠥࠉ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠢ࠲࠴ࠥࠊ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠣࡇࡵࡶࡴࡸࠬࠡࡨ࡬ࡰࡪࠦࡩ࡯ࡸࡤࡰ࡮ࡪࠢࠋ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠤ࠵࠴ࠧࠌ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠥࡉࡷࡸ࡯ࡳ࠮ࠣࡱࡦࡾࠠࡧ࡫࡯ࡩࡸࠦࡰࡦࡴࠣ࡬ࡴࡻࡲࠡࡴࡨࡥࡨ࡮ࡥࡥࠤࠍ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠦ࠷࠷ࠢࠎ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠧࡋࡲࡳࡱࡵ࠰ࠥࡳࡡࡹࠢࡩ࡭ࡱ࡫ࡳࠡࡲࡨࡶࠥࡪࡡࡺࠢࡵࡩࡦࡩࡨࡦࡦࠥࠏ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠨ࠲࠳ࠤࠐ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠢࡆࡴࡵࡳࡷ࠲ࠠ࡮ࡣࡻࠤࡧࡿࡴࡦࡵࠣࡴࡪࡸࠠࡩࡱࡸࡶࠥࡸࡥࡢࡥ࡫ࡩࡩࠨࠑ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠣ࠴࠶ࠦࠒ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠤࡈࡶࡷࡵࡲ࠭ࠢࡰࡥࡽࠦࡢࡺࡶࡨࡷࠥࡶࡥࡳࠢࡧࡥࡾࠦࡲࡦࡣࡦ࡬ࡪࡪࠢࠓ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠥ࠷࠵ࠨࠔ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠦࡊࡸࡲࡰࡴ࠯ࠤ࡫࡯࡬ࡦࠢࡷࡽࡵ࡫ࠠ࡯ࡱࡷࠤࡦࡲ࡬ࡰࡹࡨࡨࠧࠕ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠧ࠹࠱ࠣࠖ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠨࡅࡳࡴࡲࡶ࠱ࠦࡦࡪ࡮ࡨࠤ࡮ࡹࠠࡵࡱࡲࠤࡧ࡯ࡧࠡࠪࡰࡥࡽࠦ࠵ࡈࡄࠬࠦࠗ") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠢ࠴࠴ࠥ࠘") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠣࡇࡵࡶࡴࡸࠬࠡࡨ࡬ࡰࡪࠦࡢࡢࡰࡱࡩࡩࠨ࠙") + Style.RESET_ALL)
	if l11lJuanjoCG (u"ࠤ࠷࠴ࠧࠚ") in str_json_recived:
		clean()
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠥࡉࡷࡸ࡯ࡳ࠮ࠣࡷࡾࡹࡴࡦ࡯ࠣࡪࡦ࡯࡬ࡶࡴࡨࠦࠛ") + Style.RESET_ALL)
	if request.status_code == 400:
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠦࡈࡲࡩࡦࡰࡷࠤࡪࡸࡲࡰࡴࠣࠬ࠹࠶࠰ࠪࠤࠜ") + Style.RESET_ALL)
	if request.status_code == 403:
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"࡙ࠧࡥࡳࡸࡨࡶࠥࡸࡥࡧࡷࡶࡩࡩࠦࡣࡰࡰࡱࡩࡨࡺࡩࡰࡰࠣࠬ࠹࠶࠳ࠪࠤࠝ") + Style.RESET_ALL)
	if request.status_code == 404:
		print(Fore.RED + Style.BRIGHT + l11lJuanjoCG (u"ࠨࡎࡰࡶࠣࡪࡴࡻ࡮ࡥࠢࠫ࠸࠵࠺ࠩࠣࠞ") + Style.RESET_ALL)