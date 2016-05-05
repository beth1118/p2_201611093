populations=tuple()
population=[(74425, 76326), (61164, 61636),(109688, 115744), (144796, 146776), (174996, 181676), (177841, 177434), (204630, 205980), (223373, 232245), (161055, 166130), (171576, 176735),(279169, 293772),(239450, 251066), (148690, 156510), (182977, 196992), (237792, 242641), (283869, 296762), (209344, 210282), (118965, 114441), (186503, 186856), (195734, 203014), (254381, 249472), (212401, 229111), (271654, 295354), (319197, 335045), (229829, 231671)]
Msum=0
Wsum=0
Maverage=0
Waverage=0
for a in population:
 Msum+= a[0]
 Wsum+= a[1]
print "man total:", Msum
print "woman total:", Wsum

Maverage= Msum/len(population)
Waverage= Wsum/len(population)

print "man average:", Maverage
print "woman average:", Waverage

Gupop=list()
for b in population:
 Gupop.append(b[0]+b[1])
Localname={'Jongno-gu':Gupop[0],'Jung-gu':Gupop[1],'Yongsan-gu':Gupop[2],'Seongdong-gu':Gupop[3],'Gwangjin-gu':Gupop[4],'Dongdaemun-gu':Gupop[5],'Jungnang-gu':Gupop[6],'Seongbuk-gu':Gupop[7],'Gangbuk-gu':Gupop[8],'Dobong-gu':Gupop[9],'Nowon-gu':Gupop[10],'Eunpyeong-gu':Gupop[11],'Seodaemun-gu':Gupop[12],'Mapo-gu':Gupop[13],'Yangcheon-gu':Gupop[14],'Gangseo-gu':Gupop[15],'Guro-gu':Gupop[16],'Geumcheon-gu':Gupop[17],'Yeongdeungpo-gu':Gupop[18],'Dongjak-gu':Gupop[19],'Gwanak-gu':Gupop[20],'Seocho-gu':Gupop[21],'Gangnam-gu':Gupop[22],'Songpa-gu':Gupop[23],'Gangdong-gu':Gupop[24]}
print ""
print "Population by region"
print ""
print Localname 
import matplotlib 
import matplotlib.pyplot as plt
plt.bar(range(0,len(Localname)),Localname.values(), align='center')
plt.xticks(range(0,len(Localname)),list(Localname.keys()))
plt.show()
input()