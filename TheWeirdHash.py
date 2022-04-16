from random import *
import json


# The Weird Hash is going to be used to store the user's password in a high secured level that can't be decrypted(hopefully haha)

class TWH:
    def __init__(self):
        self.sample1 = 'ℵℶℷℸהוזחטיךכלםמןנסעףפץצקרשתŖǷǀǁǂǃǅǅǅǈǈǈǋǋǋǍǍǏǏǑǑǓǓǕǕǗǗǙǙǛǛƎǞǞǠǠǢǢǤǤǦǦǨǨǪǪǬǬǮǮǰǲǲǲǴ' \
                       'ǴǶɺɻɼⱤɾɿƦʁꟅƩʄʅʆꞱƮɄƱƲɅʍʎʏʐʑƷʓʔʕʖʗʘʙʚʛʜꞲꞰʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯΆ·ΈΉΊΌΎΏΐΡΣΣΤΚǷǸǸǺ' \
                       'ǺǼǼǾǾȀȀȂȂȄȄȆȆȈȈȊȊȌȌȎȎȐȐȒȒȔȔȖȖȘȘȚȚȜȜȞȞȠȡȢȢȤȤȦȦȨȨȪȪ' \
                       'ȬȬȮȮȰȰȲȲȴȵȶȷȸȹȺȻȻȽȾⱾⱿɁɁɃɄɅɆɆɈɈɊɊɌɌɎɎⱯⱭⱰƁƆɕƉƊɘƏɚƐꞫɝɞ' \
                       'ɟƓꞬɢƔɤꞍꞪɧƗƖꞮⱢꞭɭɮƜɰⱮƝɳɴƟɶɷɸɹΧΨΩΪΫΦ'

        self.sample2 = '❏❐❑❒▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐░▒▓▔▕▖▗▘▙▚▛▜' \
                       '▝▞▟■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯☰☱☲☳☴☵☶☷'

        self.sample3 = '〆一个女®×ロ卍요๏「」冬れ米・气Ð廴ゞ๔Ł⦇⦈王丶レ彡私Ø' \
                       '么刁۝ジ多卄神丨ｱム『』ॐズ【】٭シ연〖〗《ツ帝文×Īlī刁' \
                       'ΧΠΔΗΝΧΠΤΞΕΗΦΛΩΒΚΜΓΑΓΨΑΣΘΝΨΙΜΥΛΖΕΚΙΦΡΣΞΖΩΒΥΘΡΔΟΟΣ'

        self.sample4 = '⥳⥡⤞⤶⤖⤡⤷⥸⤬⤑⥂⤩⤌⤕⤎⇻⤍⥪⥒⥧⤢⥙⤫⥴⤥⥥⤦⥻⥤⤝⥵⥮⤔⤨⟹⥈⥕⤤⥝⥲⤅⤁⥭⥞' \
                       '⥫⤈⤂⤟⟿⥜⥠⤭⥰⤧⤐⤗⟴⤰⤠⤏⥩⥖⥊⥹⥆⥺⥢⥌⥣⥉⥛⟸⤱⥎⥏⥗⤲⥃⟺' \
                       '⥟⤘⤳⥐⥨⤣⤪⤯⤉⥘⥔⥚⥷⥦⥄⤮⤀⥅⇼⥓⥯⥱⥇⥍⥋⥑⥶'

        self.sample5 = '✶❃❊✩✺✫×✰❈✮✼✵✪✷❁❆✤❋✹✾✳✣❉⁑⁎✭✧✬❇★❄✲✱✡✢' \
                       '〔〕︸﹛﹜︽﹙﹚〖〗『』﹂（）︵「」︶‹›【】﹃︻⟨⟩｛｝〱︾〈〉﹤﹥﹄︼︷«»︹﹝' \
                       '﹞︺︿〚 〛﹁＜ ＞﹀〘 〙《 》❀✦✴৳₤₪₭¤₢﷼₥₴₡₱₨€₵฿₠£௹¥$¢₰৲₮₫₳₲₩₣៛₦Ƒ₧￥₯'

        self.sample6 = '㊛㊞㊥㊖㊭㊋㊏㊝㊍㊩㊣㊫㊐㊟㊦㊘㊤㊚㊨㊢㊌㊮㊑㊠㊕㊧㊓㊬㊎㊗㊰㊒㊊㊡㊪㊔' \
                       'ㅧㅢㅛㄳㅃㅻㅾㅲㅄㆄㅚㅥㅎㆂㅆㄾㅮㅅㅈㅁㄺㅙㅠㅓㅦㅟㄸㅐㅷㄲㅉㅳㅼㆆㅜㆃㄽㅺㅸㆊㅖㆅㅽㅊㅩㅋㅏ' \
                       'ㅘㄶㄵㅴㅔㅞㄱㅶㅬㅌㅫㅑㅯㄷㄿㅝㆀㆈㅪㅗㅨㅀㄼㄹㅹㅍㆇㅕㆁㅰㅵㅂㅇㅒㅱㅿㄴㅭㅡㄻㆉ'


    def create_hash(self, passwd=str):
        ### step #1 ###
        """this is mainly used to store passwords as hash"""
        alpha_hash = {}
        hash0 = ''
        password = [x for x in passwd]
        password.append(passwd[-1])


        if len(passwd) < 8:
            raise 'can\' be less than 8 characters'
        else:
            for index in range(len(password)):
                try:
                    allSamples = self.sample1 + self.sample2 + self.sample3 + self.sample4 + self.sample5 + self.sample6

                    alpha_hash[password[index]] = ''.join(sample(allSamples, 6))

                except:
                    continue
            for index in range(len(password)):
                hash0 = hash0 + alpha_hash[password[index]]
            return hash0, alpha_hash




    def mask_hash(self, hash0=str):
        ### step #2 ###
        lengh = len(hash0)
        l = []
        array = []
        process = []
        for nums in range(lengh):
            l.append(int(randint(0, 100) / 8))

        for c in range(lengh):
            process.append(l[:3])
            del l[:3]

        for values in process:
            if values == []:
                del values
            else:
                array.append(values)

        d = {}
        d[hash0] = array
        return d

    def decodeHash(self, hash_=str, dict_=dict):
        decodedPassword = ''
        process = ''
        indexes = []
        decodedAlpha = {}

        for key, value in dict_.items():
            decodedAlpha[value] = key

        for num in range(0, len(hash_), 6):
            indexes.append(num)
            """ [0, 6]
                [0, 6, 12]
                [0, 6, 12, 18]
                [0, 6, 12, 18, 24]
                [0, 6, 12, 18, 24, 30]
                [0, 6, 12, 18, 24, 30, 36]
                [0, 6, 12, 18, 24, 30, 36, 42]
                [0, 6, 12, 18, 24, 30, 36, 42, 48]
                [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]"""

        for i in indexes:
            process += hash_[i - 6:i] + ' '


        for symbols in process.split():
            decodedPassword += decodedAlpha[symbols]
        return decodedPassword



    def store_hash(self, hash_=str, decoder=dict):
        with open('ghash.json', 'w') as f:
            dump = json.dump([hash_,decoder], f)
    def load_hash(self, file=str):
        with open(file, 'r') as f:
            load = json.load(f)
            return load[0], load[1]

