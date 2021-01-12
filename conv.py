import jinja2
import sys



# M2
# 修士審査用論文提出：2月1日(月)17:00　化学科事務室に４部提出
# 修士論文題目・要旨提出：2月5日(金)12:00　化学科HP予稿投稿フォームから提出
# 修士論文審査会：2月16日（火）、17日（水）　第9講義室
# 修士論文最終版提出：3月5日(金)17:00　化学科事務室に１部提出
#
# B4
# 卒業研究発表題目・要旨提出：2月22日(月)12:00　化学科HP予稿投稿フォームから提出
# 卒業研究発表会：3月3日(水)　第21講義室
#
# M1 中間発表会
# ・teams を用いてオンデマンド方式で発表会をおこなう。
# ・発表者は 7 分の動画を作成し、teams にアップロードする。
# ・質疑応答は teams に書き込むことでおこなう。
# ・開催期間は 3/4 (木)～3/10 (水) の 1 週間とする。
# ・教員は 3/9 (火) の 17:00 までに質問を完了する。
# ・発表者は 3/10 (水) の 17:00 までに質問に対する回答をおこなう。
# ・中間発表題目・要旨提出：2月24日(水)12:00　化学科HP予稿投稿フォームから提出

y = "2021"

with open(sys.argv[1]) as file_:
    template = jinja2.Template(file_.read())
digested = template.render(
    title_ja = f"{y}年春の化学科学士，博士前期課程（修士）の発表会・審査会について",
    title_en = f"Final Presentation Requirements {y} Spring",
    safeurl  = f"finalpresentation{y}spring.html",

    m2paperdl = f"{y}年2月1日(月)17:00",             # 修士審査用論文提出
    m2abstdl  = f"{y}年2月5日(金)12:00",             # 修士論文題目・要旨提出
    m2defencedays = f"{y}年2月16日（火）、17日（水）",    # 修士論文審査会
    m2finaldl = f"{y}年3月5日(金)17:00",                  # 修士論文提出最終版提出
    m2defenceloc = "第9講義室",

    b4abstdl = f"{y}年2月22日(月)12:00",             # 卒業論文題目・要旨提出
    b4confday   = f"{y}年3月3日(水)",                # 発表会
    b4confloc = "第21講義室",

    m1abstdl = f"{y}年2月24日(水)12:00",
    m1posterday = f"{y}年3月4日(木)～10日(水)",
    m1posterloc = "Microsoft Teamsを用いたオンデマンド方式",

    cgi        = "http://www.chem.okayama-u.ac.jp/cgi-bin/reg2.cgi",
)

if len(sys.argv) > 2:
    with open(sys.argv[2], "w") as f:
        f.write(digested)
else:
    print(digested)
