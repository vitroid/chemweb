import jinja2
import sys

with open(sys.argv[1]) as file_:
    template = jinja2.Template(file_.read())
digested = template.render(
    title_ja = "2020年春の化学科学士，博士前期課程（修士）の発表会・審査会について",
    title_en = "Final Presentation Requirements 2020 Spring",
    safeurl = "finalpresentation2020spring.html",

    m2paperdl = "2020年2月3日(月)17:00",             # 修士審査用論文提出
    m2abstdl  = "2020年2月7日(金)12:00",             # 修士論文題目・要旨提出
    m2defencedays = "2020年2月17日(月), 18日(火)",    # 修士論文審査会
    m2finaldl = "3月5日(木) 17:00",                  # 修士論文提出最終版提出
    m2defenceloc = "第21講義室",

    b4abstdl = "2020年2月19日(水)12:00",             # 卒業論文題目・要旨提出
    b4confday   = "2020年3月2日(月)",                # 発表会
    b4confloc = "第21講義室",

    m1abstdl = "2020年2月20日(木)12:00",
    m1posterday = "2020年3月6日(金)",
    m1posterloc = "大学院自然科学研究科棟２F大会議室　(工学部と合同)",
)

if len(sys.argv) > 2:
    with open(sys.argv[2], "w") as f:
        f.write(digested)
else:
    print(digested)
