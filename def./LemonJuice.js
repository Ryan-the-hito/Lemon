// ==UserScript==
// @name         LemonJuice: A Web Tool for Cleaner Chinese
// @namespace    http://tampermonkey.net/
// @version      0.3
// @description  Let Clean Chinese Refresh Your Eyes! 清除中文互联网页面上的“互联网黑话”、“营销号语言”和各种低幼化词汇。
// @author       Ryan-the-hito
// @match        *://*/*
// @icon         https://github.com/Ryan-the-hito/Avocado/raw/main/image/u1fae3_u1f34b.png
// @grant        none
// @license      MIT
// @run-at       document-end
// ==/UserScript==

function walk(node)
{
    var child, next;

    switch ( node.nodeType )
    {
        case 1:  // Element
        case 9:  // Document
        case 11: // Document fragment
            child = node.firstChild;
            while ( child )
            {
                next = child.nextSibling;
                walk(child);
                child = next;
            }
            break;

        case 3: // Text node
            handleText(node);
            break;
    }
}

function handleText(textNode)
{
    var v = textNode.nodeValue;

	v = v.replace("差距居然这么大", "*");
	v = v.replace("不跟风要造风", "*");
	v = v.replace("多维矩阵闭环", "*");
	v = v.replace("打开销售通路", "*");
	v = v.replace("但我大受震撼", "*");
	v = v.replace("大数据分析", "*");
	v = v.replace("大数据杀熟", "*");
	v = v.replace("延迟满足感", "*");
	v = v.replace("地毯式轰炸", "*");
	v = v.replace("男生看了会", "*");
	v = v.replace("女生看了会", "*");
	v = v.replace("战略性亏损", "*");
	v = v.replace("系统性风险", "*");
	v = v.replace("饱和式攻击", "*");
	v = v.replace("四两拨千斤", "*");
	v = v.replace("开辟新路径", "*");
	v = v.replace("建立新习惯", "*");
	v = v.replace("用户无感知", "*");
	v = v.replace("叫好又叫座", "*");
	v = v.replace("优先级很高", "*");
	v = v.replace("拉新成本高", "*");
	v = v.replace("颠覆式创新", "*");
	v = v.replace("连续创业者", "*");
	v = v.replace("投入产出比", "*");
	v = v.replace("互联网思维", "*");
	v = v.replace("互联网红利", "*");
	v = v.replace("国民总时间", "*");
	v = v.replace("最后一公里", "*");
	v = v.replace("海豚湾模式", "*");
	v = v.replace("最大公约数", "*");
	v = v.replace("现象级事件", "*");
	v = v.replace("沉浸式体验", "*");
	v = v.replace("用户忠诚度", "*");
	v = v.replace("病毒式营销", "*");
	v = v.replace("风口上的猪", "*");
	v = v.replace("战略性投资", "*");
	v = v.replace("支棱起来", "*");
	v = v.replace("小步快跑", "*");
	v = v.replace("降维打击", "*");
	v = v.replace("体验度量", "*");
	v = v.replace("躬身入局", "*");
	v = v.replace("顺势而为", "*");
	v = v.replace("打破结界", "*");
	v = v.replace("升维定位", "*");
	v = v.replace("有机结合", "*");
	v = v.replace("起承转合", "*");
	v = v.replace("存量维持", "*");
	v = v.replace("增量博弈", "*");
	v = v.replace("拨冗参会", "*");
	v = v.replace("刻意练习", "*");
	v = v.replace("生命周期", "*");
	v = v.replace("价值转化", "*");
	v = v.replace("强化认知", "*");
	v = v.replace("强化心智", "*");
	v = v.replace("击穿心智", "*");
	v = v.replace("资源倾斜", "*");
	v = v.replace("完善逻辑", "*");
	v = v.replace("结果导向", "*");
	v = v.replace("商业模式", "*");
	v = v.replace("快速响应", "*");
	v = v.replace("垂直领域", "*");
	v = v.replace("定性定量", "*");
	v = v.replace("去中心化", "*");
	v = v.replace("关键路径", "*");
	v = v.replace("去中心化", "*");
	v = v.replace("用户画像", "*");
	v = v.replace("绝境求生", "*");
	v = v.replace("拥抱变化", "*");
	v = v.replace("重新定义", "*");
	v = v.replace("借势营销", "*");
	v = v.replace("内容创业", "*");
	v = v.replace("归因分析", "*");
	v = v.replace("逻辑推理", "*");
	v = v.replace("建立范式", "*");
	v = v.replace("高举高打", "*");
	v = v.replace("高开低走", "*");
	v = v.replace("高台跳水", "*");
	v = v.replace("全情投入", "*");
	v = v.replace("全面封锁", "*");
	v = v.replace("剑走偏锋", "*");
	v = v.replace("业务导向", "*");
	v = v.replace("人力不足", "*");
	v = v.replace("品效合一", "*");
	v = v.replace("全球领先", "*");
	v = v.replace("人无我有", "*");
	v = v.replace("人有我优", "*");
	v = v.replace("人优我变", "*");
	v = v.replace("势如破竹", "*");
	v = v.replace("势不可挡", "*");
	v = v.replace("石破天惊", "*");
	v = v.replace("集团战略", "*");
	v = v.replace("战略引擎", "*");
	v = v.replace("决策路径", "*");
	v = v.replace("天使投资", "*");
	v = v.replace("底层逻辑", "*");
	v = v.replace("顶层设计", "*");
	v = v.replace("饥饿营销", "*");
	v = v.replace("人工智能", "*");
	v = v.replace("赛博朋克", "*");
	v = v.replace("智慧城市", "*");
	v = v.replace("通证经济", "*");
	v = v.replace("中央厨房", "*");
	v = v.replace("先发优势", "*");
	v = v.replace("临门一脚", "*");
	v = v.replace("正态分布", "*");
	v = v.replace("幂律分布", "*");
	v = v.replace("二八定律", "*");
	v = v.replace("叠加效应", "*");
	v = v.replace("马太效应", "*");
	v = v.replace("偏好植入", "*");
	v = v.replace("蚂蚁市场", "*");
	v = v.replace("心动情境", "*");
	v = v.replace("利基市场", "*");
	v = v.replace("第二曲线", "*");
	v = v.replace("可替代性", "*");
	v = v.replace("信息茧房", "*");
	v = v.replace("价格歧视", "*");
	v = v.replace("心理账户", "*");
	v = v.replace("关键时期", "*");
	v = v.replace("最高规制", "*");
	v = v.replace("三位一体", "*");
	v = v.replace("不破不立", "*");
	v = v.replace("用户体验", "*");
	v = v.replace("用户调研", "*");
	v = v.replace("重度用户", "*");
	v = v.replace("沉默用户", "*");
	v = v.replace("用户黏性", "*");
	v = v.replace("千人千面", "*");
	v = v.replace("千人一面", "*");
	v = v.replace("沟通协作", "*");
	v = v.replace("品类战舰", "*");
	v = v.replace("行军路线", "*");
	v = v.replace("产品尖兵", "*");
	v = v.replace("拳头产品", "*");
	v = v.replace("超级符号", "*");
	v = v.replace("时间窗口", "*");
	v = v.replace("战略支点", "*");
	v = v.replace("声音印记", "*");
	v = v.replace("社交货币", "*");
	v = v.replace("神交已久", "*");
	v = v.replace("财务自由", "*");
	v = v.replace("打开率高", "*");
	v = v.replace("看过的都", "*");
	v = v.replace("纷纷表示", "*");
	v = v.replace("借势发酵", "*");
	v = v.replace("开篇预热", "*");
	v = v.replace("插个需求", "*");
	v = v.replace("HRBP", "*");
	v = v.replace("生态化反", "*");
	v = v.replace("本草纲目", "*");
	v = v.replace("对一下", "*");
	v = v.replace("碰一下", "*");
	v = v.replace("小前台", "*");
	v = v.replace("过一下", "*");
	v = v.replace("抢品类", "*");
	v = v.replace("卡认知", "*");
	v = v.replace("占场景", "*");
	v = v.replace("观行业", "*");
	v = v.replace("明竞争", "*");
	v = v.replace("洞自身", "*");
	v = v.replace("开场子", "*");
	v = v.replace("提调子", "*");
	v = v.replace("冷启动", "*");
	v = v.replace("秀肌肉", "*");
	v = v.replace("借东风", "*");
	v = v.replace("断舍离", "*");
	v = v.replace("薅羊毛", "*");
	v = v.replace("砍一刀", "*");
	v = v.replace("走出去", "*");
	v = v.replace("讲故事", "*");
	v = v.replace("扁平化", "*");
	v = v.replace("差异化", "*");
	v = v.replace("平台化", "*");
	v = v.replace("结构化", "*");
	v = v.replace("精细化", "*");
	v = v.replace("短平快", "*");
	v = v.replace("常态化", "*");
	v = v.replace("强依赖", "*");
	v = v.replace("不可控", "*");
	v = v.replace("有风险", "*");
	v = v.replace("护城河", "*");
	v = v.replace("资源位", "*");
	v = v.replace("优先级", "*");
	v = v.replace("制高点", "*");
	v = v.replace("可用性", "*");
	v = v.replace("易用性", "*");
	v = v.replace("稳定性", "*");
	v = v.replace("便捷性", "*");
	v = v.replace("耦合性", "*");
	v = v.replace("一致性", "*");
	v = v.replace("系统性", "*");
	v = v.replace("端到端", "*");
	v = v.replace("点对点", "*");
	v = v.replace("点线面", "*");
	v = v.replace("上半场", "*");
	v = v.replace("下半场", "*");
	v = v.replace("主战场", "*");
	v = v.replace("人货场", "*");
	v = v.replace("基本面", "*");
	v = v.replace("基本盘", "*");
	v = v.replace("操盘手", "*");
	v = v.replace("进化论", "*");
	v = v.replace("解释权", "*");
	v = v.replace("最优解", "*");
	v = v.replace("执行力", "*");
	v = v.replace("驱动力", "*");
	v = v.replace("鄙视链", "*");
	v = v.replace("生态链", "*");
	v = v.replace("生态圈", "*");
	v = v.replace("生态位", "*");
	v = v.replace("全场景", "*");
	v = v.replace("全渠道", "*");
	v = v.replace("全方位", "*");
	v = v.replace("全媒体", "*");
	v = v.replace("流量池", "*");
	v = v.replace("天花板", "*");
	v = v.replace("传话筒", "*");
	v = v.replace("转化率", "*");
	v = v.replace("颗粒感", "*");
	v = v.replace("登云梯", "*");
	v = v.replace("冲击力", "*");
	v = v.replace("视觉锤", "*");
	v = v.replace("孵化器", "*");
	v = v.replace("新零售", "*");
	v = v.replace("新物种", "*");
	v = v.replace("新品牌", "*");
	v = v.replace("新篇章", "*");
	v = v.replace("新局势", "*");
	v = v.replace("新赛道", "*");
	v = v.replace("新势能", "*");
	v = v.replace("新国货", "*");
	v = v.replace("新国潮", "*");
	v = v.replace("新动力", "*");
	v = v.replace("同理心", "*");
	v = v.replace("气氛组", "*");
	v = v.replace("竞争力", "*");
	v = v.replace("存在感", "*");
	v = v.replace("认同感", "*");
	v = v.replace("参与感", "*");
	v = v.replace("归属感", "*");
	v = v.replace("使命感", "*");
	v = v.replace("价值观", "*");
	v = v.replace("忠诚度", "*");
	v = v.replace("预热期", "*");
	v = v.replace("高峰期", "*");
	v = v.replace("高潮期", "*");
	v = v.replace("上升期", "*");
	v = v.replace("瓶颈期", "*");
	v = v.replace("大数据", "*");
	v = v.replace("云计算", "*");
	v = v.replace("区块链", "*");
	v = v.replace("比特币", "*");
	v = v.replace("虚拟币", "*");
	v = v.replace("天使轮", "*");
	v = v.replace("自媒体", "*");
	v = v.replace("新媒体", "*");
	v = v.replace("价格门", "*");
	v = v.replace("超预期", "*");
	v = v.replace("大中台", "*");
	v = v.replace("凝聚力", "*");
	v = v.replace("中国人", "*");
	v = v.replace("小姐姐", "*");
	v = v.replace("小哥哥", "*");
	v = v.replace("向心力", "*");
	v = v.replace("方法论", "*");
	v = v.replace("颗粒度", "*");
	v = v.replace("组合拳", "*");
	v = v.replace("引爆点", "*");
	v = v.replace("点线面", "*");
	v = v.replace("影响力", "*");
	v = v.replace("感知度", "*");
	v = v.replace("接地气", "*");
	v = v.replace("精细化", "*");
	v = v.replace("SPA", "*");
	v = v.replace("期待值", "*");
	v = v.replace("UGC", "*");
	v = v.replace("COE", "*");
	v = v.replace("SDC", "*");
	v = v.replace("自己人", "*");
	v = v.replace("李时珍", "*");
	v = v.replace("外国人", "*");
	v = v.replace("强化", "*");
	v = v.replace("击穿", "*");
	v = v.replace("落地", "*");
	v = v.replace("赋能", "*");
	v = v.replace("共创", "*");
	v = v.replace("共建", "*");
	v = v.replace("分发", "*");
	v = v.replace("支撑", "*");
	v = v.replace("抓手", "*");
	v = v.replace("体感", "*");
	v = v.replace("感知", "*");
	v = v.replace("融合", "*");
	v = v.replace("调性", "*");
	v = v.replace("心智", "*");
	v = v.replace("解耦", "*");
	v = v.replace("拆解", "*");
	v = v.replace("你敢", "*");
	v = v.replace("集成", "*");
	v = v.replace("打法", "*");
	v = v.replace("解法", "*");
	v = v.replace("沉淀", "*");
	v = v.replace("对齐", "*");
	v = v.replace("拉齐", "*");
	v = v.replace("对标", "*");
	v = v.replace("对焦", "*");
	v = v.replace("拉通", "*");
	v = v.replace("打通", "*");
	v = v.replace("打透", "*");
	v = v.replace("吃透", "*");
	v = v.replace("迁移", "*");
	v = v.replace("分层", "*");
	v = v.replace("老公", "*");
	v = v.replace("漏斗", "*");
	v = v.replace("闭环", "*");
	v = v.replace("战役", "*");
	v = v.replace("落盘", "*");
	v = v.replace("老婆", "*");
	v = v.replace("合力", "*");
	v = v.replace("体系", "*");
	v = v.replace("心力", "*");
	v = v.replace("赛道", "*");
	v = v.replace("痛点", "*");
	v = v.replace("履约", "*");
	v = v.replace("串联", "*");
	v = v.replace("链路", "*");
	v = v.replace("纽带", "*");
	v = v.replace("矩阵", "*");
	v = v.replace("协同", "*");
	v = v.replace("反哺", "*");
	v = v.replace("认知", "*");
	v = v.replace("下钻", "*");
	v = v.replace("挖掘", "*");
	v = v.replace("交互", "*");
	v = v.replace("兼容", "*");
	v = v.replace("包装", "*");
	v = v.replace("附能", "*");
	v = v.replace("响应", "*");
	v = v.replace("刺激", "*");
	v = v.replace("规模", "*");
	v = v.replace("重组", "*");
	v = v.replace("量化", "*");
	v = v.replace("宽松", "*");
	v = v.replace("抽离", "*");
	v = v.replace("打法", "*");
	v = v.replace("发力", "*");
	v = v.replace("闭环", "*");
	v = v.replace("布局", "*");
	v = v.replace("联动", "*");
	v = v.replace("场景", "*");
	v = v.replace("痛点", "*");
	v = v.replace("落地", "*");
	v = v.replace("聚焦", "*");
	v = v.replace("跟进", "*");
	v = v.replace("迭代", "*");
	v = v.replace("价值", "*");
	v = v.replace("细分", "*");
	v = v.replace("维度", "*");
	v = v.replace("颗粒", "*");
	v = v.replace("聚焦", "*");
	v = v.replace("梳理", "*");
	v = v.replace("输出", "*");
	v = v.replace("格局", "*");
	v = v.replace("生态", "*");
	v = v.replace("沉淀", "*");
	v = v.replace("话术", "*");
	v = v.replace("体系", "*");
	v = v.replace("对齐", "*");
	v = v.replace("同步", "*");
	v = v.replace("认知", "*");
	v = v.replace("分享", "*");
	v = v.replace("勾兑", "*");
	v = v.replace("流程", "*");
	v = v.replace("加速", "*");
	v = v.replace("打磨", "*");
	v = v.replace("占位", "*");
	v = v.replace("为王", "*");
	v = v.replace("红利", "*");
	v = v.replace("摸索", "*");
	v = v.replace("提炼", "*");
	v = v.replace("玩法", "*");
	v = v.replace("反哺", "*");
	v = v.replace("快速", "*");
	v = v.replace("担当", "*");
	v = v.replace("中台", "*");
	v = v.replace("给到", "*");
	v = v.replace("平台", "*");
	v = v.replace("优化", "*");
	v = v.replace("升级", "*");
	v = v.replace("交付", "*");
	v = v.replace("倒逼", "*");
	v = v.replace("复盘", "*");
	v = v.replace("上升", "*");
	v = v.replace("方案", "*");
	v = v.replace("踩坑", "*");
	v = v.replace("填坑", "*");
	v = v.replace("报备", "*");
	v = v.replace("透传", "*");
	v = v.replace("打平", "*");
	v = v.replace("抹平", "*");
	v = v.replace("重塑", "*");
	v = v.replace("蓄能", "*");
	v = v.replace("引爆", "*");
	v = v.replace("背书", "*");
	v = v.replace("背锅", "*");
	v = v.replace("支持", "*");
	v = v.replace("协调", "*");
	v = v.replace("支援", "*");
	v = v.replace("加持", "*");
	v = v.replace("拉升", "*");
	v = v.replace("洞察", "*");
	v = v.replace("渗透", "*");
	v = v.replace("咬合", "*");
	v = v.replace("穿梭", "*");
	v = v.replace("辐射", "*");
	v = v.replace("扩展", "*");
	v = v.replace("开拓", "*");
	v = v.replace("兜底", "*");
	v = v.replace("降级", "*");
	v = v.replace("容错", "*");
	v = v.replace("容灾", "*");
	v = v.replace("耦合", "*");
	v = v.replace("复用", "*");
	v = v.replace("封装", "*");
	v = v.replace("抽象", "*");
	v = v.replace("聚合", "*");
	v = v.replace("抓包", "*");
	v = v.replace("观察", "*");
	v = v.replace("监控", "*");
	v = v.replace("上报", "*");
	v = v.replace("捕获", "*");
	v = v.replace("回溯", "*");
	v = v.replace("回归", "*");
	v = v.replace("回流", "*");
	v = v.replace("回跳", "*");
	v = v.replace("通晒", "*");
	v = v.replace("死磕", "*");
	v = v.replace("树立", "*");
	v = v.replace("跨界", "*");
	v = v.replace("共情", "*");
	v = v.replace("演绎", "*");
	v = v.replace("画饼", "*");
	v = v.replace("打造", "*");
	v = v.replace("输血", "*");
	v = v.replace("造血", "*");
	v = v.replace("造势", "*");
	v = v.replace("造市", "*");
	v = v.replace("造事", "*");
	v = v.replace("下沉", "*");
	v = v.replace("拉新", "*");
	v = v.replace("转化", "*");
	v = v.replace("留存", "*");
	v = v.replace("促活", "*");
	v = v.replace("付费", "*");
	v = v.replace("营收", "*");
	v = v.replace("盈利", "*");
	v = v.replace("获客", "*");
	v = v.replace("邀请", "*");
	v = v.replace("助力", "*");
	v = v.replace("激励", "*");
	v = v.replace("激活", "*");
	v = v.replace("推广", "*");
	v = v.replace("投放", "*");
	v = v.replace("导流", "*");
	v = v.replace("覆盖", "*");
	v = v.replace("曝光", "*");
	v = v.replace("裂变", "*");
	v = v.replace("增长", "*");
	v = v.replace("优秀", "*");
	v = v.replace("感恩", "*");
	v = v.replace("比心", "*");
	v = v.replace("笔芯", "*");
	v = v.replace("下跪", "*");
	v = v.replace("致敬", "*");
	v = v.replace("订阅", "*");
	v = v.replace("认证", "*");
	v = v.replace("推送", "*");
	v = v.replace("唤醒", "*");
	v = v.replace("流失", "*");
	v = v.replace("召回", "*");
	v = v.replace("授权", "*");
	v = v.replace("接入", "*");
	v = v.replace("铸造", "*");
	v = v.replace("构筑", "*");
	v = v.replace("构建", "*");
	v = v.replace("搭建", "*");
	v = v.replace("组局", "*");
	v = v.replace("摸鱼", "*");
	v = v.replace("划水", "*");
	v = v.replace("众筹", "*");
	v = v.replace("收割", "*");
	v = v.replace("共享", "*");
	v = v.replace("收口", "*");
	v = v.replace("转型", "*");
	v = v.replace("围绕", "*");
	v = v.replace("出击", "*");
	v = v.replace("证言", "*");
	v = v.replace("确认", "*");
	v = v.replace("明确", "*");
	v = v.replace("评估", "*");
	v = v.replace("评审", "*");
	v = v.replace("务实", "*");
	v = v.replace("夯实", "*");
	v = v.replace("预判", "*");
	v = v.replace("预言", "*");
	v = v.replace("变迁", "*");
	v = v.replace("返佣", "*");
	v = v.replace("深入", "*");
	v = v.replace("攻坚", "*");
	v = v.replace("破冰", "*");
	v = v.replace("破题", "*");
	v = v.replace("解题", "*");
	v = v.replace("破圈", "*");
	v = v.replace("破局", "*");
	v = v.replace("定量", "*");
	v = v.replace("定性", "*");
	v = v.replace("制约", "*");
	v = v.replace("约束", "*");
	v = v.replace("触及", "*");
	v = v.replace("触达", "*");
	v = v.replace("触发", "*");
	v = v.replace("操盘", "*");
	v = v.replace("思考", "*");
	v = v.replace("反思", "*");
	v = v.replace("精简", "*");
	v = v.replace("深耕", "*");
	v = v.replace("突围", "*");
	v = v.replace("补位", "*");
	v = v.replace("进化", "*");
	v = v.replace("进军", "*");
	v = v.replace("起飞", "*");
	v = v.replace("皮实", "*");
	v = v.replace("本分", "*");
	v = v.replace("重磅", "*");
	v = v.replace("垂直", "*");
	v = v.replace("真香", "*");
	v = v.replace("自洽", "*");
	v = v.replace("精准", "*");
	v = v.replace("持续", "*");
	v = v.replace("灵活", "*");
	v = v.replace("稳定", "*");
	v = v.replace("可控", "*");
	v = v.replace("活跃", "*");
	v = v.replace("风口", "*");
	v = v.replace("渠道", "*");
	v = v.replace("入口", "*");
	v = v.replace("形态", "*");
	v = v.replace("基石", "*");
	v = v.replace("基因", "*");
	v = v.replace("因子", "*");
	v = v.replace("模型", "*");
	v = v.replace("通道", "*");
	v = v.replace("水位", "*");
	v = v.replace("水准", "*");
	v = v.replace("姿态", "*");
	v = v.replace("卡点", "*");
	v = v.replace("卡位", "*");
	v = v.replace("头部", "*");
	v = v.replace("腰部", "*");
	v = v.replace("踝部", "*");
	v = v.replace("爽点", "*");
	v = v.replace("痒点", "*");
	v = v.replace("全域", "*");
	v = v.replace("公域", "*");
	v = v.replace("私域", "*");
	v = v.replace("本我", "*");
	v = v.replace("自我", "*");
	v = v.replace("超我", "*");
	v = v.replace("蓝海", "*");
	v = v.replace("红海", "*");
	v = v.replace("纵向", "*");
	v = v.replace("横向", "*");
	v = v.replace("上限", "*");
	v = v.replace("下限", "*");
	v = v.replace("上游", "*");
	v = v.replace("下游", "*");
	v = v.replace("阈值", "*");
	v = v.replace("场域", "*");
	v = v.replace("架构", "*");
	v = v.replace("系统", "*");
	v = v.replace("标配", "*");
	v = v.replace("长尾", "*");
	v = v.replace("态势", "*");
	v = v.replace("锚点", "*");
	v = v.replace("标杆", "*");
	v = v.replace("壁垒", "*");
	v = v.replace("变量", "*");
	v = v.replace("期权", "*");
	v = v.replace("边界", "*");
	v = v.replace("品牌", "*");
	v = v.replace("阵地", "*");
	v = v.replace("高地", "*");
	v = v.replace("洼地", "*");
	v = v.replace("高空", "*");
	v = v.replace("革命", "*");
	v = v.replace("变革", "*");
	v = v.replace("内卷", "*");
	v = v.replace("外包", "*");
	v = v.replace("福报", "*");
	v = v.replace("脑暴", "*");
	v = v.replace("脑洞", "*");
	v = v.replace("圈层", "*");
	v = v.replace("层级", "*");
	v = v.replace("段位", "*");
	v = v.replace("环节", "*");
	v = v.replace("困局", "*");
	v = v.replace("文案", "*");
	v = v.replace("议程", "*");
	v = v.replace("公关", "*");
	v = v.replace("配称", "*");
	v = v.replace("力场", "*");
	v = v.replace("魔方", "*");
	v = v.replace("触点", "*");
	v = v.replace("势能", "*");
	v = v.replace("流量", "*");
	v = v.replace("资源", "*");
	v = v.replace("排期", "*");
	v = v.replace("延期", "*");
	v = v.replace("弹窗", "*");
	v = v.replace("浮层", "*");
	v = v.replace("引导", "*");
	v = v.replace("蒙层", "*");
	v = v.replace("幕帘", "*");
	v = v.replace("遮罩", "*");
	v = v.replace("埋点", "*");
	v = v.replace("坑位", "*");
	v = v.replace("楼层", "*");
	v = v.replace("按钮", "*");
	v = v.replace("推送", "*");
	v = v.replace("红包", "*");
	v = v.replace("峰值", "*");
	v = v.replace("漏洞", "*");
	v = v.replace("风险", "*");
	v = v.replace("瓶颈", "*");
	v = v.replace("策略", "*");
	v = v.replace("成本", "*");
	v = v.replace("复利", "*");
	v = v.replace("人性", "*");
	v = v.replace("利器", "*");
	v = v.replace("玩家", "*");
	v = v.replace("小白", "*");
	v = v.replace("韭菜", "*");
	v = v.replace("置换", "*");
	v = v.replace("羊毛", "*");
	v = v.replace("福利", "*");
	v = v.replace("套路", "*");
	v = v.replace("情怀", "*");
	v = v.replace("标准", "*");
	v = v.replace("规范", "*");
	v = v.replace("报备", "*");
	v = v.replace("社群", "*");
	v = v.replace("产业", "*");
	v = v.replace("载体", "*");
	v = v.replace("服务", "*");
	v = v.replace("粘性", "*");
	v = v.replace("属性", "*");
	v = v.replace("地域", "*");
	v = v.replace("终端", "*");
	v = v.replace("版本", "*");
	v = v.replace("口碑", "*");
	v = v.replace("指标", "*");
	v = v.replace("年框", "*");
	v = v.replace("试点", "*");
	v = v.replace("母体", "*");
	v = v.replace("空白", "*");
	v = v.replace("银弹", "*");
	v = v.replace("忠诚", "*");
	v = v.replace("使命", "*");
	v = v.replace("打破", "*");
	v = v.replace("占领", "*");
	v = v.replace("作战", "*");
	v = v.replace("弹射", "*");
	v = v.replace("战略", "*");
	v = v.replace("模式", "*");
	v = v.replace("行业", "*");
	v = v.replace("市场", "*");
	v = v.replace("消费", "*");
	v = v.replace("知识", "*");
	v = v.replace("经济", "*");
	v = v.replace("定律", "*");
	v = v.replace("理论", "*");
	v = v.replace("沉没", "*");
	v = v.replace("边际", "*");
	v = v.replace("机会", "*");
	v = v.replace("市场", "*");
	v = v.replace("集群", "*");
	v = v.replace("优势", "*");
	v = v.replace("颠覆", "*");
	v = v.replace("意识", "*");
	v = v.replace("情绪", "*");
	v = v.replace("G点", "*");
	v = v.replace("航母", "*");
	v = v.replace("用户", "*");
	v = v.replace("支点", "*");
	v = v.replace("男人", "*");
	v = v.replace("女人", "*");
	v = v.replace("网友", "*");
	v = v.replace("古人", "*");
	v = v.replace("干货", "*");
	v = v.replace("高优", "*");
	v = v.replace("体验", "*");
	v = v.replace("创新", "*");
	v = v.replace("数据", "*");
	v = v.replace("回顾", "*");
	v = v.replace("降维", "*");
	v = v.replace("沉浸", "*");
	v = v.replace("撬动", "*");
	v = v.replace("盘活", "*");
	v = v.replace("整合", "*");
	v = v.replace("路径", "*");
	v = v.replace("抓住", "*");
	v = v.replace("顶层", "*");
	v = v.replace("化反", "*");
	v = v.replace("基建", "*");
	v = v.replace("男生", "*");
	v = v.replace("老外", "*");
	v = v.replace("躺平", "*");
	v = v.replace("破防", "*");
	v = v.replace("深", "*");
	v = v.replace("期", "*");
	v = v.replace("率", "*");
	v = v.replace("度", "*");
	
	textNode.nodeValue = v;
}

walk(document.body);




new MutationObserver(function() {
    walk(document.body);
}).observe(document.body, {
    childList: true
});