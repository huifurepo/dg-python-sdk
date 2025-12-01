import unittest
import dg_sdk
import json
from demo.demo_config import *


def get7c9ad9fcD8a5406dB03fCfe3334893ee():
    dto = dict()
    # 入账接收方明细
    # dto["acct_infos"] = getF92bb2ca1c7b4758Adb382a0a3eeeb16()

    return json.dumps(dto)

def getF92bb2ca1c7b4758Adb382a0a3eeeb16():
    dto = dict()
    # 入账金额
    # dto["div_amt"] = "test"
    # 接收方ID
    # dto["huifu_id"] = "test"
    # 接收方账户号
    # dto["acct_id"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 原请求流水号
    extend_infos["efp_req_seq_id"] = "20241128164919defaultit687891821"
    # 原请求日期
    extend_infos["efp_req_date"] = "20241128"
    # 联行号
    extend_infos["branch_code"] = ""
    # 备注
    extend_infos["remark"] = "saas申请付款"
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.service.com/getresp"
    return extend_infos


class TestV2EfpSurrogateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 全渠道资金付款申请 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2EfpSurrogateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108422302"
        request.cash_amt = "0.01"
        request.card_no = "cDH2Gq/a7PnrH5tvA6JNEFEcLewpEW3x5cRiyJRUEwpoqTMmp74ObRCJCarqKPRnMrnHbXfa1WGAXW24f6SLiDKqCdI0zc5+tQtKBXS5Kh/mfmJIDNU710i5IDs+7luEIpRrsppg6YJejRhGY0TvPVY19dRaJ3KxIeyTkUDv/9KEb8TELxm2GBgfiFlKVPKxf95WpaZWV2kT3rh0ddJXA9YgUvHcTcEEY7GeCv5OHOaquIcP38kv27ZL2rScqgGpmluhyevPtDmvXRkdGK68IfNnWeqfCRjDAdVqcMskTb5Ajq8dtnNlx7uuSwYYKBeJKCzoPX8SE5X+f/9d62Cutw=="
        request.bank_code = "01050000"
        request.card_name = "交通银行股份有限公司"
        request.card_acct_type = "E"
        request.prov_id = "310000"
        request.area_id = "310100"
        request.mobile_no = "AJnlbnjQcbTgyDv2NSNdVpMlpE5PkMqtppZj1AQ7yxAbvPhWHwHUzq7J+6C8PIrsHWwI6iwAo07N77zUIbMmORzRY1eENJ9intq0/nGEbRDQ3s6EtV/AXVUR9Pv+GOqetpX5Yi+htEbpKObW8V+jEUngz4L08E5VsPLSjmLKeLkVXGKiMr8jeZf/+QAhDiJFyi533dxHL+KPT0qCa3iebau1NXy17sZm4izmeYf35LxTlgZbQdxhC50z3zlkhZvMsArtod1CmlzI+SB5T3bwqpVkR22o6BkTbLrqBZp+zz5x99o6sqIEKMrwKYjDOJ0UjYsjn+KFTa+PFvJzstmqhg=="
        request.cert_type = "11"
        request.cert_no = "KbQ+WwhycbCOeIbrB+pH+eEsJPcYo2Q1IhMUQosshs00qy7hor+CA71bZLMazVOuFkeJxex9BfhR9W2hQNbRaqdWI4yxkDOTw9Qkx1PDTDl/n8CXpxWqQKhObCE5UEd5b+M/wWe+iKNYGcJkcoyswHdMA8kZoezxqwVUi0tbq//1Ov+kTyMVhmIwNbWJpahDvS+f780opCAtlMbz9hl25EcPpeTtNgbruKY+jeO4j6oejFK0epg616uC9jQalryERsX4EjaLqQrtd5nwZBkASc5Up56xkVqvaOo+6hFQP/KbCymxWbM3J0/PFsJtv/CPM4+9JkWusX/Q1ZEH8wdZ+A=="
        request.licence_code = "9131000010000595XD"
        request.acct_split_bunch = get7c9ad9fcD8a5406dB03fCfe3334893ee()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""