# Lead Consistency Report: Wikimania

**Ideal sentence:** "Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wikimedia Foundation."
**Run:** Wikimania_run003_results.json
**Date:** 2026-06-12 15:35 UTC

**Total languages checked:** 94
**Successful fetches:** 90
**Not found/error:** 4

## Scoring Method

Each language's lead section is scored using a **combined metric**:

- **Best-sentence match (70% weight):** The ideal sentence is compared against every individual sentence in the lead. The highest similarity is retained. This captures whether *any* sentence in the lead conveys the core idea.
- **Lead-section match (30% weight):** The ideal sentence is compared against the combined first 3 sentences of the lead. This captures how well the *overall* lead aligns at the paragraph level.

Using a multilingual sentence transformer (`LaBSE`), semantic similarity is computed as cosine similarity between embeddings.

## Quick Summary

The ideal sentence has **two key clauses**:
1. "annual conference of the Wikimedia movement"
2. "organized by the community of contributors and hosted by the Wikimedia Foundation"

The combined score (0–1 scale) measures how closely each language's lead conveys both ideas.

## Key Findings

1. **Top performers:** Wikimania (en, 0.92), Wikimania (sl, 0.90), Βικιμάνια (el, 0.89) — these languages closely match the ideal sentence.
2. **English (en)** ranks **#1** with a combined score of 0.9169 (best-sentence: 0.9876, lead-section: 0.7521).
3. **Distribution:** 32 languages high (≥0.80), 40 moderate (0.70–0.79), 15 fair (0.50–0.69), 3 low (<0.50).
4. **Common divergence pattern:** Many languages frame the article subject differently from the ideal, often shifting emphasis from community agency to institutional framing.

## Overall Statistics

| Metric | Value |
|--------|-------|
| Mean combined score | 0.7496 |
| Median combined score | 0.7613 |
| Standard deviation | 0.1053 |
| Min score | 0.2881 |
| Max score | 0.9169 |
| Languages ≥ 0.80 | 32 / 90 (35.6%) |
| Languages ≥ 0.90 | 1 / 90 (1.1%) |

## Similarity Distribution

```
  0.90–1.00      | █                                        |  1 (  1.1%)
  0.80–0.89      | ███████████████████████████████          | 31 ( 34.4%)
  0.70–0.79      | ████████████████████████████████████████ | 40 ( 44.4%)
  0.60–0.69      | ███████████                              | 11 ( 12.2%)
  0.50–0.59      | ████                                     |  4 (  4.4%)
  0.00–0.49      | ███                                      |  3 (  3.3%)
  <0.00          | ·                                        |  0 (  0.0%)
```

## All Languages (sorted by combined score)

