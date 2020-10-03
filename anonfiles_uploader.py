# coding: UTF-8
import sys
l1llJuanjoCG = sys.version_info [0] == 2
llJuanjoCG = 2048
l111JuanjoCG = 7
def l11JuanjoCG (l1ll1JuanjoCG):
    global l1JuanjoCG
    l1lllJuanjoCG = ord (l1ll1JuanjoCG [-1])
    l1l1JuanjoCG = l1ll1JuanjoCG [:-1]
    l11lJuanjoCG = l1lllJuanjoCG % len (l1l1JuanjoCG)
    l1l11JuanjoCG = l1l1JuanjoCG [:l11lJuanjoCG] + l1l1JuanjoCG [l11lJuanjoCG:]
    if l1llJuanjoCG:
        l1lJuanjoCG = unicode () .join ([unichr (ord (char) - llJuanjoCG - (l1l1lJuanjoCG + l1lllJuanjoCG) % l111JuanjoCG) for l1l1lJuanjoCG, char in enumerate (l1l11JuanjoCG)])
    else:
        l1lJuanjoCG = str () .join ([chr (ord (char) - llJuanjoCG - (l1l1lJuanjoCG + l1lllJuanjoCG) % l111JuanjoCG) for l1l1lJuanjoCG, char in enumerate (l1l11JuanjoCG)])
    return eval (l1lJuanjoCG)
import os
import sys
import time
import argparse
import requests, json
import methods
import datetime
from colorama import Fore, Style
methods.clean()
# l1ll1l1llJuanjoCG l1l1lllllJuanjoCG
if os.path.isdir(l11JuanjoCG (u"ࠨࡵࡱ࡮ࡲࡥࡩࠨ࢕")):
	time.sleep(0.1)
else:
	os.mkdir(l11JuanjoCG (u"ࠢࡶࡲ࡯ࡳࡦࡪࠢ࢖"))
	methods.clean()
	print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠣࡨࡲࡰࡩ࡫ࡲࠡࠩࡸࡴࡱࡵࡡࡥࠩࠣࡧࡷ࡫ࡡࡵࡧࡧ࠰ࠥࡳ࡯ࡷࡧࠣࡽࡴࡻࡲࠡࡨ࡬ࡰࡪࡹࠠࡵࡱࠣࡦࡪࠦࡵࡱ࡮ࡲࡥࡩ࡫ࡤࠡࡶ࡫ࡩࡷ࡫ࠠࡢࡰࡧࠤࡷ࡫ࡳࡵࡣࡵࡸࠥࡺࡨࡦࠢࡶࡧࡷ࡯ࡰࡵࠤࢗ") + Style.RESET_ALL)
	print(l11JuanjoCG (u"ࠤࠥ࢘"))
	sys.exit()
