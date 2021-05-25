import math
import datetime
from os import path

def getnowdatetime():
    dtm_now = datetime.datetime.now()
    return dtm_now.strftime('%Y年%m月%d日 %H時%M分')

result = math.sqrt(25)
print(result)
#print(help(result))

s = "12件中3件ダウンロードしました。"
print("0件" not in s)

#commonmessage = "4件中4件ダウンロードしました。（検索結果500件以上はカウントしていません。）ダウンロード結果は「C:\\Users\rpa_001\Desktop\社労夢実行フォルダ\電子申請ダウンロード\実行結果\20210520_132248」フォルダに格納してあります。（ファイル名:「送信案件一覧.xlsx」）"
commonmessage ="4件中4件ダウンロードしました。"
id = "rpa_001"
_programname = "電子申請ダウンロード"
_commonmessage = "4件中4件ダウンロードしました。"
#title =":smile::thumbsup:  事業所長BOTからRPAクラウド維持管理者へ　\n" \
#       "ID= {0} , {1} が、{2} に正常終了しました。".format(id,_programname,getnowdatetime()) +  \
#        " \n{0}".format(commonmessage) +  \
#       " \n Hava a nice day :wave:"
errormessage = "%USERNAME%へのリモート接続はされているが何らかの理由で設定ファイルにて指定されたフォルダにアクセスできない為、異常終了しました。ダウンロード件数は$totalDownloadCompletedCount$件でした、「C:\\Users\%USERNAME%\_電子申請一時保存」テンポラリフォルダにダウンロードファイルを格納しました。"
f = open(r'C:\Users\kreis1g-tpc-029\Desktop\ワーニングメモ.txt', 'r', encoding='UTF-8')
warningmessage = f.read()
f.close()
#warningmessage = "2021/05/01～2021/05/17期間、2021/05/05～2021/05/21期間、2021/05/06～2021/05/22期間に排他制御が発生し更新できませんでした。再度実行してください。" \
#+ "\n 2021/03/04～2021/03/07期間、2021/05/02～2021/05/18期間、2021/05/04～2021/05/20期間の検索結果が500件以上があったため更新できないレコードがあります。検索条件を見直し再度実行してください。" \
#+ "\n 奥野友美2021/03/04～2021/03/07期間、國分真貴子2021/03/04～2021/03/07期間、2021/05/03～2021/05/19期間、2021/05/07～2021/05/23期間の検索結果が500件以上があったためダウンロードできないレコードがあります。検索条件を見直し再度実行してください。"
title = ":scream:事業所長BOTからRPAクラウド維持管理者へ　\n" \
        "ID= {0} , {1} が、{2} に異常終了しました。:collision:".format(id,_programname,getnowdatetime()) +  \
        "対応してください　:sob:" \
        " \n {0}".format(commonmessage) +  \
        " \n {0}".format(errormessage) +  \
        " \n {0}".format(warningmessage)
     #   "対応してください　:sob:"
print(title)

#path1 = r"C:\Users\kreis1g-tpc-029\Desktop"
#path = path1 + "\ワーニングメモ.txt"
#print(path)



#f = open(r'C:\Users\kreis1g-tpc-029\Desktop\ワーニングメモ.txt', 'r', encoding='UTF-8')
#data = f.read()
#print(data)
#f.close()

w = "python"
print(w[0:2])
print(w[:2])
print(w[2:])
print(len(w))

import smtplib


smtpobj = smtplib.SMTP('smtp.kreis-inc.jp',25)
#smtpobj = smtplib.SMTP('smtp.gmail.com',587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login("shinrei-boku@kreis-inc.jp","shinrei0406")
if smtpobj.has_extn('STARTTLS'):
    print("tt")
#smtpobj.login("zhenling54@gmail.com","Dawa$1023")

common = "4件中4件ダウンロードしました。（検索結果500件以上はカウントしていません。）ダウンロード結果は「C:\\Users\\kreis1g-tpc-029\\Desktop\\穆作業\\教育カリキュラム」フォルダに格納してあります。（ファイル名:「送信案件一覧.xlsx」）"
#common ="4件中4件ダウンロードしました"
path_start = common.find("「C:")
_path_start = path_start + 1
path_end = common.find("」フォルダに格納")
path = common[_path_start:path_end] + "\python.txt"
print(path)
print(common[6:11])
print(path_start)
print(_path_start)
print(path_end)