| # | Article | Code | Combined | Best-Sent | Lead-Sect | Original snippet | → English translation |
|---|---------|------|----------|-----------|-----------|-----------------|----------------------|
| 1 | Wikimania | **en** | 0.9169 | 0.9876 | 0.7521 | Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wi... | (English — original) |
| 2 | Wikimania | sl | 0.8987 | 0.8987 | 0.8987 | Wikimania je letna konferenca za uporabnike projektov Wiki, ki jih koordinira Fundacija Wikimedia | Wikimania is an annual conference for users of Wiki projects coordinated by the Wikimedia Foundation |
| 3 | Βικιμάνια | el | 0.8871 | 0.9372 | 0.7701 | Το Βικιμάνια είναι το ετήσιο συνέδριο του κινήματος Wikimedia, που διοργανώνεται από εθελοντές και φιλοξενείται από το Ί... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and hosted by the Wikimedia Founda... |
| 4 | Wikimania | cs | 0.8857 | 0.8857 | 0.8857 | Wikimania je konference uživatelů wiki projektů spravovaných nadací Wikimedia Foundation | Wikimania is a conference of users of wiki projects managed by the Wikimedia Foundation |
| 5 | Wikimanía | es | 0.8799 | 0.9503 | 0.7154 | Wikimania es la conferencia anual del movimiento Wikimedia, organizada por voluntarios y patrocinada por la Fundación Wi... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Fou... |
| 6 | Wikimania | an | 0.8743 | 0.9339 | 0.7352 | Wikimania ye la conferencia anyal d'o movimiento Wikimedia, organizada per voluntarios y auspiciada per a Fundación Wiki... | Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Fou... |
| 7 | Wikimania | nn | 0.8654 | 0.8598 | 0.8783 | Wikimania er ein internasjonal konferanse for brukarar av wikiprosjekt drivne av Wikimedia-stiftinga | Wikimania is an international conference for users of the Wikimedia project run by the Wikimedia Foundation |
| 8 | Wikimánia | hu | 0.8534 | 0.8797 | 0.7921 | A Wikimánia (Wikimedia International Conference) a wikiprojektek szerkesztőinek megrendezett évenkénti konferencia, mely... | Wikimania (Wikimedia International Conference) is an annual conference organized by the Wikimedia Foundation for editors... |
| 9 | Wikimania | sq | 0.8532 | 0.8773 | 0.7968 | Wikimania është një konferencë ndërkombëtare vjetore për përdoruesit e projekteve wiki të cilat mbikëqyren nga Fondacion... | Wikimania is an annual international conference for users of wiki projects overseen by the Wikimedia Foundation |
| 10 | Wikimania | lb | 0.8440 | 0.8345 | 0.8662 | Wikimania ass eng international Konferenz, déi vun der Wikimedia Foundation all Joer op enger anerer Plaz organiséiert g... | Wikimania is an international conference organized by the Wikimedia Foundation at a different location every year |
| 11 | Wikimania | mg | 0.8432 | 0.8681 | 0.7852 | Wikimania dia fihaonambe iraisam-pirenena atao isan-taona ka ivondronan'ireo mpandrindra ny volavola tetikasa Wikimedia | Wikimania is an annual international conference for Wikimedia project fundraisers |
| 12 | Wikimania | et | 0.8429 | 0.8429 | 0.8429 | Wikimania on konverents, mis toob kokku Wikimedia Sihtasutuse koordineeritavates projektides osalejad | Wikimania is a conference that brings together participants in projects coordinated by the Wikimedia Foundation |
| 13 | 위키마니아 | ko | 0.8400 | 0.8968 | 0.7075 | 위키마니아(Wikimania)는 위키미디어 재단이 운영하는 여러 위키 프로젝트 사용자들의 국제회의로 매년 개최된다 | Wikimania is an international conference of users of various Wiki projects operated by the Wikimedia Foundation and is h... |
| 14 | Wikimania | lv | 0.8348 | 0.8790 | 0.7317 | Wikimania ir ikgadēja starptautiska konference Wikimedia Foundation uzturēto projektu lietotājiem | Wikimania is an annual international conference for users of projects maintained by the Wikimedia Foundation |
| 15 | Wikimania | fi | 0.8306 | 0.8540 | 0.7761 | Wikimania on vuosittainen kansainvälinen konferenssi Wikimedia-säätiön wikihankkeiden käyttäjille | Wikimania is an annual international conference for users of the Wikimedia Foundation's wiki projects |
| 16 | Wikimania | eu | 0.8264 | 0.8747 | 0.7136 | Wikimania nazioarteko kongresua da, Wikimedia Fundazioak kudeatzen dituen wikietan ekarpenak egiten dituzten erabiltzail... | Wikimania is an international conference attended by users who contribute to wikis managed by the Wikimedia Foundation |
| 17 | Wikimania | nl | 0.8262 | 0.8751 | 0.7120 | Wikimania is een jaarlijkse conferentie voor gebruikers van de wikiprojecten die zijn opgezet door de Wikimedia Foundati... | Wikimania is an annual conference for users of the wiki projects created by the Wikimedia Foundation |
| 18 | விக்கிமேனியா | ta | 0.8260 | 0.8347 | 0.8058 | விக்கிமேனியா என்பது விக்கிமீடியா நிறுவனம் நடத்தும் விக்கிப்பீடியா, விக்சனரி போன்ற விக்கித்திட்டங்களின் பங்களிப்பாளர்கள் ... | Wikimania is an annual international conference organized by Wikimedia that brings together contributors to wiki project... |
| 19 | Wikimania | bcl | 0.8242 | 0.8706 | 0.7159 | An Wikimania iyo an taonan na komperensya kan Wikimedia, na inorganisar kan mga boluntaryo asin pinapadrinohan kan Wikim... | Wikimania is the annual Wikimedia conference, organized by volunteers and sponsored by the Wikimedia Foundation |
| 20 | ვიკიმანია | ka | 0.8184 | 0.8637 | 0.7125 | ვიკიმანია — ყოველწლიური კონფერენცია, რომელიც ორგანიზებულია მოხალისეების მიერ და მასპინძლობს ფონდი ვიკიმედია | Wikimania is an annual conference organized by volunteers and hosted by the Wikimedia Foundation. |
| 21 | Wikimania | pl | 0.8161 | 0.8161 | 0.8161 | Wikimania – doroczna konferencja dla edytorów, użytkowników i osób w inny sposób zainteresowanych projektami wiki prowad... | Wikimania - an annual conference for editors, users and those otherwise interested in wiki projects operated by the Wiki... |
| 22 | ವಿಕಿಮೇನಿಯಾ | kn | 0.8123 | 0.8057 | 0.8276 | ) ವಿಕಿಮೀಡಿಯಾ ಚಳುವಳಿಯ ವಾರ್ಷಿಕ ಸಮ್ಮೇಳನವಾಗಿದ್ದು, ಸ್ವಯಂಸೇವಕ ಸಮುದಾಯಗಳು ಮತ್ತು ಮತ್ತು ವಿಕಿಮೀಡಿಯಾ ಫೌಂಡೇಶನ್- ಇವೆರಡೂ ಸೇರಿ ಆಯೋಜಿಸುವ ... | ) is the annual conference of the Wikimedia movement, a massive event jointly organized by volunteer communities and the... |
| 23 | Вікіманія | uk | 0.8120 | 0.8321 | 0.7652 | «Вікіма́нія» — щорічна міжнародна конференція, яку організовує Фонд Вікімедіа | Wikimania is an annual international conference organized by the Wikimedia Foundation |
| 24 | Wikimania | sk | 0.8117 | 0.8822 | 0.6473 | Wikimania je každoročná medzinárodná konferencia pre participantov wikiprojektov nadácie Wikimedia Foundation | Wikimania is an annual international conference for participants of wikiprojects of the Wikimedia Foundation |
| 25 | Vikimaniya | az | 0.8114 | 0.7992 | 0.8398 | Vikimaniya — Vikimedia Fondunun hər il təşkil etdiyi beynəlxalq konfrans | Wikimania is an international conference organized annually by the Wikimedia Foundation |
| 26 | Wikimania | tl | 0.8098 | 0.8307 | 0.7611 | Ang Wikimania ay ang taunang pagtitipong pandaigdig ng mga tagagamit ng mga proyektong pinatatakbo ng Pundasyong Wikimed... | Wikimania is the annual global gathering of users of projects run by the Wikimedia Foundation, such as Wikipedia and its... |
| 27 | ৱিকিমেনিয়া | as | 0.8090 | 0.8090 | 0.8090 | ৱিকিমেনিয়া হৈছে ৱিকিমিডিয়া ফাউণ্ডেশ্যনৰ দ্বাৰা পৰিচালিত ৱিকি প্ৰকল্পসমূহ -ৰ ব্যৱহাৰকাৰী আৰু সদস্যসকলৰ বাবে আয়োজিত এখন... | Wikimania is an annual international conference for users and members of wiki projects run by the Wikimedia Foundation. ... |
| 28 | Wikimania | tr | 0.8086 | 0.8435 | 0.7272 | Wikimania, viki projeleri kullanıcıları için Wikimedia Vakfı tarafından düzenlenen uluslararası bir konferanstır | Wikimania is an international conference organized by the Wikimedia Foundation for users of wiki projects |
| 29 | Wikimanija | hr | 0.8063 | 0.8278 | 0.7562 | Wikimania je godišnja međunarodna konferencija za suradnike projekata Zaklade Wikimedije | Wikimania is an annual international conference for project collaborators of the Wikimedia Foundation |
| 30 | Vikimaniya | uz | 0.8041 | 0.8041 | 0.8041 | Vikimaniya har yili oʻtkaziladigan xalqaro konferensiya boʻlib, unda Vikimedia Jamgʻarmasi loyihalari, xususan, Vikipedi... | Wikimania is an annual international conference that brings together Wikimedia Foundation projects and Wikipedia users i... |
| 31 | Wikimania | id | 0.8029 | 0.8698 | 0.6468 | Wikimania merupakan sebuah konferensi pengguna proyek wiki yang dijalankan oleh Yayasan Wikimedia | Wikimania is a wiki project user conference run by the Wikimedia Foundation |
| 32 | Wikimania | fr | 0.8022 | 0.8007 | 0.8055 | Wikimania ou la Wikimania est la principale conférence organisée par la fondation Wikimédia à partir de 2005 | Wikimania or Wikimania is the main conference organized by the Wikimedia foundation from 2005 |
| 33 | వికీమానియా | te | 0.7993 | 0.8386 | 0.7075 | వికీమానియా (Wikimania)వికీమీడియా ఫౌండేషన్ సహాయంతో సముదాయం నిర్వహించే వార్షిక సమావేశం | Wikimania is an annual conference organized by the community with the help of the Wikimedia Foundation |
| 34 | Wikimania | ny | 0.7978 | 0.8411 | 0.6969 | Wikimania ndi msonkhano wa pachaka wa Wikimedia Foundation | Wikimania is the Wikimedia Foundation's annual event |
| 35 | വിക്കിമാനിയ | ml | 0.7949 | 0.7949 | 0.7949 | വിക്കിമീഡിയ ഫൗണ്ടേഷന്റെ കീഴിലുള്ള വിക്കി സം‌രഭങ്ങളിൽ പ്രവർത്തിക്കുന്ന ഉപയോക്താക്കൾക്കായി നടത്തപ്പെടുന്ന ആഗോള സംഗമമാണ്‌ വ... | Wikimania is a global gathering of users working on wiki initiatives under the auspices of the Wikimedia Foundation. |
| 36 | Wikimania | sv | 0.7866 | 0.8010 | 0.7530 | Wikimania är en internationell konferens som Wikimedia Foundation sedan 2005 årligen har organiserat på olika platser, i... | Wikimania is an international conference that the Wikimedia Foundation has organized annually since 2005 in various loca... |
| 37 | विकिमेनिया | ne | 0.7797 | 0.7797 | 0.7797 | विकिमेनिया विकीकर्मीहरूको बार्षिक महासम्मेलन हो। यसमा विश्वभरका विकीकर्मीहरू भेला भई विभिन्न विषयमा छलफल गर्ने गर्दछन्। | Wikimania is an annual convention of wikipedia. In it, wiki workers from all over the world gather and discuss various t... |
| 38 | Wikimania | vi | 0.7795 | 0.8291 | 0.6638 | Wikimania là tên gọi của hội nghị quốc tế thường niên được Wikimedia Foundation tổ chức | Wikimania is the name of the annual international conference organized by the Wikimedia Foundation |
| 39 | Wikimania | it | 0.7748 | 0.7835 | 0.7544 | Wikimania è una conferenza per gli utenti dei progetti Wikimedia | Wikimania is a conference for users of Wikimedia projects |
| 40 | Wikimania | kk | 0.7736 | 0.7680 | 0.7866 | «Уикиманиа» — «Уикимедиа қорының» жыл сайынғы халықаралық конференциясы | Wikimania is an annual international conference of the Wikimedia Foundation |
| 41 | Wikimania | ms | 0.7719 | 0.8609 | 0.5642 | Wikimania merupakan sebuah persidangan untuk pengguna projek wiki yang dijalankan oleh Yayasan Wikimedia | Wikimania is a conference for wiki project users run by the Wikimedia Foundation |
| 42 | Wikimania | jv | 0.7677 | 0.8320 | 0.6179 | Wikimania iku konferènsi para naraguna proyèk wiki kang dianakaké déning Yayasan Wikimedia | Wikimania is a conference of wiki project users held by the Wikimedia Foundation |
| 43 | Wikimania | war | 0.7674 | 0.7674 | 0.7674 | Iton wikimania in tinuig nga kirigta han mga gumaramit han mga proyekto nga wiki nga ginpapadalagan han Wikimedia Founda... | Wikimania is an annual meeting of wiki projects run by the Wikimedia Foundation |
| 44 | Вікіманія | be-tarask | 0.7655 | 0.7876 | 0.7141 | Вікіманія — штогадовая міжнародная канфэрэнцыя фонду Вікімэдыя | Wikimania is the Wikimedia Foundation's annual international conference |
| 45 | Уикимания | bg | 0.7634 | 0.8062 | 0.6634 | Уикимания (Wikimania) е официалната ежегодна конференция на Фондация Уикимедия | Wikimania is the official annual conference of the Wikimedia Foundation |
| 46 | Викимания | ru | 0.7592 | 0.7825 | 0.7050 | «Викима́ния» — ежегодная международная конференция «Фонда Викимедиа» | Wikimania is an annual international conference of the Wikimedia Foundation. |
| 47 | Вікіманія | be | 0.7574 | 0.7772 | 0.7113 | «Вікіманія» — штогадовая міжнародная канферэнцыя «Фонду Вікімедыя» | Wikimania is the annual international conference of the Wikimedia Foundation |
| 48 | Vikimanija | lt | 0.7552 | 0.7721 | 0.7158 | Vikimanija – oficiali kasmetinė Wikimedia Foundation konferencija | Wikimania is the official annual conference of the Wikimedia Foundation |
| 49 | Wikimania | de | 0.7535 | 0.7760 | 0.7009 | Wikimania ist die Bezeichnung für eine internationale Tagung, die von der Wikimedia Foundation seit dem Jahr 2005 jährli... | Wikimania is the name for an international conference that has been organized annually by the Wikimedia Foundation at di... |
| 50 | Wikimania | ha | 0.7510 | 0.7826 | 0.6773 | Wikimania Wato ya kasan ce wani babban taron shekara-shekara ne na Gidauniyar Wikimedia | Wikimania is basically an annual event of the Wikimedia Foundation |
| 51 | Wikimania | sh | 0.7483 | 0.7978 | 0.6328 | Wikimania [ˌwɪkiˈmeɪniə], službena godišnja konferencija Wikimedia Foundationa | Wikimania [ˌwɪkiˈmeɪniə], the official annual conference of the Wikimedia Foundation |
| 52 | Wikimania | mad | 0.7447 | 0.7973 | 0.6219 | Wikimania iyâ arèya konferensi ghâbây pangghuna proyèk wiki sè èjalanaghi sareng Yayasan Wikimedia | Wikimania is a conference for wiki users run by the Wikimedia Foundation |
| 53 | Викиманија | mk | 0.7446 | 0.7736 | 0.6768 | Викиманија — меѓународен собир за корисниците и уредниците на вики-проектите на Фондацијата Викимедија | Wikimania — an international gathering for users and editors of the Wikimedia Foundation's wiki projects |
| 54 | Vouiquimânie | frp | 0.7438 | 0.7438 | 0.7438 | La Vouiquimânie est la confèrence annuâla de la Wikimedia Foundation | La Vouiquimânie is the annual conference of the Wikimedia Foundation |
| 55 | Wikimania | ro | 0.7427 | 0.7672 | 0.6856 | Wikimania este conferința anuală oficială a Fundației Wikimedia, care se organizează anual din anul 2005, în diferite lo... | Wikimania is the official annual conference of the Wikimedia Foundation, held annually since 2005 in various locations |
| 56 | Vikimanio | eo | 0.7413 | 0.8176 | 0.5631 | Vikimanio estas ĉiujara internacia konferenco por uzantoj de vikiprojektoj fondita de Fondaĵo Vikimedio | Wikimania is an annual international conference for users of wiki projects founded by the Wikimedia Foundation |
| 57 | Wikimania | simple | 0.7406 | 0.7114 | 0.8088 | It is organized by the Wikimedia Foundation and brings together authors, programmers, and researchers | It is organized by the Wikimedia Foundation and brings together authors, programmers, and researchers |
| 58 | Wikimania | sw | 0.7405 | 0.7872 | 0.6314 | Wikimania  ni tukio la kila mwaka la kimataifa wa Wikimedia | Wikimania is Wikimedia's annual international event |
| 59 | 維基媒體國際會議 | zh | 0.7381 | 0.7381 | 0.7381 | 維基媒體國際會議（Wikimania）是維基媒體基金會主辦的有關維基及维基相關計畫的學術會議，使維基編者及用戶得以相見，並與維基研究者、維基開發者、媒體及公眾，共同探討維基各計畫、維基技術與文化、自由內容與文化運動的實踐、進展與未來。 | 維基媒體國際會議（Wikimania）是維基媒體基金會主辦的有關維基及维基相關計畫的學術會議，使維基編者及用戶得以相見，並與維基研究者、維基開發者、媒體及公眾，共同探討維基各計畫、維基技術與文化、自由內容與文化運動的實踐、進展與未來。 |
| 60 | Wikimania | af | 0.7354 | 0.7354 | 0.7354 | Die term Wikimania verwys na 'n internasionale konferensie, wat sedert 2005 deur die Wikimedia-stigting jaarliks op vers... | The term Wikimania refers to an international conference, held annually by the Wikimedia Foundation in different locatio... |
| 61 | Wikimania | gor | 0.7326 | 0.7816 | 0.6183 | Wikimania yito konferensi lo ta hepopohunawa proyek wiki u hepopona'o lo Yayasan Wikimedia | Wikimania is a conference that is part of the wiki project that is part of Yayasan Wikimedia |
| 62 | ויקימניה | he | 0.7314 | 0.7791 | 0.6203 | ויקימניה הוא הכנס השנתי הבין-לאומי של קרן ויקימדיה | Wikimania is the international annual conference of the Wikimedia Foundation |
| 63 | Wikimania | pt | 0.7305 | 0.7305 | 0.7305 | Wikimania é a conferência internacional anual dos colaboradores voluntários dos projectos da fundação Wikimedia realizad... | Wikimania is the annual international conference of voluntary contributors to Wikimedia Foundation projects held since 2... |
| 64 | ویکی‌مانیا | fa | 0.7302 | 0.7560 | 0.6701 | ویکی‌مانیا یکی از رخدادهای سالانه و جهانی بنیاد ویکی‌مدیا است | Wikimania is one of the annual and global events of the Wikimedia Foundation |
| 65 | Викимания | tg | 0.7301 | 0.7553 | 0.6714 | Викиманиа — конфронси ҳарсолаи бунёди Викимедиа мебошад | Wikimania is an annual conference organized by Wikimedia |
| 66 | 维基媒体国际会议 | wuu | 0.7298 | 0.7298 | 0.7298 | 维基媒体国际会议（Wikimania）是维基媒体基金会主办个有关维基搭维基相关项目个学术会议，让维基编者搭用户得以相见，并搭维基研究者、维基开发者、媒体搭公众，共同探讨维基各项目、维基技术搭文化、自由内容搭文化运动个实践、进展搭未来。 | Wikimania is an academic conference on Wiki and Wiki-related projects sponsored by the Wikimedia Foundation, allowing Wi... |
| 67 | Викиманий | mhr | 0.7232 | 0.7232 | 0.7232 | «Викиманий» (англичанла Wikimania) — «Викимедий фондын» кажне ийын эртарыме тӱнямбал конференцийже | Wikimania is an annual international conference of the Wikimedia Foundation |
| 68 | ویکی مینیا | ur | 0.7227 | 0.7227 | 0.7227 | ویکی مینیا موسسہ ویکیمیڈیا کے تحت منصوبوں کے صارفین کا سالانہ اجلاس ہے، جس میں ویکیمیڈیا منصوبوں، دیگر ویکیوں، آزاد مصدر... | Wikimania is an annual meeting of users of projects under the Wikimedia Foundation, where issues related to Wikimedia pr... |
| 69 | विकिमेनिया | mai | 0.7226 | 0.7226 | 0.7226 | विकिमेनिया विकीकर्मीसभक बार्षिक महासम्मेलन छी। एहिमे विश्वभरिक विकीकर्मीसभ जमा भ विभिन्न विषयसभमे छलफल करैत अछि। | Wikimania is the annual conference of wikiworkers. It brings together wikiers from around the world to discuss various t... |
| 70 | Wikimania | ca | 0.7114 | 0.7136 | 0.7064 | Wikimania és un congrés internacional, on es realitzen conferències per a presentar estudis, investigacions, observacion... | Wikimania is an international congress, where conferences are held to present studies, research, observations and experi... |
| 71 | Викимани | ce | 0.7061 | 0.6968 | 0.7277 | Wikimania) — «Викимедиан фондан» хӀора шера дуьненайукъара конференци | Wikimania) is an annual international conference of the Wikimedia Foundation |
| 72 | Wikimania | sr | 0.7031 | 0.7284 | 0.6442 | Викиманија је конференција за кориснике вики пројеката Задужбине Викимедије | Wikimania is a conference for users of Wikimedia Endowment wiki projects |
| 73 | Wikimania | scn | 0.6971 | 0.7117 | 0.6632 | Wikimania è na cunfirenza accademica ppi utenti di lu pruggetti wiki cuurdinati dâ Funnazzioni Wikimedia | Wikimania is an academic conference for users of wiki projects coordinated by the Wikimedia Foundation |
| 74 | វីគីប្រជុំ | km | 0.6910 | 0.6910 | 0.6910 | វីគីប្រជុំ គឺជាសន្និសិទមួយសំរាប់អ្នកប្រើប្រាស់ របស់គំរោងវីគី ដែលបានប្រតិបត្ដិដោយមូលស្ថាបនា វីគីមីឌា ។ នៅក្នុងភាសាអង់គ្លេ... | Wiki Meeting is a conference for users of the wiki project operated by Wikimedia Foundation. In English, we call a wiki ... |
| 75 | ਵਿੱਕੀਮੈਨੀਆ | pa | 0.6852 | 0.6852 | 0.6852 | ਵਿੱਕੀਮੈਨੀਆ ਵਿਕੀਮੀਡੀਆ ਫਾਊਂਡੇਸ਼ਨ ਦੀ ਅਧਿਕਾਰਿਤ ਸਾਲਾਨਾ ਕਾਨਫਰੰਸ ਹੈ। ਪੇਸ਼ਕਾਰੀ ਅਤੇ ਵਿਚਾਰ ਚਰਚਾਵਾਂ ਦੇ ਵਿਸ਼ਿਆਂ ਵਿੱਚ ਵਿਕੀਪੀਡੀਆ, ਹੋਰ ... | Wikimania is the official annual conference of the Wikimedia Foundation. Topics for presentations and discussions includ... |
| 76 | ويكيمانيا | ar | 0.6845 | 0.7084 | 0.6286 | ويكيمانيا هو المؤتمر السنوي الذي يُعقد للاحتفال بجميع مشاريع المعرفة الحرة التي تستضيفها مؤسسة ويكيميديا وتشمل: ويكيميدي... | Wikimania is an annual conference held to celebrate all free knowledge projects hosted by the Wikimedia Foundation inclu... |
| 77 | وکیمینیا | pnb | 0.6840 | 0.6840 | 0.6840 | وکیمینیا وکیپیڈیا دے ورتنوالیاں دی اک سلانہ ملنی اے۔ اہ ہر سال دنیا دے وکھرے تھانوان تے ہوندی اے۔ ایدا پربندھ وکیمیڈیا ف... | Wikimania is an annual meeting of Wikipedia users. It takes place every year in different parts of the world. It is host... |
| 78 | วิกิเมเนีย | th | 0.6746 | 0.6746 | 0.6746 | วิกิเมเนีย เป็นการประชุมระดับนานาชาติประจำปีสำหรับผู้ใช้ของโครงการวิกิที่ดำเนินการโดยมูลนิธิวิกิมีเดีย หัวข้อการนำเสนอแล... | Wikimania is an annual international conference for users of the Wikimedia project run by the Wikimedia Foundation. Pres... |
| 79 | وڪي مينيا | sd | 0.6602 | 0.6602 | 0.6602 | وڪي مينيا وڪيميڊيا فائونڊيشن جي تحت منصوبن جي صارفن جو سالانو اجلاس آھي، جنھن ۾ وڪيميڊيا منصوبن، ٻين وڪين، آزاد مصدر ساف... | Wikimania is an annual meeting of users of projects under the Wikimedia Foundation, in which issues related to Wikimedia... |
| 80 | Վիքիմանիա | hy | 0.6548 | 0.6548 | 0.6548 | Վիքիմանիա, Վիքիմեդիա Հիմնադրամի տարեկան պաշտոնական համաժողովը, որի ընթացքում քննարկվում և ներկայացվում են Վիքիմեդիայի նա... | Wikimania, the annual official conference of the Wikimedia Foundation, during which Wikimedia projects are discussed and... |
| 81 | विकिमेनिया | hi | 0.6519 | 0.6519 | 0.6519 | विकिमेनिया विकीमीडिया फाउंडेशन का आधिकारिक वार्षिक सम्मेलन है। प्रस्तुतियों और चर्चाओं के विषयों में विकिपीडिया, अन्य वि... | Wikimania is the official annual conference of the Wikimedia Foundation. Topics of presentations and discussions include... |
| 82 | Викимани | cv | 0.6417 | 0.6417 | 0.6417 | «Викимани» — «Викимедиа Фондăн» çулсерен иртекен тĕнчери конференцийĕ | Wikimania is an annual international conference of the Wikimedia Foundation |
| 83 | উইকিম্যানিয়া | bn | 0.6409 | 0.6409 | 0.6409 | উইকিম্যানিয়া উইকিমিডিয়া ফাউন্ডেশনের আনুষ্ঠানিক বার্ষিক সম্মেলন। এই সম্মেলনে উইকিমিডিয়া প্রকল্পের অন্তর্ভুক্ত যেমন উইক... | Wikimania is the official annual conference of the Wikimedia Foundation. The conference covers Wikimedia projects such a... |
| 84 | Wikimania | cdo | 0.5945 | 0.5945 | 0.5945 | Wikimania sê Wikimedia bâing gì siŏh cṳ̄ng guók-cié hŏk-sŭk huôi-ngiê | Wikimania is Wikimedia Commons. |
| 85 | Wikimania | hak | 0.5902 | 0.5902 | 0.5902 | Wikimania he Wikimedia phan ke yit-chak fi-ngi, chhṳ 2005-ngièn khôi-sṳ́ yit ngièn khôi yit fi, yung lòi ngiong wiki-ló ... | Wikimania on Wikimedia was created in 2005, when the wiki was created. |
| 86 | Vicimania | la | 0.5760 | 0.5760 | 0.5760 | Vicimania, nomen est coetus internationalis ad quem confluunt quotannis usores Fundationis Vicimediae | Vicimania is the name of the international group to which the users of the Vicimedia Foundation flock every year |
| 87 | ویکیمانیا | ckb | 0.5286 | 0.5411 | 0.4995 | ویکیمانیا کۆنفرانسی ساڵانەی بزووتنەوەی ویکیمیدیایە کە لەلایەن کەسانی خۆبەخشەوە ڕێکدەخرێت و لەلایەن دامەزراوەی ویکیمیدیا ... | Wikimania is an annual conference of the Wikimedia movement organized by volunteers and hosted by the Wikimedia Foundati... |
| 88 | Wukimania | kcg | 0.4074 | 0.4245 | 0.3674 | Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni̱ njhyi a̱ni dundung ma̱ng Sotbeang Wuki... | Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni njhyi a̱ni dundung ma̱ng Sotbeang Wukim... |
| 89 | وِکیٖمینِیا | ks | 0.3404 | 0.3404 | 0.3404 | وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔... | وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔... |
| 90 | ವಿಕಿಮೇನಿಯಾ | tcy | 0.2881 | 0.2881 | 0.2881 | ಟೆಂಪ್ಲೇಟ್:Infobox recurring event | Template:Infobox recurring event |