try:
	# l1ll1l111JuanjoCG paths
	path = os.getcwd()
	l1ll1l1l1JuanjoCG = path + l11JuanjoCG (u"ࠥ࠳ࡺࡶ࡬ࡰࡣࡧ࢙ࠦ")
	# l1ll111llJuanjoCG l1ll1ll11JuanjoCG
	parser = argparse.ArgumentParser(description= l11JuanjoCG (u"࡚ࠦࡶ࡬ࡰࡣࡧࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡡ࡯ࡱࡱࡪ࡮ࡲࡥࡴ࠰ࡦࡳࡲࠨ࢚"))
	parser.add_argument(l11JuanjoCG (u"ࠬ࠳ࡦࠨ࢛"), l11JuanjoCG (u"࠭࠭࠮ࡨ࡬ࡰࡪࡴࡡ࡮ࡧࠪ࢜"), metavar=l11JuanjoCG (u"ࠧࠨ࢝"), type=str, required=True, help=l11JuanjoCG (u"ࠣ࡫ࡱࡴࡺࡺࠠࡧ࡫࡯ࡩࡳࡧ࡭ࡦࠢࠫ࡭ࡳࠦࡵࡱ࡮ࡲࡥࡩ࠲ࠠࡪࡰࠣࡷࡨࡸࡩࡱࡶࠪࡷࠥ࡬࡯࡭ࡦࡨࡶ࠮ࠨ࢞"))
	parser.add_argument(l11JuanjoCG (u"ࠩ࠰ࡴࠬ࢟"), l11JuanjoCG (u"ࠪ࠱࠲ࡶࡲࡰࡺࡼࠫࢠ"), metavar=l11JuanjoCG (u"ࠫࠬࢡ"), type=str, required=False, help=l11JuanjoCG (u"ࠬࡪ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡪࡷࡸࡵ࠵ࡨࡵࡶࡳࡷࠥࡶࡲࡰࡺࡼࠤ࠭ࡶࡲࡰࡺࡼ࠾ࡵࡵࡲࡵࠫࠪࢢ"))
	parser.add_argument(l11JuanjoCG (u"࠭࠭ࡵࠩࢣ"), l11JuanjoCG (u"ࠧ࠮࠯ࡷࡳࡷ࠭ࢤ"), metavar=l11JuanjoCG (u"ࠨࠩࢥ"), type=bool, required=False, help=l11JuanjoCG (u"ࠩࡶࡩࡹࠦࡴࡰࠢࡗࡶࡺ࡫ࠠࡵࡱࠣࡹࡸ࡫ࠠࡵࡱࡵࠫࢦ"))
	parser.add_argument(l11JuanjoCG (u"ࠪ࠱ࡴ࠭ࢧ"), l11JuanjoCG (u"ࠫ࠲࠳࡯ࡶࡶࡳࡹࡹ࠭ࢨ"), metavar=l11JuanjoCG (u"ࠬ࠭ࢩ"), type=str, required=False, help=l11JuanjoCG (u"࠭ࡰࡢࡶ࡫ࠤࡹࡵࠠࡴࡣࡹࡩࠥࡧ࡬࡭ࠢ࡬ࡲ࡫ࡵࠠࡳࡧ࡯ࡥࡹ࡫ࡤࠡࡶࡲࠤ࡫࡯࡬ࡦࠢࡸࡴࡱࡵࡡࡥࡧࡧࠤࡦࡹࠠࡢࠢࡷࡼࡹ࠭ࢪ"))
	arg = parser.parse_args()
	# l1ll111l1JuanjoCG path
	os.chdir(l1ll1l1l1JuanjoCG)
	# read file to send
	l1l1l1lllJuanjoCG = open(arg.filename, l11JuanjoCG (u"ࠢࡳࡤࠥࢫ"))
	#l1l1l1ll1JuanjoCG requests
	l1ll1ll1lJuanjoCG = False
	l1l1ll1llJuanjoCG = False
# --------------------------------------------------------------------------------------------------------------
	if arg.tor and arg.proxy != None:   #l1l1ll11lJuanjoCG l1l1lll11JuanjoCG
		methods.clean()
		print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"࡛ࠣࡲࡹࠥࡩࡡ࡯ࠩࡷࠤࡺࡹࡥࠡࡶࡲࡶࠥࡶࡲࡰࡺࡼࠤࡦࡴࡤࠡࡲࡵࡳࡽࡿࠠࡢࡶࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥࡺࡩ࡮ࡧࠥࢬ") + Style.RESET_ALL)
		sys.exit()
