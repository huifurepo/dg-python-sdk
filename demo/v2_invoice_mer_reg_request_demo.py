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
    # 联系人
    extend_infos["contact"] = "王姗"
    # 联系人身份证号
    extend_infos["id_card_no"] = "210123198702122747"
    # 业务到期年限
    extend_infos["valid_period"] = "1"
    # 自动续约
    extend_infos["auto_renewal"] = "Y"
    # 商户入驻结果异步通知地址
    extend_infos["callback_url"] = "http: //service.example.com/to/path"
    return extend_infos


class TestV2InvoiceMerRegRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 商户注册 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceMerRegRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000149801800"
        request.tax_payer_id = "91310000795605184T"
        request.tax_payer_name = "汇付网络技术（上海）有限公司"
        request.tel_no = "021-33323999"
        request.reg_address = "徐汇宜山路700号C5栋021-33323999"
        request.bank_name = "民生银行徐汇支行"
        request.account_no = "0206014180001609"
        request.contact_phone_no = "17621100776"
        request.open_mode = "2"
        request.prov_id = "310000"
        request.city_id = "310100"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""