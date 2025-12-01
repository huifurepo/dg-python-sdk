import unittest
import dg_sdk
import json
from demo.demo_config import *


def get5f9a6c9a2f274b58B08b898a909edb95():
    dto = dict()
    # 经度
    # dto["longitude"] = ""
    # 纬度
    # dto["latitude"] = ""
    # 基站地址
    # dto["base_station"] = ""
    # IP地址
    dto["ip_addr"] = "172.31.11.11"

    return json.dumps(dto)

def get401cdbafBf0248b9Bd22Fc29c064ec90():
    dto = dict()
    # 交易设备类型
    dto["device_type"] = "4"
    # 交易设备IP
    dto["device_ip"] = "172.31.11.11"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 备注
    extend_infos["remark"] = "部分退款看看"
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.baidu.com"
    return extend_infos


class TestV2LlaWithholdRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 代运营佣金代扣退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2LlaWithholdRefundRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.org_req_date = "20250822"
        request.org_req_seq_id = ""
        request.org_hf_seq_id = "00470topotB250827093537P979c0a8408100000"
        request.agency_huifu_id = "6666000108967194"
        request.trans_amt = "25.00"
        request.terminal_device_data = get401cdbafBf0248b9Bd22Fc29c064ec90()
        request.risk_check_data = get5f9a6c9a2f274b58B08b898a909edb95()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""