## Top 5 Most Aligned Leads

### EN: Wikimania (combined: 0.9169, best-sentence: 0.9876)

> **Translation:** (English — original)

> *Original lead:* Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wikimedia Foundation. Topics of presentations and discussions include Wikimedia projects such as Wikipedia, other wikis, open-source software, free knowledge and free content, and social and technical aspects related to these topics.

### SL: Wikimania (combined: 0.8987, best-sentence: 0.8987)

> **Translation:** Wikimania is an annual conference for users of Wiki projects coordinated by the Wikimedia Foundation

> *Original lead:* Wikimania je letna konferenca za uporabnike projektov Wiki, ki jih koordinira Fundacija Wikimedia.

### EL: Βικιμάνια (combined: 0.8871, best-sentence: 0.9372)

> **Translation:** Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and hosted by the Wikimedia Foundation

> *Original lead:* Το Βικιμάνια είναι το ετήσιο συνέδριο του κινήματος Wikimedia, που διοργανώνεται από εθελοντές και φιλοξενείται από το Ίδρυμα Wikimedia. Τα θέματα των παρουσιάσεων και των συζητήσεων περιλαμβάνουν διάφορα πρότζεκτ της Wikimedia, όπως η Wikipedia, άλλα wiki, το λογισμικό ανοιχτού κώδικα, την ελεύθερη γνώση, το ελεύθερο περιεχόμενο και τις κοινωνικές και τεχνικές πτυχές που σχετίζονται με αυτά τα θέματα.

