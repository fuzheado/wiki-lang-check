# Lead Consistency Report: Wikimania

**Ideal sentence:** "Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wikimedia Foundation."
**Run:** Wikimania_run005_results.json
**Date:** 2026-06-12 14:40 UTC

**Total languages checked:** 94
**Successful fetches:** 90
**Not found/error:** 4

## Scoring Method

Each language's lead section is scored using a **combined metric**:

- **Best-sentence match (70% weight):** The ideal sentence is compared against every individual sentence in the lead. The highest similarity is retained. This captures whether *any* sentence in the lead conveys the core idea.
- **Lead-section match (30% weight):** The ideal sentence is compared against the combined first 3 sentences of the lead. This captures how well the *overall* lead aligns at the paragraph level.

Using a multilingual sentence transformer (`distiluse-base-multilingual-cased-v2`), semantic similarity is computed as cosine similarity between embeddings.

## Quick Summary

The ideal sentence has **two key clauses**:
1. "annual conference of the Wikimedia movement"
2. "organized by the community of contributors and hosted by the Wikimedia Foundation"

The combined score (0–1 scale) measures how closely each language's lead conveys both ideas.

## Key Findings

1. **Top performers:** Wikimania (en, 0.91), Wikimanía (es, 0.88), Wikimania (an, 0.85) — these languages closely match the ideal sentence.
2. **English (en)** ranks **#1** with a combined score of 0.9147 (best-sentence: 0.9846, lead-section: 0.7515).
3. **Distribution:** 4 languages high (≥0.80), 10 moderate (0.70–0.79), 44 fair (0.50–0.69), 32 low (<0.50).
4. **Common divergence pattern:** Many languages frame the article subject differently from the ideal, often shifting emphasis from community agency to institutional framing.

## Overall Statistics

| Metric | Value |
|--------|-------|
| Mean combined score | 0.5098 |
| Median combined score | 0.5641 |
| Standard deviation | 0.2267 |
| Min score | -0.0328 |
| Max score | 0.9147 |
| Languages ≥ 0.80 | 4 / 90 (4.4%) |
| Languages ≥ 0.90 | 1 / 90 (1.1%) |

## Similarity Distribution

```
  0.90–1.00      | █                                        |  1 (  1.1%)
  0.80–0.89      | ████                                     |  3 (  3.3%)
  0.70–0.79      | ██████████████                           | 10 ( 11.1%)
  0.60–0.69      | ████████████████████████████████████████ | 27 ( 30.0%)
  0.50–0.59      | █████████████████████████                | 17 ( 18.9%)
  0.00–0.49      | █████████████████████████████████████    | 25 ( 27.8%)
  <0.00          | ██████████                               |  7 (  7.8%)
```

## All Languages (sorted by combined score)

