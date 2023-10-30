import openai
openai.api_key = 'API-KEY'

# Count tokens in the text
token_count = openai.Completion.create(
    engine="text-davinci-003",  # Modell
    prompt= "Kreuzzüge LK Geschichte 1. Beschreibe die Ursachen, die 1095 zum ersten Kreuzzug unter Papst Urban II. geführt haben. 2. Im Lexikonbeitrag der Kinderzeitmaschine zu den sieben Kreuzzüge sind einige Wörter abhandengekommen. Vervollständige den Artikel, indem du die Lücken angegeben mit: [ ] mit Hilfe der vorgegebenen Begriffe füllst. Konrad III. - Jerusalems - Fluss Saleph - Venedig - Akkon - 1099 - Konstantinopel - 1229 - Muslime - Ägypten - 1270 - Friedrich III - 1149 - Friedrich Barbarossa - Christen – Kreuzfahrerstaaten  Sieben Mal auf Kreuzzug Der Erste Kreuzzug dauerte von 1095 bis [1099] und endete mit der Einnahme [Jerusalems] Es wurden vier [Kreuzfahrerstaaten] gegründet: das Königreich Jerusalem, die Grafschaft Edessa, das Fürstentum Antiochia und die Grafschaft Tripolis. Als die Grafschaft Edessa 1144 an die Muslime verloren ging, kam es 1147 zum Zweiten Kreuzzug. Auch [Konrad III.] nahm daran teil. Der Kreuzzug endete [1149] ergebnislos. Der Dritte Kreuzzug fand 1189 bis 1192 statt. Die Kreuzfahrerstaaten hatten Probleme, sich gegen die Muslime zu halten. Der Sultan Saladin hatte Jerusalem erobert. Philipp II. August von Frankreich, Richard Löwenherz aus England und [Friedrich III] Kaiser des Heiligen Römischen Reiches, riefen gemeinsam zum Kreuzzug auf. Friedrich ertrank 1190 im [Fluss Saleph] in der heutigen Türkei. Sein Heer löste sich auf. Jerusalem konnte nicht eingenommen werden. Im Vierten Kreuzzug kämpften französische Ritter und solche aus der Republik [Venedig]. Eigentlich war [Ägypten] das Ziel, doch dann wurde [Konstantinople] geplündert - obwohl es christlich war. Es hatte dort Konflikte mit den dort lebenden Kaufleuten aus Venedig gegeben. Der Fünfte Kreuzzug wurde von Kaiser [Babarossa] angeführt und dauerte von 1228 bis [1229] Friedrich schloss einen Friedensvertrag mit dem Sultan al-Kamil. Die [Christen] erhielten im Frieden von Jaffa Jerusalem zurück, Friedrich durfte sich gar zum König von Jerusalem krönen lassen. Der Tempelberg und der Felsendom, also ein Gebiet innerhalb Jerusalems, sollte jedoch in muslimischer Hand bleiben. Nicht alle waren mit diesem Kompromiss glücklich. 1244 war Jerusalem wieder an die [Muslime] gefallen. So brach der französische König Ludwig IX. 1248 zum Sechsten Kreuzzug auf. Er scheiterte allerdings schon im April 1250. Der Siebte Kreuzzug fand [1270] statt. Die Mameluken hatten die Herrschaft in Ägypten errungen. Die Kreuzfahrerfestungen wurden nach und nach von ihnen erobert. 1291 fiel die letzte Kreuzfahrerburg in [Akkon]. Die letzten Kreuzfahrer wurden vertrieben. Quelle: https://www.kinderzeitmaschine.de/mittelalter/hochmittelalter/lucys-wissensbox/religion/die-sieben-kreuzzuege/    3. Fasse die Einschätzung des Historikers Nikolaus Jaspert zur Bedeutung der Kreuzzüge für den Kulturaustausch zusammen.  Nachleben der Kreuzzüge In der Tat lässt sich eine Vielzahl von kulturellen Errungenschaften benennen, die aus der muslimischen Welt Einzug in den lateinischen Westen fanden. Arabische Lehnwörter aus der Welt des Handels wie Basar, Scheck oder Tarif, oder aus den Naturwissenschaften wie Algebra oder Algorithmus lassen sich in diesem Zusammenhang anführen. Künstlerische Errungenschaften [...] sowie Fertigkeiten in der Metall-, Textil-, Keramik- und Lederverarbeitung wurden nachweislich aus der islamischen Welt übernommen. Auch aus muslimischer Sicht lassen sich Transferprozesse erkennen, obwohl die lateinischen Christen den Muslimen in kultureller Hinsicht wenig zu bieten hatten. In der Militärtechnik z.B. führte die Begegnung mit den fremden Kriegern zu wichtigen Neuerungen, von der Einführung gepanzerter Reiter bis zu Veränderungen in der Belagerungstechnik und im Festungsbau. Die konfessionelle Grenze war also durchlässiger als man annehmen könnte. Doch wie viel von alledem fand über die Kreuzfahrerherrschaften des Vorderen Orients seinen Weg in den Westen? Die Forschung ist sich mittlerweile weitgehend einig, dass in den Kreuzfahrerherrschaften Palästinas und Syriens vergleichsweise wenige derartige Transfervorgänge stattfanden. Andere Kontaktzonen dienten in stärkerem Maße als Einfallstore für fremdes Wissen. Sizilien und Süditalien blieben mehrere Jahrhunderte stark von der Kultur der unterworfenen Muslime geprägt, und in vielen islamischen Hafenstädten des Mittelmeers traten christliche Händler in Kontakt mit Andersgläubigen und ihrer Kultur [...]. Eigenes und Fremdes Die Begegnung mit dem Islam führte dem lateinischen Westen seine Gemeinsamkeit vor Augen [...]. Ebenso, wie eine bislang unbekannte Bündelung von Kräften über bisherige politische Grenzen hinweg den militärischen Erfolg des Ersten Kreuzzuges überhaupt erst ermöglichte, wurde die Besiedlung und Verteidigung des Eroberten über fast zwei Jahrhunderte hinweg nur durch immer wieder erneuerte gemeinsame Anstrengungen gewährleisten. So lässt sich wohl feststellen, dass die Begegnung mit andersartigen Kulturen weniger zu einem größeren Verständnis für das Fremde als vielmehr zu einer genaueren Kenntnis des Eigenen führte - mit allen positiven wie negativen Folgen. Die Kreuzzüge trugen wesentlich zur Selbstfindung sowohl des Christentums als auch des Islams bei. Quelle: Jaspert, Nikolaus: Die Kreuzzüge. Darmstadt 2003. S. 158ff.  4. Positioniere dich selbst und lege dar, ob die Kreuzzüge deiner Meinung nach eher das Verständnis für das Fremde gefördert oder aber die Zusammengehörigkeit der Christen gestärkt haben.  Zu Aufgabe 1) -In Palestina war das Leben schlimm/kritisch -Papst wurde aufgefordert einen Kreuzzug zu starten, dadie Pilger wege versperrt waren -Papst wollte glauben verbreiten -Die Pilgerwege waren versperrt, da in Jerusalem Muslime waren   Aufgabe 3. Nichts schließt sich aus einem Land sondern die Welt wird erst besser, wenn man zusammen arbeitet. Arabisch: -Lehnwörter: Basar, Scheck, Tarif -Naturwissenschaft: Algebra -> Algorythmus Islam: -Kunstleriche Errungenschaften -Fertigkeiten: Metall, textil, Keramik, Lederverarbeitung Muslimwelt: -Transferprozesse Begegnung mit Fremden: -Bessere Militärtechnik: Belagerungstechnik, Panzerung Vorderer Orient -Kreuzfahrerheerschaft  -> Die Kreuzzüge waren das Falsche für die Welt  4. Die Kreuzzüge stärkten wenn überhaupt nur die Zusammengehörigkeit der Christen. Da sonst andere Religionen zerrissen wurden. Die Kreuzzüge stärkten durch den Gewinn den Zusammenhalt   -> man will mehr. Aber die Welt kann sich nur erweitern wenn man zusammenhält aber die Kreuzzüge bewirkten genau das gegenteil, da sie Religionen asroteten. Fehleranalyse: Aufgabe 1 (4 von 8 Punkte): - \"In Palästina war das Leben schlimm/kritisch\" Was ist damit gemeint? Zu welcher Zeit? (-1 Punkt) -\"Papst wollte glauben verbreiten\" Welchen Glauben? (-1 Punkt) - Motive der Kreuzfahrer wurden nicht genannt! (-2 Punkte) - Formuliere vollständige Sätze und einen geschlossenen Text! (keine Punkte Abzug) Aufgabe 2 (7 von 8 Punkte): - \"Friedrich III\" wurde im Lückentext falsch zugeordnet! (-0,5 Punkte) - \"Friedrich Barbarossa\" wurde im Lückentext falsch zugeordnet! (-0,5 Punkte) Aufgabe 3 (2 von 4 Punkte): - \"Muslimwelt: Transferprozesse\" Welche genau? (keine Punkte erhalten) - \"Begegnung mit Fremden: Bessere Militärtechnik, Belagerungstechnik, Panzerung\" Was ist damit gemeint? = Transfer aus muslimischer Sicht! (keine Punkte erhalten) - \"Vorderer Orient: Kreuzfahrerherrschaft\" Was ist damit genau gemeint? (keine Punkte erhalten) - \"Die Kreuzzüge waren das Falsche für die Welt\" Was ist damit gemeint? Unzureichende Zusammenfassung! (-2 Punkte)  Aufgabe 4 (2 von 4 Punkte) - \"gegenteil, da sie Religion ausroteten\" Die Kreuzzüge rotteten keine Religionen aus, sondern sorgten nur für Veränderungen (-1 Punkt) - Gegenargumente fehlen, um deine Position zwischen den beiden Aussagen zu begründen! (-1 Punkt) Insgesamt: Punkte: 15 von24, das entspricht einer Leistung von: 62% Vorgeschlagene Note: 3-   ENDSTOP",
    max_tokens=0
)['usage']['total_tokens']

print(f"Token count: {token_count}")