### CS: Wikimania (combined: 0.8857, best-sentence: 0.8857)

> **Translation:** Wikimania is a conference of users of wiki projects managed by the Wikimedia Foundation

> *Original lead:* Wikimania je konference uživatelů wiki projektů spravovaných nadací Wikimedia Foundation.

### ES: Wikimanía (combined: 0.8799, best-sentence: 0.9503)

> **Translation:** Wikimania is the annual conference of the Wikimedia movement, organized by volunteers and sponsored by the Wikimedia Foundation

> *Original lead:* Wikimania es la conferencia anual del movimiento Wikimedia, organizada por voluntarios y patrocinada por la Fundación Wikimedia. Los temas de las presentaciones y discusiones incluyen proyectos de Wikimedia como Wikipedia, otras wikis, software de código abierto, conocimiento libre y contenido libre, y aspectos sociales y técnicos relacionados con estos temas.

## Bottom 5 Least Aligned Leads

### LA: Vicimania (combined: 0.5760)

> **Translation:** Vicimania is the name of the international group to which the users of the Vicimedia Foundation flock every year

> *Original lead:* Vicimania, nomen est coetus internationalis ad quem confluunt quotannis usores Fundationis Vicimediae.

### CKB: ویکیمانیا (combined: 0.5286)

> **Translation:** Wikimania is an annual conference of the Wikimedia movement organized by volunteers and hosted by the Wikimedia Foundation