| # | Article | Code | Combined | Best-Sent | Lead-Sect | Original snippet | → English translation |
|---|---------|------|----------|-----------|-----------|-----------------|----------------------|
| 1 | Wikimania | **en** | 0.9147 | 0.9846 | 0.7515 | Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wi... | (English — original) |
| 2 | Wikimanía | es | 0.8754 | 0.9253 | 0.7591 | Wikimania es la conferencia anual del movimiento Wikimedia, organizada por voluntarios y patrocinada por la Fundación Wi... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Fou... |
| 3 | Wikimania | an | 0.8480 | 0.8867 | 0.7579 | Wikimania ye la conferencia anyal d'o movimiento Wikimedia, organizada per voluntarios y auspiciada per a Fundación Wiki... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Fou... |
| 4 | Βικιμάνια | el | 0.8340 | 0.8671 | 0.7568 | Το Βικιμάνια είναι το ετήσιο συνέδριο του κινήματος Wikimedia, που διοργανώνεται από εθελοντές και φιλοξενείται από το Ί... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and hosted by the Wikimedia Founda... |
| 5 | Wikimania | nl | 0.7739 | 0.8097 | 0.6904 | Wikimania is een jaarlijkse conferentie voor gebruikers van de wikiprojecten die zijn opgezet door de Wikimedia Foundati... | Wikimania is an annual conference for users of the wiki projects created by the Wikimedia Foundation |
| 6 | Wikimania | sl | 0.7555 | 0.7555 | 0.7555 | Wikimania je letna konferenca za uporabnike projektov Wiki, ki jih koordinira Fundacija Wikimedia | Wikimania is an annual conference for users of Wiki projects coordinated by the Wikimedia Foundation |
| 7 | Wikimania | sq | 0.7498 | 0.7580 | 0.7305 | Wikimania është një konferencë ndërkombëtare vjetore për përdoruesit e projekteve wiki të cilat mbikëqyren nga Fondacion... | Wikimania is an annual international conference for users of wiki projects overseen by the Wikimedia Foundation |
| 8 | Wikimania | sv | 0.7399 | 0.7565 | 0.7013 | Wikimania är en internationell konferens som Wikimedia Foundation sedan 2005 årligen har organiserat på olika platser, i... | Wikimania is an international conference that the Wikimedia Foundation has organized annually since 2005 in various loca... |
| 9 | Wikimania | vi | 0.7364 | 0.7970 | 0.5950 | Wikimania là tên gọi của hội nghị quốc tế thường niên được Wikimedia Foundation tổ chức | Wikimania is the name of the annual international conference organized by the Wikimedia Foundation |
| 10 | Wikimánia | hu | 0.7314 | 0.7338 | 0.7257 | A Wikimánia (Wikimedia International Conference) a wikiprojektek szerkesztőinek megrendezett évenkénti konferencia, mely... | Wikimania (Wikimedia International Conference) is an annual conference organized by the Wikimedia Foundation for editors... |
| 11 | Wikimania | ro | 0.7181 | 0.7397 | 0.6678 | Wikimania este conferința anuală oficială a Fundației Wikimedia, care se organizează anual din anul 2005, în diferite lo... | Wikimania is the official annual conference of the Wikimedia Foundation, held annually since 2005 in various locations |
| 12 | Уикимания | bg | 0.7146 | 0.7578 | 0.6137 | Уикимания (Wikimania) е официалната ежегодна конференция на Фондация Уикимедия | Wikimania is the official annual conference of the Wikimedia Foundation |
| 13 | Wikimania | cs | 0.7139 | 0.7139 | 0.7139 | Wikimania je konference uživatelů wiki projektů spravovaných nadací Wikimedia Foundation | Wikimania is a conference of users of wiki projects managed by the Wikimedia Foundation |
| 14 | Wikimania | sk | 0.7010 | 0.7581 | 0.5677 | Wikimania je každoročná medzinárodná konferencia pre participantov wikiprojektov nadácie Wikimedia Foundation | Wikimania is an annual international conference for participants of wikiprojects of the Wikimedia Foundation |
| 15 | Wikimania | fr | 0.6935 | 0.6807 | 0.7233 | Wikimania ou la Wikimania est la principale conférence organisée par la fondation Wikimédia à partir de 2005 | Wikimania or Wikimania is the main conference organized by the Wikimedia foundation from 2005 |
| 16 | ویکی مینیا | ur | 0.6928 | 0.6928 | 0.6928 | ویکی مینیا موسسہ ویکیمیڈیا کے تحت منصوبوں کے صارفین کا سالانہ اجلاس ہے، جس میں ویکیمیڈیا منصوبوں، دیگر ویکیوں، آزاد مصدر... | Wikimania is an annual meeting of users of projects under the Wikimedia Foundation, where issues related to Wikimedia pr... |
| 17 | Wikimania | et | 0.6894 | 0.6894 | 0.6894 | Wikimania on konverents, mis toob kokku Wikimedia Sihtasutuse koordineeritavates projektides osalejad | Wikimania is a conference that brings together participants in projects coordinated by the Wikimedia Foundation |
| 18 | Wikimania | de | 0.6884 | 0.7386 | 0.5715 | Wikimania ist die Bezeichnung für eine internationale Tagung, die von der Wikimedia Foundation seit dem Jahr 2005 jährli... | Wikimania is the name for an international conference that has been organized annually by the Wikimedia Foundation at di... |
| 19 | Wikimania | fi | 0.6824 | 0.6915 | 0.6612 | Wikimania on vuosittainen kansainvälinen konferenssi Wikimedia-säätiön wikihankkeiden käyttäjille | Wikimania is an annual international conference for users of the Wikimedia Foundation's wiki projects |
| 20 | Wikimania | it | 0.6802 | 0.6674 | 0.7101 | Wikimania è una conferenza per gli utenti dei progetti Wikimedia | Wikimania is a conference for users of Wikimedia projects |
| 21 | Wikimania | nn | 0.6723 | 0.6599 | 0.7013 | Wikimania er ein internasjonal konferanse for brukarar av wikiprosjekt drivne av Wikimedia-stiftinga | Wikimania is an international conference for users of the Wikimedia project run by the Wikimedia Foundation |
| 22 | Wikimania | lv | 0.6722 | 0.7089 | 0.5865 | Wikimania ir ikgadēja starptautiska konference Wikimedia Foundation uzturēto projektu lietotājiem | Wikimania is an annual international conference for users of projects maintained by the Wikimedia Foundation |
| 23 | Wikimania | sh | 0.6687 | 0.7126 | 0.5663 | Wikimania [ˌwɪkiˈmeɪniə], službena godišnja konferencija Wikimedia Foundationa | Wikimania [ˌwɪkiˈmeɪniə], the official annual conference of the Wikimedia Foundation |
| 24 | Wikimania | pl | 0.6581 | 0.6581 | 0.6581 | Wikimania – doroczna konferencja dla edytorów, użytkowników i osób w inny sposób zainteresowanych projektami wiki prowad... | Wikimania - an annual conference for editors, users and those otherwise interested in wiki projects operated by the Wiki... |
| 25 | ويكيمانيا | ar | 0.6538 | 0.6597 | 0.6400 | ويكيمانيا هو المؤتمر السنوي الذي يُعقد للاحتفال بجميع مشاريع المعرفة الحرة التي تستضيفها مؤسسة ويكيميديا وتشمل: ويكيميدي... | Wikimania is an annual conference held to celebrate all free knowledge projects hosted by the Wikimedia Foundation inclu... |
| 26 | Wikimania | id | 0.6508 | 0.7148 | 0.5014 | Wikimania merupakan sebuah konferensi pengguna proyek wiki yang dijalankan oleh Yayasan Wikimedia | Wikimania is a wiki project user conference run by the Wikimedia Foundation |
| 27 | Wikimania | bcl | 0.6481 | 0.6773 | 0.5799 | An Wikimania iyo an taonan na komperensya kan Wikimedia, na inorganisar kan mga boluntaryo asin pinapadrinohan kan Wikim... | Wikimania is the annual Wikimedia conference, organized by volunteers and sponsored by the Wikimedia Foundation |
| 28 | Vouiquimânie | frp | 0.6455 | 0.6455 | 0.6455 | La Vouiquimânie est la confèrence annuâla de la Wikimedia Foundation | La Vouiquimânie is the annual conference of the Wikimedia Foundation |
| 29 | ویکیمانیا | ckb | 0.6442 | 0.6545 | 0.6200 | ویکیمانیا کۆنفرانسی ساڵانەی بزووتنەوەی ویکیمیدیایە کە لەلایەن کەسانی خۆبەخشەوە ڕێکدەخرێت و لەلایەن دامەزراوەی ویکیمیدیا ... | Wikimania is an annual conference of the Wikimedia movement organized by volunteers and hosted by the Wikimedia Foundati... |
| 30 | Vikimanija | lt | 0.6425 | 0.6685 | 0.5817 | Vikimanija – oficiali kasmetinė Wikimedia Foundation konferencija | Wikimania is the official annual conference of the Wikimedia Foundation |
| 31 | Wikimania | lb | 0.6405 | 0.6102 | 0.7113 | Wikimania ass eng international Konferenz, déi vun der Wikimedia Foundation all Joer op enger anerer Plaz organiséiert g... | Wikimania is an international conference organized by the Wikimedia Foundation at a different location every year |
| 32 | Wikimanija | hr | 0.6326 | 0.6448 | 0.6042 | Wikimania je godišnja međunarodna konferencija za suradnike projekata Zaklade Wikimedije | Wikimania is an annual international conference for project collaborators of the Wikimedia Foundation |
| 33 | Wikimania | simple | 0.6266 | 0.5984 | 0.6922 | It is organized by the Wikimedia Foundation and brings together authors, programmers, and researchers | It is organized by the Wikimedia Foundation and brings together authors, programmers, and researchers |
| 34 | Wikimania | tr | 0.6254 | 0.6702 | 0.5209 | Wikimania, viki projeleri kullanıcıları için Wikimedia Vakfı tarafından düzenlenen uluslararası bir konferanstır | Wikimania is an international conference organized by the Wikimedia Foundation for users of wiki projects |
| 35 | 위키마니아 | ko | 0.6175 | 0.6577 | 0.5236 | 위키마니아(Wikimania)는 위키미디어 재단이 운영하는 여러 위키 프로젝트 사용자들의 국제회의로 매년 개최된다 | Wikimania is an international conference of users of various Wiki projects operated by the Wikimedia Foundation and is h... |
| 36 | Викиманий | mhr | 0.6145 | 0.6145 | 0.6145 | «Викиманий» (англичанла Wikimania) — «Викимедий фондын» кажне ийын эртарыме тӱнямбал конференцийже | Wikimania is an annual international conference of the Wikimedia Foundation |
| 37 | Wikimania | af | 0.6132 | 0.6132 | 0.6132 | Die term Wikimania verwys na 'n internasionale konferensie, wat sedert 2005 deur die Wikimedia-stigting jaarliks op vers... | The term Wikimania refers to an international conference, held annually by the Wikimedia Foundation in different locatio... |
| 38 | Вікіманія | uk | 0.6079 | 0.5930 | 0.6429 | «Вікіма́нія» — щорічна міжнародна конференція, яку організовує Фонд Вікімедіа | Wikimania is an annual international conference organized by the Wikimedia Foundation |
| 39 | Викимания | ru | 0.6057 | 0.6245 | 0.5619 | «Викима́ния» — ежегодная международная конференция «Фонда Викимедиа» | Wikimania is an annual international conference of the Wikimedia Foundation. |
| 40 | 维基媒体国际会议 | wuu | 0.6029 | 0.6029 | 0.6029 | 维基媒体国际会议（Wikimania）是维基媒体基金会主办个有关维基搭维基相关项目个学术会议，让维基编者搭用户得以相见，并搭维基研究者、维基开发者、媒体搭公众，共同探讨维基各项目、维基技术搭文化、自由内容搭文化运动个实践、进展搭未来。 | Wikimania is an academic conference on Wiki and Wiki-related projects sponsored by the Wikimedia Foundation, allowing Wi... |
| 41 | Wikimania | ms | 0.6017 | 0.6733 | 0.4347 | Wikimania merupakan sebuah persidangan untuk pengguna projek wiki yang dijalankan oleh Yayasan Wikimedia | Wikimania is a conference for wiki project users run by the Wikimedia Foundation |
| 42 | Викимани | ce | 0.5805 | 0.6030 | 0.5281 | Wikimania) — «Викимедиан фондан» хӀора шера дуьненайукъара конференци | Wikimania) is an annual international conference of the Wikimedia Foundation |
| 43 | Wikimania | mad | 0.5747 | 0.6270 | 0.4527 | Wikimania iyâ arèya konferensi ghâbây pangghuna proyèk wiki sè èjalanaghi sareng Yayasan Wikimedia | Wikimania is a conference for wiki users run by the Wikimedia Foundation |
| 44 | Викимани | cv | 0.5746 | 0.5746 | 0.5746 | «Викимани» — «Викимедиа Фондăн» çулсерен иртекен тĕнчери конференцийĕ | Wikimania is an annual international conference of the Wikimedia Foundation |
| 45 | विकिमेनिया | hi | 0.5689 | 0.5689 | 0.5689 | विकिमेनिया विकीमीडिया फाउंडेशन का आधिकारिक वार्षिक सम्मेलन है। प्रस्तुतियों और चर्चाओं के विषयों में विकिपीडिया, अन्य वि... | Wikimania is the official annual conference of the Wikimedia Foundation. Topics of presentations and discussions include... |
| 46 | Wikimania | war | 0.5594 | 0.5594 | 0.5594 | Iton wikimania in tinuig nga kirigta han mga gumaramit han mga proyekto nga wiki nga ginpapadalagan han Wikimedia Founda... | Wikimania is an annual meeting of wiki projects run by the Wikimedia Foundation |
| 47 | 維基媒體國際會議 | zh | 0.5589 | 0.5589 | 0.5589 | 維基媒體國際會議（Wikimania）是維基媒體基金會主辦的有關維基及维基相關計畫的學術會議，使維基編者及用戶得以相見，並與維基研究者、維基開發者、媒體及公眾，共同探討維基各計畫、維基技術與文化、自由內容與文化運動的實踐、進展與未來。 | 維基媒體國際會議（Wikimania）是維基媒體基金會主辦的有關維基及维基相關計畫的學術會議，使維基編者及用戶得以相見，並與維基研究者、維基開發者、媒體及公眾，共同探討維基各計畫、維基技術與文化、自由內容與文化運動的實踐、進展與未來。 |
| 48 | Wikimania | ca | 0.5556 | 0.5542 | 0.5588 | Wikimania és un congrés internacional, on es realitzen conferències per a presentar estudis, investigacions, observacion... | Wikimania is an international congress, where conferences are held to present studies, research, observations and experi... |
| 49 | ویکی‌مانیا | fa | 0.5418 | 0.5369 | 0.5532 | ویکی‌مانیا یکی از رخدادهای سالانه و جهانی بنیاد ویکی‌مدیا است | Wikimania is one of the annual and global events of the Wikimedia Foundation |
| 50 | Wikimania | pt | 0.5416 | 0.5416 | 0.5416 | Wikimania é a conferência internacional anual dos colaboradores voluntários dos projectos da fundação Wikimedia realizad... | Wikimania is the annual international conference of voluntary contributors to Wikimedia Foundation projects held since 2... |
| 51 | Wikimania | scn | 0.5399 | 0.5312 | 0.5602 | Wikimania è na cunfirenza accademica ppi utenti di lu pruggetti wiki cuurdinati dâ Funnazzioni Wikimedia | Wikimania is an academic conference for users of wiki projects coordinated by the Wikimedia Foundation |
| 52 | Wikimania | jv | 0.5370 | 0.6167 | 0.3512 | Wikimania iku konferènsi para naraguna proyèk wiki kang dianakaké déning Yayasan Wikimedia | Wikimania is a conference of wiki project users held by the Wikimedia Foundation |
| 53 | Wikimania | eu | 0.5323 | 0.6127 | 0.3447 | Wikimania nazioarteko kongresua da, Wikimedia Fundazioak kudeatzen dituen wikietan ekarpenak egiten dituzten erabiltzail... | Wikimania is an international conference attended by users who contribute to wikis managed by the Wikimedia Foundation |
| 54 | Wikimania | gor | 0.5265 | 0.5713 | 0.4220 | Wikimania yito konferensi lo ta hepopohunawa proyek wiki u hepopona'o lo Yayasan Wikimedia | Wikimania is a conference that is part of the wiki project that is part of Yayasan Wikimedia |
| 55 | Wikimania | sr | 0.5221 | 0.5319 | 0.4992 | Викиманија је конференција за кориснике вики пројеката Задужбине Викимедије | Wikimania is a conference for users of Wikimedia Endowment wiki projects |
| 56 | ვიკიმანია | ka | 0.5215 | 0.5497 | 0.4557 | ვიკიმანია — ყოველწლიური კონფერენცია, რომელიც ორგანიზებულია მოხალისეების მიერ და მასპინძლობს ფონდი ვიკიმედია | Wikimania is an annual conference organized by volunteers and hosted by the Wikimedia Foundation. |
| 57 | Vikimaniya | uz | 0.5145 | 0.5145 | 0.5145 | Vikimaniya har yili oʻtkaziladigan xalqaro konferensiya boʻlib, unda Vikimedia Jamgʻarmasi loyihalari, xususan, Vikipedi... | Wikimania is an annual international conference that brings together Wikimedia Foundation projects and Wikipedia users i... |
| 58 | Wikimania | ny | 0.5075 | 0.5406 | 0.4304 | Wikimania ndi msonkhano wa pachaka wa Wikimedia Foundation | Wikimania is the Wikimedia Foundation's annual event |
| 59 | ויקימניה | he | 0.4981 | 0.5542 | 0.3669 | ויקימניה הוא הכנס השנתי הבין-לאומי של קרן ויקימדיה | Wikimania is the international annual conference of the Wikimedia Foundation |
| 60 | Wikimania | cdo | 0.4958 | 0.4958 | 0.4958 | Wikimania sê Wikimedia bâing gì siŏh cṳ̄ng guók-cié hŏk-sŭk huôi-ngiê | Wikimania is Wikimedia Commons. |
| 61 | Викиманија | mk | 0.4871 | 0.5070 | 0.4408 | Викиманија — меѓународен собир за корисниците и уредниците на вики-проектите на Фондацијата Викимедија | Wikimania — an international gathering for users and editors of the Wikimedia Foundation's wiki projects |
| 62 | Վիքիմանիա | hy | 0.4507 | 0.4507 | 0.4507 | Վիքիմանիա, Վիքիմեդիա Հիմնադրամի տարեկան պաշտոնական համաժողովը, որի ընթացքում քննարկվում և ներկայացվում են Վիքիմեդիայի նա... | Wikimania, the annual official conference of the Wikimedia Foundation, during which Wikimedia projects are discussed and... |
| 63 | Wikimania | sw | 0.4499 | 0.5000 | 0.3332 | Wikimania  ni tukio la kila mwaka la kimataifa wa Wikimedia | Wikimania is Wikimedia's annual international event |
| 64 | Wikimania | tl | 0.4379 | 0.4618 | 0.3823 | Ang Wikimania ay ang taunang pagtitipong pandaigdig ng mga tagagamit ng mga proyektong pinatatakbo ng Pundasyong Wikimed... | Wikimania is the annual global gathering of users of projects run by the Wikimedia Foundation, such as Wikipedia and its... |
| 65 | Wikimania | hak | 0.4288 | 0.4288 | 0.4288 | Wikimania he Wikimedia phan ke yit-chak fi-ngi, chhṳ 2005-ngièn khôi-sṳ́ yit ngièn khôi yit fi, yung lòi ngiong wiki-ló ... | Wikimania on Wikimedia was created in 2005, when the wiki was created. |
| 66 | Wikimania | ha | 0.4217 | 0.4313 | 0.3995 | Wikimania Wato ya kasan ce wani babban taron shekara-shekara ne na Gidauniyar Wikimedia | Wikimania is basically an annual event of the Wikimedia Foundation |
| 67 | Wikimania | mg | 0.4153 | 0.4265 | 0.3893 | Wikimania dia fihaonambe iraisam-pirenena atao isan-taona ka ivondronan'ireo mpandrindra ny volavola tetikasa Wikimedia | Wikimania is an annual international conference for Wikimedia project fundraisers |
| 68 | วิกิเมเนีย | th | 0.3962 | 0.3962 | 0.3962 | วิกิเมเนีย เป็นการประชุมระดับนานาชาติประจำปีสำหรับผู้ใช้ของโครงการวิกิที่ดำเนินการโดยมูลนิธิวิกิมีเดีย หัวข้อการนำเสนอแล... | Wikimania is an annual international conference for users of the Wikimedia project run by the Wikimedia Foundation. Pres... |
| 69 | Wikimania | kk | 0.3870 | 0.5232 | 0.0692 | «Уикиманиа» — «Уикимедиа қорының» жыл сайынғы халықаралық конференциясы | Wikimania is an annual international conference of the Wikimedia Foundation |
| 70 | Vikimaniya | az | 0.3643 | 0.4167 | 0.2420 | Vikimaniyada Vikimedia Fondunun müxtəlif layihələrində iştirak edən istifadəçilər toplaşırlar | Users participating in various projects of the Wikimedia Foundation gather in Wikimania |
| 71 | وڪي مينيا | sd | 0.3625 | 0.3625 | 0.3625 | وڪي مينيا وڪيميڊيا فائونڊيشن جي تحت منصوبن جي صارفن جو سالانو اجلاس آھي، جنھن ۾ وڪيميڊيا منصوبن، ٻين وڪين، آزاد مصدر ساف... | Wikimania is an annual meeting of users of projects under the Wikimedia Foundation, in which issues related to Wikimedia... |
| 72 | Вікіманія | be | 0.3542 | 0.3570 | 0.3475 | «Вікіманія» — штогадовая міжнародная канферэнцыя «Фонду Вікімедыя» | Wikimania is the annual international conference of the Wikimedia Foundation |
| 73 | وکیمینیا | pnb | 0.3456 | 0.3456 | 0.3456 | وکیمینیا وکیپیڈیا دے ورتنوالیاں دی اک سلانہ ملنی اے۔ اہ ہر سال دنیا دے وکھرے تھانوان تے ہوندی اے۔ ایدا پربندھ وکیمیڈیا ف... | Wikimania is an annual meeting of Wikipedia users. It takes place every year in different parts of the world. It is host... |
| 74 | Vicimania | la | 0.3139 | 0.3139 | 0.3139 | Vicimania, nomen est coetus internationalis ad quem confluunt quotannis usores Fundationis Vicimediae | Vicimania is the name of the international group to which the users of the Vicimedia Foundation flock every year |
| 75 | Vikimanio | eo | 0.3025 | 0.3054 | 0.2956 | Uzantoj de Vikipedio en Esperanto organizis en 2011 Esperantan Vikimanion en Svitavy (Ĉeĥio) | Users of Wikipedia in Esperanto organized in 2011 an Esperanto Wikimania in Svitavy (Czech Republic) |
| 76 | Вікіманія | be-tarask | 0.2956 | 0.3647 | 0.1345 | Вікіманія — штогадовая міжнародная канфэрэнцыя фонду Вікімэдыя | Wikimania is the Wikimedia Foundation's annual international conference |
| 77 | Викимания | tg | 0.2727 | 0.3755 | 0.0329 | Викиманиа — конфронси ҳарсолаи бунёди Викимедиа мебошад | Wikimania is an annual conference organized by Wikimedia |
| 78 | Wukimania | kcg | 0.2643 | 0.2761 | 0.2367 | Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni̱ njhyi a̱ni dundung ma̱ng Sotbeang Wuki... | Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni njhyi a̱ni dundung ma̱ng Sotbeang Wukim... |
| 79 | विकिमेनिया | mai | 0.2038 | 0.2038 | 0.2038 | विकिमेनिया विकीकर्मीसभक बार्षिक महासम्मेलन छी। एहिमे विश्वभरिक विकीकर्मीसभ जमा भ विभिन्न विषयसभमे छलफल करैत अछि। | Wikimania is the annual conference of wikiworkers. It brings together wikiers from around the world to discuss various t... |
| 80 | ವಿಕಿಮೇನಿಯಾ | tcy | 0.1776 | 0.1776 | 0.1776 | ಟೆಂಪ್ಲೇಟ್:Infobox recurring event | Template:Infobox recurring event |
| 81 | وِکیٖمینِیا | ks | 0.1730 | 0.1730 | 0.1730 | وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔... | وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔... |
| 82 | विकिमेनिया | ne | 0.1677 | 0.1677 | 0.1677 | विकिमेनिया विकीकर्मीहरूको बार्षिक महासम्मेलन हो। यसमा विश्वभरका विकीकर्मीहरू भेला भई विभिन्न विषयमा छलफल गर्ने गर्दछन्। | Wikimania is an annual convention of wikipedia. In it, wiki workers from all over the world gather and discuss various t... |
| 83 | ವಿಕಿಮೇನಿಯಾ | kn | 0.0064 | 0.0150 | -0.0137 | ವಿಕಿಮೇನಿಯಾ(ವಿಕಿಮಾನಿಯಾ ಎಂದೂ ಕರೆಯುತ್ತಾರೆ | Wikimania (also known as Wikimania |
| 84 | వికీమానియా | te | -0.0066 | -0.0019 | -0.0175 | వికీమానియా (Wikimania)వికీమీడియా ఫౌండేషన్ సహాయంతో సముదాయం నిర్వహించే వార్షిక సమావేశం | Wikimania is an annual conference organized by the community with the help of the Wikimedia Foundation |
| 85 | ਵਿੱਕੀਮੈਨੀਆ | pa | -0.0145 | -0.0145 | -0.0145 | ਵਿੱਕੀਮੈਨੀਆ ਵਿਕੀਮੀਡੀਆ ਫਾਊਂਡੇਸ਼ਨ ਦੀ ਅਧਿਕਾਰਿਤ ਸਾਲਾਨਾ ਕਾਨਫਰੰਸ ਹੈ। ਪੇਸ਼ਕਾਰੀ ਅਤੇ ਵਿਚਾਰ ਚਰਚਾਵਾਂ ਦੇ ਵਿਸ਼ਿਆਂ ਵਿੱਚ ਵਿਕੀਪੀਡੀਆ, ਹੋਰ ... | Wikimania is the official annual conference of the Wikimedia Foundation. Topics for presentations and discussions includ... |
| 86 | വിക്കിമാനിയ | ml | -0.0147 | -0.0147 | -0.0147 | വിക്കിമീഡിയ ഫൗണ്ടേഷന്റെ കീഴിലുള്ള വിക്കി സം‌രഭങ്ങളിൽ പ്രവർത്തിക്കുന്ന ഉപയോക്താക്കൾക്കായി നടത്തപ്പെടുന്ന ആഗോള സംഗമമാണ്‌ വ... | Wikimania is a global gathering of users working on wiki initiatives under the auspices of the Wikimedia Foundation. |
| 87 | விக்கிமேனியா | ta | -0.0148 | -0.0138 | -0.0171 | விக்கிமேனியா என்பது விக்கிமீடியா நிறுவனம் நடத்தும் விக்கிப்பீடியா, விக்சனரி போன்ற விக்கித்திட்டங்களின் பங்களிப்பாளர்கள் ... | Wikimania is an annual international conference organized by Wikimedia that brings together contributors to wiki project... |
| 88 | ৱিকিমেনিয়া | as | -0.0195 | -0.0195 | -0.0195 | ৱিকিমেনিয়া হৈছে ৱিকিমিডিয়া ফাউণ্ডেশ্যনৰ দ্বাৰা পৰিচালিত ৱিকি প্ৰকল্পসমূহ -ৰ ব্যৱহাৰকাৰী আৰু সদস্যসকলৰ বাবে আয়োজিত এখন... | Wikimania is an annual international conference for users and members of wiki projects run by the Wikimedia Foundation. ... |
| 89 | উইকিম্যানিয়া | bn | -0.0232 | -0.0232 | -0.0232 | উইকিম্যানিয়া উইকিমিডিয়া ফাউন্ডেশনের আনুষ্ঠানিক বার্ষিক সম্মেলন। এই সম্মেলনে উইকিমিডিয়া প্রকল্পের অন্তর্ভুক্ত যেমন উইক... | Wikimania is the official annual conference of the Wikimedia Foundation. The conference covers Wikimedia projects such a... |
| 90 | វីគីប្រជុំ | km | -0.0328 | -0.0328 | -0.0328 | វីគីប្រជុំ គឺជាសន្និសិទមួយសំរាប់អ្នកប្រើប្រាស់ របស់គំរោងវីគី ដែលបានប្រតិបត្ដិដោយមូលស្ថាបនា វីគីមីឌា ។ នៅក្នុងភាសាអង់គ្លេ... | Wiki Meeting is a conference for users of the wiki project operated by Wikimedia Foundation. In English, we call a wiki ... |

## Top 5 Most Aligned Leads

### EN: Wikimania (combined: 0.9147, best-sentence: 0.9846)

> **Translation:** (English — original)

> *Original lead:* Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wikimedia Foundation. Topics of presentations and discussions include Wikimedia projects such as Wikipedia, other wikis, open-source software, free knowledge and free content, and social and technical aspects related to these topics.

### ES: Wikimanía (combined: 0.8754, best-sentence: 0.9253)

> **Translation:** Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Foundation

> *Original lead:* Wikimania es la conferencia anual del movimiento Wikimedia, organizada por voluntarios y patrocinada por la Fundación Wikimedia. Los temas de las presentaciones y discusiones incluyen proyectos de Wikimedia como Wikipedia, otras wikis, software de código abierto, conocimiento libre y contenido libre, y aspectos sociales y técnicos relacionados con estos temas.

### AN: Wikimania (combined: 0.8480, best-sentence: 0.8867)

> **Translation:** Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Foundation

> *Original lead:* Wikimania ye la conferencia anyal d'o movimiento Wikimedia, organizada per voluntarios y auspiciada per a Fundación Wikimedia. Os temas de presentacions y debaz incluyen prochectos de Wikimedia como Wikipedia, atras wikis, software de codigo ubierto, conoixencia y conteniu gratuitos, y aspectos socials y tecnicos relacionaus con estes temas.

### EL: Βικιμάνια (combined: 0.8340, best-sentence: 0.8671)

> **Translation:** Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and hosted by the Wikimedia Foundation

> *Original lead:* Το Βικιμάνια είναι το ετήσιο συνέδριο του κινήματος Wikimedia, που διοργανώνεται από εθελοντές και φιλοξενείται από το Ίδρυμα Wikimedia. Τα θέματα των παρουσιάσεων και των συζητήσεων περιλαμβάνουν διάφορα πρότζεκτ της Wikimedia, όπως η Wikipedia, άλλα wiki, το λογισμικό ανοιχτού κώδικα, την ελεύθερη γνώση, το ελεύθερο περιεχόμενο και τις κοινωνικές και τεχνικές πτυχές που σχετίζονται με αυτά τα θέματα.

### NL: Wikimania (combined: 0.7739, best-sentence: 0.8097)

> **Translation:** Wikimania is an annual conference for users of the wiki projects created by the Wikimedia Foundation

> *Original lead:* Wikimania is een jaarlijkse conferentie voor gebruikers van de wikiprojecten die zijn opgezet door de Wikimedia Foundation. De eerste conferentie werd in 2005 gehouden in Frankfurt (Duitsland). De onderwerpen van de presentaties en discussies betreffen de projecten van de Wikimedia Foundation, andere wiki's, open source software, en vrije inhoud.

## Bottom 5 Least Aligned Leads

### ML: വിക്കിമാനിയ (combined: -0.0147)

> **Translation:** Wikimania is a global gathering of users working on wiki initiatives under the auspices of the Wikimedia Foundation.

> *Original lead:* വിക്കിമീഡിയ ഫൗണ്ടേഷന്റെ കീഴിലുള്ള വിക്കി സം‌രഭങ്ങളിൽ പ്രവർത്തിക്കുന്ന ഉപയോക്താക്കൾക്കായി നടത്തപ്പെടുന്ന ആഗോള സംഗമമാണ്‌ വിക്കിമാനിയ.

### TA: விக்கிமேனியா (combined: -0.0148)

> **Translation:** Wikimania is an annual international conference organized by Wikimedia that brings together contributors to wiki projects such as Wikipedia and Wiktionary.

> *Original lead:* 

விக்கிமேனியா என்பது விக்கிமீடியா நிறுவனம் நடத்தும் விக்கிப்பீடியா, விக்சனரி போன்ற விக்கித்திட்டங்களின் பங்களிப்பாளர்கள் ஆண்டு தோறும் ஒன்று கூடும் பன்னாட்டு மாநாடு ஆகும். இம்மாநாட்டில் பல்வேறு விக்கிமீடியா நிறுவனத் திட்டங்கள், திறமூல மென்பொருள், கட்டற்ற அறிவு / உள்ளடக்கம், இவற்றோடு தொடர்புடைய சமூக, நுட்பப் புலங்கள் குறித்து கலந்துரையாடப்படுகிறது.

### AS: ৱিকিমেনিয়া (combined: -0.0195)

> **Translation:** Wikimania is an annual international conference for users and members of wiki projects run by the Wikimedia Foundation. The conference will feature mainly Wikimedia Foundation Proc

> *Original lead:* ৱিকিমেনিয়া হৈছে ৱিকিমিডিয়া ফাউণ্ডেশ্যনৰ দ্বাৰা পৰিচালিত ৱিকি প্ৰকল্পসমূহ -ৰ ব্যৱহাৰকাৰী আৰু সদস্যসকলৰ বাবে আয়োজিত এখন বাৰ্ষিক আন্তৰাষ্ট্ৰীয় সন্মিলন। এই সন্মিলনত মূলতঃ ৱিকিমিডিয়া ফাউণ্ডেশ্যনৰ প্ৰকল্পসমূহ, অন্য ৱিকি, মুক্ত উৎসৰ ছফ্টৱেৰ, মুক্ত জ্ঞান আৰু মুক্ত সমল, আৰু এই বিষয়সমূহৰ লগত জড়িত বিভিন্ন সামাজিক আৰু কাৰিকৰী দিশবোৰৰ বিষয়ে আলোচনা কৰা হয়।

### BN: উইকিম্যানিয়া (combined: -0.0232)

> **Translation:** Wikimania is the official annual conference of the Wikimedia Foundation. The conference covers Wikimedia projects such as Wikipedia, other wikis, open-source software, open knowledge and open content.

> *Original lead:* উইকিম্যানিয়া উইকিমিডিয়া ফাউন্ডেশনের আনুষ্ঠানিক বার্ষিক সম্মেলন। এই সম্মেলনে উইকিমিডিয়া প্রকল্পের অন্তর্ভুক্ত যেমন উইকিপিডিয়া, অন্যান্য উইকিসমূহ, ওপেন-সোর্স সফটওয়্যার, মুক্ত জ্ঞান ও মুক্ত বিষয়বস্তু, এবং এসকল বিষয় সম্পর্কিত সামাজিক এবং প্রযুক্তিগত দিক উপস্থাপনা এবং আলোচনা করা হয়।

### KM: វីគីប្រជុំ (combined: -0.0328)

> **Translation:** Wiki Meeting is a conference for users of the wiki project operated by Wikimedia Foundation. In English, we call a wiki meeting wiki mana. Topics of presentation and discussion including

> *Original lead:* វីគីប្រជុំ គឺជាសន្និសិទមួយសំរាប់អ្នកប្រើប្រាស់ របស់គំរោងវីគី ដែលបានប្រតិបត្ដិដោយមូលស្ថាបនា វីគីមីឌា ។ នៅក្នុងភាសាអង់គ្លេស យើងហៅវីគីប្រជុំថា វីគីម៉ានា ។ ប្រធាបបទនៃ ការបង្ហាញ និង ពិភាក្សារាប់បញ្ចូល ទាំងគំរោងរបស់មូលស្ថាបនាវីគីប្រជុំ, វីគីផ្សេងទៀត បង្ហាញនូវប្រភពហ្សបហ្វា ហើយនិង សេចក្ដីពេញចិត្ដផងដែរ។

## Languages Not Found

| Code | Title tried |
|------|-------------|
| ja | ウィキマニア |
| nb | Wikimania |
| ps | ويکي مانيا |
| yue | 維基狂歡節 |

---

> **🗣️ Translation note:** The "→ English translation" column uses Google Translate (auto-detect source language).
> Translations are of the *best-matching sentence* in each lead (the one that scored highest against the ideal).
> English rows show "(English — original)". Failed translations show "[translation failed]".

*Generated by `lang-check` pipeline v2*
*Model: `distiluse-base-multilingual-cased-v2`*
*Scoring: Combined = 0.7 × best-sentence + 0.3 × lead-section*