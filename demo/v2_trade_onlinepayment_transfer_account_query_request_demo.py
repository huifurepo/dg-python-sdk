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
    # 订单模式
    # extend_infos["order_mode"] = ""
    # 原请求流水号
    extend_infos["org_req_seq_id"] = "20211659949882"
    # 原请求日期
    extend_infos["org_req_date"] = "20220808"
    # 银行卡号
    extend_infos["bank_card_no"] = "Xmjm1RB4AAOaFYQ+PgjBlpugXbd8VAYAGB3J2zrbLfC42Bh5xiB47OOV1EdXyGpBq4H8je7mB/MlyEEs6O8PX6aoI4QHumr8VglrLM6uzbVNCIc3S5RPSmi2M+9+EdIQ6nlWd5+XQ7RJXX5Uvnegn74XzQBcN1d4gd04buwKbLpUPV3tWd1qjQwEE8w4gwEtH3L5AP75Mynz+wHFrUKJF3BTiW2/zJlcq5GJomOl06GEW52AZkXwn6U2suP3a0ySd0Rxbf1yQ1lj3SP56NeeEzuBaFLQWB7mEqJfZF3pE9MHNfi6tR1xwLdcxt98bdIqlteKdNAmgfQzcS13UcwH+w=="
    # 付款方名称
    extend_infos["certificate_name"] = "沈显龙"
    # 入账标识
    extend_infos["in_acct_flag"] = "YDNI2NDJIKKPAFGQ"
    # 交易开始日期
    extend_infos["trans_start_date"] = "20220801"
    # 交易结束日期
    extend_infos["trans_end_date"] = "20220808"
    # 实际打款日期
    # extend_infos["remit_date"] = ""
    # 每页条数
    # extend_infos["page_size"] = ""
    # 分页页码
    # extend_infos["page_no"] = ""
    return extend_infos


class TestV2TradeOnlinepaymentTransferAccountQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银行大额资金流水查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentTransferAccountQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100615"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""