> *Original lead:* ویکیمانیا کۆنفرانسی ساڵانەی بزووتنەوەی ویکیمیدیایە کە لەلایەن کەسانی خۆبەخشەوە ڕێکدەخرێت و لەلایەن دامەزراوەی ویکیمیدیا میوانداری دەکرێت. بابەتەکانی پێشکەشکردن و گفتوگۆکان بریتین لە پڕۆژەکانی ویکیمیدیا وەک ویکیپیدیا، ویکیەکانی تر، نەرمەکاڵای سەرچاوە کراوە، زانیاری ئازاد و ناوەڕۆکی ئازاد، هەروەها لایەنە کۆمەڵایەتی و تەکنیکییەکانی پەیوەست بەم بابەتانە.

### KCG: Wukimania (combined: 0.4074)

> **Translation:** Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni njhyi a̱ni dundung ma̱ng Sotbeang Wukimedia

> *Original lead:* Wukimania yet a̱tung kuzang a̱lyia̱ a̱guguut Wukimedia kya, nang á̱nietnjhyet ni̱ njhyi a̱ni dundung ma̱ng Sotbeang Wukimedia. Pyipyia̱-a̱lyiat ma̱ng bwoi a̱lyiat nang á̱ ni̱ neap ni̱ byia̱ a̱ka̱ta ma̱ng nta̱m Wukimedia nang Wukipedia, ngwuki ghyáng, kyanglilyiit a̱nan-ganng, lyen ma̱sa̱t ma̱ng nkyangmami ma̱sa̱t, mbeang nfam á̱niet ma̱ng ma̱ng lyennkyangta̱m na̱ byia̱ a̱ka̱ta ma̱ng pyipyia̱-a̱lyiat huni.

