import unittest
import dg_sdk
import json
from demo.demo_config import *


def getFb3598d168734104Bb0d164b578aab34():
    dto = dict()
    # 签约人类型
    dto["type"] = "LEGAL"
    # 签约人手机号
    dto["mobile_no"] = "18611111111"

    return json.dumps(dto)

def getC8f0b784B86845ff95598724e11c009b():
    dto = dict()
    # 商家配置开关
    dto["switch_state"] = "1"
    # 最大代扣比例(0,100]区间的整数,商家配置开关为开时必填&lt;font color&#x3D;&quot;green&quot;&gt;示例值：50&lt;/font&gt;
    dto["max_withhold_percent"] = "50"
    # 抖音来客配置json对象,商家配置开关为开时必填
    dto["lla_dylk_config"] = getAaee4569633d42ba879536a3ee7acdc4()

    return json.dumps(dto)

def getAaee4569633d42ba879536a3ee7acdc4():
    dto = dict()
    # 抖音来客配置开关
    dto["switch_state"] = "1"
    # 关联代运营汇付id抖音来客配置开关为开时必填,&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000109812124&lt;/font&gt;
    dto["agency_huifu_id"] = "6666000109812124"
    # 代扣卡token抖音来客配置开关为开时必填
    dto["token_no"] = "32231131111"
    # 抖音账户号
    dto["dy_acct_no"] = "132123111"
    # 抖音网店名称抖音来客配置开关为开时必填
    dto["dy_online_store_name"] = "网店名称"
    # 抖音业务类型
    dto["dy_busi_type"] = "1"
    # 商家与代运营合作协议(抖音来客)抖音来客配置开关为开时必填，商家与代运营方的扣款协议，文件类型F636；详见[文件类型说明](https://paas.huifu.com/open/doc/api/#/csfl/api_csfl_wjlx)；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：57cc7f00-600a-33ab-b614-6221bbf2e530&lt;/font&gt;
    dto["madylk_cooperation_agreement_file"] = "57cc7f00-600a-33ab-b614-6221bbf2e530"
    # 商家抖音来客平台材料抖音来客配置开关为开时必填，提供商家在抖音来客平台的店铺名称、结算账户截图、经营照片等信息，文件类型F637；详见[文件类型说明](https://paas.huifu.com/open/doc/api/#/csfl/api_csfl_wjlx)；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：57cc7f00-600a-33ab-b614-6221bbf2e530&lt;/font&gt;
    dto["merchant_dylk_file"] = "57cc7f00-600a-33ab-b614-6221bbf2e530"

    return dto;

def getEfde4fc4C2bc4b65Bb9aFa44c01e4e03():
    dto = dict()
    # 代运营配置开关
    # dto["switch_state"] = "test"
    # 佣金手续费百分比代运营配置开关为开时必填,[0-100]区间的数,小数位最多两位 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;；&lt;br/&gt;
    # dto["fee_rate"] = "test"
    # 佣金手续费内外扣标记代运营配置开关为开时必填,1:外扣 2:内扣 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：2&lt;/font&gt;；&lt;br/&gt;
    # dto["out_fee_flag"] = "test"
    # 佣金手续费外扣汇付ID佣金手续费内外扣标记为 1:外扣时必填 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000109812120&lt;/font&gt;
    # dto["out_fee_huifuid"] = "test"
    # 佣金手续费外扣子账户类型01-基本户，05-充值户，09：营销户，佣金手续费内外扣标记为 1:外扣时必填 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：01&lt;/font&gt;
    # dto["out_fee_acct_type"] = "test"
    # 商家与代运营合作协议代运营配置开关为开时必填，商家与代运营方的扣款协议，文件类型F634；详见[文件类型说明](https://paas.huifu.com/open/doc/api/#/csfl/api_csfl_wjlx)；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：57cc7f00-600a-33ab-b614-6221bbf2e530&lt;/font&gt;
    # dto["ma_cooperation_agreement_file"] = "test"
    # 代运营服务证明材料代运营配置开关为开时必填，文件类型F635；详见[文件类型说明](https://paas.huifu.com/open/doc/api/#/csfl/api_csfl_wjlx)；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：57cc7f00-600a-33ab-b614-6221bbf2e530&lt;/font&gt;
    # dto["agency_service_prove_file"] = "test"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 业务角色
    extend_infos["busi_role"] = "MERCHANT"
    # 协议类型
    extend_infos["agreement_type"] = "0"
    # 审核异步消息接收地址
    # extend_infos["audit_async_return_url"] = ""
    # 电子协议签约链接异步通知地址
    # extend_infos["agreement_async_return_url"] = ""
    # 交易异步应答地址
    # extend_infos["recon_resp_addr"] = ""
    return extend_infos


class TestV2MerchantBusiLlaconfigRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 代运营代扣业务配置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantBusiLlaconfigRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000123123123"
        request.upper_huifu_id = "6666000109812120"
        request.lla_agency_config = getEfde4fc4C2bc4b65Bb9aFa44c01e4e03()
        request.lla_merchant_config = getC8f0b784B86845ff95598724e11c009b()
        request.paper_agreement_file = "test"
        request.sign_user_info = getFb3598d168734104Bb0d164b578aab34()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""