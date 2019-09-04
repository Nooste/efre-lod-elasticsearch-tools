marc2relation = {
    "VD-16 Mitverf": "contributor",
    "v:Mitverf": "contributor",
    "v:Co-Autor": "contributor",
    "v:Doktorvater": "contributor",
    "v:Illustrator": "contributor",
    "v:Übersetzer": "contributor",
    "v:Biograf": "contributor",
    "v:Förderer": "contributor",
    "v:Berater": "contributor",
    "v:hrsg": "contributor",
    "v:Mitautor": "contributor",
    "v:Partner": "contributor",
    
    "v:Tocher": "children",            #several typos in SWB dataset
    "tochter": "children",
    "Z:Tochter":"children",
    "Sohn": "children",
    "v:Nachkomme": "children",
    "v:zweites Kind": "children",
    
    "v:Erste Ehefrau":"spouse",
    "v:Zweite Ehefrau":"spouse",
    "v:Gattin": "spouse",
    "v:Gatte": "spouse",
    "v:Gemahl": "spouse",
    "Ehe": "spouse",
    "Frau": "spouse",
    "Mann": "spouse",
    
    "v:Jüngster Bruder": "sibling",
    "Bruder": "sibling",
    "v:Zwilling": "sibling",
    "Schwester": "sibling",
    "v:Halbschwester": "sibling",
    "v:Halbbruder": "sibling",
    "Vater": "parent",
    "Z:Vater":"parent",
    "v:Stiefvater": "parent",
    "Mutter": "parent",
    
    "Nachfolger": "follows",
    "Vorgänger": "follows",
    
    "v:Vorfahr": "relatedTo",
        
    "v:Schüler": "relatedTo",        
    "Lehrer": "relatedTo",        
    "v:frühere Ehefrau": "relatedTo",
    "v:Schwager": "relatedTo",        
    "v:Ur": "relatedTo",          
    "v:Muse": "relatedTo",
    "v:Nachfahre": "relatedTo",         
    "v:Groß": "relatedTo",    
    "v:Langjähriger Geliebter": "relatedTo",    
    "v:Lebensgefährt": "relatedTo",    
    "v:Nichte": "relatedTo",
    "v:Stiefnichte": "relatedTo",
    "v:Neffe": "relatedTo",
    "v:Onkel": "relatedTo",
    "v:Tante": "relatedTo",
    "v:Verlobt": "relatedTo",
    "v:Vorfahren": "relatedTo",
    "v:Vetter": "relatedTo",
    "v:Tauf": "relatedTo",
    "v:Pate": "relatedTo",
    "v:Schwägerin": "relatedTo",
    "v:Schwiegervater": "relatedTo",
    "v:Schwiegermutter": "relatedTo",
    "v:Schwiegertochter": "relatedTo",
    "v:Schwiegersohn": "relatedTo",
    "v:Enkel": "relatedTo",
    "v:Mätresse": "relatedTo",
    "Freund": "knows",
    "v:Großvater": "relatedTo",
    "v:Cousin": "relatedTo",
    "v:Lebenspartner": "relatedTo",
    "v:Berater und Freund": "relatedTo",
    "v:Geliebte": "relatedTo",
    "v:Modell und Lebensgefährtin":"relatedTo",
    "v:Liebesbeziehung":"relatedTo",
    
    "v:publizistische Zusammenarbeit und gemeinsame öffentliche Auftritte": "colleague",
    "v:Sekretär": "colleague", 
    "v:Privatsekretär": "colleague", 
    "v:Kolleg": "colleague", 
    "v:Mitarbeiter": "colleague", 
    "v:Kommilitone": "colleague", 
    "v:Zusammenarbeit mit": "colleague", 
    "v:gemeinsames Atelier": "colleague", 
    "v:Geschäftspartner": "colleague" , 
    "v:musik. Partnerin": "colleague" ,
    "v:Künstler. Partner": "colleague" ,  
    "assistent": "colleague",
    
    #see also http://www.dnb.de/SharedDocs/Downloads/DE/DNB/standardisierung/inhaltserschliessung/gndCodes.pdf?__blob=publicationFile
    "adel":"honorificPrefix",
    "adre":"recipent",
    "adue":"parentOrganization",
    "affi":"affiliation",
    #"akad":"honorificPrefix",
    "akti":"hasProfession",
    "bezf":"relatedTo",
    "bezb":"colleague",
    "beza":"knows",
    "bete": "contributor",
    "rela":"knows",
    "affi":"knows",
    "aut1":"author",
}
rolemapping={
"abr":"KürzendeR",
"acp":"HerstellerIn von Nachbildungen",
"act":"SchauspielerIn",
"adi":"Art Director",
"adp":"BearbeiterIn",
"aft":"VerfasserIn eines Nachworts",
"anl":"AnalytikerIn",
"anm":"TrickfilmzeichnerIn",
"ann":"KommentatorIn",
"ant":"BibliographischeR VorgängerIn",
"ape":"BerufungsbeklagteR/RevisionsbeklagteR",
"apl":"BerufungsklägerIn/RevisionsklägerIn",
"app":"AntragstellerIn",
"aqt":"AutorIn von Zitaten oder Textabschnitten",
"arc":"ArchitektIn",
"ard":"künstlerische Leitung",
"arr":"ArrangeurIn",
"art":"KünstlerIn",
"asg":"RechtsnachfolgerIn",
"asn":"zugehöriger Name",
"ato":"AutographIn",
"att":"zugehöriger Name",
"auc":"AuktionatorIn",
"aud":"AutorIn des Dialogs",
"aui":"VerfasserIn eines Geleitwortes",
"aus":"DrehbuchautorIn",
"aut":"VerfasserIn",
"bdd":"BindungsgestalterIn",
"bjd":"EinbandgestalterIn",
"bkd":"BuchgestalterIn",
"bkp":"BuchherstellerIn",
"blw":"AutorIn des Klappentextes",
"bnd":"BuchbinderIn",
"bpd":"GestalterIn des Exlibris",
"brd":"Sender",
"brl":"BrailleschriftprägerIn",
"bsl":"BuchhändlerIn",
"cas":"FormgießerIn",
"ccp":"konzeptionelle Leitung",
"chr":"ChoreografIn",
"clb":"MitarbeiterIn",
"cli":"KlientIn, AuftraggeberIn",
"cll":"KalligrafIn",
"clr":"KoloristIn",
"clt":"LichtdruckerIn",
"cmm":"KommentatorIn",
"cmp":"KomponistIn",
"cmt":"SchriftsetzerIn",
"cnd":"DirigentIn",
"cng":"Kameramann/frau",
"cns":"ZensorIn",
"coe":"BerufungsbeklagteR im streitigen Verfahren",
"col":"SammlerIn",
"com":"ZusammenstellendeR",
"con":"KonservatorIn",
"cor":"SammlungskuratorIn",
"cos":"AnfechtendeR, bestreitende Partei",
"cot":"BerufungsklägerIn im streitigen Verfahren",
"cou":"zuständiges Gericht",
"cov":"UmschlaggestalterIn",
"cpc":"BeansprucherIn des Urheberrechts",
"cpe":"BeschwerdeführerIn-BerufungsbeklagteR",
"cph":"InhaberIn des Urheberrechts",
"cpl":"BeschwerdeführerIn/KlägerIn",
"cpt":"KlägerIn/BerufungsklägerIn",
"cre":"GeistigeR SchöpferIn",
"crp":"KorrespondentIn",
"crr":"KorrektorIn",
"crt":"GerichtsstenografIn",
"csl":"BeraterIn",
"csp":"ProjektberaterIn",
"cst":"KostümbildnerIn",
"ctb":"MitwirkendeR",
"cte":"AnfechtungsgegnerIn-BerufungsbeklagteR",
"ctg":"KartografIn",
"ctr":"VertragspartnerIn",
"cts":"AnfechtungsgegnerIn",
"ctt":"AnfechtungsgegnerIn-BerufungsklägerIn",
"cur":"KuratorIn",
"cwt":"KommentatorIn",
"dbp":"Erscheinungsort",
"dfd":"AngeklagteR/BeklagteR",
"dfe":"AngeklagteR/BeklagteR-BerufungsbeklagteR",
"dft":"AngeklagteR/BeklagteR-BerufungsklägerIn",
"dgg":"Grad-verleihende Institution",
"dgs":"AkademischeR BetreuerIn",
"dir":"Dirigent",
"dis":"PromovierendeR",
"dln":"VorzeichnerIn",
"dnc":"TänzerIn",
"dnr":"GeldgeberIn",
"dpc":"AbgebildeteR",
"dpt":"AnlegerIn",
"drm":"TechnischeR ZeichnerIn",
"drt":"RegisseurIn",
"dsr":"DesignerIn",
"dst":"Vertrieb",
"dtc":"BereitstellerIn von Daten",
"dte":"WidmungsempfängerIn",
"dtm":"DatenmanagerIn",
"dto":"WidmendeR",
"dub":"angeblicheR AutorIn",
"edc":"BearbeiterIn der Zusammenstellung",
"edm":"CutterIn",
"edt":"HerausgeberIn",
"egr":"StecherIn",
"elg":"ElektrikerIn",
"elt":"GalvanisiererIn",
"eng":"IngenieurIn",
"enj":"Normerlassende Gebietskörperschaft",
"etr":"RadiererIn",
"evp":"Veranstaltungsort",
"exp":"ExperteIn",
"fac":"FacsimilistIn",
"fds":"Filmvertrieb",
"fld":"BereichsleiterIn",
"flm":"BearbeiterIn des Films",
"fmd":"FilmregisseurIn",
"fmk":"FilmemacherIn",
"fmo":"frühereR BesitzerIn",
"fmp":"FilmproduzentIn",
"fnd":"GründerIn",
"fpy":"Erste Partei",
"frg":"FälscherIn",
"gis":"GeographIn",
"grt":"GraphischeR TechnikerIn",
"hg":"Herausgeber",
"his":"Gastgebende Institution",
"hnr":"GefeierteR",
"hst":"GastgeberIn",
"Ill":"Illustrator",
"ill":"IllustratorIn",
"ilu":"Illuminator, BuchmalerIn",
"ins":"InserierendeR",
"inv":"ErfinderIn",
"isb":"Herausgebendes Organ",
"itr":"InstrumentalmusikerIn",
"ive":"InterviewteR",
"ivr":"InterviewerIn",
"jud":"RichterIn",
"jug":"zuständige Gerichtsbarkeit",
"kad":"Kadenzverfasser",
"lbr":"Labor",
"lbt":"LibrettistIn",
"ldr":"Laborleitung",
"led":"Führung",
"lee":"Libelee-appellee",
"lel":"BeklagteR im Seerecht/Kirchenrecht",
"len":"LeihgeberIn",
"let":"Libelee-appellant",
"lgd":"LichtgestalterIn",
"lie":"Libelant-appellee",
"lil":"KlägerIn im Seerecht/Kirchenrecht",
"lit":"Libelant-appellant",
"lsa":"LandschaftsarchitektIn",
"lse":"LizenznehmerIn",
"lso":"LizenzgeberIn",
"ltg":"LithographIn",
"lyr":"TextdichterIn",
"mcp":"ArrangeurIn, Notenleser/-schreiberIn",
"mdc":"Metadatenkontakt",
"med":"Medium",
"mfp":"Herstellungsort",
"mfr":"HerstellerIn",
"mod":"ModeratorIn",
"mon":"BeobachterIn",
"mrb":"MarmorarbeiterIn, MarmoriererIn",
"mrk":"Markup-EditorIn",
"msd":"MusikalischeR LeiterIn",
"mte":"Metall-GraveurIn",
"mtk":"ProtokollantIn",
"mus":"MusikerIn",
"nrt":"ErzählerIn",
"opn":"GegnerIn",
"org":"UrheberIn",
"orm":"VeranstalterIn",
"osp":"On-screen PräsentatorIn",
"oth":"BerichterstatterIn",
"own":"BesitzerIn",
"pan":"DiskussionsteilnehmerIn",
"pat":"SchirmherrIn",
"pbd":"Verlagsleitung",
"pbl":"Verlag",
"pdr":"Projektleitung",
"pfr":"Korrektur",
"pht":"FotografIn",
"plt":"DruckformherstellerIn",
"pma":"Genehmigungsstelle",
"pmn":"Produktionsleitung",
"pop":"PlattendruckerIn",
"ppm":"PapiermacherIn",
"ppt":"PuppenspielerIn",
"pra":"Praeses",
"prc":"Prozesskontakt",
"prd":"Produktionspersonal",
"pre":"PräsentatorIn",
"prf":"AusführendeR",
"prg":"ProgrammiererIn",
"prm":"DruckgrafikerIn",
"prn":"Produktionsfirma",
"pro":"ProduzentIn",
"prp":"Produktionsort",
"prs":"SzenenbildnerIn",
"prt":"DruckerIn",
"prv":"AnbieterIn",
"pta":"PatentanwärterIn",
"pte":"KlägerIn-BerufungsbeklagteR",
"ptf":"ZivilklägerIn",
"pth":"PatentinhaberIn",
"ptt":"KlägerIn-BerufungsklägerIn",
"pup":"Veröffentlichungsort",
"rbr":"RubrikatorIn",
"rcd":"TonmeisterIn",
"rce":"ToningenieurIn",
"rcp":"AdressatIn",
"rdd":"HörfunkregisseurIn",
"Red":"Redakteur",
"red":"RedakteurIn",
"ren":"RendererIn (Bildverarbeitung)",
"res":"ForscherIn",
"rev":"RezensentIn, GutachterIn",
"rpc":"HörfunkproduzentIn",
"rps":"Aufbewahrungsort, TreuhänderIn",
"rpt":"ReporterIn",
"rpy":"Verantwortliche Partei",
"rse":"AntragsgegnerIn-BerufungsbeklagteR",
"rsg":"RegisseurIn der Wiederaufführung",
"rsp":"RespondentIn",
"rsr":"RestauratorIn",
"rst":"AntragsgegnerIn-BerufungsklägerIn",
"rth":"Leitung des Forschungsteams",
"rtm":"Mitglied des Forschungsteams",
"sad":"WissenschaftlicheR BeraterIn",
"sce":"DrehbuchautorIn",
"scl":"BildhauerIn",
"scr":"SchreiberIn",
"sds":"Tongestalter",
"sec":"SekretärIn",
"sgd":"BühnenregisseurIn",
"sgn":"UnterzeichnerIn",
"sht":"Unterstützender Veranstalter",
"sll":"VerkäuferIn",
"sng":"SängerIn",
"spk":"RednerIn",
"spn":"SponsorIn",
"spy":"Zweite Partei",
"srv":"LandvermesserIn",
"std":"BühnenbildnerIn",
"stg":"Kulisse",
"stl":"GeschichtenerzählerIn",
"stm":"InszenatorIn",
"stn":"Normungsorganisation",
"str":"StereotypeurIn",
"tcd":"Technische Leitung",
"tch":"LehrerIn",
"ths":"BetreuerIn (Doktorarbeit)",
"tld":"FernsehregisseurIn",
"tlp":"FernsehproduzentIn",
"trc":"TranskribiererIn",
"trl":"ÜbersetzerIn",
"tyd":"Schrift-DesignerIn",
"tyg":"SchriftsetzerIn",
"uvp":"Hochschulort",
"vac":"SynchronsprecherIn",
"vdg":"BildregisseurIn",
"voc":"VokalistIn",
"wac":"KommentarverfasserIn",
"wal":"VerfasserIn von zusätzlichen Lyrics",
"wam":"AutorIn des Begleitmaterials",
"wat":"VerfasserIn von Zusatztexten",
"wdc":"HolzschneiderIn",
"wde":"HolzschnitzerIn",
"win":"VerfasserIn einer Einleitung",
"wit":"ZeugeIn",
"wpr":"VerfasserIn eines Vorworts",
"wst":"VerfasserIn von ergänzendem Text"
}
