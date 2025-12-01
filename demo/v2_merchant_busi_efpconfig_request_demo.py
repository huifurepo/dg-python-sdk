import unittest
import dg_sdk
import json
from demo.demo_config import *


def get9ec48f90E352499a9addA378f6846dcd():
    dto = dict()
    # 全域资金分账配置开关
    # dto["switch_state"] = "test"
    # 全域资金分账手续费百分比全域资金分账配置开关为开时必填，0-100之间的数,&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.21&lt;/font&gt;
    # dto["fee_rate"] = "test"
    # 全域资金分账手续费固定值全域资金分账配置开关为开时必填，整数位最多12位，小数位最多2位；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;
    # dto["fee_fix_amt"] = "test"

    return json.dumps(dto)

def get6674d93b18814bcc858f0f1e23cb758e():
    dto = dict()
    # 全域资金付款手续费百分比
    # dto["fee_rate"] = "test"
    # 全域资金付款手续费固定值
    # dto["fee_fix_amt"] = "test"
    # 全域资金付款手续费收取类型
    # dto["fee_charge_type"] = "test"
    # 全域资金付款手续费内外扣标记
    # dto["out_fee_flag"] = "test"
    # 全域资金付款手续费外扣汇付ID全域资金付款手续费内外扣标记为1:外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000109812123&lt;/font&gt;
    # dto["out_fee_huifuid"] = "test"
    # 全域资金付款手续费外扣子账户号全域资金付款手续费内外扣标记为1:外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：F00598600&lt;/font&gt;
    # dto["out_fee_acctid"] = "test"

    return json.dumps(dto)

def get675abd59Bc414653870397ac8658856a():
    dto = dict()
    # 全域资金取现手续费百分比
    # dto["fee_rate"] = "test"
    # 全域资金取现手续费固定值
    # dto["fee_fix_amt"] = "test"
    # 全域资金取现手续费收取类型
    # dto["fee_charge_type"] = "test"
    # 全域资金取现手续费内外扣标记
    # dto["out_fee_flag"] = "test"
    # 全域资金取现手续费外扣汇付ID全域资金取现手续费内外扣标记为1:外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000109812123&lt;/font&gt;
    # dto["out_fee_huifuid"] = "test"
    # 全域资金取现手续费外扣子账户号全域资金取现手续费内外扣标记为1:外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：F00598600&lt;/font&gt;
    # dto["out_fee_acctid"] = "test"

    return json.dumps(dto)

def getE51a678c64564cdaA4906cdce29b00db():
    dto = dict()
    # 分账规则来源
    # dto["rule_origin"] = "test"
    # 全域资金分账手续费外扣标记1:外扣 2:内扣 规则来源为01时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1&lt;/font&gt;；
    # dto["out_fee_flag"] = "test"
    # 全域资金分账内扣规则01-商户承担02-分账接收方承担 交易手续费外扣标记为2时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：01&lt;/font&gt;；
    # dto["in_fee_rule"] = "test"
    # 全域资金分账手续费外扣汇付ID交易手续费外扣标记为1时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000109812123&lt;/font&gt;；
    # dto["out_fee_huifuid"] = "test"
    # 全域资金分账手续费外扣账户类型交易手续费外扣标记为1时必填 01-基本户05-充值户 09-营销户；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：01&lt;/font&gt;；
    # dto["out_fee_acct_type"] = "test"
    # 分账规则明细规则来源为01时必填 jsonArray格式 最多7条
    # dto["rule_detail"] = getBb6718bbAd03446bB717002c3721ae4e()

    return json.dumps(dto)

def getBb6718bbAd03446bB717002c3721ae4e():
    dto = dict()
    # 分账接收方汇付ID
    # dto["huifu_id"] = "test"
    # 分账接收方账户类型
    # dto["acct_type"] = "test"
    # 分账比例(百分比)
    # dto["split_bill_rate"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def getB0c2d37e3c094da782d9E728d2d25a6d():
    dto = dict()
    # 签约人类型
    dto["type"] = "LEGAL"
    # 签约人手机号
    dto["mobile_no"] = "13777842539"
    # 签约人姓名签约人类型为OTHER时必填 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：张三&lt;/font&gt;
    # dto["name"] = "test"
    # 签约人身份证签约人类型为OTHER时必填 &lt;font color&#x3D;&quot;green&quot;&gt;示例值：321012313213222133&lt;/font&gt;
    # dto["cert_no"] = "test"

    return json.dumps(dto)

def getD53d1c3c72614602A54aA3127ca006f4():
    dto = dict()
    # 开户固定手续费(元)
    dto["fee_fix_amt"] = "0"
    # 开户手续费外扣时的账户类型
    dto["out_fee_acct_type"] = ""
    # 开户手续费外扣汇付ID
    dto["out_fee_huifuid"] = ""

    return json.dumps(dto)

