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
    # 销方名称
    extend_infos["tax_payer_name"] = "汇付网络技术（上海）有限公司"
    # 公司电话
    extend_infos["tel_no"] = "021-33323999"
    # 公司地址
    extend_infos["reg_address"] = "徐汇宜山路700号C5栋021-33323999"
    # 开户银行
    extend_infos["bank_name"] = "民生银行徐汇支行"
    # 开户账户
    extend_infos["account_no"] = "0206014180001609"
    # 联系人手机号
    extend_infos["contact_phone_no"] = "17621100776"
    # 联系人
    extend_infos["contact"] = "王姗"
    # 联系人身份证号
    extend_infos["id_card_no"] = "210123198702122747"
    # 所属省
    extend_infos["prov_id"] = "310000"
    # 所属市
    extend_infos["city_id"] = "310100"
    return extend_infos


class TestV2InvoiceMerModifyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 商户注册信息修改 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceMerModifyRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000149801800"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""