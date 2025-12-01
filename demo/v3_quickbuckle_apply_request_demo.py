import unittest
import dg_sdk
import json
from demo.demo_config import *


def getRiskInfo():
    dto = dict()
    # IP类型
    dto["ip_type"] = "04"
    # IP值
    dto["source_ip"] = "192.168.17.01"
    # 设备标识
    dto["device_id"] = "666666"
    # 设备类型
    dto["device_type"] = "1"
    # 银行预留手机号
    dto["mobile"] = "18255906937"

    return json.dumps(dto)

def getTrxDeviceInf():
    dto = dict()
    # 银行预留手机号
    dto["trx_mobile_num"] = "15556622368"
    # 设备类型
    dto["trx_device_type"] = "1"
    # 交易设备IP
    dto["trx_device_ip"] = "10.10.0.1"
    # 交易设备MAC
    dto["trx_device_mac"] = "10.10.0.1"
    # 交易设备IMEI
    dto["trx_device_imei"] = "030147441006000182623"
    # 交易设备IMSI
    dto["trx_device_imsi"] = "030147441006000182623"
    # 交易设备ICCID
    dto["trx_device_icc_id"] = "030147441006000182623"
    # 交易设备WIFIMAC
    dto["trx_device_wfifi_mac"] = "030147441006000182623"
    # 交易设备GPS
    dto["trx_device_gps"] = "030147441006000182623"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # CVV2
    extend_infos["cvv2"] = ""
    # 卡有效期
    extend_infos["expiration"] = ""
    # 卡的借贷类型
    extend_infos["dc_type"] = "D"
    # 设备信息域 
    extend_infos["trx_device_inf"] = getTrxDeviceInf()
    # 风控信息
    extend_infos["risk_info"] = getRiskInfo()
    return extend_infos


class TestV3QuickbuckleApplyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 快捷绑卡申请接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V3QuickbuckleApplyRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000107052905"
        request.out_cust_id = "123456232222222"
        request.card_no = "Wru7xKezRvcZVbrIWEQxkZ3drPPGZXqN46SX4BVNQG95g/oNXVLzZp0dQ9pEi/eE6MMoaK4BUhv7Z/FRzVpacM+vsBYX/FnwQWdRrYm3ziMMdcCG1VFTGhNoYuezROzeFmu5Ol31rp3xy10BZxC/DqRCEIM6JKgzLmx1i3wRYh2XkATzVQ7C/ovdpIERuvEAQuX/aIimWRagUU3agsgiUsd7hu9DkwwfY9eKEAZa5BmM79RWdDj6mOCNIsA05qVEpSe5EBFypZCz8YkoJAiHshlzXOXz0oqTvrNyhsMQuPfnhlcm2i+JDmuja9TlR6xVHBv2MS1v8OdQl8PtBNma/w=="
        request.card_name = "YNPU8HnWVCF0ct7thu3nFXt/5tlJZ0ajvFjlgEpAcc4/fKJMsq9JnC5/z9D8AUHTeVLknENjeceblJ+8rr4liYGNxb6LRhVppsahWZObb1L1l32+beYC6801Yyvb/YSgEPLCTJHJQRy+BPrrKsqAEgql8VueqQvOdHee7iyzlqa76oXZOEmTzzoxeGVl5GTqPz9mwL2s3N7SovTGruGy5KQceFx8QH3SgBxRimbD2i6WY4catrPyXFjElegHRDdq6QLTCgb6nUdj5f5WDsLjQYQ2dGFd+qfESpDpjBw9plKiE7CfQrId0Np9ZD2nWe4HScmyrWyRZgRs8AqmuOnBBA=="
        request.cert_no = "dldU2hVyr55qKinWJOgGeGDsvKkM01bR5iWgPZwMibKECdawzJo254J1r1KEqJjv3NjN4OhO6PsUSxVDO0w6JlB1Sa6MHJcsAqoeMO5pTQ60SaGaZh31Busf5HxeUqOAiqT5do7uPW+krHe71i6jIIat2pIVaMXmSC6aicE6Ei3Lil0j9n0nDDQP/Jw53pyiTeuUr2p9uh8Hx5Og4Q4kkuhtmUEyiwqiLV6uaJObNvnvx4tr31nZcPRalVkfBWduxmwOZpkcPiEILpKAcCow9nv+c1C/olX6eSE1nvFH6kaRat3Web2tYR/Pmy5emvgZhZDzMzaAN9rnIZn2V15Pog=="
        request.cert_validity_type = "1"
        request.cert_begin_date = "20101201"
        request.cert_end_date = "20301201"
        request.mobile_no = "LXZKQaNRSxtvuTfjLt/2XUlnd8/Qo+ZWPoGlmJr4uCyQZvjvGM/c91pJtBWoS3Yn7/0GF/pS6W1FR7QcQXCcfifqUBFWuz5Babga7D+LykM3NUrP1d+8T/bMqbkeRpaKwwtCHkOkguHbacOsGGDNaOhkGuRN3GLwMI4ldaSKNbIs9jJmf1ed37jSX2wWCMAWg+D1b743yZIe1RQSrw/S/UMmFEZcAWJjnhlmGh3xFkm7EjXp0e3wCB4t3H7faHcLMBMhY21779XUVitxRm/7B5mlD/ozIDO18Ds754OBM0iRe4NaKdW4Ve/i+UV8dV0nfeSpO5mk0RxHT510ceVW3w=="
        request.protocol_no = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""