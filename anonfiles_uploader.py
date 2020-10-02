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
import time
import argparse
import requests, json
import methods
import datetime
if os.path.isdir(l1llJuanjoCG (u"ࠨࡵࡱ࡮ࡲࡥࡩࠨ࢕")):
	time.sleep(0.1)
else:
	os.mkdir(l1llJuanjoCG (u"ࠢࡶࡲ࡯ࡳࡦࡪࠢ࢖"))
	methods.clean()
	print(l1llJuanjoCG (u"ࠣࡨࡲࡰࡩ࡫ࡲࠡࠩࡸࡴࡱࡵࡡࡥࠩࠣࡧࡷ࡫ࡡࡵࡧࡧ࠰ࠥࡳ࡯ࡷࡧࠣࡽࡴࡻࡲࠡࡨ࡬ࡰࡪࡹࠠࡵࡱࠣࡦࡪࠦࡵࡱ࡮ࡲࡥࡩ࡫ࡤࠡࡶ࡫ࡩࡷ࡫ࠠࡢࡰࡧࠤࡷ࡫ࡳࡵࡣࡵࡸࠥࡺࡨࡦࠢࡶࡧࡷ࡯ࡰࡵࠤࢗ"))
	print(l1llJuanjoCG (u"ࠤࠥ࢘"))
	sys.exit()
try:
	# l1ll111l1JuanjoCG paths
	path = os.getcwd()
	l1ll1l11lJuanjoCG = path + l1llJuanjoCG (u"ࠥ࠳ࡺࡶ࡬ࡰࡣࡧ࢙ࠦ")
	# l1l1lll1lJuanjoCG l1ll11ll1JuanjoCG
	parser = argparse.ArgumentParser(description=l1llJuanjoCG (u"࡚ࠦࡶ࡬ࡰࡣࡧࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡡ࡯ࡱࡱࡪ࡮ࡲࡥࡴ࠰ࡦࡳࡲࠨ࢚"))
	parser.add_argument(l1llJuanjoCG (u"ࠬ࠳ࡦࠨ࢛"), l1llJuanjoCG (u"࠭࠭࠮ࡨ࡬ࡰࡪࡴࡡ࡮ࡧࠪ࢜"), metavar=l1llJuanjoCG (u"ࠧࠨ࢝"), type=str, required=True, help=l1llJuanjoCG (u"ࠣ࡫ࡱࡴࡺࡺࠠࡧ࡫࡯ࡩࡳࡧ࡭ࡦࠢࠫ࡭ࡳࠦࡵࡱ࡮ࡲࡥࡩ࠲ࠠࡪࡰࠣࡷࡨࡸࡩࡱࡶࠪࡷࠥ࡬࡯࡭ࡦࡨࡶ࠮ࠨ࢞"))
	parser.add_argument(l1llJuanjoCG (u"ࠩ࠰ࡴࠬ࢟"), l1llJuanjoCG (u"ࠪ࠱࠲ࡶࡲࡰࡺࡼࠫࢠ"), metavar=l1llJuanjoCG (u"ࠫࠬࢡ"), type=str, required=False, help=l1llJuanjoCG (u"ࠬࡪ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡪࡷࡸࡵ࠵ࡨࡵࡶࡳࡷࠥࡶࡲࡰࡺࡼࠤ࠭ࡶࡲࡰࡺࡼ࠾ࡵࡵࡲࡵࠫࠪࢢ"))
	parser.add_argument(l1llJuanjoCG (u"࠭࠭ࡵࠩࢣ"), l1llJuanjoCG (u"ࠧ࠮࠯ࡷࡳࡷ࠭ࢤ"), metavar=l1llJuanjoCG (u"ࠨࠩࢥ"), type=bool, required=False, help=l1llJuanjoCG (u"ࠩࡶࡩࡹࠦࡴࡰࠢࡗࡶࡺ࡫ࠠࡵࡱࠣࡹࡸ࡫ࠠࡵࡱࡵࠫࢦ"))
	parser.add_argument(l1llJuanjoCG (u"ࠪ࠱ࡴ࠭ࢧ"), l1llJuanjoCG (u"ࠫ࠲࠳࡯ࡶࡶࡳࡹࡹ࠭ࢨ"), metavar=l1llJuanjoCG (u"ࠬ࠭ࢩ"), type=str, required=False, help=l1llJuanjoCG (u"࠭ࡰࡢࡶ࡫ࠤࡹࡵࠠࡴࡣࡹࡩࠥࡧ࡬࡭ࠢ࡬ࡲ࡫ࡵࠠࡳࡧ࡯ࡥࡹ࡫ࡤࠡࡶࡲࠤ࡫࡯࡬ࡦࠢࡸࡴࡱࡵࡡࡥࡧࡧࠤࡦࡹࠠࡢࠢࡷࡼࡹ࠭ࢪ"))
	arg = parser.parse_args()
	# l1ll1l1l1JuanjoCG path
	os.chdir(l1ll1l11lJuanjoCG)
	# read file to send
	l1l1lllllJuanjoCG = open(arg.filename, l1llJuanjoCG (u"ࠢࡳࡤࠥࢫ"))
	#l1l1llll1JuanjoCG requests
