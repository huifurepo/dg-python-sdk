import unittest
import dg_sdk
import json
from demo.demo_config import *


def getFileList():
    dto = dict()
    # 文件jfileID
    # dto["file_id"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 账户号
    extend_infos["acct_id"] = "C02730634"
    # 银行卡绑定身份证
    extend_infos["cert_no"] = "k05wtsAi+WSv8rdRaj24nOGQetL4L8k5VFRGPdljb1O/5pOJYe4o3ofwiKNjaVyAwvGFWIqMNEu0GU1gcq+UDmnabOROcneJVNGu+XMy5J9I55OqBDOC5lIiiuSWQux7TlaDCZT7ACpYHjRI2r3bzOASgzPXebjYLllnuEg2kxYpGqJBe8jsjaTpAzoEB1Yoy6I0sAn4xxl8IjmGu5AHEA/drWyrAIT0GsEhmeR6wkJK3iCjShqIQ317BkNBzXsdt8dGZLF4M/7iwiQXaVP2KLWKtX+gn2oI19ckTTiFXnvuNtNPJEUEayTbsAODHKvo5wsYLUdbnO2UFJ6wlE3rOQ=="
    # 联行号
    extend_infos["branch_code"] = "105290071051"
    # 银行所在省
    extend_infos["prov_id"] = "130000"
    # 银行所在市
    extend_infos["area_id"] = "130300"
    # 补充资质材料列表
    extend_infos["file_list"] = getFileList()
    return extend_infos


class TestV2LargeamtBindcardBindRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银行大额支付绑卡 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2LargeamtBindcardBindRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108312997"
        request.card_type = "1"
        request.card_name = "许溪证"
        request.card_no = "GCMghaHLsWffNmBl/uuvVnv+kzwvBSLaZR+AsldnabAMzjPUzw4SMe2DX8IvVTM/Qb/tbiQwayeQ+TwkeSyQ0IB6oy/BNgM3rl7wZsdTzKbyigyGQvtOYsauk3IUuiJ8ptJ1k0C4Ysd5Z4+6ApLmOZhAem1pqu+DUk8EpKMj37RDgk3zWgVIf1wX9nBaSN1IGIoVjmweg8/r/UVWqCKoYrEWHxO1R0elZM9+hXTwXEKHFc2L2yossgDGjJDKuykaN0DzVunz1uQbxuvg4lMCmycSRjlQ1MCsIzqs4oiVNW3PCqAwoFkdRKL879e5/EsvohJJNVuX6YOeefFdJOC8Ug=="
        request.bank_code = ""
        request.mobile_no = "dFw39mqjcPyZJk5ukKiH5oL+LyJLdJ2DfPgXcOCCgYfsUuCcOJLPnBc6f0nybPDBnfgLCcK31wG5TLFi97EttpBsrQVI6kEWMrxUAAcIehSMuWEBBuGG8QnaayE0tZa2gSgQZgFltCrkgfQ08N6TwLmvZEJ3z+gudsIPRaMXAgxMgnyH6xjuFbdOWJKfgcTQxpIirIQg0bWPpBPnO6HizB3z435qeep7WVCRK7c+tvYxjLRm7jDEeUCd9c0yZ4eKWOt1vLini6kqAwXuCTXa10z1NEnGbFlBrOK5/R5ZK977BmuAD7ZLuHU6T/j2Ca1nG6JOJwXT827CVo/sU7osjQ=="

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""