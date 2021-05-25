import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
import email.utils
import datetime

def getnowdatetime():
    dtm_now = datetime.datetime.now()
    return dtm_now.strftime('%Y年%m月%d日 %H時%M分')

id = "rpa_001"
_programname = "電子申請ダウンロード"
commonmessage = "0件中0件ダウンロードしました。（検索結果500件以上はカウントしていません。）ダウンロード結果は「C:\\Users\kreis1g-tpc-029\Desktop\穆作業\教育カリキュラム」フォルダに格納してあります。（ファイル名:「送信案件一覧.xlsx」）"
#errormessage = "%USERNAME%へのリモート接続はされているが何らかの理由で設定ファイルにて指定されたフォルダにアクセスできない為、異常終了しました。ダウンロード件数は$totalDownloadCompletedCount$件でした、「C:\\Users\%USERNAME%\_電子申請一時保存」テンポラリフォルダにダウンロードファイルを格納しました。"
errormessage = "予期せぬエラーが発生しため、開いたエクセルを閉じ、ログインした社労夢システムを閉じ、再度実行してください。"
f = open(r'C:\Users\kreis1g-tpc-029\Desktop\ワーニングメモ.txt', 'r', encoding='UTF-8')
warningmessage = f.read()
f.close()
from_address = "shinrei-boku@kreis-inc.jp"
my_password = "shinrei0406"
to_address = email.utils.formataddr(('boku', "shinrei-boku@kreis-inc.jp"))
cc = "shinrei-boku@kreis-inc.jp"
subject = "電子申請ダウンロード自動実行結果"
#body = "ID= {0} , {1} が、{2} に異常終了しました。:collision:".format(id,_programname,getnowdatetime())
body = ":scream:事業所長BOTからRPAクラウド維持管理者へ　\n" \
        "ID= {0} , {1} が、{2} に異常終了しました。:collision:".format(id,_programname,getnowdatetime()) +  \
        "対応してください　:sob:\n" \
        "\nダウンロード件数：\n{0}\n".format(commonmessage) + \
        "\n異常終了の原因：\n{0}\n".format(errormessage) +  \
        "\nワーニング： \n{0}".format(warningmessage)
print(body)

def create_message(from_addr,to_addr,cc_addr,subj,bod):
    #msg = MIMEText(bod,"html/text/plain","utf-8")
    msg = MIMEMultipart()
    msg['Subject'] = subj
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Cc'] = cc_addr
    msg.attach(MIMEText(bod))
    #commont = ""
    # ファイルを添付
    
    if (len(commonmessage) == 0) or ("0件ダウンロード" in commonmessage):
        print("no attach")
        return msg
    else:
        path_start = commonmessage.find("「C:")
        _path_start = path_start + 1
        path_end = commonmessage.find("」フォルダに格納")
        path = commonmessage[_path_start:path_end] + "\python.txt"
        print(path)
        #path = r"C:\Users\kreis1g-tpc-029\Desktop\穆作業\教育カリキュラム\python.txt"
        with open(path, "rb") as f:
            part = MIMEApplication(f.read(),Name=basename(path))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
        msg.attach(part)
        return msg

def send(from_addr,to_addr,msg):
    smtpobj = smtplib.SMTP('smtp.kreis-inc.jp',25)
    ##smtpobj.ehlo()
    ##smtpobj.starttls()
    ##smtpobj.ehlo()
    smtpobj.login(from_address,my_password)
    #smtpobj.sendmail(from_addr,to_addr,msg.as_string())
    smtpobj.send_message(msg)
    smtpobj.close()
    #smtpobj.quit()

if __name__ == '__main__':
    to_addr = to_address
    subj =subject
    bod = body

    msg = create_message(from_address,to_addr,cc,subj,bod)
    send(from_address,to_addr,msg)