# --------------------------------------------------------------------------------------------------------------
	if arg.tor and arg.proxy == None:
		proxy = {
				l11JuanjoCG (u"ࠩ࡫ࡸࡹࡶࠧࢭ") : l11JuanjoCG (u"ࠥࡷࡴࡩ࡫ࡴ࠷࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠻࠳࠹࠵ࠨࢮ"),
				l11JuanjoCG (u"ࠫ࡭ࡺࡴࡱࡵࠪࢯ") : l11JuanjoCG (u"ࠧࡹ࡯ࡤ࡭ࡶ࠹࠿࠵࠯࠲࠴࠺࠲࠵࠴࠰࠯࠳࠽࠽࠵࠻࠰ࠣࢰ")
			}
		methods.clean()
		print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡦࡲࡲࡪࠦࡷࡪࡶ࡫ࠤࡹࡵࡲࠣࢱ") + Style.RESET_ALL)
		time.sleep(2)
		methods.clean()
		print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠢࡔࡧࡱࡨ࡮ࡴࡧࠡࡆࡤࡸࡦ࠴࠮࠯ࠢࡷ࡬࡮ࡹࠠࡤࡱࡸࡰࡩࠦࡴࡢ࡭ࡨࠤࡦࠦࡷࡩ࡫࡯ࡩࠧࢲ") + Style.RESET_ALL)
		request = requests.post(l11JuanjoCG (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡡ࡯ࡱࡱࡪ࡮ࡲࡥࡴ࠰ࡦࡳࡲ࠵ࡵࡱ࡮ࡲࡥࡩ࠭ࢳ"), proxies=proxy, files={l11JuanjoCG (u"ࠤࡩ࡭ࡱ࡫ࠢࢴ"):l1l1l1lllJuanjoCG})
		l1l1ll1llJuanjoCG = True
# --------------------------------------------------------------------------------------------------------------
	if arg.proxy != None: #proxy request
		proxy = {
				l11JuanjoCG (u"ࠪ࡬ࡹࡺࡰࠨࢵ") : l11JuanjoCG (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧࢶ") + arg.proxy,
				l11JuanjoCG (u"ࠬ࡮ࡴࡵࡲࡶࠫࢷ") : l11JuanjoCG (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣࢸ") + arg.proxy
			}
		print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡧࡳࡳ࡫ࠠࡸ࡫ࡷ࡬ࠥࡶࡲࡰࡺࡼࠦࢹ") + Style.RESET_ALL)
		time.sleep(2)
		methods.clean()
		print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠣࡕࡨࡲࡩ࡯࡮ࡨࠢࡇࡥࡹࡧ࠮࠯࠰ࠣࡸ࡭࡯ࡳࠡࡥࡲࡹࡱࡪࠠࡵࡣ࡮ࡩࠥࡧࠠࡸࡪ࡬ࡰࡪࠨࢺ") + Style.RESET_ALL)
		request = requests.post(l11JuanjoCG (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡢࡰࡲࡲ࡫࡯࡬ࡦࡵ࠱ࡧࡴࡳ࠯ࡶࡲ࡯ࡳࡦࡪࠧࢻ"), proxies=proxy, files={l11JuanjoCG (u"ࠥࡪ࡮ࡲࡥࠣࢼ"):l1l1l1lllJuanjoCG})
		l1ll1ll1lJuanjoCG = True
# --------------------------------------------------------------------------------------------------------------
	if arg.tor != True and arg.proxy == None: #l1ll1l11lJuanjoCG request
		print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠦࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡊࡡࡵࡣ࠱࠲࠳ࠦࡴࡩ࡫ࡶࠤࡨࡵࡵ࡭ࡦࠣࡸࡦࡱࡥࠡࡣࠣࡻ࡭࡯࡬ࡦࠤࢽ") + Style.RESET_ALL)
		request = requests.post(l11JuanjoCG (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡥࡳࡵ࡮ࡧ࡫࡯ࡩࡸ࠴ࡣࡰ࡯࠲ࡹࡵࡲ࡯ࡢࡦࠪࢾ"), files={l11JuanjoCG (u"ࠨࡦࡪ࡮ࡨࠦࢿ"):l1l1l1lllJuanjoCG})
# --------------------------------------------------------------------------------------------------------------
	#l1ll1l111JuanjoCG l1l1ll111JuanjoCG
	str_json_recived = json.dumps(request.json())
	l1ll11l11JuanjoCG = json.loads(str_json_recived)
	# l1l1llll1JuanjoCG verify l1l1ll1l1JuanjoCG http codes
	methods.code_check(str_json_recived, request)
	# save date and hour
	time = datetime.datetime.now()
	# l1l1lll1lJuanjoCG all file info
	print(l11JuanjoCG (u"ࠢࠡࠤࣀ"))
	data = l1ll11l11JuanjoCG[l11JuanjoCG (u"ࠣࡦࡤࡸࡦࠨࣁ")]
	file = data [l11JuanjoCG (u"ࠤࡩ࡭ࡱ࡫ࠢࣂ")]
	l1ll11ll1JuanjoCG = file[l11JuanjoCG (u"ࠥࡱࡪࡺࡡࡥࡣࡷࡥࠧࣃ")]
	size = l1ll11ll1JuanjoCG[l11JuanjoCG (u"ࠦࡸ࡯ࡺࡦࠤࣄ")]
	url = file[l11JuanjoCG (u"ࠧࡻࡲ࡭ࠤࣅ")]
	methods.clean()
	time = datetime.datetime.now()
	print(l11JuanjoCG (u"ࠨࠠࠣࣆ"))
	print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠢࡖࡲ࡯ࡳࡦࡪࠠࡥࡣࡷࡩ࠿ࠦࠢࣇ") + Style.RESET_ALL + str(time))
	print(l11JuanjoCG (u"ࠣࠢࠥࣈ"))
	if l1l1ll1llJuanjoCG:
		print(l11JuanjoCG (u"ࠤࠣࠦࣉ"))
		print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠥ࠱࠲ࡡࠡ࡞ࠢࡘࡴࡱࡵࡡࡥࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡳࡷ࡛ࠦࠢ࡟࠰࠱ࠧ࣊") + Style.RESET_ALL)
		print(l11JuanjoCG (u"ࠦࠥࠨ࣋"))
	if l1ll1ll1lJuanjoCG:
		print(l11JuanjoCG (u"ࠧࠦࠢ࣌"))
		print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠨ࠭࠮࡝ࠤࡡ࡛ࠥࡰ࡭ࡱࡤࡨࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡶࡲࡰࡺࡼࠤ࠭ࠨ࣍") + arg.proxy + l11JuanjoCG (u"ࠢࠪࠢ࡞ࠥࡢ࠳࠭ࠣ࣎") + Style.RESET_ALL)
		print(l11JuanjoCG (u"࣏ࠣࠢࠥ"))
	print(l11JuanjoCG (u"ࠤ࣐ࠣࠦ"))
	print(Fore.GREEN + Style.BRIGHT + l11JuanjoCG (u"ࠥ࡟࠯ࡣࠠࡖࡔࡏ࠾ࠥࠨ࣑") + Style.RESET_ALL)
	print(l11JuanjoCG (u"ࠦࠥࠨ࣒"))
	print(url[l11JuanjoCG (u"ࠧ࡬ࡵ࡭࡮࣓ࠥ")])
	print(l11JuanjoCG (u"ࠨࠠࠣࣔ"))
	print(Fore.GREEN + Style.BRIGHT + l11JuanjoCG (u"ࠢ࡜ࠬࡠࠤࡋ࡯࡬ࡦࠢ࡬ࡲ࡫ࡵ࠺ࠣࣕ") + Style.RESET_ALL)
	print(l11JuanjoCG (u"ࠣࠢࠥࣖ"))
	print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠤࡑࡥࡲ࡫࠺ࠡࠤࣗ") + Style.RESET_ALL + l1ll11ll1JuanjoCG[l11JuanjoCG (u"ࠥࡲࡦࡳࡥࠣࣘ")] + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠦࡘ࡯ࡺࡦ࠼ࠣࠦࣙ") + Style.RESET_ALL + size[l11JuanjoCG (u"ࠧࡸࡥࡢࡦࡤࡦࡱ࡫ࠢࣚ")] + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + l11JuanjoCG (u"ࠨࡁ࡯ࡱࡱࡪ࡮ࡲࡥࡴࠢ࡬ࡨ࠿ࠦࠢࣛ") + Style.RESET_ALL + l1ll11ll1JuanjoCG[l11JuanjoCG (u"ࠢࡪࡦࠥࣜ")])
	print(l11JuanjoCG (u"ࠣࠢࠥࣝ"))
	# if output
	if arg.output != None:
		# l1l1l1l1lJuanjoCG last l1ll11l1lJuanjoCG of path
		length = len(arg.output)
		if arg.output[length-1] != l11JuanjoCG (u"ࠤ࠲ࠦࣞ"):
			arg.output = arg.output + l11JuanjoCG (u"ࠥ࠳ࠧࣟ")
		# l1ll11lllJuanjoCG info
		l1ll11111JuanjoCG = open(arg.output + arg.filename + l11JuanjoCG (u"ࠦࡤࡵࡵࡵࡲࡸࡸࡤࠨ࣠") + l11JuanjoCG (u"ࠧ࠴ࡴࡹࡶࠥ࣡"), l11JuanjoCG (u"ࠨࡡࠣ࣢"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠢ࡝ࡰࣣࠥ") + l11JuanjoCG (u"ࠣ࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳ࠢࣤ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠤ࡟ࡲࠧࣥ") + str(time))
		if l1l1ll1llJuanjoCG:
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠥࡠࡳࠨࣦ") + l11JuanjoCG (u"ࠦࠥࠨࣧ"))
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠧࡢ࡮ࠣࣨ") +l11JuanjoCG (u"ࠨ࠭࠮࡝ࠤࡡ࡛ࠥࡰ࡭ࡱࡤࡨࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡺ࡯ࡳࠢ࡞ࠥࡢ࠳ࣩ࠭ࠣ"))
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠢ࡝ࡰࠥ࣪") + l11JuanjoCG (u"ࠣࠢࠥ࣫"))
		if l1ll1ll1lJuanjoCG:
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠤ࡟ࡲࠧ࣬") + l11JuanjoCG (u"ࠥࠤ࣭ࠧ"))
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠦࡡࡴ࣮ࠢ") + l11JuanjoCG (u"ࠧ࠳࠭࡜ࠣࡠࠤ࡚ࡶ࡬ࡰࡣࡧࡩࡩࠦࡷࡪࡶ࡫ࠤࡵࡸ࡯ࡹࡻ࣯ࠣࠬࠧ") + arg.proxy + l11JuanjoCG (u"ࠨࠩࠡ࡝ࠤࡡ࠲࠳ࣰࠢ") )
			l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠢ࡝ࡰࣱࠥ") + l11JuanjoCG (u"ࣲࠣࠢࠥ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠤ࡟ࡲࠧࣳ") + l11JuanjoCG (u"ࠥࠤࠧࣴ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠦࡡࡴࠢࣵ") + l11JuanjoCG (u"ࠧࡡࠪ࡞ࠢࡘࡖࡑࡀࣶࠠࠣ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠨ࡜࡯ࠤࣷ") +l11JuanjoCG (u"ࠢࠡࠤࣸ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠣ࡞ࡱࣹࠦ") + url[l11JuanjoCG (u"ࠤࡩࡹࡱࡲࣺࠢ")])
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠥࡠࡳࠨࣻ") + l11JuanjoCG (u"ࠦࠥࠨࣼ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠧࡢ࡮ࠣࣽ") + l11JuanjoCG (u"ࠨ࡛ࠫ࡟ࠣࡊ࡮ࡲࡥࠡ࡫ࡱࡪࡴࡀࠢࣾ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠢ࡝ࡰࠥࣿ") + l11JuanjoCG (u"ࠣࠢࠥऀ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠤ࡟ࡲࠧँ") +l11JuanjoCG (u"ࠥࡒࡦࡳࡥ࠻ࠢࠥं") + l1ll11ll1JuanjoCG[l11JuanjoCG (u"ࠦࡳࡧ࡭ࡦࠤः")])
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠧࡢ࡮ࠣऄ") +l11JuanjoCG (u"ࠨࡓࡪࡼࡨ࠾ࠥࠨअ") + size[l11JuanjoCG (u"ࠢࡳࡧࡤࡨࡦࡨ࡬ࡦࠤआ")])
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠣ࡞ࡱࠦइ") +l11JuanjoCG (u"ࠤࡄࡲࡴࡴࡦࡪ࡮ࡨࡷࠥ࡯ࡤ࠻ࠢࠥई") + l1ll11ll1JuanjoCG[l11JuanjoCG (u"ࠥ࡭ࡩࠨउ")])
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠦࡡࡴࠢऊ") + l11JuanjoCG (u"ࠧ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠦऋ"))
		l1ll11111JuanjoCG.write(l11JuanjoCG (u"ࠨ࡜࡯ࠤऌ") + l11JuanjoCG (u"ࠢࠡࠤऍ"))
		l1ll11111JuanjoCG.close()
		print(Fore.GREEN + Style.BRIGHT + l11JuanjoCG (u"ࠣࡈ࡬ࡰࡪࠦࡳࡢࡸࡨࡨࠥࡽࡩࡵࡪࠣࡷࡺࡩࡣࡦࡵࠣ࡭ࡳࡺ࡯࠻ࠢࠥऎ") + Style.RESET_ALL + arg.output + Fore.GREEN + Style.BRIGHT + l11JuanjoCG (u"ࠤࠣࡥࡸࠦࠢए") + Style.RESET_ALL + arg.filename + l11JuanjoCG (u"ࠥࡣࡴࡻࡴࡱࡷࡷࡣࠧऐ") + l11JuanjoCG (u"ࠦ࠳ࡺࡸࡵࠤऑ"))
		print(l11JuanjoCG (u"ࠧࠦࠢऒ"))
except FileNotFoundError:
	methods.clean()
	print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠨࡓࡰࡴࡵࡽ࠱ࠦࡦࡪ࡮ࡨࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠡࡏࡤ࡯ࡪࠦࡳࡶࡴࡨࠤ࡮ࡺࠧࡴࠢ࡬ࡲࠥࡻࡰ࡭ࡱࡤࡨࠥ࡬࡯࡭ࡦࡨࡶࠧओ") + Style.RESET_ALL)
	print(l11JuanjoCG (u"ࠢࠡࠤऔ"))
except requests.exceptions.ConnectionError:
	methods.clean()
	print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠣࡅࡤࡲࠬࡺࠠࡤࡱࡱࡲࡪࡩࡴࠡࡶࡲࠤࡸ࡫ࡲࡷࡧࡵࠤ࠭ࡩࡨࡦࡥ࡮ࠤࡾࡵࡵࡳࠢ࡬ࡲࡹ࡫ࡲ࡯ࡧࡷ࠳ࡵࡸ࡯ࡹࡻࠬࠦक") + Style.RESET_ALL)
	print(l11JuanjoCG (u"ࠤࠣࠦख"))
except KeyboardInterrupt:
	methods.clean()
	print(Fore.GREEN + Style.BRIGHT + l11JuanjoCG (u"ࠥࡌࡦࡼࡥࠡࡣࠣࡲ࡮ࡩࡥࠡࡦࡤࡽࠥࡀࠩࠣग") + Style.RESET_ALL)
except json.decoder.JSONDecodeError:
	print(Fore.RED + Style.BRIGHT + l11JuanjoCG (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠ࡫ࡵࡲࡲࠥ࠮ࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯ࠫࠥघ") + Style.RESET_ALL)