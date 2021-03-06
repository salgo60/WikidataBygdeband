# WikidataBygdeband
Arbetsyta för att städa data et al mellan  Wikidata och Bygdeband. [Bygdeband](https://www.hembygd.se/shf/page/34831) har bytt plattform till moderna byggstenar som [Leaflet](https://leafletjs.com/) / [Angular](https://angular.io/) --> nya möjligheter... och projektfolk finns på plats... 

Förslag/issues Prio se [Github projektyta](https://github.com/salgo60/WikidataBygdeband/projects/1?fullscreen=true) och [Issues](https://github.com/salgo60/WikidataBygdeband/issues)

<img src="BygdeWD.png" alt="drawing" width="400"/>

Se också 
* [T248875](https://phabricator.wikimedia.org/T248875) "Bygdeband has changed URLs"
* [Issue #4](https://github.com/salgo60/WikidataBygdeband/issues/4) är gjord och Wikipedia mallen ändrad för socknar och WIkipedia länkar nu Bygdeband på > [2600 socken artiklar i Wikipedia](http://petscan.wmflabs.org/?psid=16089584)
  * Wikipedia [Jälluntofta socken](https://sv.wikipedia.org/wiki/J%C3%A4lluntofta_socken) kopplas till Bygdeband 1304 [Jälluntofta distrikt](https://www.hembygd.se/shf/plats/1304)
  * se beskrivning [Issue 8](https://github.com/salgo60/WikidataBygdeband/issues/8)
  * Wikipedia har 2694 artiklar om socknar som har ungefär [2 734 sidvisningar per dag](https://tools.wmflabs.org/massviews/?platform=all-access&agent=user&source=category&range=this-year&subjectpage=0&subcategories=1&sort=views&direction=1&view=list&target=https://sv.wikipedia.org/wiki/Kategori:Socknar_i_Sverige) och [1 075 657](https://tools.wmflabs.org/massviews/?platform=all-access&agent=user&source=category&range=last-year&subjectpage=0&subcategories=1&sort=views&direction=1&view=list&target=https://sv.wikipedia.org/wiki/Kategori:Socknar_i_Sverige) visningar 2018

<img src="images/Test%20koppla%20Wiki%20Bygdeband.png" alt="drawing" width="200"/>


* POCar
  * UI API:Search [prototyp Wikipedia sökning distrikt](https://jsfiddle.net/salgo60/0baqun1h/embedded/result/) som ett alternativ att länka direkt till en artikel. Fler liknande [exempel](https://minancestry.blogspot.com/2018/10/nobel-data-api-test.html)
  * POC använda [scannade kartor i WIkipedia commons](https://jsfiddle.net/salgo60/0L3ofn9h/embedded/result/) med georeferenser se vidare [issue 9](https://github.com/salgo60/WikidataBygdeband/issues/9) 

Här borde finnas en tanke / ide hur Bygdeband kopplar personer/bilder/platser/byggnader tillbaka till Wikipedia / Wikidata Digitaltmuseum / Europeana / RAÄ / Riksarkivet.... 

Se exempel [karta hur vi kopplar ihop RAÄ böcker](https://goo.gl/Ftkd3F) om kyrkor med Wikidata dom borde kunna synas i Bygdeband [GITHUB SamlaLibris](https://github.com/salgo60/SamlaLibris) där borde museernas bilder om kyrkor synas se även test med Gotlands museum <-> Wikidata [T227736](https://phabricator.wikimedia.org/T227736) där mycket om kyrkor finns men väldigt dålig metadata

![xxx](https://github.com/salgo60/SamlaLibris/blob/master/www/SamlaLIBRIS_small.png)

Bok om Riddarholms kyrkan som beskriver olika personers gravar där vi kopplar ihop i WIkidata 
* Boken
* Personerna vilkas gravar beskrivs
* Kyrkan
* Författaren

[Wikidata SPARQL fråga](http://tinyurl.com/y334xnvy) hitta personer beskrivna i boken [WD Q61765464](https://www.wikidata.org/wiki/Q61765464?uselang=sv)

![Book about the Riddarholm church](https://github.com/salgo60/SamlaLibris/blob/master/www/Book.png)

![How its done in Wikidata and the metadatadebt at RAÄ and LIBRISXL](https://github.com/salgo60/SamlaLibris/blob/master/www/Book_libris.png)

* [Video om detta](https://www.youtube.com/watch?v=6szCrwKdji0) ser att vi bör ha samma tankar hur Bygdebandsrörelsen passar ihop med alla oss andra
* [tweet](https://twitter.com/salgo60/status/1247438144494022656?s=20) till Digitaltmuseum Ulf Bodin om han har förslag hur Bygdeband kan kopplas till dom....
* [tweet](https://twitter.com/salgo60/status/1247449028146667522?s=20) Digisam/Nordiska museet
* [Bygdeband FaceBook](https://www.facebook.com/Bygdeband/posts/10156622211357315?__xts__[0]=68.ARCPR6tAlDO6J6_qLXDNC3fQGP_zSy1AMBg-_BrlXq5OJ15nPpjBEoBdwiHMbbBRWPPnyIizs2RLlvldmYxwUGh7UkSxn5a6Js2ySHfCDkUpZ3i_c7FfEAO3pr3ptHX8Kg_hFV3glU1TTanonz7-38PW8X6Um_Y64Jf55XvEXdgOk8g3RTCaXQF5JtE&__tn__=-R)
* [Frågade LIBRISXL](https://kundo.se/org/librisxl/d/semantisk-koppling-i-librisxl/#c3490545) hur tänker dom? Hur skall man i framtiden hitta alla böcker som berör ens hembyggd och hur skall hembygdsföreninbgarna göra sina skriftyer tillgängliga så fler hittar dom
* Diskussion i FB gruppen ["Släktforskning Semantisk Web"](https://www.facebook.com/groups/345973895882090/permalink/821965711616237/)
  * visa [gamla kartor](https://www.facebook.com/groups/345973895882090/permalink/821965711616237/?comment_id=824154984730643)
  * kopplingar med [LIBRIS och böcker om orten](https://www.facebook.com/groups/345973895882090/permalink/821965711616237/?comment_id=824164161396392)
  * kan vi koppla Arkiv DIgital se [FB fråga](https://www.facebook.com/arkivdigital/posts/4292085774150601?comment_id=4294350610590784)
## Lite om Wikidata 
* [An introduction to Wikidata](https://www.youtube.com/watch?v=m_9_23jXPoE)  
* [Dev plan](https://www.wikidata.org/wiki/Wikidata:Development_plan) 2020 se även Phabricator ex. [Wikibase](https://phabricator.wikimedia.org/project/view/3079/)
  * Lydia om [Wikidata/Wikibase framtiden 2019](https://media.ccc.de/v/wikidatacon2019-3-glimpse_over_wikidata)
  * Denny Vrandečić som [skapade Wikidata om framtiden och källor](https://youtu.be/VdAc0JReVSw?t=2450)
* [Structured data on commons](https://www.youtube.com/watch?v=lmWmMIuCJVM) - länkad data i bilder
* Ny utveckling hämtar förslag poå referenser från referererade källor med bra metadata dvs. det är viktigt att vara maskinläsbar 
