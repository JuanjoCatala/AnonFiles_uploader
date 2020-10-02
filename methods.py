# coding: UTF-8
import sys
l1l11JuanjoCG = sys.version_info [0] == 2
l111JuanjoCG = 2048
l11lJuanjoCG = 7
def l1llJuanjoCG (llJuanjoCG):
    global l11JuanjoCG
    l1JuanjoCG = ord (llJuanjoCG [-1])
    l1l1lJuanjoCG = llJuanjoCG [:-1]
    l1l1JuanjoCG = l1JuanjoCG % len (l1l1lJuanjoCG)
    l1ll1JuanjoCG = l1l1lJuanjoCG [:l1l1JuanjoCG] + l1l1lJuanjoCG [l1l1JuanjoCG:]
    if l1l11JuanjoCG:
        l1lJuanjoCG = unicode () .join ([unichr (ord (char) - l111JuanjoCG - (l1lllJuanjoCG + l1JuanjoCG) % l11lJuanjoCG) for l1lllJuanjoCG, char in enumerate (l1ll1JuanjoCG)])
    else:
        l1lJuanjoCG = str () .join ([chr (ord (char) - l111JuanjoCG - (l1lllJuanjoCG + l1JuanjoCG) % l11lJuanjoCG) for l1lllJuanjoCG, char in enumerate (l1ll1JuanjoCG)])
    return eval (l1lJuanjoCG)
import os
import sys
def clean():
	if os.name == l1llJuanjoCG (u"ࠦࡵࡵࡳࡪࡺࠥࠀ"):
		os.system (l1llJuanjoCG (u"ࠧࡩ࡬ࡦࡣࡵࠦࠁ"))
	elif os.name == l1llJuanjoCG (u"ࠨࡣࡦࠤࠂ") or os.name == l1llJuanjoCG (u"ࠢ࡯ࡶࠥࠃ") or os.name == l1llJuanjoCG (u"ࠣࡦࡲࡷࠧࠄ"):
		os.system (l1llJuanjoCG (u"ࠤࡦࡰࡸࠨࠅ"))
def code_check(str_json_recived, request):
	if l1llJuanjoCG (u"ࠥ࠵࠵ࠨࠆ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠦࡊࡸ࡯ࡳ࠮ࠣࡲࡴࠦࡦࡪ࡮ࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠨࠇ"))
	if l1llJuanjoCG (u"ࠧ࠷࠱ࠣࠈ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠨࡅࡳࡴࡲࡶ࠱ࠦࡦࡪ࡮ࡨࠤࡪࡳࡰࡵࡻࠥࠉ"))
	if l1llJuanjoCG (u"ࠢ࠲࠴ࠥࠊ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠣࡇࡵࡶࡴࡸࠬࠡࡨ࡬ࡰࡪࠦࡩ࡯ࡸࡤࡰ࡮ࡪࠢࠋ"))
	if l1llJuanjoCG (u"ࠤ࠵࠴ࠧࠌ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠥࡉࡷࡸ࡯ࡳ࠮ࠣࡱࡦࡾࠠࡧ࡫࡯ࡩࡸࠦࡰࡦࡴࠣ࡬ࡴࡻࡲࠡࡴࡨࡥࡨ࡮ࡥࡥࠤࠍ"))
	if l1llJuanjoCG (u"ࠦ࠷࠷ࠢࠎ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠧࡋࡲࡳࡱࡵ࠰ࠥࡳࡡࡹࠢࡩ࡭ࡱ࡫ࡳࠡࡲࡨࡶࠥࡪࡡࡺࠢࡵࡩࡦࡩࡨࡦࡦࠥࠏ"))
	if l1llJuanjoCG (u"ࠨ࠲࠳ࠤࠐ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠢࡆࡴࡵࡳࡷ࠲ࠠ࡮ࡣࡻࠤࡧࡿࡴࡦࡵࠣࡴࡪࡸࠠࡩࡱࡸࡶࠥࡸࡥࡢࡥ࡫ࡩࡩࠨࠑ"))
	if l1llJuanjoCG (u"ࠣ࠴࠶ࠦࠒ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠤࡈࡶࡷࡵࡲ࠭ࠢࡰࡥࡽࠦࡢࡺࡶࡨࡷࠥࡶࡥࡳࠢࡧࡥࡾࠦࡲࡦࡣࡦ࡬ࡪࡪࠢࠓ"))
	if l1llJuanjoCG (u"ࠥ࠷࠵ࠨࠔ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠦࡊࡸࡲࡰࡴ࠯ࠤ࡫࡯࡬ࡦࠢࡷࡽࡵ࡫ࠠ࡯ࡱࡷࠤࡦࡲ࡬ࡰࡹࡨࡨࠧࠕ"))
	if l1llJuanjoCG (u"ࠧ࠹࠱ࠣࠖ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠨࡅࡳࡴࡲࡶ࠱ࠦࡦࡪ࡮ࡨࠤ࡮ࡹࠠࡵࡱࡲࠤࡧ࡯ࡧࠡࠪࡰࡥࡽࠦ࠵ࡈࡄࠬࠦࠗ"))
	if l1llJuanjoCG (u"ࠢ࠴࠴ࠥ࠘") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠣࡇࡵࡶࡴࡸࠬࠡࡨ࡬ࡰࡪࠦࡢࡢࡰࡱࡩࡩࠨ࠙"))
	if l1llJuanjoCG (u"ࠤ࠷࠴ࠧࠚ") in str_json_recived:
		clean()
		print(l1llJuanjoCG (u"ࠥࡉࡷࡸ࡯ࡳ࠮ࠣࡷࡾࡹࡴࡦ࡯ࠣࡪࡦ࡯࡬ࡶࡴࡨࠦࠛ"))
	if request.status_code == 400:
		print(l1llJuanjoCG (u"ࠦࡈࡲࡩࡦࡰࡷࠤࡪࡸࡲࡰࡴࠣࠬ࠹࠶࠰ࠪࠤࠜ"))
	if request.status_code == 403:
		print(l1llJuanjoCG (u"࡙ࠧࡥࡳࡸࡨࡶࠥࡸࡥࡧࡷࡶࡩࡩࠦࠨ࠵࠲࠶࠭ࠧࠝ"))
	if request.status_code == 404:
		print(l1llJuanjoCG (u"ࠨࡎࡰࡶࠣࡪࡴࡻ࡮ࡥࠢࠫ࠸࠵࠺ࠩࠣࠞ"))