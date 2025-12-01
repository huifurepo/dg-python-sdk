import unittest
import dg_sdk
import json
from demo.demo_config import *


def getF1feffe72adf427594625abfeb040860():
    dto = dict()
    # 用户号
    dto["huifu_id"] = "6666000107979716"
    # 分配金额(元)
    dto["div_amt"] = "0.11"
    # 微信openid
    dto["sub_openid"] = "13232"
    # 转账备注
    dto["remark"] = "灵工代发1"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 出款方账户号
    extend_infos["acct_id"] = "C02418374"
    # 合作平台
    # extend_infos["lg_platform_type"] = ""
    return extend_infos


class TestV2TradeLgwxSurrogateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 灵工微信代发 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeLgwxSurrogateRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000107755175"
        request.cash_amt = "0.11"
        request.salary_modle_type = "1"
        request.bmember_id = "396117173653968220"
        request.sub_appid = "123213"
        request.notify_url = "virgo://http://www.gangcai.com"
        request.acct_split_bunch = getF1feffe72adf427594625abfeb040860()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""