def get5b8384af41c949a087dc041b1f43e416():
    dto = dict()
    # 结算账户名
    dto["card_name"] = "圆务铁白事"
    # 银行卡号
    dto["card_no"] = "4340622119959288"
    # 卡类型
    dto["card_type"] = "0"
    # 银行卡绑定手机号
    dto["mp"] = "13777842539"
    # 开户许可证核准号对公卡必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：J2900123456789&lt;/font&gt;
    dto["open_licence_no"] = "123456789"
    # 银行所在省
    dto["prov_id"] = "310000"
    # 银行所在市
    dto["area_id"] = "310100"
    # 银行编码
    dto["bank_code"] = "01050000"
    # 支行联行号
    dto["branch_code"] = "105290071113"
    # 支行名称
    dto["branch_name"] = "中国建设银行股份有限公司上海市中支行"
    # 持卡人证件有效期（起始）
    dto["cert_begin_date"] = "20240314"
    # 持卡人证件有效期（截止）
    dto["cert_end_date"] = ""
    # 持卡人证件号码
    dto["cert_no"] = "340000199810170714"
    # 持卡人证件类型
    dto["cert_type"] = "00"
    # 持卡人证件有效期类型
    dto["cert_validity_type"] = "1"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 开关
    extend_infos["switch_state"] = "1"
    # 支付手续费百分比
    extend_infos["fee_rate"] = "0.04"
    # 支付手续费最小值
    extend_infos["fee_min_amt"] = ""
    # 支付手续费外扣账户类型
    extend_infos["out_fee_acct_type"] = ""
    # 支付手续费外扣标记
    extend_infos["out_fee_flag"] = "2"
    # 全渠道资金管理补充材料id
    extend_infos["other_payment_institutions_pic"] = "8c4f6254-6c36-3b3c-ae8b-efcf24ca215e"
    # XW银行数字证书及电子签名授权委托书
    # extend_infos["xw_digital_certificate_pic"] = ""
    # 异步消息接收地址
    extend_infos["async_return_url"] = "http://service.example.com/to/path"
    # 业务开通结果异步消息接收地址
    extend_infos["busi_async_return_url"] = "http://service.example.com/to/path"
    # 申请单笔限额
    extend_infos["pay_every_deal"] = ""
    # 申请单日限额
    extend_infos["pay_every_day"] = ""
    # 全域资金分账规则
    # extend_infos["efp_spb_config"] = getE51a678c64564cdaA4906cdce29b00db()
    # 客户ip地址
    # extend_infos["ip_address"] = ""
    # 是否线上场景
    # extend_infos["online_scene_flag"] = ""
    # 网店网址
    # extend_infos["online_store_website"] = ""
    # 网店名称
    # extend_infos["online_store_name"] = ""
    # 是否加盟连锁
    # extend_infos["franchise_chain_flag"] = ""
    # 交易异步应答地址
    # extend_infos["recon_resp_addr"] = ""
    # 协议类型
    # extend_infos["agreement_type"] = ""
    # 全域资金取现手续费配置
    # extend_infos["efp_encash_fee_config"] = get675abd59Bc414653870397ac8658856a()
    # 全域资金付款手续费配置
    # extend_infos["efp_payment_fee_config"] = get6674d93b18814bcc858f0f1e23cb758e()
    # 纸质协议开始日期
    # extend_infos["agree_begin_date"] = ""
    # 纸质协议结束日期
    # extend_infos["agree_end_date"] = ""
    # 是否店群
    # extend_infos["store_group_flag"] = ""
    # 商户经营类型
    # extend_infos["store_busi_type"] = ""
    # 行业类型
    # extend_infos["store_industry_type"] = ""
    # 经营信息材料
    # extend_infos["management_file"] = ""
    # 全域资金分账手续费配置
    # extend_infos["efp_spb_fee_config"] = get9ec48f90E352499a9addA378f6846dcd()
    return extend_infos


class TestV2MerchantBusiEfpconfigRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 全渠道资金管理配置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantBusiEfpconfigRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108139646"
        request.upper_huifu_id = "6666000108120249"
        request.out_fee_huifuid = ""
        request.out_order_acct_card = get5b8384af41c949a087dc041b1f43e416()
        request.out_order_acct_open_fees = getD53d1c3c72614602A54aA3127ca006f4()
        request.business_model = "acquiringMode"
        request.out_funds_gate_id = "xw0"
        request.sign_user_info = getB0c2d37e3c094da782d9E728d2d25a6d()
        request.acct_source = "01"
        request.dy_cooperation_prove_pic = "test"
        request.mt_cooperation_prove_pic = "test"
        request.ks_cooperation_prove_pic = "test"
        request.pdd_cooperation_prove_pic = "test"
        request.xhs_cooperation_prove_pic = "test"
        request.zfb_cooperation_prove_pic = "test"
        request.wx_cooperation_prove_pic = "test"
        request.jd_cooperation_prove_pic = "test"
        request.elm_cooperation_prove_pic = "test"
        request.dw_cooperation_prove_pic = "test"
        request.wph_cooperation_prove_pic = "test"
        request.xc_cooperation_prove_pic = "test"
        request.zfbzl_cooperation_prove_pic = "test"
        request.wxzl_cooperation_prove_pic = "test"
        request.ddjy_cooperation_prove_pic = "test"
        request.ty_cooperation_prove_pic = "test"
        request.tl_cooperation_prove_pic = "test"
        request.yb_cooperation_prove_pic = "test"
        request.efp_paper_agreement_file = "test"
        request.bd_cooperation_prove_pic = "test"
        request.main_store_huifu_id = "test"
        request.sf_cooperation_prove_pic = "test"
        request.xy_cooperation_prove_pic = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""