import unittest
import dg_sdk
import json
from demo.demo_config import *



def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 分页页码
    extend_infos["page_num"] = "0"
    # 分页条数
    extend_infos["page_size"] = "5"
    # 归集状态
    extend_infos["status"] = ""
    # 转出方账户号
    extend_infos["out_acct_id"] = ""
    # 转入方账户号
    extend_infos["in_acct_id"] = ""
    return extend_infos


class TestV2TradeSettleCollectionDetailQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 资金归集明细查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeSettleCollectionDetailQueryRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.begin_date = "20240711"
        request.end_date = "20240718"
        request.out_huifu_id = ""
        request.in_huifu_id = "6666000146178696"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""