# --------------------------------------------------------------------------------------------------------------
	if arg.tor and arg.proxy != None:   #l1ll1l111JuanjoCG l1ll111llJuanjoCG
		methods.clean()
		print(l1llJuanjoCG (u"࡛ࠣࡲࡹࠥࡩࡡ࡯ࠩࡷࠤࡺࡹࡥࠡࡶࡲࡶࠥࡶࡲࡰࡺࡼࠤࡦࡴࡤࠡࡲࡵࡳࡽࡿࠠࡢࡶࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥࡺࡩ࡮ࡧࠥࢬ"))
		sys.exit()
# --------------------------------------------------------------------------------------------------------------
	if arg.tor and arg.proxy == None:
		proxy = {
				l1llJuanjoCG (u"ࠩ࡫ࡸࡹࡶࠧࢭ") : l1llJuanjoCG (u"ࠥࡷࡴࡩ࡫ࡴ࠷࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠻࠳࠹࠵ࠨࢮ"),
				l1llJuanjoCG (u"ࠫ࡭ࡺࡴࡱࡵࠪࢯ") : l1llJuanjoCG (u"ࠧࡹ࡯ࡤ࡭ࡶ࠹࠿࠵࠯࠲࠴࠺࠲࠵࠴࠰࠯࠳࠽࠽࠵࠻࠰ࠣࢰ")
			}
		methods.clean()
		print(l1llJuanjoCG (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡦࡲࡲࡪࠦࡷࡪࡶ࡫ࠤࡹࡵࡲࠣࢱ"))
		time.sleep(2)
		request = requests.post(l1llJuanjoCG (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡧ࡮ࡰࡰࡩ࡭ࡱ࡫ࡳ࠯ࡥࡲࡱ࠴ࡻࡰ࡭ࡱࡤࡨࠬࢲ"), proxies=proxy, files={l1llJuanjoCG (u"ࠣࡨ࡬ࡰࡪࠨࢳ"):l1l1lllllJuanjoCG})
# --------------------------------------------------------------------------------------------------------------
	if arg.proxy != None: #proxy request
		proxy = {
				l1llJuanjoCG (u"ࠩ࡫ࡸࡹࡶࠧࢴ") : l1llJuanjoCG (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦࢵ") + arg.proxy,
				l1llJuanjoCG (u"ࠫ࡭ࡺࡴࡱࡵࠪࢶ") : l1llJuanjoCG (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢࢷ") + arg.proxy
			}
		print(l1llJuanjoCG (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡦࡲࡲࡪࠦࡷࡪࡶ࡫ࠤࡵࡸ࡯ࡹࡻࠥࢸ"))
		time.sleep(2)
		request = requests.post(l1llJuanjoCG (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡧ࡮ࡰࡰࡩ࡭ࡱ࡫ࡳ࠯ࡥࡲࡱ࠴ࡻࡰ࡭ࡱࡤࡨࠬࢹ"), proxies=proxy, files={l1llJuanjoCG (u"ࠣࡨ࡬ࡰࡪࠨࢺ"):l1l1lllllJuanjoCG})
# --------------------------------------------------------------------------------------------------------------
	if arg.tor != True and arg.proxy == None: #l1ll11l1lJuanjoCG request
		request = requests.post(l1llJuanjoCG (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡢࡰࡲࡲ࡫࡯࡬ࡦࡵ࠱ࡧࡴࡳ࠯ࡶࡲ࡯ࡳࡦࡪࠧࢻ"), files={l1llJuanjoCG (u"ࠥࡪ࡮ࡲࡥࠣࢼ"):l1l1lllllJuanjoCG})
# --------------------------------------------------------------------------------------------------------------
	#l1ll111l1JuanjoCG l1ll1l1llJuanjoCG
	str_json_recived = json.dumps(request.json())
	l1ll11111JuanjoCG = json.loads(str_json_recived)
	# l1l1lll11JuanjoCG verify l1ll1ll11JuanjoCG http codes
	methods.code_check(str_json_recived, request)
	# save date and hour
	time = datetime.datetime.now()
	# l1ll11lllJuanjoCG all file info
	print(l1llJuanjoCG (u"ࠦࠥࠨࢽ"))
	data = l1ll11111JuanjoCG[l1llJuanjoCG (u"ࠧࡪࡡࡵࡣࠥࢾ")]
	file = data [l1llJuanjoCG (u"ࠨࡦࡪ࡮ࡨࠦࢿ")]
	l1ll11l11JuanjoCG = file[l1llJuanjoCG (u"ࠢ࡮ࡧࡷࡥࡩࡧࡴࡢࠤࣀ")]
	size = l1ll11l11JuanjoCG[l1llJuanjoCG (u"ࠣࡵ࡬ࡾࡪࠨࣁ")]
	url = file[l1llJuanjoCG (u"ࠤࡸࡶࡱࠨࣂ")]
	methods.clean()
	print(l1llJuanjoCG (u"ࠥࠤࠧࣃ"))
	print(l1llJuanjoCG (u"ࠦࡠ࠰࡝ࠡࡗࡕࡐ࠿ࠦࠢࣄ"))
	print(l1llJuanjoCG (u"ࠧࠦࠢࣅ"))
	print(url[l1llJuanjoCG (u"ࠨࡦࡶ࡮࡯ࠦࣆ")])
	print(l1llJuanjoCG (u"ࠢࠡࠤࣇ"))
	print(l1llJuanjoCG (u"ࠣ࡝࠭ࡡࠥࡌࡩ࡭ࡧࠣ࡭ࡳ࡬࡯࠻ࠤࣈ"))
	print(l1llJuanjoCG (u"ࠤࠣࠦࣉ"))
	print(l1llJuanjoCG (u"ࠥࡒࡦࡳࡥ࠻ࠢࠥ࣊") + l1ll11l11JuanjoCG[l1llJuanjoCG (u"ࠦࡳࡧ࡭ࡦࠤ࣋")])
	print(l1llJuanjoCG (u"࡙ࠧࡩࡻࡧ࠽ࠤࠧ࣌") + size[l1llJuanjoCG (u"ࠨࡲࡦࡣࡧࡥࡧࡲࡥࠣ࣍")])
	print(l1llJuanjoCG (u"ࠢࡂࡰࡲࡲ࡫࡯࡬ࡦࡵࠣ࡭ࡩࡀࠠࠣ࣎") + l1ll11l11JuanjoCG[l1llJuanjoCG (u"ࠣ࡫ࡧ࣏ࠦ")])
	print(l1llJuanjoCG (u"ࠤ࣐ࠣࠦ"))
	time = datetime.datetime.now()
	if arg.output != None:
		l1ll1111lJuanjoCG = open(arg.output + arg.filename + l1llJuanjoCG (u"ࠥࡣࡴࡻࡴࡱࡷࡷࡣ࣑ࠧ") + l1llJuanjoCG (u"ࠦ࠳ࡺࡸࡵࠤ࣒"), l1llJuanjoCG (u"ࠧࡧ࣓ࠢ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠨ࡜࡯ࠤࣔ") + l1llJuanjoCG (u"ࠢ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠨࣕ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠣ࡞ࡱࠦࣖ") + str(time))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠤ࡟ࡲࠧࣗ") + l1llJuanjoCG (u"ࠥࠤࠧࣘ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠦࡡࡴࠢࣙ") + l1llJuanjoCG (u"ࠧࡡࠪ࡞ࠢࡘࡖࡑࡀࠠࠣࣚ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠨ࡜࡯ࠤࣛ") +l1llJuanjoCG (u"ࠢࠡࠤࣜ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠣ࡞ࡱࠦࣝ") + url[l1llJuanjoCG (u"ࠤࡩࡹࡱࡲࠢࣞ")])
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠥࡠࡳࠨࣟ") + l1llJuanjoCG (u"ࠦࠥࠨ࣠"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠧࡢ࡮ࠣ࣡") + l1llJuanjoCG (u"ࠨ࡛ࠫ࡟ࠣࡊ࡮ࡲࡥࠡ࡫ࡱࡪࡴࡀࠢ࣢"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠢ࡝ࡰࣣࠥ") + l1llJuanjoCG (u"ࠣࠢࠥࣤ"))
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠤ࡟ࡲࠧࣥ") +l1llJuanjoCG (u"ࠥࡒࡦࡳࡥ࠻ࣦࠢࠥ") + l1ll11l11JuanjoCG[l1llJuanjoCG (u"ࠦࡳࡧ࡭ࡦࠤࣧ")])
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠧࡢ࡮ࠣࣨ") +l1llJuanjoCG (u"ࠨࡓࡪࡼࡨ࠾ࠥࠨࣩ") + size[l1llJuanjoCG (u"ࠢࡳࡧࡤࡨࡦࡨ࡬ࡦࠤ࣪")])
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠣ࡞ࡱࠦ࣫") +l1llJuanjoCG (u"ࠤࡄࡲࡴࡴࡦࡪ࡮ࡨࡷࠥ࡯ࡤ࠻ࠢࠥ࣬") + l1ll11l11JuanjoCG[l1llJuanjoCG (u"ࠥ࡭ࡩࠨ࣭")])
		l1ll1111lJuanjoCG.write(l1llJuanjoCG (u"ࠦࡡࡴ࣮ࠢ") + l1llJuanjoCG (u"ࠧ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࣯ࠦ"))
		l1ll1111lJuanjoCG.close()
		print(l1llJuanjoCG (u"ࠨࡆࡪ࡮ࡨࠤࡸࡧࡶࡦࡦࠣࡻ࡮ࡺࡨࠡࡵࡸࡧࡨ࡫ࡳࠡ࡫ࡱࡸࡴࡀࣰࠠࠣ") + arg.output + l1llJuanjoCG (u"ࠢࠡࡣࡶࠤࣱࠧ") + arg.filename + l1llJuanjoCG (u"ࠣࡡࡲࡹࡹࡶࡵࡵࡡࣲࠥ") + l1llJuanjoCG (u"ࠤ࠱ࡸࡽࡺࠢࣳ"))
		print(l1llJuanjoCG (u"ࠥࠤࠧࣴ"))
except FileNotFoundError:
	methods.clean()
	print(l1llJuanjoCG (u"ࠦࡘࡵࡲࡳࡻ࠯ࠤ࡫࡯࡬ࡦࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠳ࠦࡍࡢ࡭ࡨࠤࡸࡻࡲࡦࠢ࡬ࡸࠬࡹࠠࡪࡰࠣࡹࡵࡲ࡯ࡢࡦࠣࡪࡴࡲࡤࡦࡴࠥࣵ"))
	print(l1llJuanjoCG (u"ࣶࠧࠦࠢ"))
except requests.exceptions.ConnectionError:
	methods.clean()
	print(l1llJuanjoCG (u"ࠨࡃࡢࡰࠪࡸࠥࡩ࡯࡯ࡰࡨࡧࡹࠦࡴࡰࠢࡶࡩࡷࡼࡥࡳࠢࠫࡧ࡭࡫ࡣ࡬ࠢࡼࡳࡺࡸࠠࡪࡰࡷࡩࡷࡴࡥࡵࠫࠥࣷ"))
	print(l1llJuanjoCG (u"ࠢࠡࠤࣸ"))
except KeyboardInterrupt:
	methods.clean()
	print(l1llJuanjoCG (u"ࠣࡊࡤࡺࡪࠦࡡࠡࡰ࡬ࡧࡪࠦࡤࡢࡻࠣ࠾࠮ࠨࣹ"))
except json.decoder.JSONDecodeError:
	print(l1llJuanjoCG (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡰࡳࡰࡰࠣࠬࡹࡸࡹࠡࡣࡪࡥ࡮ࡴࣺࠩࠣ"))