### KS: وِکیٖمینِیا (combined: 0.3404)

> **Translation:** وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔ اَتھ دوران چھِ وِکیٖمیٖڈیا مَنصوبَن پؠٹھ کَتھ باتھ کَرنہٕ یِوان

> *Original lead:* وِکیٖمینِیا چھِ وِکیٖمیٖڈیا مومینٹ ہُنٛد اَکھ سالانہٕ اِجلاس، یَتھ زَضاکار تہٕ وِکیٖمیٖڈیا فاوٗنڈیشَن مُنَقٕد چھِ کَران۔ اَتھ دوران چھِ وِکیٖمیٖڈیا مَنصوبَن پؠٹھ کَتھ باتھ کَرنہٕ یِوان.

### TCY: ವಿಕಿಮೇನಿಯಾ (combined: 0.2881)

> **Translation:** Template:Infobox recurring event

> *Original lead:* ಟೆಂಪ್ಲೇಟ್:Infobox recurring event

## Languages Not Found

| Code | Title tried |
|------|-------------|
| ja | ウィキマニア |
| nb | Wikimania |
| ps | ويکي مانيا |
| yue | 維基狂歡節 |

---

> **🗣️ Translation note:** The "→ English translation" column uses **Google Translate** (auto-detect source language, free, no API key required).
> Translations are of the *best-matching sentence* in each lead (the one that scored highest against the ideal).
> English rows show "(English — original)". Failed translations show "[translation failed]".

*Generated by `lang-check` pipeline v2*
*Model: `LaBSE`*
*Scoring: Combined = 0.7 × best-sentence + 0.3 × lead-section*