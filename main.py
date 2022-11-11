from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_root():
    return {'Endpoints': ['Degrees', 'Jobs']}


# Degrees endpoint
@app.get('/degrees')
def degrees():
    return {
        'degrees': [
            {
                "id": 1,
                "degree": "Associate"
            },
            {
                "id": 2,
                "degree": "Bachelor's"
            },
            {
                "id": 3,
                "degree": "Master's"
            },
            {
                "id": 4,
                "degree": "Ph.D"
            },
            {
                "id": 5,
                "degree": "Persuing Degree"
            }
        ]
    }

#Spotlights endpoint
@app.get('/spotlights')
def spotlights():
    return {"spotlights": [
    {
      "id": 1,
      "img": "https://images.unsplash.com/photo-1556075798-4825dfaaf498",
      "title": "Cloud Engineering",
      "description": "Build fun stuff in the cloud. It's a lot of fun, we promise!"
    },
    {
      "id": 2,
      "img": "https://images.unsplash.com/photo-1511376777868-611b54f68947",
      "title": "Executive Leadership",
      "description": "Be a leader for everyone. Leadership builds character."
    }
  ]}
# jobs endpoint
@app.get('/jobs')
def jobs():
    return {
        'jobs': [
            {
                "id": 1,
                "title": "Angular Developer",
                "organization": "Vue and Me",
                "degree": "Master's",
                "jobType": "Intern",
                "locations": [
                    "Lisbon"
                ],
                "minimumQualifications": [
                    "Mesh granular deliverables, engineer enterprise convergence, and synergize B2C initiatives",
                    "Morph bricks-and-clicks relationships, whiteboard one-to-one experiences, and innovate distributed schemas",
                    "Drive intuitive deliverables, exploit vertical users, and optimize interactive e-commerce",
                    "Embrace sticky infrastructures, incubate B2C portals, and drive killer applications"
                ],
                "preferredQualifications": [
                    "Mesh wireless metrics, syndicate innovative markets, and disintermediate intuitive niches",
                    "Matrix next-generation vortals, cultivate virtual relationships, and unleash wireless platforms",
                    "Brand granular roi, transform mission-critical users, and target value-added models",
                    "Envisioneer b2b web services, aggregate clicks-and-mortar architectures, and target synergistic initiatives"
                ],
                "description": [
                    "Away someone forget effect wait land.",
                    "State even create can either. Character almost turn idea born its to. Understand ability another lose. Smile interesting claim difference.",
                    "Author act increase worry yeah. Positive medical shake include serious check state."
                ],
                "dateAdded": "2021-07-04"
            },
            {
                "id": 2,
                "title": "Java Coder",
                "organization": "VueTube",
                "degree": "Bachelor's",
                "jobType": "Part-time",
                "locations": [
                    "Buenos Aires",
                    "Oslo"
                ],
                "minimumQualifications": [
                    "Redefine ubiquitous supply-chains, whiteboard 24/365 channels, and repurpose dynamic action-items",
                    "Brand mission-critical paradigms, engage enterprise technologies, and re-intermediate sticky mindshare",
                    "Incubate b2c users, repurpose leading-edge convergence, and extend frictionless technologies",
                    "Orchestrate clicks-and-mortar portals, revolutionize turn-key convergence, and expedite bricks-and-clicks action-items"
                ],
                "preferredQualifications": [
                    "Synergize real-time infrastructures, matrix e-business e-tailers, and redefine customized action-items",
                    "Syndicate front-end e-business, optimize granular action-items, and implement best-of-breed technologies",
                    "Facilitate impactful functionalities, extend holistic users, and maximize 24/7 deliverables"
                ],
                "description": [
                    "Form wind put day inside. Say stand apply full boy speak. Memory remain room finish phone. Nation movement place.",
                    "Top person value season. Key best line safe break then. Single music just country.",
                    "Green as something when. Heavy PM head both rate mouth drug nation."
                ],
                "dateAdded": "2021-06-19"
            },
            {
                "id": 3,
                "title": "Svelte Ninja",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Yokohama",
                    "The Hague",
                    "Stockholm",
                    "Ottawa"
                ],
                "minimumQualifications": [
                    "Expedite cross-platform initiatives, empower user-centric models, and revolutionize bleeding-edge e-tailers",
                    "Incubate bricks-and-clicks supply-chains, empower B2B mindshare, and extend integrated functionalities",
                    "Expedite rich convergence, embrace interactive web-readiness, and optimize value-added portals"
                ],
                "preferredQualifications": [
                    "Unleash granular channels, redefine best-of-breed initiatives, and seize efficient ROI",
                    "Transform revolutionary vortals, enhance cross-platform partnerships, and revolutionize robust convergence",
                    "Embrace compelling relationships, enable scalable solutions, and whiteboard front-end synergies",
                    "Brand ubiquitous markets, exploit 24/7 functionalities, and redefine sticky schemas"
                ],
                "description": [
                    "Page significant democratic. Check pretty toward beat church perform.",
                    "Know detail cold degree scene popular then. Maybe result close wall town perhaps.",
                    "Perhaps particularly easy mean black ever professional. Republican physical my effort close admit."
                ],
                "dateAdded": "2021-01-04"
            },
            {
                "id": 4,
                "title": "Software Designer",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Part-time",
                "locations": [
                    "Memphis",
                    "Hong Kong"
                ],
                "minimumQualifications": [
                    "Expedite global experiences, utilize virtual niches, and syndicate cross-platform niches",
                    "Harness impactful roi, drive one-to-one architectures, and repurpose synergistic web-readiness",
                    "Extend e-business action-items, matrix front-end e-business, and drive clicks-and-mortar web-readiness",
                    "Generate frictionless action-items, engage out-of-the-box functionalities, and utilize real-time paradigms"
                ],
                "preferredQualifications": [
                    "Drive vertical mindshare, evolve granular technologies, and benchmark web-enabled channels",
                    "Architect turn-key initiatives, grow frictionless convergence, and maximize one-to-one action-items",
                    "Mesh efficient systems, target mission-critical ROI, and monetize extensible vortals",
                    "Benchmark extensible architectures, innovate virtual networks, and incentivize dot-com e-services"
                ],
                "description": [
                    "Everything always surface prepare level center happen. Nothing out investment crime arm nor event.",
                    "My whose art simply range garden police nor. Firm series difference help new. Pretty response government big will travel certainly. Stuff ok simple eight.",
                    "Set race best the during. Mean two yes door effect near."
                ],
                "dateAdded": "2021-04-02"
            },
            {
                "id": 5,
                "title": "C++ VP",
                "organization": "Point of Vue",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Yokohama"
                ],
                "minimumQualifications": [
                    "Leverage ubiquitous metrics, generate rich deliverables, and target real-time schemas",
                    "Syndicate web-enabled infrastructures, disintermediate B2B channels, and incentivize back-end content",
                    "Streamline cross-platform methodologies, repurpose transparent niches, and incentivize real-time platforms",
                    "Synergize frictionless partnerships, integrate efficient functionalities, and repurpose viral ROI"
                ],
                "preferredQualifications": [
                    "Transition synergistic interfaces, facilitate world-class info-mediaries, and deliver robust e-business",
                    "Enhance strategic interfaces, incubate user-centric e-tailers, and strategize web-enabled experiences",
                    "Maximize scalable e-tailers, productize innovative e-commerce, and cultivate granular mindshare"
                ],
                "description": [
                    "Individual land myself loss treat long. Large commercial final guess others reason. Beautiful sport including deal billion get teach when. Present democratic much boy budget party letter.",
                    "Difficult small positive far cover although reveal. Human hour wide line full national success scientist. Within drop investment. Situation threat star red.",
                    "Thing difficult wear. Key difficult gun despite recently need arrive. Material relationship may result cell remember. Control represent take reality speak."
                ],
                "dateAdded": "2021-01-25"
            },
            {
                "id": 6,
                "title": "Knockout Designer",
                "organization": "Point of Vue",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Glasgow",
                    "Leipzig",
                    "Québec"
                ],
                "minimumQualifications": [
                    "Enable interactive users, empower cutting-edge metrics, and engineer dynamic e-markets",
                    "Cultivate 24/7 e-commerce, extend magnetic ROI, and empower bleeding-edge web services",
                    "Synthesize impactful channels, expedite collaborative platforms, and reinvent value-added e-commerce"
                ],
                "preferredQualifications": [
                    "Enable ubiquitous applications, productize global experiences, and leverage leading-edge networks",
                    "E-enable killer partnerships, seize turn-key action-items, and innovate synergistic e-tailers",
                    "Re-intermediate frictionless technologies, integrate innovative architectures, and revolutionize 24/7 convergence"
                ],
                "description": [
                    "One relationship teach local wide good. Leg green cover meeting.",
                    "Without team how south peace evidence political. Hair during the. Take them else this thus style stand.",
                    "Miss control performance agent price technology. Body idea anyone federal."
                ],
                "dateAdded": "2021-05-25"
            },
            {
                "id": 7,
                "title": "Full Stack Coder",
                "organization": "Vue Can Do It",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Essen",
                    "Detroit",
                    "Buffalo"
                ],
                "minimumQualifications": [
                    "Reinvent plug-and-play methodologies, engage impactful relationships, and synergize front-end technologies",
                    "Transition integrated infrastructures, mesh visionary systems, and implement synergistic synergies",
                    "Generate clicks-and-mortar solutions, mesh holistic platforms, and productize robust content"
                ],
                "preferredQualifications": [
                    "Incentivize customized mindshare, generate transparent web-readiness, and visualize bricks-and-clicks platforms",
                    "Facilitate plug-and-play paradigms, morph vertical convergence, and grow one-to-one solutions",
                    "Unleash frictionless solutions, reinvent dot-com web-readiness, and scale compelling ROI"
                ],
                "description": [
                    "Computer early Democrat when like big attorney answer. Draw discover he mean. Him usually character entire international.",
                    "House turn raise phone become past significant anyone. Practice international line whatever yes once. Write far happy yes.",
                    "One buy ready bit avoid call reality training."
                ],
                "dateAdded": "2021-06-07"
            },
            {
                "id": 8,
                "title": "Angular Developer",
                "organization": "Vue and a Half Men",
                "degree": "Pursuing Degree",
                "jobType": "Part-time",
                "locations": [
                    "Rotterdam"
                ],
                "minimumQualifications": [
                    "Deliver wireless synergies, generate web-enabled paradigms, and aggregate rich communities",
                    "Aggregate global info-mediaries, iterate end-to-end mindshare, and incentivize efficient technologies",
                    "Cultivate holistic interfaces, morph robust deliverables, and reinvent B2B e-business",
                    "Engage ubiquitous e-markets, visualize value-added initiatives, and architect extensible platforms"
                ],
                "preferredQualifications": [
                    "Strategize magnetic applications, exploit integrated schemas, and synergize value-added networks",
                    "Benchmark visionary e-tailers, benchmark intuitive experiences, and unleash intuitive web services",
                    "Incubate bleeding-edge vortals, innovate rich experiences, and implement global technologies",
                    "Utilize open-source applications, optimize B2B supply-chains, and orchestrate next-generation e-tailers"
                ],
                "description": [
                    "Food development if history choose bank. Garden movement determine one.",
                    "Magazine five few artist. Man bring where power figure ok seem.",
                    "Team forward adult participant general study professor. Challenge wait maybe service partner. Few coach future no close increase."
                ],
                "dateAdded": "2021-01-06"
            },
            {
                "id": 9,
                "title": "Go Specialist",
                "organization": "VueTube",
                "degree": "Bachelor's",
                "jobType": "Full-time",
                "locations": [
                    "Jacksonville",
                    "Kyoto"
                ],
                "minimumQualifications": [
                    "Deploy mission-critical web services, revolutionize extensible schemas, and matrix mission-critical infrastructures",
                    "Embrace cross-platform partnerships, matrix virtual channels, and visualize wireless portals",
                    "Scale front-end models, transform out-of-the-box niches, and matrix world-class interfaces"
                ],
                "preferredQualifications": [
                    "Iterate back-end web services, seize one-to-one e-business, and unleash out-of-the-box markets",
                    "Scale strategic metrics, grow leading-edge portals, and e-enable user-centric systems",
                    "Monetize revolutionary e-services, cultivate value-added channels, and mesh turn-key bandwidth",
                    "Re-intermediate granular schemas, streamline user-centric eyeballs, and extend B2C channels"
                ],
                "description": [
                    "Similar final however increase half. Late quite stop half more democratic heavy give. Section finally cost land rule degree admit.",
                    "Possible produce same drop admit.",
                    "Think modern decade standard instead. Experience front teach one maybe. Goal support agree eight."
                ],
                "dateAdded": "2021-01-04"
            },
            {
                "id": 10,
                "title": "Software Supervisor",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Pittsburgh",
                    "Kansas City"
                ],
                "minimumQualifications": [
                    "Reinvent collaborative paradigms, envisioneer scalable schemas, and implement value-added e-business",
                    "Redefine robust technologies, enhance scalable applications, and transition enterprise communities",
                    "Target b2b e-services, reinvent strategic metrics, and utilize rich channels",
                    "Facilitate dynamic supply-chains, innovate integrated technologies, and exploit holistic info-mediaries"
                ],
                "preferredQualifications": [
                    "Extend next-generation bandwidth, maximize user-centric technologies, and revolutionize strategic networks",
                    "Repurpose b2b infrastructures, productize best-of-breed e-services, and incubate wireless relationships",
                    "Streamline viral synergies, benchmark leading-edge convergence, and e-enable mission-critical e-markets"
                ],
                "description": [
                    "Air outside first nothing. Yeah campaign for where deal both leader. Approach individual consumer if author why first.",
                    "Food serve happen. Individual beautiful sure life. Difficult establish entire near.",
                    "Computer soldier during whose receive fall rule. Shake administration more better break others political. Even purpose course rise up surface."
                ],
                "dateAdded": "2021-05-10"
            },
            {
                "id": 11,
                "title": "UI Coder",
                "organization": "Vue and a Half Men",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Kuala Lumpur",
                    "Berlin",
                    "Albuquerque",
                    "Nagoya"
                ],
                "minimumQualifications": [
                    "Harness transparent info-mediaries, empower granular ROI, and enhance scalable solutions",
                    "Aggregate holistic e-tailers, e-enable leading-edge e-markets, and e-enable dynamic metrics",
                    "Re-intermediate intuitive models, harness revolutionary eyeballs, and maximize proactive systems",
                    "Evolve magnetic experiences, productize visionary methodologies, and iterate killer users"
                ],
                "preferredQualifications": [
                    "Aggregate value-added content, implement wireless portals, and disintermediate global applications",
                    "Empower interactive systems, syndicate out-of-the-box relationships, and incubate web-enabled partnerships",
                    "Aggregate b2b users, exploit value-added deliverables, and visualize leading-edge niches"
                ],
                "description": [
                    "Town wrong happy environment federal soon see. Sign bed summer attack.",
                    "Road book significant police. Career kitchen officer research Mrs role. Discussion campaign least state.",
                    "Security unit western it list stage control. Turn begin research sometimes in life. None decide rise fish movie them now."
                ],
                "dateAdded": "2021-01-11"
            },
            {
                "id": 12,
                "title": "CSS VP",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Tokyo",
                    "Orlando",
                    "Milan"
                ],
                "minimumQualifications": [
                    "Monetize dot-com e-commerce, utilize robust markets, and transform cutting-edge relationships",
                    "Architect holistic relationships, expedite cross-platform action-items, and syndicate holistic markets",
                    "Syndicate bricks-and-clicks niches, integrate 24/365 action-items, and empower distributed synergies",
                    "Seize cross-platform markets, maximize revolutionary infrastructures, and facilitate world-class platforms"
                ],
                "preferredQualifications": [
                    "Incubate leading-edge platforms, harness transparent applications, and target compelling channels",
                    "Envisioneer compelling technologies, engage granular bandwidth, and redefine customized channels",
                    "E-enable enterprise mindshare, unleash rich eyeballs, and envisioneer value-added content"
                ],
                "description": [
                    "Mr risk bad security. Star ability property.",
                    "Worry in public leg majority simply. Bit especially goal will life course. Name forward court general never section pick.",
                    "Thank easy much quickly view participant indeed. Around expert form cut."
                ],
                "dateAdded": "2021-05-16"
            },
            {
                "id": 13,
                "title": "Backbone Lead",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Intern",
                "locations": [
                    "Boulder"
                ],
                "minimumQualifications": [
                    "Innovate magnetic solutions, repurpose cross-media e-commerce, and brand dot-com synergies",
                    "Deliver plug-and-play eyeballs, maximize front-end architectures, and e-enable best-of-breed technologies",
                    "Generate open-source networks, syndicate clicks-and-mortar e-markets, and optimize cross-media convergence",
                    "Extend efficient web-readiness, drive cross-media content, and whiteboard end-to-end channels"
                ],
                "preferredQualifications": [
                    "Disintermediate cross-platform web services, grow cross-platform functionalities, and re-contextualize ubiquitous e-business",
                    "Drive next-generation portals, maximize efficient web-readiness, and architect one-to-one infrastructures",
                    "Revolutionize enterprise paradigms, innovate customized communities, and synergize back-end interfaces",
                    "Maximize web-enabled bandwidth, strategize one-to-one systems, and envisioneer granular e-markets"
                ],
                "description": [
                    "Financial song write since ground security week. People provide special push sense create nation large. Hospital travel white join hit security while wall.",
                    "Lay benefit it lead yes. Company tree yeah test top than news. Up wonder manage six. Assume almost like under.",
                    "Whose support trade shake. Eat require concern in guess kind. Official nor personal religious imagine number south."
                ],
                "dateAdded": "2021-06-23"
            },
            {
                "id": 14,
                "title": "C++ Ninja",
                "organization": "Et Vue Brute",
                "degree": "Pursuing Degree",
                "jobType": "Part-time",
                "locations": [
                    "Medellin",
                    "Los Angeles",
                    "Tokyo",
                    "El Paso"
                ],
                "minimumQualifications": [
                    "Syndicate mission-critical portals, optimize sticky content, and re-contextualize frictionless architectures",
                    "Synthesize distributed deliverables, incentivize front-end info-mediaries, and synthesize bricks-and-clicks supply-chains",
                    "Morph out-of-the-box roi, exploit strategic vortals, and implement rich content",
                    "Re-intermediate scalable eyeballs, incentivize plug-and-play info-mediaries, and evolve collaborative ROI"
                ],
                "preferredQualifications": [
                    "Streamline compelling functionalities, incentivize cutting-edge networks, and brand interactive portals",
                    "Deliver value-added action-items, visualize real-time initiatives, and maximize sticky metrics",
                    "Harness innovative paradigms, enable compelling e-markets, and exploit sticky experiences"
                ],
                "description": [
                    "Family from bill sister candidate rate top. Strong official may lay child eye. World public new give put suddenly.",
                    "Second work eight read crime various issue. Property perhaps truth main.",
                    "Prevent Democrat against realize teach. Mention land federal enjoy if cover. Expert start give near half design."
                ],
                "dateAdded": "2021-06-12"
            },
            {
                "id": 15,
                "title": "UI Specialist",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Prague",
                    "Kuala Lumpur",
                    "Buffalo",
                    "Liverpool"
                ],
                "minimumQualifications": [
                    "Monetize impactful methodologies, enable clicks-and-mortar relationships, and grow innovative interfaces",
                    "Transition rich content, visualize innovative niches, and repurpose magnetic metrics",
                    "Synergize seamless markets, re-contextualize e-business synergies, and evolve proactive ROI",
                    "Visualize ubiquitous supply-chains, visualize plug-and-play action-items, and re-intermediate killer systems"
                ],
                "preferredQualifications": [
                    "Re-contextualize virtual eyeballs, mesh dot-com e-commerce, and iterate cross-media paradigms",
                    "Incubate vertical eyeballs, aggregate killer models, and drive intuitive models",
                    "Exploit cross-media eyeballs, synthesize web-enabled convergence, and iterate mission-critical initiatives",
                    "Transition dot-com models, orchestrate plug-and-play platforms, and unleash cutting-edge metrics"
                ],
                "description": [
                    "Information list provide know institution each reduce. Party person strong exactly concern only. High beat fall edge collection treat event.",
                    "Daughter light well. Above final effect technology beat simply yet. Together it meeting require lay property physical. Risk star Mr movie everybody meeting rock.",
                    "Suddenly indeed run miss attack country. Participant either surface speak Mrs our."
                ],
                "dateAdded": "2021-02-26"
            },
            {
                "id": 16,
                "title": "Java Engineer",
                "organization": "VueTube",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Providence",
                    "St Louis",
                    "Bangkok",
                    "Napoli (Naples)"
                ],
                "minimumQualifications": [
                    "Transform revolutionary functionalities, strategize best-of-breed schemas, and maximize bricks-and-clicks channels",
                    "Disintermediate b2b web-readiness, expedite magnetic markets, and envisioneer out-of-the-box systems",
                    "Unleash holistic technologies, incubate frictionless schemas, and morph revolutionary convergence",
                    "Mesh front-end platforms, seize revolutionary paradigms, and syndicate scalable interfaces"
                ],
                "preferredQualifications": [
                    "Grow ubiquitous e-commerce, re-contextualize B2B functionalities, and envisioneer end-to-end functionalities",
                    "Visualize seamless e-services, deploy turn-key markets, and seize global e-business",
                    "Visualize sticky technologies, enhance viral supply-chains, and morph world-class channels"
                ],
                "description": [
                    "Often interest particularly quickly. Agree enough authority history allow.",
                    "Since region station involve. See call thank far.",
                    "Behind sense west. Set difference green stage police place could. Simple generation high effect exactly gas part."
                ],
                "dateAdded": "2021-01-09"
            },
            {
                "id": 17,
                "title": "Backend Developer",
                "organization": "Vue Can Do It",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Phoenix",
                    "Yokohama"
                ],
                "minimumQualifications": [
                    "Target rich web services, integrate mission-critical methodologies, and enable holistic e-commerce",
                    "Engage cross-platform schemas, innovate robust architectures, and monetize front-end networks",
                    "Incubate one-to-one applications, re-contextualize killer applications, and implement collaborative systems",
                    "Incubate collaborative functionalities, aggregate holistic e-tailers, and matrix rich experiences"
                ],
                "preferredQualifications": [
                    "Enhance proactive experiences, leverage bleeding-edge ROI, and implement bleeding-edge portals",
                    "Exploit strategic solutions, e-enable out-of-the-box deliverables, and iterate bleeding-edge vortals",
                    "Streamline scalable eyeballs, engineer vertical portals, and grow innovative niches",
                    "Syndicate 24/7 web services, drive customized info-mediaries, and benchmark compelling ROI"
                ],
                "description": [
                    "Beautiful world wonder others. Detail realize have whether. Peace expect product drug dark his statement.",
                    "Operation north back town adult course sort wall. Election official prevent his music.",
                    "Age appear sister will yourself student though. Political do specific career break. List reflect light expert none."
                ],
                "dateAdded": "2021-06-17"
            },
            {
                "id": 18,
                "title": "Meteor Developer",
                "organization": "Vue and Me",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "San Francisco",
                    "Abu Dhabi",
                    "Boulder",
                    "Tokyo"
                ],
                "minimumQualifications": [
                    "Incubate next-generation models, transition real-time schemas, and maximize bricks-and-clicks supply-chains",
                    "Repurpose distributed roi, envisioneer viral experiences, and scale user-centric networks",
                    "Re-contextualize rich architectures, mesh plug-and-play networks, and brand cross-platform content"
                ],
                "preferredQualifications": [
                    "Cultivate interactive niches, incubate integrated e-markets, and integrate collaborative ROI",
                    "Brand transparent schemas, whiteboard global systems, and streamline granular action-items",
                    "Streamline open-source interfaces, enable 24/365 partnerships, and e-enable B2B e-services"
                ],
                "description": [
                    "Four single term material consider across policy per. Also history good city kind pass.",
                    "Big care television degree natural. Since sit fall do can.",
                    "Gas deep plan like end trouble beat. Begin trial pressure political report some analysis."
                ],
                "dateAdded": "2021-06-12"
            },
            {
                "id": 19,
                "title": "Ember Lead",
                "organization": "VueTube",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Fort Lauderdale",
                    "Chicago",
                    "Bilbao",
                    "Perth"
                ],
                "minimumQualifications": [
                    "Benchmark vertical niches, transform B2C e-business, and streamline synergistic web services",
                    "Embrace customized supply-chains, empower ubiquitous methodologies, and extend sticky communities",
                    "Cultivate wireless schemas, evolve frictionless systems, and evolve B2C e-business",
                    "Repurpose bricks-and-clicks channels, unleash out-of-the-box communities, and benchmark viral mindshare"
                ],
                "preferredQualifications": [
                    "Expedite web-enabled users, orchestrate e-business infrastructures, and scale revolutionary e-tailers",
                    "Transition front-end eyeballs, benchmark best-of-breed eyeballs, and matrix user-centric models",
                    "Envisioneer revolutionary vortals, facilitate back-end portals, and deliver cross-media schemas",
                    "Whiteboard cross-platform niches, target turn-key e-markets, and evolve customized relationships"
                ],
                "description": [
                    "Option read place how foot threat discussion. Question someone cold. Him prevent professor nearly.",
                    "Democrat floor kitchen necessary write until. Daughter church then reason of turn performance.",
                    "Window lead including professor since. Message he already hospital control service. Hair group right suffer on when between politics. Development center until trial."
                ],
                "dateAdded": "2021-01-22"
            },
            {
                "id": 20,
                "title": "TypeScript Wizard",
                "organization": "Et Vue Brute",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Milwaukee"
                ],
                "minimumQualifications": [
                    "Synergize customized web-readiness, cultivate holistic e-business, and innovate wireless technologies",
                    "Iterate b2c communities, engineer holistic models, and syndicate strategic deliverables",
                    "Orchestrate efficient e-commerce, engage 24/7 models, and benchmark innovative systems"
                ],
                "preferredQualifications": [
                    "Brand visionary action-items, visualize scalable schemas, and cultivate value-added models",
                    "Implement integrated partnerships, architect global systems, and innovate 24/365 mindshare",
                    "Architect mission-critical e-commerce, expedite one-to-one info-mediaries, and harness user-centric users",
                    "Drive extensible users, architect proactive channels, and incubate 24/7 relationships"
                ],
                "description": [
                    "Bag course politics blue official not. Possible and age unit too eat staff product.",
                    "Gun life open ask walk task reduce. Poor among try garden present.",
                    "Hospital movie somebody case certainly. Number serve next example oil since. Improve arm top water site personal."
                ],
                "dateAdded": "2021-05-07"
            },
            {
                "id": 21,
                "title": "Ruby VP",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Riverside"
                ],
                "minimumQualifications": [
                    "Exploit holistic applications, syndicate web-enabled synergies, and brand dot-com users",
                    "Exploit collaborative supply-chains, extend end-to-end communities, and iterate user-centric platforms",
                    "Re-intermediate one-to-one synergies, morph sticky mindshare, and iterate open-source e-tailers"
                ],
                "preferredQualifications": [
                    "Harness mission-critical niches, target out-of-the-box relationships, and syndicate dynamic deliverables",
                    "Harness virtual infrastructures, synthesize interactive infrastructures, and generate global supply-chains",
                    "Synthesize real-time eyeballs, harness rich e-commerce, and incentivize collaborative content"
                ],
                "description": [
                    "Determine half go medical trouble force assume bit.",
                    "Turn director speak western tree. Young hit leg product. Newspaper wrong form system hundred east anything him.",
                    "Challenge effort sign be bar term. Race participant concern tonight only determine political."
                ],
                "dateAdded": "2021-04-27"
            },
            {
                "id": 22,
                "title": "CSS Director",
                "organization": "VueTube",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Eindhoven",
                    "New York"
                ],
                "minimumQualifications": [
                    "Drive efficient convergence, repurpose front-end infrastructures, and brand transparent e-business",
                    "Re-contextualize enterprise roi, transition web-enabled functionalities, and drive wireless e-markets",
                    "Enhance granular e-commerce, orchestrate extensible users, and scale bricks-and-clicks functionalities"
                ],
                "preferredQualifications": [
                    "Enable innovative e-business, engineer leading-edge channels, and cultivate world-class web-readiness",
                    "Orchestrate dot-com e-markets, engineer bleeding-edge solutions, and transition plug-and-play deliverables",
                    "Syndicate holistic initiatives, utilize virtual methodologies, and monetize plug-and-play content"
                ],
                "description": [
                    "Land leader citizen. Recognize especially say hot understand. Choice rise base concern.",
                    "Church later now week. His nature everyone million.",
                    "So prevent purpose add great. Process against arm require look everything star property."
                ],
                "dateAdded": "2021-03-20"
            },
            {
                "id": 23,
                "title": "Svelte Manager",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "San Francisco"
                ],
                "minimumQualifications": [
                    "Generate efficient initiatives, innovate viral systems, and transform transparent networks",
                    "Incentivize best-of-breed applications, productize next-generation deliverables, and benchmark killer e-commerce",
                    "Integrate world-class eyeballs, empower impactful niches, and re-contextualize plug-and-play metrics"
                ],
                "preferredQualifications": [
                    "Enable value-added systems, extend real-time infrastructures, and benchmark global content",
                    "Incubate dot-com niches, mesh proactive deliverables, and harness visionary synergies",
                    "Whiteboard enterprise vortals, envisioneer sticky networks, and exploit back-end web services"
                ],
                "description": [
                    "Lay thank task value vote black. Billion amount affect everybody. Military grow baby significant upon candidate.",
                    "All collection ok. Major organization friend purpose quickly though.",
                    "Past few upon challenge."
                ],
                "dateAdded": "2021-03-13"
            },
            {
                "id": 24,
                "title": "CSS Associate",
                "organization": "Point of Vue",
                "degree": "Master's",
                "jobType": "Full-time",
                "locations": [
                    "Beijing"
                ],
                "minimumQualifications": [
                    "Benchmark one-to-one users, leverage 24/365 mindshare, and aggregate virtual web services",
                    "Re-contextualize frictionless networks, re-contextualize collaborative info-mediaries, and optimize ubiquitous systems",
                    "Transform next-generation action-items, leverage efficient markets, and integrate rich schemas",
                    "Generate 24/7 e-commerce, expedite visionary solutions, and strategize proactive users"
                ],
                "preferredQualifications": [
                    "Enhance one-to-one action-items, transition granular communities, and aggregate clicks-and-mortar portals",
                    "Matrix out-of-the-box convergence, whiteboard one-to-one convergence, and streamline holistic systems",
                    "Maximize integrated experiences, leverage frictionless eyeballs, and revolutionize leading-edge web services"
                ],
                "description": [
                    "Adult strategy religious matter security thousand thought. Investment government claim case. Station without thousand agency.",
                    "Right ground range material care study foot.",
                    "Summer state less despite gas. Feel weight region give treatment. Positive four black national focus. Enough treat write book by."
                ],
                "dateAdded": "2021-04-01"
            },
            {
                "id": 25,
                "title": "Frontend Ninja",
                "organization": "Vue and a Half Men",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Montréal"
                ],
                "minimumQualifications": [
                    "Morph world-class web services, syndicate turn-key networks, and deliver plug-and-play bandwidth",
                    "Cultivate bricks-and-clicks e-commerce, e-enable user-centric markets, and exploit global solutions",
                    "Leverage web-enabled technologies, aggregate innovative vortals, and strategize web-enabled infrastructures"
                ],
                "preferredQualifications": [
                    "Embrace one-to-one portals, incubate 24/365 platforms, and evolve integrated deliverables",
                    "Generate clicks-and-mortar architectures, embrace impactful portals, and generate transparent models",
                    "Synergize integrated synergies, utilize cross-media systems, and empower leading-edge methodologies"
                ],
                "description": [
                    "Attorney policy stuff discussion role. Skill institution where cut someone she above. On anything parent give want share. Meet scene teacher talk.",
                    "Take resource group that friend. Beyond piece resource here very church like table. He health happy majority Democrat economy.",
                    "Significant national game development movie add. Responsibility financial population."
                ],
                "dateAdded": "2021-04-29"
            },
            {
                "id": 26,
                "title": "Ember Lead",
                "organization": "VueTube",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Abu Dhabi",
                    "Salt Lake City",
                    "Santiago"
                ],
                "minimumQualifications": [
                    "Mesh user-centric e-commerce, productize open-source vortals, and architect efficient e-business",
                    "Integrate collaborative metrics, scale out-of-the-box channels, and synthesize web-enabled functionalities",
                    "Drive sticky convergence, incentivize visionary deliverables, and iterate B2B methodologies"
                ],
                "preferredQualifications": [
                    "Integrate intuitive architectures, syndicate distributed info-mediaries, and transform 24/365 action-items",
                    "Leverage innovative infrastructures, re-contextualize one-to-one bandwidth, and innovate 24/7 users",
                    "Whiteboard proactive relationships, streamline revolutionary content, and transform sticky relationships",
                    "Re-intermediate frictionless deliverables, benchmark bleeding-edge channels, and incubate 24/365 vortals"
                ],
                "description": [
                    "Attorney fast figure brother me where senior. By work close mouth article pretty professor.",
                    "Claim ok least house once cultural worker. Tend painting suffer bring create.",
                    "Research near decade power. Factor some bag owner sometimes place win quality. Last foot mother only poor heart."
                ],
                "dateAdded": "2021-06-27"
            },
            {
                "id": 27,
                "title": "UI Programmer",
                "organization": "Vue Can Do It",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Copenhagen"
                ],
                "minimumQualifications": [
                    "Redefine proactive models, envisioneer turn-key web-readiness, and mesh revolutionary bandwidth",
                    "Utilize transparent interfaces, orchestrate robust action-items, and transform out-of-the-box experiences",
                    "Benchmark wireless infrastructures, exploit collaborative infrastructures, and innovate strategic relationships",
                    "Facilitate robust models, drive integrated bandwidth, and utilize user-centric schemas"
                ],
                "preferredQualifications": [
                    "Integrate 24/7 e-business, synergize B2B portals, and evolve turn-key synergies",
                    "Aggregate real-time paradigms, optimize killer e-tailers, and cultivate plug-and-play interfaces",
                    "Aggregate 24/365 applications, re-intermediate front-end interfaces, and e-enable efficient mindshare"
                ],
                "description": [
                    "Century thousand page meet send go full. Argue admit should walk social five.",
                    "Stage team doctor attack house prevent. Produce oil almost professor base. Network attack never represent next animal perhaps either.",
                    "Nor name ability cause floor simply. Seek improve trade left mind its."
                ],
                "dateAdded": "2021-02-09"
            },
            {
                "id": 28,
                "title": "Mobile Programmer",
                "organization": "VueTube",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Taipei"
                ],
                "minimumQualifications": [
                    "Enhance intuitive experiences, benchmark magnetic markets, and evolve out-of-the-box deliverables",
                    "Synergize bleeding-edge partnerships, matrix B2B deliverables, and drive revolutionary solutions",
                    "Deploy one-to-one architectures, utilize holistic e-markets, and engage B2B systems"
                ],
                "preferredQualifications": [
                    "Benchmark extensible architectures, productize plug-and-play initiatives, and enhance proactive models",
                    "Enhance virtual niches, streamline bricks-and-clicks communities, and innovate seamless interfaces",
                    "Engineer world-class architectures, target customized markets, and strategize holistic technologies"
                ],
                "description": [
                    "Item off drop. Where sense instead phone crime stage write. Design image production hit.",
                    "Clearly service physical sign dark. Wall boy small meet.",
                    "Soldier run turn spend. Save move marriage chance seat. After cause partner decade across."
                ],
                "dateAdded": "2021-02-17"
            },
            {
                "id": 29,
                "title": "Ember Supervisor",
                "organization": "VueTube",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Fort Lauderdale",
                    "Budapest",
                    "Vancouver"
                ],
                "minimumQualifications": [
                    "Embrace killer initiatives, syndicate world-class vortals, and enhance enterprise users",
                    "Generate revolutionary partnerships, disintermediate next-generation e-commerce, and leverage visionary users",
                    "Disintermediate cross-media solutions, productize mission-critical channels, and disintermediate web-enabled systems"
                ],
                "preferredQualifications": [
                    "Target sticky portals, transition B2B users, and expedite vertical solutions",
                    "Architect real-time mindshare, repurpose bleeding-edge metrics, and maximize innovative solutions",
                    "Orchestrate b2b users, optimize turn-key interfaces, and innovate scalable networks"
                ],
                "description": [
                    "Southern meeting future require science our author. Car what behavior especially. Board my chair decision call.",
                    "Indicate raise player discuss thought yet. Nation letter account sing speak drop. Action spend food away position.",
                    "Rich or however decide. Purpose both past clear face market."
                ],
                "dateAdded": "2021-06-30"
            },
            {
                "id": 30,
                "title": "JavaScript Ninja",
                "organization": "Vue and Me",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Austin",
                    "Prague",
                    "Bilbao"
                ],
                "minimumQualifications": [
                    "Enhance cross-platform action-items, transform back-end networks, and deliver holistic deliverables",
                    "Innovate end-to-end paradigms, synergize dot-com portals, and e-enable transparent e-tailers",
                    "Harness cross-platform channels, matrix clicks-and-mortar metrics, and expedite B2C initiatives"
                ],
                "preferredQualifications": [
                    "Re-contextualize e-business architectures, architect plug-and-play e-markets, and incentivize strategic infrastructures",
                    "Scale next-generation e-business, re-contextualize interactive networks, and engage efficient channels",
                    "Visualize transparent e-commerce, synergize out-of-the-box action-items, and mesh dot-com applications",
                    "Architect bleeding-edge action-items, integrate vertical vortals, and enable world-class supply-chains"
                ],
                "description": [
                    "Value case resource ready evidence meet itself. Training man buy. Skill me day before quickly serious build.",
                    "Yes girl manager outside road door great. Car window Congress myself.",
                    "From toward any maintain. Image including those exactly population always election. Behavior do room rate. Kitchen like wear off college half ok."
                ],
                "dateAdded": "2021-05-21"
            },
            {
                "id": 31,
                "title": "Angular 2 Specialist",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Temporary",
                "locations": [
                    "Lisbon",
                    "Leipzig"
                ],
                "minimumQualifications": [
                    "Drive extensible partnerships, engineer holistic e-business, and target virtual synergies",
                    "Productize customized paradigms, empower clicks-and-mortar platforms, and enable 24/7 schemas",
                    "Integrate best-of-breed e-commerce, innovate intuitive applications, and productize transparent solutions"
                ],
                "preferredQualifications": [
                    "Enhance plug-and-play info-mediaries, reinvent viral ROI, and utilize cross-media networks",
                    "Reinvent efficient interfaces, mesh cross-platform schemas, and enable leading-edge relationships",
                    "Exploit 24/365 portals, monetize transparent communities, and orchestrate cross-platform deliverables"
                ],
                "description": [
                    "Director stay treatment east position eight fire.",
                    "Hope address report test travel college consider. Heart author crime door natural sport. Coach energy anyone seven protect should.",
                    "Class page order. Short writer wait pay best."
                ],
                "dateAdded": "2021-06-15"
            },
            {
                "id": 32,
                "title": "Ruby VP",
                "organization": "Vue Can Do It",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Shenzhen"
                ],
                "minimumQualifications": [
                    "Drive seamless e-business, expedite enterprise synergies, and maximize frictionless web-readiness",
                    "E-enable global eyeballs, target granular experiences, and empower dot-com functionalities",
                    "Cultivate cross-media communities, utilize world-class interfaces, and implement transparent niches",
                    "Scale global interfaces, leverage impactful vortals, and leverage efficient eyeballs"
                ],
                "preferredQualifications": [
                    "Incubate holistic functionalities, target transparent partnerships, and enhance seamless infrastructures",
                    "Brand granular convergence, integrate impactful supply-chains, and benchmark visionary action-items",
                    "Engineer killer methodologies, productize cutting-edge experiences, and engineer holistic applications",
                    "Architect open-source networks, unleash B2C systems, and transform vertical functionalities"
                ],
                "description": [
                    "During letter very give. Follow significant nearly matter size military last. Share others bar page.",
                    "Service scientist late town particular talk. Down nothing both sign concern important. Manage level cultural daughter.",
                    "Series smile cold score environmental local. Television toward necessary personal."
                ],
                "dateAdded": "2021-01-04"
            },
            {
                "id": 33,
                "title": "jQuery Designer",
                "organization": "Vue and a Half Men",
                "degree": "Pursuing Degree",
                "jobType": "Part-time",
                "locations": [
                    "Cologne",
                    "Atlanta",
                    "Milwaukee"
                ],
                "minimumQualifications": [
                    "Target seamless relationships, orchestrate best-of-breed markets, and syndicate enterprise markets",
                    "Enhance seamless solutions, evolve dynamic schemas, and mesh virtual communities",
                    "Unleash magnetic initiatives, synergize bricks-and-clicks web-readiness, and e-enable synergistic systems"
                ],
                "preferredQualifications": [
                    "Reinvent cross-media markets, enable holistic interfaces, and facilitate granular platforms",
                    "Whiteboard cross-media channels, re-intermediate visionary channels, and grow efficient methodologies",
                    "Deploy seamless e-services, orchestrate transparent metrics, and deploy impactful deliverables",
                    "Repurpose clicks-and-mortar communities, aggregate revolutionary relationships, and aggregate cross-platform architectures"
                ],
                "description": [
                    "Interest matter popular inside. About bad like heavy through recent cover.",
                    "Product reveal science radio garden think. Mean record present nearly. Rest win these event society.",
                    "Better their seven billion standard tree official. Some course key piece race. Suggest quality decide bar."
                ],
                "dateAdded": "2021-05-28"
            },
            {
                "id": 34,
                "title": "C++ Manager",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Seattle",
                    "Paris",
                    "Memphis",
                    "Louisville"
                ],
                "minimumQualifications": [
                    "Monetize world-class e-business, integrate B2B schemas, and expedite revolutionary technologies",
                    "Repurpose end-to-end supply-chains, deploy cutting-edge interfaces, and re-contextualize cutting-edge communities",
                    "Exploit granular action-items, scale synergistic models, and facilitate strategic deliverables"
                ],
                "preferredQualifications": [
                    "Expedite sticky deliverables, engage rich markets, and architect innovative web services",
                    "Integrate clicks-and-mortar portals, benchmark magnetic e-business, and cultivate distributed web-readiness",
                    "Visualize next-generation web-readiness, deliver wireless relationships, and scale magnetic functionalities",
                    "Embrace open-source technologies, cultivate leading-edge communities, and scale customized functionalities"
                ],
                "description": [
                    "Space common apply arrive again defense many. Action last own how candidate.",
                    "Raise industry TV sister. Model worker which think pass fast sometimes. See try large above.",
                    "Far owner rate what up heart prepare. Across PM measure surface everybody."
                ],
                "dateAdded": "2021-05-27"
            },
            {
                "id": 35,
                "title": "C++ Director",
                "organization": "Vue Can Do It",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Barcelona",
                    "Montréal",
                    "El Paso"
                ],
                "minimumQualifications": [
                    "Streamline synergistic networks, revolutionize 24/7 eyeballs, and transform world-class functionalities",
                    "Transform bleeding-edge models, transition transparent e-commerce, and drive mission-critical architectures",
                    "Disintermediate open-source e-services, monetize seamless communities, and mesh rich niches"
                ],
                "preferredQualifications": [
                    "Evolve plug-and-play e-services, drive 24/365 ROI, and streamline interactive supply-chains",
                    "Iterate 24/365 info-mediaries, leverage robust content, and repurpose best-of-breed interfaces",
                    "Innovate global technologies, scale collaborative eyeballs, and incubate dot-com web services",
                    "Cultivate clicks-and-mortar e-commerce, scale scalable paradigms, and grow intuitive info-mediaries"
                ],
                "description": [
                    "Really happy current away. National collection detail economy water year point. Keep week especially collection wait. Personal if skin suffer off player bed.",
                    "Character local usually finish truth deal source. Ground area serve serious upon.",
                    "Song area agree technology discussion mouth lot cause. Rock tree sound statement fire chance. Letter painting reach report."
                ],
                "dateAdded": "2021-04-02"
            },
            {
                "id": 36,
                "title": "Full Stack VP",
                "organization": "Vue and Me",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Albany",
                    "Boulder",
                    "Geneva",
                    "Denver"
                ],
                "minimumQualifications": [
                    "Embrace holistic communities, visualize wireless markets, and benchmark killer models",
                    "Whiteboard back-end action-items, engage customized mindshare, and revolutionize 24/7 e-tailers",
                    "Revolutionize out-of-the-box bandwidth, innovate cutting-edge web-readiness, and redefine wireless methodologies"
                ],
                "preferredQualifications": [
                    "Repurpose b2b convergence, harness 24/365 communities, and envisioneer impactful synergies",
                    "Deliver extensible e-markets, deploy extensible interfaces, and reinvent efficient eyeballs",
                    "Productize end-to-end niches, revolutionize intuitive content, and mesh B2B web services"
                ],
                "description": [
                    "World draw same one think instead. Short plan specific management.",
                    "Perhaps her share provide my. Four hand simply agent. Body address life condition foot.",
                    "None Mrs watch loss picture you require. Real small road hotel."
                ],
                "dateAdded": "2021-02-24"
            },
            {
                "id": 37,
                "title": "UI Ninja",
                "organization": "Vue Can Do It",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Jakarta"
                ],
                "minimumQualifications": [
                    "Synergize ubiquitous e-business, matrix front-end vortals, and engineer B2C synergies",
                    "Seize compelling applications, re-intermediate value-added e-tailers, and re-intermediate 24/365 experiences",
                    "Monetize sticky experiences, maximize vertical users, and implement B2C vortals"
                ],
                "preferredQualifications": [
                    "Envisioneer e-business roi, reinvent enterprise e-business, and facilitate transparent vortals",
                    "Monetize frictionless supply-chains, engineer frictionless systems, and innovate granular functionalities",
                    "Implement interactive deliverables, enable leading-edge paradigms, and revolutionize back-end experiences"
                ],
                "description": [
                    "Town decision foreign what can authority teach. It week attack maybe each them.",
                    "Service indeed picture girl PM example large.",
                    "Thing case worker none perform. Black exactly political but. Opportunity stop vote expert beyond blood strong. Soon suddenly assume lead arrive alone suggest."
                ],
                "dateAdded": "2021-05-21"
            },
            {
                "id": 38,
                "title": "Kotlin Specialist",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Toronto",
                    "Perth",
                    "Guangzhou"
                ],
                "minimumQualifications": [
                    "Enable clicks-and-mortar users, enhance web-enabled e-services, and redefine web-enabled systems",
                    "Orchestrate robust supply-chains, monetize compelling methodologies, and cultivate efficient metrics",
                    "Synergize transparent mindshare, e-enable global infrastructures, and innovate ubiquitous info-mediaries"
                ],
                "preferredQualifications": [
                    "Incentivize strategic infrastructures, expedite real-time web services, and synergize global applications",
                    "Architect viral relationships, monetize 24/7 convergence, and productize mission-critical vortals",
                    "Optimize bleeding-edge solutions, mesh dot-com e-commerce, and expedite one-to-one methodologies"
                ],
                "description": [
                    "Lead must less. By smile put.",
                    "Provide thousand well choice it. May create knowledge sign skin.",
                    "Big audience bank million ever skin participant fly. Middle wife control pull compare notice."
                ],
                "dateAdded": "2021-02-23"
            },
            {
                "id": 39,
                "title": "JavaScript Manager",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Sacramento",
                    "Helsinki",
                    "Paris",
                    "Buffalo"
                ],
                "minimumQualifications": [
                    "Brand distributed schemas, streamline innovative solutions, and revolutionize real-time models",
                    "Whiteboard 24/365 functionalities, morph global bandwidth, and unleash vertical experiences",
                    "Reinvent seamless solutions, empower 24/365 vortals, and innovate bleeding-edge systems"
                ],
                "preferredQualifications": [
                    "Enhance compelling mindshare, enhance enterprise metrics, and strategize turn-key methodologies",
                    "Revolutionize user-centric platforms, mesh impactful bandwidth, and integrate bleeding-edge vortals",
                    "Iterate dot-com e-tailers, re-contextualize enterprise e-commerce, and synergize one-to-one portals",
                    "Transition seamless initiatives, architect interactive supply-chains, and unleash vertical relationships"
                ],
                "description": [
                    "Them red better ask believe want prove detail. Which main kitchen political green news city.",
                    "Tv myself blue determine forget treatment. Want fly lose city show. Product century seven reach of I.",
                    "Body very animal professional. Whether detail economic court strategy wear long."
                ],
                "dateAdded": "2021-04-07"
            },
            {
                "id": 40,
                "title": "React Lead",
                "organization": "Vue Can Do It",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Salt Lake City",
                    "Wellington",
                    "Medellin"
                ],
                "minimumQualifications": [
                    "Target 24/7 partnerships, unleash e-business channels, and engage back-end markets",
                    "Maximize dynamic technologies, optimize bleeding-edge content, and generate rich models",
                    "Revolutionize cutting-edge mindshare, disintermediate sticky convergence, and scale robust web services",
                    "Cultivate viral vortals, engage cutting-edge initiatives, and engineer best-of-breed paradigms"
                ],
                "preferredQualifications": [
                    "Enable b2c applications, extend robust content, and morph granular niches",
                    "Exploit collaborative platforms, iterate best-of-breed e-business, and drive cross-media e-services",
                    "Integrate impactful supply-chains, brand strategic models, and strategize viral paradigms",
                    "Incubate collaborative e-markets, innovate distributed markets, and innovate plug-and-play architectures"
                ],
                "description": [
                    "Popular present perhaps teacher couple. Recently local rise range. Explain usually drop TV but.",
                    "South animal process do pay affect point young. Culture police group so how. Detail this mouth ahead know dream successful in.",
                    "Development country network student activity support. Manager police plant baby. Thus either commercial design attack country whom teacher."
                ],
                "dateAdded": "2021-04-11"
            },
            {
                "id": 41,
                "title": "React Coder",
                "organization": "Vue and Me",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Leipzig"
                ],
                "minimumQualifications": [
                    "Leverage frictionless vortals, reinvent value-added e-business, and transform global synergies",
                    "Scale revolutionary solutions, productize killer relationships, and benchmark revolutionary info-mediaries",
                    "Synergize value-added e-markets, revolutionize vertical e-commerce, and engage ubiquitous content",
                    "Expedite best-of-breed methodologies, target cross-platform methodologies, and benchmark 24/365 partnerships"
                ],
                "preferredQualifications": [
                    "Enable cross-media initiatives, expedite real-time relationships, and syndicate cutting-edge e-services",
                    "Incentivize proactive markets, e-enable interactive channels, and e-enable scalable e-commerce",
                    "Expedite rich metrics, integrate viral niches, and embrace rich models"
                ],
                "description": [
                    "Edge traditional meeting election chance pick west. Type understand look full benefit.",
                    "Television computer race letter anyone. Would future building either than color look cell.",
                    "Break have one moment."
                ],
                "dateAdded": "2021-01-16"
            },
            {
                "id": 42,
                "title": "Ruby Lead",
                "organization": "Vue and a Half Men",
                "degree": "Master's",
                "jobType": "Full-time",
                "locations": [
                    "Oporto"
                ],
                "minimumQualifications": [
                    "Syndicate cutting-edge metrics, incentivize cross-platform users, and reinvent ubiquitous info-mediaries",
                    "Evolve next-generation systems, enhance impactful supply-chains, and transition cutting-edge convergence",
                    "Mesh revolutionary e-business, drive interactive e-markets, and transition extensible schemas"
                ],
                "preferredQualifications": [
                    "Enhance compelling roi, target next-generation action-items, and expedite magnetic paradigms",
                    "Monetize frictionless models, incubate dot-com niches, and revolutionize intuitive mindshare",
                    "Aggregate web-enabled partnerships, productize collaborative initiatives, and disintermediate next-generation portals"
                ],
                "description": [
                    "Important player society radio may spring political security. Wide probably old himself keep outside.",
                    "College knowledge money little may. Company high song president. Because evening seem decide open.",
                    "Rate good hear either from thus standard. Practice where religious. Evidence class now they alone add."
                ],
                "dateAdded": "2021-01-02"
            },
            {
                "id": 43,
                "title": "React Native Ninja",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Part-time",
                "locations": [
                    "Guangzhou"
                ],
                "minimumQualifications": [
                    "Enable out-of-the-box interfaces, expedite 24/365 relationships, and grow impactful mindshare",
                    "Generate sticky applications, synthesize intuitive mindshare, and exploit intuitive technologies",
                    "Deliver back-end e-commerce, matrix bricks-and-clicks partnerships, and brand 24/7 paradigms",
                    "Enhance impactful partnerships, harness transparent experiences, and incentivize clicks-and-mortar web-readiness"
                ],
                "preferredQualifications": [
                    "Mesh proactive convergence, brand next-generation content, and incentivize frictionless e-markets",
                    "E-enable b2c metrics, architect B2C mindshare, and scale collaborative architectures",
                    "Optimize 24/7 content, revolutionize dot-com models, and orchestrate seamless methodologies"
                ],
                "description": [
                    "Crime say government expert treatment particularly. Customer concern still day.",
                    "Sister particularly bring. Physical onto herself cold city.",
                    "Book kitchen save reflect north including. Where reduce for teacher."
                ],
                "dateAdded": "2021-06-19"
            },
            {
                "id": 44,
                "title": "Mobile Specialist",
                "organization": "Vue and Me",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Warsaw",
                    "Houston",
                    "Québec",
                    "Budapest"
                ],
                "minimumQualifications": [
                    "Mesh transparent functionalities, streamline best-of-breed platforms, and reinvent seamless metrics",
                    "Architect frictionless eyeballs, architect robust ROI, and productize out-of-the-box web-readiness",
                    "Optimize transparent web services, streamline cross-platform platforms, and transform transparent technologies",
                    "Drive efficient content, grow revolutionary web services, and mesh end-to-end interfaces"
                ],
                "preferredQualifications": [
                    "Re-intermediate collaborative web services, disintermediate distributed infrastructures, and revolutionize customized action-items",
                    "Deliver visionary technologies, redefine extensible solutions, and visualize sticky vortals",
                    "Embrace innovative relationships, grow frictionless schemas, and generate enterprise metrics"
                ],
                "description": [
                    "Stock ok finally environment must son hear.",
                    "Reveal yourself tree available different court artist bed. Drop value statement international coach. Consumer able face cultural floor south.",
                    "Business trouble space wife. Rather toward others event thousand language evening. Your top oil American significant. Finally maintain economic manage she."
                ],
                "dateAdded": "2021-01-11"
            },
            {
                "id": 45,
                "title": "Angular 2 Lead",
                "organization": "Et Vue Brute",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Helsinki"
                ],
                "minimumQualifications": [
                    "Streamline next-generation markets, deploy B2B paradigms, and orchestrate dynamic supply-chains",
                    "Unleash integrated initiatives, transform visionary relationships, and iterate dot-com eyeballs",
                    "Re-intermediate efficient e-commerce, mesh proactive interfaces, and strategize dynamic mindshare"
                ],
                "preferredQualifications": [
                    "Drive seamless eyeballs, monetize open-source convergence, and visualize mission-critical mindshare",
                    "Brand bricks-and-clicks eyeballs, synthesize visionary infrastructures, and harness open-source models",
                    "Deliver open-source e-services, repurpose killer architectures, and whiteboard leading-edge e-markets"
                ],
                "description": [
                    "Carry approach maybe partner business. Agree experience character head.",
                    "Manager outside receive three customer teacher. Need name debate allow project.",
                    "Partner mission always as upon sport. Side particularly place born ago happen group southern. Environmental stock nor society discussion spend write."
                ],
                "dateAdded": "2021-03-08"
            },
            {
                "id": 46,
                "title": "Kotlin Coder",
                "organization": "Vue and a Half Men",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Jacksonville"
                ],
                "minimumQualifications": [
                    "Deploy magnetic e-tailers, generate user-centric models, and re-contextualize clicks-and-mortar paradigms",
                    "Transform global partnerships, strategize dynamic paradigms, and matrix open-source bandwidth",
                    "Synthesize wireless infrastructures, engage robust e-commerce, and exploit compelling applications"
                ],
                "preferredQualifications": [
                    "Seize vertical e-tailers, brand one-to-one experiences, and orchestrate cross-platform applications",
                    "Extend end-to-end niches, exploit cross-media architectures, and incubate visionary markets",
                    "Generate efficient channels, visualize viral web services, and utilize visionary niches",
                    "Redefine revolutionary mindshare, streamline interactive channels, and target holistic interfaces"
                ],
                "description": [
                    "Until building vote. Speech change democratic rock chance left above.",
                    "Mean position total follow pressure everyone ten.",
                    "Full action wait bag personal. Somebody night occur. Many necessary civil listen model development election."
                ],
                "dateAdded": "2021-03-16"
            },
            {
                "id": 47,
                "title": "Frontend Coder",
                "organization": "Vue and a Half Men",
                "degree": "Ph.D.",
                "jobType": "Intern",
                "locations": [
                    "New York"
                ],
                "minimumQualifications": [
                    "Reinvent viral functionalities, embrace seamless ROI, and exploit wireless deliverables",
                    "Evolve one-to-one applications, whiteboard virtual communities, and re-intermediate synergistic networks",
                    "Scale world-class deliverables, innovate next-generation synergies, and revolutionize integrated web services"
                ],
                "preferredQualifications": [
                    "Revolutionize cross-platform models, evolve frictionless content, and incentivize 24/7 initiatives",
                    "Unleash scalable functionalities, embrace e-business e-commerce, and whiteboard web-enabled supply-chains",
                    "Synthesize b2c users, embrace user-centric platforms, and target one-to-one applications"
                ],
                "description": [
                    "Protect red far strategy wonder record. Since others PM house. Do piece involve none all.",
                    "Source necessary town. Full still TV our class represent. Themselves view experience score discover example local.",
                    "Must want note contain heavy eat respond case. Least budget effect fish store. Wear indicate store reflect important both change."
                ],
                "dateAdded": "2021-03-10"
            },
            {
                "id": 48,
                "title": "Swift Wizard",
                "organization": "Vue and Me",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Prague",
                    "Tokyo",
                    "Nagoya"
                ],
                "minimumQualifications": [
                    "Morph scalable portals, extend cutting-edge methodologies, and generate value-added models",
                    "Syndicate out-of-the-box communities, integrate leading-edge e-tailers, and transform cross-media metrics",
                    "Deploy strategic vortals, strategize clicks-and-mortar relationships, and facilitate B2C architectures"
                ],
                "preferredQualifications": [
                    "Syndicate interactive metrics, engineer rich platforms, and extend clicks-and-mortar ROI",
                    "Embrace ubiquitous channels, maximize 24/7 paradigms, and monetize dynamic initiatives",
                    "Incentivize next-generation e-services, drive synergistic architectures, and facilitate customized web services"
                ],
                "description": [
                    "Heavy treat another four ball. Culture your movement stop medical choice attack. Mouth space no wide station region tax.",
                    "Return early yourself remain minute. Record argue old require consumer remember Mrs. Dark performance recognize pattern find.",
                    "Live good significant how."
                ],
                "dateAdded": "2021-06-25"
            },
            {
                "id": 49,
                "title": "HTML Programmer",
                "organization": "VueTube",
                "degree": "Bachelor's",
                "jobType": "Part-time",
                "locations": [
                    "Memphis",
                    "Columbus"
                ],
                "minimumQualifications": [
                    "Utilize proactive eyeballs, facilitate wireless mindshare, and iterate proactive supply-chains",
                    "Reinvent next-generation convergence, transform compelling solutions, and embrace next-generation applications",
                    "Facilitate customized users, revolutionize best-of-breed methodologies, and leverage interactive e-markets"
                ],
                "preferredQualifications": [
                    "Grow synergistic roi, exploit sticky users, and optimize sticky vortals",
                    "Grow cross-media e-services, exploit global web services, and productize clicks-and-mortar initiatives",
                    "Visualize interactive users, aggregate real-time e-business, and empower magnetic action-items",
                    "Envisioneer visionary technologies, drive transparent info-mediaries, and brand back-end technologies"
                ],
                "description": [
                    "Southern worker other them item. Cup seven federal understand room hear. Southern government American already value would meeting.",
                    "Hour event while defense forward everybody form. Soon hear candidate truth. Player major may body education upon sound we.",
                    "Traditional floor various about. Side race true boy style hard box. Work artist treatment want to son."
                ],
                "dateAdded": "2021-03-25"
            },
            {
                "id": 50,
                "title": "Go Supervisor",
                "organization": "Vue and a Half Men",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Barcelona",
                    "Phoenix"
                ],
                "minimumQualifications": [
                    "E-enable best-of-breed solutions, benchmark global deliverables, and implement dynamic e-business",
                    "Engineer customized e-services, repurpose enterprise portals, and matrix end-to-end e-commerce",
                    "Incubate distributed infrastructures, transform dot-com markets, and reinvent holistic technologies",
                    "Utilize interactive paradigms, scale plug-and-play synergies, and iterate extensible web services"
                ],
                "preferredQualifications": [
                    "Cultivate open-source networks, integrate innovative ROI, and whiteboard virtual e-markets",
                    "Engage cutting-edge paradigms, embrace global channels, and cultivate visionary experiences",
                    "Cultivate 24/365 web-readiness, implement intuitive ROI, and scale 24/365 functionalities",
                    "Grow out-of-the-box web services, maximize visionary web services, and generate B2B models"
                ],
                "description": [
                    "Responsibility item senior later attorney. My discover prove memory. Try audience director offer science.",
                    "Consumer somebody bar attack trial skill protect herself.",
                    "Get away yes attack include often."
                ],
                "dateAdded": "2021-02-01"
            },
            {
                "id": 51,
                "title": "Swift Director",
                "organization": "Vue Can Do It",
                "degree": "Bachelor's",
                "jobType": "Full-time",
                "locations": [
                    "Bristol"
                ],
                "minimumQualifications": [
                    "Re-intermediate customized eyeballs, expedite global technologies, and exploit synergistic e-commerce",
                    "Strategize e-business niches, aggregate best-of-breed e-tailers, and unleash front-end applications",
                    "Iterate clicks-and-mortar partnerships, unleash customized ROI, and mesh distributed web services"
                ],
                "preferredQualifications": [
                    "Repurpose impactful relationships, reinvent customized networks, and visualize synergistic experiences",
                    "Facilitate plug-and-play metrics, revolutionize seamless paradigms, and streamline impactful e-commerce",
                    "Mesh granular metrics, maximize interactive e-business, and cultivate value-added convergence"
                ],
                "description": [
                    "Around keep early general this reduce worker. Break even win unit. Much policy song tough.",
                    "Four sport all method I level.",
                    "History manage provide too. Husband police Congress total later program case. Rate rich visit buy try system."
                ],
                "dateAdded": "2021-03-19"
            },
            {
                "id": 52,
                "title": "C Associate",
                "organization": "Et Vue Brute",
                "degree": "Master's",
                "jobType": "Full-time",
                "locations": [
                    "Baltimore",
                    "Napoli (Naples)"
                ],
                "minimumQualifications": [
                    "Reinvent rich experiences, leverage distributed portals, and incentivize transparent infrastructures",
                    "Benchmark vertical metrics, target collaborative architectures, and e-enable efficient synergies",
                    "Innovate front-end web-readiness, streamline plug-and-play supply-chains, and incentivize proactive portals"
                ],
                "preferredQualifications": [
                    "Extend viral interfaces, engineer seamless technologies, and deliver synergistic e-markets",
                    "Maximize enterprise synergies, harness 24/365 e-business, and facilitate holistic supply-chains",
                    "Deliver mission-critical markets, utilize out-of-the-box experiences, and benchmark magnetic bandwidth",
                    "Drive granular convergence, utilize out-of-the-box technologies, and transition wireless convergence"
                ],
                "description": [
                    "Study different discuss loss these. Name break catch material discussion.",
                    "Operation upon red rate. Positive try chance mouth city perform ball. Up less against region break cost administration certainly.",
                    "Address drive end. Stuff office third agreement similar development stay."
                ],
                "dateAdded": "2021-02-21"
            },
            {
                "id": 53,
                "title": "Software Engineer",
                "organization": "Point of Vue",
                "degree": "Associate",
                "jobType": "Full-time",
                "locations": [
                    "Buenos Aires",
                    "Cincinnati",
                    "Brussels",
                    "Stuttgart"
                ],
                "minimumQualifications": [
                    "Mesh viral experiences, cultivate plug-and-play ROI, and re-contextualize cutting-edge relationships",
                    "Exploit compelling roi, whiteboard dot-com e-commerce, and harness extensible networks",
                    "Productize next-generation methodologies, productize 24/7 niches, and exploit web-enabled models"
                ],
                "preferredQualifications": [
                    "Evolve global architectures, strategize vertical paradigms, and morph turn-key interfaces",
                    "Revolutionize dynamic markets, target scalable metrics, and architect enterprise platforms",
                    "Maximize synergistic technologies, expedite visionary systems, and transition end-to-end applications"
                ],
                "description": [
                    "Always compare feeling general. Impact south class finish new hour reduce.",
                    "Because people pressure. From sport crime market painting. Laugh turn choice however little always.",
                    "Room it through matter yes give. Maintain brother news table budget pattern. Behavior tough join mouth region."
                ],
                "dateAdded": "2021-05-03"
            },
            {
                "id": 54,
                "title": "Java Ninja",
                "organization": "Point of Vue",
                "degree": "Pursuing Degree",
                "jobType": "Intern",
                "locations": [
                    "Taipei",
                    "Bangkok",
                    "Portland"
                ],
                "minimumQualifications": [
                    "Utilize efficient partnerships, drive dot-com infrastructures, and re-contextualize bricks-and-clicks deliverables",
                    "Evolve cutting-edge interfaces, synergize rich e-business, and whiteboard integrated networks",
                    "Cultivate cross-platform systems, brand virtual bandwidth, and target cross-media vortals"
                ],
                "preferredQualifications": [
                    "Drive interactive portals, revolutionize granular solutions, and monetize plug-and-play e-commerce",
                    "Evolve back-end roi, incentivize B2B platforms, and integrate cutting-edge synergies",
                    "Synthesize holistic niches, integrate user-centric mindshare, and integrate leading-edge partnerships"
                ],
                "description": [
                    "American either case both free somebody at. Action top indeed. Political hope service current.",
                    "Personal name upon strategy. Both carry music. Main whatever want.",
                    "Someone participant onto eight section. Money activity enter while about religious."
                ],
                "dateAdded": "2021-03-08"
            },
            {
                "id": 55,
                "title": "Go Associate",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Temporary",
                "locations": [
                    "Santiago"
                ],
                "minimumQualifications": [
                    "Benchmark back-end e-markets, aggregate viral experiences, and cultivate granular content",
                    "Repurpose b2b technologies, deploy granular content, and transition viral networks",
                    "Transition strategic relationships, disintermediate 24/7 paradigms, and monetize cross-platform solutions",
                    "Monetize frictionless relationships, orchestrate seamless ROI, and leverage strategic content"
                ],
                "preferredQualifications": [
                    "Monetize front-end content, re-contextualize wireless mindshare, and scale web-enabled methodologies",
                    "Reinvent scalable supply-chains, implement impactful content, and e-enable vertical markets",
                    "Morph customized convergence, synthesize real-time models, and deploy leading-edge eyeballs",
                    "Whiteboard enterprise methodologies, mesh strategic communities, and embrace virtual vortals"
                ],
                "description": [
                    "Sound street sign whole rest. Available end green else. Herself special including safe teacher.",
                    "Get difference very carry whether leg art. Resource effect spring husband carry piece police. Thought check realize.",
                    "Artist who look white shake church assume public. Machine move may sea produce wall. Charge option bring wall evening bank argue."
                ],
                "dateAdded": "2021-02-15"
            },
            {
                "id": 56,
                "title": "Software Coder",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Barcelona",
                    "The Hague"
                ],
                "minimumQualifications": [
                    "Unleash granular convergence, transition cutting-edge relationships, and enable back-end web services",
                    "Leverage open-source partnerships, generate visionary bandwidth, and transform killer communities",
                    "Generate wireless infrastructures, brand robust relationships, and morph value-added interfaces"
                ],
                "preferredQualifications": [
                    "Enhance dot-com markets, unleash web-enabled ROI, and incubate leading-edge e-markets",
                    "Utilize magnetic mindshare, maximize seamless technologies, and aggregate e-business synergies",
                    "Drive cutting-edge vortals, empower dot-com e-commerce, and orchestrate visionary methodologies"
                ],
                "description": [
                    "Left decision deep could create. Vote have speak key model different the knowledge.",
                    "Kid cut trial her middle market. Quickly government direction pass. Television town clear price.",
                    "Hundred turn cell like. Clearly hot per before food bad situation."
                ],
                "dateAdded": "2021-03-19"
            },
            {
                "id": 57,
                "title": "Full Stack Specialist",
                "organization": "Vue and Me",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Brussels",
                    "Leeds",
                    "Honolulu",
                    "Frankfurt"
                ],
                "minimumQualifications": [
                    "E-enable real-time technologies, productize intuitive partnerships, and iterate one-to-one portals",
                    "Incentivize compelling deliverables, seize synergistic infrastructures, and re-contextualize seamless web-readiness",
                    "Synthesize real-time interfaces, drive viral communities, and synergize real-time functionalities"
                ],
                "preferredQualifications": [
                    "Seize bleeding-edge relationships, cultivate holistic infrastructures, and drive plug-and-play schemas",
                    "Deliver proactive bandwidth, visualize real-time content, and redefine back-end metrics",
                    "Maximize one-to-one web services, evolve leading-edge synergies, and transform granular e-markets",
                    "Extend compelling deliverables, grow holistic methodologies, and synergize mission-critical schemas"
                ],
                "description": [
                    "Ask wrong hard meet. After marriage thing party from assume think worry. Budget big morning light suffer. Too audience ask financial father finish whether put.",
                    "Move best action moment. Property measure fund. Stage population arrive interview.",
                    "Whose why learn factor into. Rich fact speech office."
                ],
                "dateAdded": "2021-01-19"
            },
            {
                "id": 58,
                "title": "CSS Supervisor",
                "organization": "Vue and a Half Men",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Memphis",
                    "Budapest",
                    "St Petersburg",
                    "Munich"
                ],
                "minimumQualifications": [
                    "Target distributed networks, mesh seamless initiatives, and deploy efficient vortals",
                    "Expedite compelling partnerships, envisioneer best-of-breed convergence, and productize magnetic web services",
                    "Revolutionize cross-media interfaces, e-enable sticky interfaces, and grow 24/7 networks",
                    "Optimize dynamic architectures, orchestrate out-of-the-box e-tailers, and unleash dynamic technologies"
                ],
                "preferredQualifications": [
                    "Incubate turn-key portals, transform frictionless applications, and evolve viral portals",
                    "Mesh 24/7 paradigms, cultivate open-source systems, and cultivate world-class users",
                    "Iterate 24/365 models, synergize front-end architectures, and iterate visionary content"
                ],
                "description": [
                    "Ten behavior son medical plant begin eye. Few group around organization trade traditional.",
                    "Billion management fine fill rather difference court bad. Key direction program choose color. Say decade floor imagine. Away deep study develop significant.",
                    "Stop artist traditional measure their pull. Mr activity myself specific."
                ],
                "dateAdded": "2021-05-14"
            },
            {
                "id": 59,
                "title": "Swift Lead",
                "organization": "Vue and a Half Men",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Helsinki",
                    "Edinburgh",
                    "The Hague",
                    "Marseille"
                ],
                "minimumQualifications": [
                    "Drive best-of-breed models, maximize wireless metrics, and transition B2B systems",
                    "Reinvent holistic metrics, re-intermediate synergistic info-mediaries, and streamline wireless e-commerce",
                    "Utilize mission-critical content, envisioneer holistic bandwidth, and synergize end-to-end web services"
                ],
                "preferredQualifications": [
                    "Disintermediate scalable communities, harness user-centric ROI, and transform dot-com niches",
                    "Synthesize mission-critical action-items, benchmark out-of-the-box eyeballs, and brand extensible users",
                    "Synthesize web-enabled supply-chains, e-enable scalable users, and streamline sticky action-items",
                    "Synergize user-centric systems, cultivate 24/7 systems, and mesh revolutionary networks"
                ],
                "description": [
                    "Child green agency instead provide character. Before level cold line help sing.",
                    "Might current beautiful trip technology. Meeting single risk performance although. If international attention. Nothing foreign fill describe.",
                    "True paper this. Mission process entire face."
                ],
                "dateAdded": "2021-01-31"
            },
            {
                "id": 60,
                "title": "Backbone Designer",
                "organization": "Et Vue Brute",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Montréal"
                ],
                "minimumQualifications": [
                    "E-enable wireless experiences, integrate scalable functionalities, and target mission-critical users",
                    "Expedite customized methodologies, embrace interactive functionalities, and maximize turn-key supply-chains",
                    "Implement virtual niches, facilitate seamless systems, and target collaborative communities"
                ],
                "preferredQualifications": [
                    "Empower sticky e-markets, extend granular functionalities, and mesh 24/365 applications",
                    "Seize front-end supply-chains, scale magnetic initiatives, and e-enable visionary applications",
                    "Reinvent scalable partnerships, disintermediate cross-platform e-commerce, and matrix cutting-edge metrics",
                    "Empower bleeding-edge channels, synergize cutting-edge partnerships, and extend customized bandwidth"
                ],
                "description": [
                    "Choose above air economic. Point skin floor. Become but eat wife citizen enter.",
                    "Might reveal notice read treatment wall other. We avoid law kind prove song color. Size spend environment approach traditional prepare director.",
                    "Yourself though use teach amount often manager team."
                ],
                "dateAdded": "2021-05-11"
            },
            {
                "id": 61,
                "title": "Swift Manager",
                "organization": "Vue and a Half Men",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Indianapolis",
                    "Seattle",
                    "Las Vegas"
                ],
                "minimumQualifications": [
                    "Unleash e-business platforms, unleash best-of-breed networks, and productize impactful infrastructures",
                    "Maximize turn-key content, re-intermediate killer action-items, and brand front-end initiatives",
                    "Reinvent customized bandwidth, disintermediate web-enabled channels, and iterate revolutionary e-markets"
                ],
                "preferredQualifications": [
                    "Enhance robust synergies, innovate leading-edge mindshare, and engage innovative eyeballs",
                    "Maximize mission-critical vortals, brand 24/7 portals, and engage wireless synergies",
                    "Seize intuitive channels, target 24/7 solutions, and whiteboard viral partnerships",
                    "Revolutionize extensible relationships, generate distributed schemas, and target cutting-edge synergies"
                ],
                "description": [
                    "Picture per finally minute up other edge. Data positive state outside so age person. Car them do government pattern accept turn.",
                    "Sometimes girl remember give. Go Mrs game family but. Action choose move.",
                    "Into say project sport."
                ],
                "dateAdded": "2021-02-13"
            },
            {
                "id": 62,
                "title": "React Programmer",
                "organization": "Et Vue Brute",
                "degree": "Master's",
                "jobType": "Part-time",
                "locations": [
                    "Seoul",
                    "Tokyo",
                    "Seoul"
                ],
                "minimumQualifications": [
                    "Matrix bleeding-edge supply-chains, scale back-end experiences, and scale open-source paradigms",
                    "Expedite sticky interfaces, incubate cutting-edge e-markets, and matrix virtual e-tailers",
                    "Redefine 24/365 infrastructures, optimize intuitive technologies, and expedite frictionless interfaces"
                ],
                "preferredQualifications": [
                    "Iterate intuitive info-mediaries, unleash dynamic synergies, and scale enterprise metrics",
                    "Unleash magnetic schemas, integrate user-centric eyeballs, and transition out-of-the-box architectures",
                    "Redefine turn-key functionalities, generate viral systems, and exploit out-of-the-box metrics"
                ],
                "description": [
                    "Live style however who. Manage degree hear Republican data within want. Close cup weight send issue.",
                    "Tonight give happy commercial dream clear. Boy past staff small. Enough area their all build.",
                    "Before policy impact popular man other. Moment able view good."
                ],
                "dateAdded": "2021-03-15"
            },
            {
                "id": 63,
                "title": "Angular Supervisor",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Intern",
                "locations": [
                    "Oslo",
                    "Calgary"
                ],
                "minimumQualifications": [
                    "Deploy web-enabled platforms, synergize granular ROI, and facilitate wireless applications",
                    "Transform extensible e-commerce, whiteboard cross-platform metrics, and synthesize bricks-and-clicks partnerships",
                    "Enable viral schemas, deploy bricks-and-clicks channels, and utilize mission-critical portals"
                ],
                "preferredQualifications": [
                    "Morph 24/7 infrastructures, seize one-to-one info-mediaries, and redefine B2B action-items",
                    "Repurpose synergistic eyeballs, incubate scalable portals, and orchestrate best-of-breed communities",
                    "Target world-class e-tailers, extend magnetic experiences, and enhance rich communities",
                    "Matrix real-time bandwidth, empower 24/7 e-tailers, and incubate turn-key partnerships"
                ],
                "description": [
                    "Team lead project view require. Month among year former foot. Recently begin huge very not.",
                    "Media appear participant scene course plan run ahead. Difference range finish even indicate.",
                    "Deep party technology reach board. His long free figure international society sign job."
                ],
                "dateAdded": "2021-06-05"
            },
            {
                "id": 64,
                "title": "Go VP",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Zürich",
                    "Manchester"
                ],
                "minimumQualifications": [
                    "Deploy frictionless e-tailers, re-contextualize interactive convergence, and engage back-end content",
                    "Innovate 24/7 mindshare, iterate virtual supply-chains, and engage granular niches",
                    "Brand b2b experiences, harness transparent markets, and redefine magnetic metrics",
                    "Engineer synergistic info-mediaries, utilize customized infrastructures, and reinvent end-to-end systems"
                ],
                "preferredQualifications": [
                    "Seize best-of-breed models, syndicate seamless convergence, and synergize real-time action-items",
                    "Re-intermediate real-time communities, transition customized paradigms, and productize end-to-end applications",
                    "Re-intermediate next-generation channels, integrate transparent metrics, and maximize transparent e-commerce"
                ],
                "description": [
                    "Green still hundred seven fact very weight. Line long risk million treatment material majority edge. Direction civil may.",
                    "Send believe pick they police. Reason professional ask leg ball.",
                    "Including current school fall. Again become ask threat act."
                ],
                "dateAdded": "2021-01-24"
            },
            {
                "id": 65,
                "title": "Full Stack Wizard",
                "organization": "Vue and a Half Men",
                "degree": "Bachelor's",
                "jobType": "Full-time",
                "locations": [
                    "Paris"
                ],
                "minimumQualifications": [
                    "Engage mission-critical technologies, aggregate plug-and-play networks, and scale bricks-and-clicks e-services",
                    "Facilitate best-of-breed markets, innovate 24/365 convergence, and incubate rich niches",
                    "Iterate frictionless synergies, iterate bleeding-edge paradigms, and maximize vertical niches"
                ],
                "preferredQualifications": [
                    "Strategize seamless deliverables, brand global niches, and innovate user-centric networks",
                    "Productize one-to-one bandwidth, benchmark ubiquitous methodologies, and target out-of-the-box markets",
                    "Facilitate dynamic bandwidth, maximize wireless infrastructures, and engage B2B e-markets"
                ],
                "description": [
                    "Bar body beyond figure they. Nice realize subject health way research mother.",
                    "Traditional maintain without floor bill high risk. Certain Mrs game about floor mean daughter. Pretty their power political loss quickly.",
                    "Next glass similar north important office Democrat still. College city box run future beat rate. Show left mention activity ten father vote line."
                ],
                "dateAdded": "2021-04-16"
            },
            {
                "id": 66,
                "title": "Meteor Coder",
                "organization": "Et Vue Brute",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Rio De Janeiro"
                ],
                "minimumQualifications": [
                    "Target global systems, deliver distributed methodologies, and incubate rich systems",
                    "Leverage next-generation synergies, re-contextualize intuitive synergies, and extend plug-and-play paradigms",
                    "Enable end-to-end e-tailers, leverage mission-critical vortals, and empower robust e-markets"
                ],
                "preferredQualifications": [
                    "Leverage revolutionary interfaces, innovate customized systems, and disintermediate robust supply-chains",
                    "Exploit ubiquitous convergence, strategize sticky relationships, and harness B2C infrastructures",
                    "Matrix viral metrics, orchestrate magnetic deliverables, and monetize frictionless schemas",
                    "Repurpose cross-platform channels, enhance scalable convergence, and repurpose efficient e-markets"
                ],
                "description": [
                    "Difficult prove baby strategy focus. Not build realize try quite relate write.",
                    "From trial research physical social share discover. Office Congress matter system. My response any provide fact between.",
                    "What visit arrive last clearly. Phone leave sense staff available hard. Happy hot trial talk only pattern."
                ],
                "dateAdded": "2021-06-21"
            },
            {
                "id": 67,
                "title": "jQuery Manager",
                "organization": "Vue and Me",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Des Moines",
                    "Rome"
                ],
                "minimumQualifications": [
                    "Productize 24/7 action-items, deploy user-centric markets, and extend intuitive technologies",
                    "Expedite world-class e-commerce, re-contextualize next-generation communities, and productize web-enabled models",
                    "Cultivate customized content, enable out-of-the-box partnerships, and maximize turn-key metrics"
                ],
                "preferredQualifications": [
                    "Scale efficient infrastructures, re-intermediate collaborative bandwidth, and enable seamless action-items",
                    "Orchestrate synergistic applications, integrate integrated networks, and embrace bleeding-edge e-services",
                    "Optimize ubiquitous networks, reinvent sticky web services, and orchestrate distributed technologies"
                ],
                "description": [
                    "Course home put fall. Foot maybe better. Word enough country impact commercial can around.",
                    "Color crime avoid age author coach car. At indeed idea shoulder popular carry.",
                    "Anyone brother hand head simple. Whom water create best mention election yes."
                ],
                "dateAdded": "2021-03-07"
            },
            {
                "id": 68,
                "title": "Meteor Coder",
                "organization": "Vue Can Do It",
                "degree": "Pursuing Degree",
                "jobType": "Full-time",
                "locations": [
                    "Delhi"
                ],
                "minimumQualifications": [
                    "Incentivize compelling markets, morph holistic models, and expedite B2B relationships",
                    "Cultivate extensible deliverables, empower customized info-mediaries, and strategize cutting-edge solutions",
                    "Exploit wireless networks, seize world-class content, and unleash best-of-breed mindshare",
                    "Aggregate distributed paradigms, iterate clicks-and-mortar methodologies, and deliver mission-critical convergence"
                ],
                "preferredQualifications": [
                    "Disintermediate leading-edge vortals, seize collaborative content, and redefine cross-platform mindshare",
                    "Morph bricks-and-clicks technologies, evolve bleeding-edge action-items, and engineer scalable infrastructures",
                    "Seize mission-critical synergies, re-intermediate value-added networks, and expedite back-end partnerships"
                ],
                "description": [
                    "War camera official example benefit white. Bar you company center.",
                    "Wind suggest hold ever common worker. South chance thought plan. Analysis lot listen suddenly old region.",
                    "Small mind always serious pretty Democrat no. Your or reach certain."
                ],
                "dateAdded": "2021-06-18"
            },
            {
                "id": 69,
                "title": "Java Associate",
                "organization": "VueTube",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Osaka",
                    "Amsterdam",
                    "Vienna"
                ],
                "minimumQualifications": [
                    "Engineer 24/7 portals, syndicate 24/7 functionalities, and architect global ROI",
                    "Grow real-time experiences, implement turn-key infrastructures, and re-intermediate innovative portals",
                    "Disintermediate mission-critical communities, productize interactive relationships, and utilize back-end methodologies"
                ],
                "preferredQualifications": [
                    "Deliver b2c e-tailers, unleash open-source e-business, and scale dot-com metrics",
                    "Revolutionize frictionless roi, incentivize sticky supply-chains, and exploit extensible web services",
                    "Leverage plug-and-play solutions, architect e-business technologies, and aggregate impactful partnerships"
                ],
                "description": [
                    "Student thank admit garden face. Run join without should.",
                    "Story try personal enjoy. Local lot investment strategy huge win year.",
                    "Help rather performance kind television real country. Whatever including nor thing turn stuff could."
                ],
                "dateAdded": "2021-06-19"
            },
            {
                "id": 70,
                "title": "React Native Manager",
                "organization": "Vue and Me",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Seoul",
                    "Singapore",
                    "Montréal"
                ],
                "minimumQualifications": [
                    "Benchmark cross-media portals, synergize innovative e-business, and seize clicks-and-mortar partnerships",
                    "Syndicate b2c networks, engineer visionary markets, and incentivize holistic networks",
                    "Disintermediate granular partnerships, redefine clicks-and-mortar vortals, and morph world-class e-markets",
                    "Harness out-of-the-box mindshare, facilitate vertical functionalities, and scale leading-edge convergence"
                ],
                "preferredQualifications": [
                    "Whiteboard holistic channels, unleash integrated niches, and syndicate world-class schemas",
                    "Seize collaborative deliverables, transition user-centric channels, and unleash dot-com initiatives",
                    "Grow clicks-and-mortar web services, harness open-source technologies, and expedite rich e-business",
                    "Whiteboard seamless solutions, transition scalable markets, and utilize viral info-mediaries"
                ],
                "description": [
                    "Body lead involve television believe. Example fall remain employee event million point. Friend receive bit continue type.",
                    "Certainly whether really say positive boy expert. Realize better game big specific design. Seven which role value modern rule around. Political goal factor those.",
                    "Near expert down myself office receive edge choose."
                ],
                "dateAdded": "2021-06-08"
            },
            {
                "id": 71,
                "title": "HTML Lead",
                "organization": "Vue Can Do It",
                "degree": "Associate",
                "jobType": "Intern",
                "locations": [
                    "Mumbai",
                    "Miami"
                ],
                "minimumQualifications": [
                    "Integrate compelling markets, morph sticky methodologies, and mesh open-source platforms",
                    "Scale real-time web services, morph visionary supply-chains, and scale 24/7 deliverables",
                    "Syndicate virtual experiences, drive impactful communities, and morph killer solutions",
                    "Unleash killer markets, drive customized web-readiness, and deliver frictionless initiatives"
                ],
                "preferredQualifications": [
                    "Innovate b2c e-markets, scale dynamic web services, and streamline user-centric action-items",
                    "Aggregate holistic initiatives, productize web-enabled markets, and embrace out-of-the-box interfaces",
                    "Revolutionize synergistic web services, implement transparent schemas, and incentivize leading-edge eyeballs"
                ],
                "description": [
                    "Movie go less value attorney seven. Recent officer room beat worry head car.",
                    "All pull however knowledge move try behind. Contain thought television week by their price less.",
                    "Race peace newspaper group indicate in. Today daughter phone Mrs. First man smile decision also wife free."
                ],
                "dateAdded": "2021-06-15"
            },
            {
                "id": 72,
                "title": "Backend Developer",
                "organization": "Vue and Me",
                "degree": "Associate",
                "jobType": "Full-time",
                "locations": [
                    "San Francisco"
                ],
                "minimumQualifications": [
                    "Scale value-added vortals, reinvent mission-critical technologies, and iterate granular bandwidth",
                    "Maximize bricks-and-clicks metrics, engineer rich supply-chains, and redefine best-of-breed relationships",
                    "Drive real-time users, e-enable efficient content, and synergize dynamic e-markets"
                ],
                "preferredQualifications": [
                    "E-enable plug-and-play technologies, aggregate cross-media supply-chains, and strategize visionary web-readiness",
                    "Mesh open-source e-commerce, integrate collaborative e-markets, and synergize scalable systems",
                    "Transform interactive supply-chains, repurpose world-class methodologies, and cultivate seamless architectures",
                    "Reinvent synergistic info-mediaries, engineer best-of-breed deliverables, and monetize viral portals"
                ],
                "description": [
                    "Dog voice onto throw somebody call hair. Free experience beat green number young year. Trip purpose quality central education development.",
                    "Not similar word hundred they yeah color modern. College learn throughout say race. Key left toward research.",
                    "Air this candidate meet eat. Car there quickly hard a admit treatment."
                ],
                "dateAdded": "2021-03-05"
            },
            {
                "id": 73,
                "title": "Kotlin Manager",
                "organization": "Point of Vue",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "New York",
                    "Calgary"
                ],
                "minimumQualifications": [
                    "Envisioneer virtual e-markets, visualize magnetic interfaces, and transform robust action-items",
                    "Integrate one-to-one mindshare, transition proactive e-markets, and exploit seamless action-items",
                    "Envisioneer visionary e-services, drive robust methodologies, and seize leading-edge platforms"
                ],
                "preferredQualifications": [
                    "Re-intermediate integrated architectures, empower revolutionary relationships, and syndicate e-business platforms",
                    "Aggregate one-to-one bandwidth, benchmark bricks-and-clicks mindshare, and synergize synergistic info-mediaries",
                    "Strategize ubiquitous initiatives, embrace wireless markets, and architect revolutionary architectures",
                    "Brand holistic e-commerce, envisioneer e-business models, and orchestrate seamless communities"
                ],
                "description": [
                    "Medical try tend who success worker religious politics. Wonder garden collection too require democratic. Conference federal finish mouth seat.",
                    "Hear event lose we hotel defense. Seven compare pass too course. Husband candidate subject fall north several century.",
                    "Campaign language specific task office give produce. Unit field back interview rise quickly. General affect stop support note wall."
                ],
                "dateAdded": "2021-01-12"
            },
            {
                "id": 74,
                "title": "Meteor Ninja",
                "organization": "Point of Vue",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Fort Lauderdale",
                    "Liverpool"
                ],
                "minimumQualifications": [
                    "Deploy granular applications, strategize e-business e-services, and innovate cutting-edge applications",
                    "Orchestrate bricks-and-clicks e-markets, aggregate synergistic e-tailers, and maximize bleeding-edge solutions",
                    "Deploy plug-and-play partnerships, redefine bleeding-edge users, and redefine enterprise networks",
                    "Strategize leading-edge initiatives, engage front-end supply-chains, and leverage interactive communities"
                ],
                "preferredQualifications": [
                    "Monetize integrated info-mediaries, facilitate granular partnerships, and facilitate enterprise communities",
                    "Transform synergistic e-business, engage dot-com e-commerce, and benchmark global deliverables",
                    "Envisioneer scalable metrics, architect global e-services, and e-enable global synergies"
                ],
                "description": [
                    "Scene head current gas music reason research. Everybody operation say on.",
                    "Their mind total read gas together. Fire high water. Mind about left poor institution spring institution.",
                    "Marriage hit every side. Try difficult debate fine."
                ],
                "dateAdded": "2021-06-07"
            },
            {
                "id": 75,
                "title": "Software Developer",
                "organization": "Vue and a Half Men",
                "degree": "Master's",
                "jobType": "Part-time",
                "locations": [
                    "Los Angeles",
                    "Mexico City",
                    "Fort Lauderdale"
                ],
                "minimumQualifications": [
                    "Expedite global partnerships, leverage scalable portals, and monetize visionary convergence",
                    "Incentivize bricks-and-clicks users, optimize distributed technologies, and transition out-of-the-box ROI",
                    "Benchmark clicks-and-mortar convergence, cultivate strategic experiences, and transform value-added functionalities"
                ],
                "preferredQualifications": [
                    "Maximize next-generation supply-chains, incentivize proactive systems, and incentivize killer markets",
                    "Evolve killer synergies, aggregate dynamic deliverables, and architect seamless technologies",
                    "Deliver vertical communities, mesh end-to-end metrics, and re-intermediate B2B web services",
                    "E-enable wireless solutions, strategize plug-and-play supply-chains, and generate virtual mindshare"
                ],
                "description": [
                    "Order once trial behind. Minute Democrat wonder get quickly attack.",
                    "Similar day role public keep. Economy yet because see leg baby.",
                    "School action in themselves risk reason miss special. Test western federal. Rate firm girl certain. Only subject single trouble accept mention."
                ],
                "dateAdded": "2021-06-05"
            },
            {
                "id": 76,
                "title": "Meteor Developer",
                "organization": "Point of Vue",
                "degree": "Master's",
                "jobType": "Full-time",
                "locations": [
                    "Bristol"
                ],
                "minimumQualifications": [
                    "Monetize cutting-edge communities, enhance 24/7 vortals, and re-intermediate global applications",
                    "Re-contextualize distributed e-markets, transition robust content, and integrate cutting-edge infrastructures",
                    "Aggregate seamless interfaces, monetize plug-and-play relationships, and target wireless mindshare",
                    "Morph mission-critical info-mediaries, incentivize intuitive e-services, and iterate end-to-end info-mediaries"
                ],
                "preferredQualifications": [
                    "Reinvent open-source mindshare, synthesize mission-critical initiatives, and facilitate best-of-breed architectures",
                    "Utilize integrated web services, seize extensible content, and deploy integrated mindshare",
                    "Whiteboard wireless mindshare, facilitate bleeding-edge channels, and aggregate strategic synergies",
                    "Transition efficient mindshare, deliver one-to-one convergence, and re-intermediate impactful experiences"
                ],
                "description": [
                    "Product leg one people share.",
                    "Pm fine detail approach no toward writer. Company time help executive politics.",
                    "Modern culture Congress blood only. Remain suggest work civil eight see."
                ],
                "dateAdded": "2021-02-11"
            },
            {
                "id": 77,
                "title": "jQuery Manager",
                "organization": "VueTube",
                "degree": "Ph.D.",
                "jobType": "Temporary",
                "locations": [
                    "Copenhagen",
                    "Calgary"
                ],
                "minimumQualifications": [
                    "Extend dynamic convergence, unleash value-added e-business, and deliver 24/7 deliverables",
                    "Transition next-generation deliverables, orchestrate robust ROI, and benchmark innovative niches",
                    "Productize out-of-the-box schemas, maximize 24/7 users, and engineer B2B initiatives"
                ],
                "preferredQualifications": [
                    "Leverage best-of-breed vortals, grow strategic eyeballs, and mesh impactful ROI",
                    "Extend visionary metrics, extend visionary ROI, and revolutionize dynamic models",
                    "Unleash web-enabled e-commerce, incentivize open-source experiences, and optimize synergistic bandwidth"
                ],
                "description": [
                    "Message one military eat almost dinner particular theory. Her might care even thus scene already. Cost like management need allow explain. Might Democrat ready special lot second.",
                    "Officer will area share build stay. Race forget hospital national marriage gas. Tend consumer east artist strong of trouble.",
                    "Factor more human two along significant each. Arrive her feel city model make suffer seat. Law city sell newspaper crime buy answer yeah."
                ],
                "dateAdded": "2021-02-28"
            },
            {
                "id": 78,
                "title": "React Supervisor",
                "organization": "Vue and Me",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Toronto",
                    "Hong Kong"
                ],
                "minimumQualifications": [
                    "Matrix seamless schemas, scale value-added metrics, and embrace bleeding-edge content",
                    "E-enable dynamic metrics, strategize front-end e-business, and empower robust models",
                    "Revolutionize web-enabled convergence, aggregate 24/365 supply-chains, and architect end-to-end networks"
                ],
                "preferredQualifications": [
                    "Integrate revolutionary experiences, orchestrate user-centric e-services, and benchmark holistic relationships",
                    "Re-contextualize magnetic platforms, syndicate holistic platforms, and expedite integrated content",
                    "Redefine collaborative paradigms, target value-added solutions, and redefine integrated e-business"
                ],
                "description": [
                    "Financial can become commercial police he.",
                    "Hard second manage sell ball. Difference describe religious deep home old. Choice star success writer.",
                    "Mention PM history white anything per. Better born none charge media light us."
                ],
                "dateAdded": "2021-04-21"
            },
            {
                "id": 79,
                "title": "Java VP",
                "organization": "Vue and Me",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Columbus",
                    "Oakland",
                    "Marseille",
                    "Buenos Aires"
                ],
                "minimumQualifications": [
                    "Synthesize e-business initiatives, benchmark turn-key partnerships, and repurpose magnetic eyeballs",
                    "Deploy next-generation markets, innovate enterprise models, and revolutionize web-enabled systems",
                    "Whiteboard holistic e-commerce, evolve cutting-edge schemas, and synergize virtual mindshare",
                    "Re-contextualize b2c applications, deploy frictionless supply-chains, and matrix world-class interfaces"
                ],
                "preferredQualifications": [
                    "Monetize visionary e-commerce, leverage customized architectures, and drive B2B functionalities",
                    "Seize cross-platform technologies, engineer bricks-and-clicks technologies, and syndicate granular ROI",
                    "Morph killer solutions, mesh front-end schemas, and repurpose revolutionary solutions"
                ],
                "description": [
                    "Have believe professional clear. Summer create approach nearly carry institution century participant. Maintain young young Congress change such run.",
                    "Within their ever either. That question catch customer. Serve letter perform recent structure wait. Book during school people final arrive realize.",
                    "Exist let interview space fall including."
                ],
                "dateAdded": "2021-04-02"
            },
            {
                "id": 80,
                "title": "Backbone Director",
                "organization": "Vue and a Half Men",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Bangkok",
                    "Toulouse",
                    "Delhi",
                    "Bangalore"
                ],
                "minimumQualifications": [
                    "Strategize end-to-end schemas, optimize revolutionary deliverables, and e-enable cutting-edge initiatives",
                    "Engage viral initiatives, exploit global e-commerce, and re-intermediate out-of-the-box ROI",
                    "Syndicate viral experiences, transform front-end ROI, and unleash integrated applications"
                ],
                "preferredQualifications": [
                    "Strategize cross-media networks, unleash dot-com content, and deploy robust synergies",
                    "Seize robust e-tailers, monetize revolutionary info-mediaries, and monetize distributed channels",
                    "Deliver open-source technologies, exploit magnetic relationships, and visualize intuitive paradigms",
                    "Re-contextualize real-time web-readiness, seize clicks-and-mortar platforms, and monetize best-of-breed metrics"
                ],
                "description": [
                    "Make walk meet short feel simply. Hold human reveal red. Customer trade campaign nice.",
                    "Process no red drug. Couple lay people more or hand less.",
                    "Television sometimes story local. Cold food memory back nearly wear consider read. Why seven until forward behavior among beat."
                ],
                "dateAdded": "2021-05-28"
            },
            {
                "id": 81,
                "title": "jQuery Lead",
                "organization": "Et Vue Brute",
                "degree": "Ph.D.",
                "jobType": "Intern",
                "locations": [
                    "Frankfurt",
                    "Medellin",
                    "Las Vegas",
                    "Washington DC"
                ],
                "minimumQualifications": [
                    "Expedite compelling markets, optimize cross-media metrics, and synthesize user-centric functionalities",
                    "Grow integrated supply-chains, enhance wireless niches, and empower seamless convergence",
                    "Enable back-end metrics, grow impactful mindshare, and transition cross-platform experiences"
                ],
                "preferredQualifications": [
                    "Strategize cross-platform web-readiness, scale best-of-breed networks, and generate extensible synergies",
                    "Whiteboard clicks-and-mortar e-markets, synergize frictionless channels, and redefine ubiquitous convergence",
                    "Disintermediate open-source architectures, redefine 24/365 experiences, and generate front-end models",
                    "Orchestrate next-generation functionalities, generate B2B e-business, and orchestrate rich users"
                ],
                "description": [
                    "Floor little manager. Month back little.",
                    "Red than letter company cup. Popular bring news relationship official choice. Employee affect full technology learn big rise.",
                    "However ability moment something. Them another four lose trade."
                ],
                "dateAdded": "2021-02-10"
            },
            {
                "id": 82,
                "title": "PHP Supervisor",
                "organization": "Point of Vue",
                "degree": "Bachelor's",
                "jobType": "Full-time",
                "locations": [
                    "Nashville",
                    "Wellington",
                    "Edinburgh",
                    "Tel Aviv"
                ],
                "minimumQualifications": [
                    "Envisioneer wireless niches, enable integrated e-markets, and scale B2B functionalities",
                    "Utilize efficient e-services, cultivate cutting-edge e-commerce, and seize 24/7 mindshare",
                    "Empower collaborative applications, architect leading-edge convergence, and empower synergistic methodologies",
                    "Generate e-business action-items, grow scalable supply-chains, and innovate seamless solutions"
                ],
                "preferredQualifications": [
                    "Engage user-centric niches, disintermediate ubiquitous synergies, and streamline holistic functionalities",
                    "Enhance enterprise users, empower real-time networks, and deliver B2C e-markets",
                    "E-enable user-centric metrics, mesh customized schemas, and whiteboard ubiquitous e-markets",
                    "Enable open-source initiatives, drive impactful infrastructures, and generate revolutionary e-markets"
                ],
                "description": [
                    "Dark position worry no create language. Recognize expert lawyer traditional agency try.",
                    "Family size trial reflect sell security show. Economy give case across middle office.",
                    "From generation ball against guy. Member system officer father debate. Could at community board opportunity."
                ],
                "dateAdded": "2021-07-01"
            },
            {
                "id": 83,
                "title": "JavaScript Programmer",
                "organization": "Vue and a Half Men",
                "degree": "Associate",
                "jobType": "Temporary",
                "locations": [
                    "Helsinki",
                    "Bangalore",
                    "Perth"
                ],
                "minimumQualifications": [
                    "Syndicate efficient paradigms, expedite turn-key systems, and redefine collaborative mindshare",
                    "Cultivate 24/7 eyeballs, synthesize efficient networks, and extend front-end schemas",
                    "Embrace seamless action-items, optimize 24/365 infrastructures, and maximize out-of-the-box interfaces",
                    "Iterate visionary e-markets, synergize customized networks, and engage visionary synergies"
                ],
                "preferredQualifications": [
                    "Productize efficient methodologies, scale plug-and-play deliverables, and envisioneer compelling systems",
                    "Visualize cutting-edge users, streamline global e-business, and aggregate compelling experiences",
                    "Leverage turn-key experiences, evolve granular ROI, and exploit customized experiences",
                    "Orchestrate impactful architectures, cultivate real-time initiatives, and deploy bleeding-edge interfaces"
                ],
                "description": [
                    "System base visit whose teacher. Friend position someone data child sense factor. Your money treat such step.",
                    "Star thus decision step prove. Source into card service own will power loss. Program history coach cell statement.",
                    "Learn player spring throughout themselves. Pretty issue occur your lawyer director. Key system avoid interest industry."
                ],
                "dateAdded": "2021-05-08"
            },
            {
                "id": 84,
                "title": "Knockout Ninja",
                "organization": "Vue and a Half Men",
                "degree": "Ph.D.",
                "jobType": "Part-time",
                "locations": [
                    "Santiago",
                    "Santa Ana-Anaheim",
                    "Brussels",
                    "Philadelphia"
                ],
                "minimumQualifications": [
                    "Disintermediate collaborative platforms, embrace 24/7 interfaces, and integrate sticky relationships",
                    "Synthesize 24/365 methodologies, empower cutting-edge e-services, and deliver rich e-services",
                    "Redefine customized users, synergize open-source paradigms, and utilize back-end ROI",
                    "Iterate vertical functionalities, aggregate best-of-breed vortals, and visualize integrated markets"
                ],
                "preferredQualifications": [
                    "Exploit front-end e-services, generate B2C functionalities, and transition revolutionary convergence",
                    "Evolve plug-and-play roi, redefine B2B mindshare, and harness granular paradigms",
                    "Extend best-of-breed web-readiness, cultivate bleeding-edge interfaces, and repurpose visionary info-mediaries",
                    "Syndicate ubiquitous relationships, e-enable back-end deliverables, and generate wireless portals"
                ],
                "description": [
                    "Reality catch decision remember every. Difficult well draw group ever room close represent.",
                    "Ability later everyone week general space the. Ago draw specific evidence process power foreign right.",
                    "Discussion federal under now indicate use forward. Build so industry else give management serious spend."
                ],
                "dateAdded": "2021-04-07"
            },
            {
                "id": 85,
                "title": "Svelte Lead",
                "organization": "Vue Can Do It",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "St Louis",
                    "Medellin",
                    "Raleigh-Durham",
                    "Jacksonville"
                ],
                "minimumQualifications": [
                    "Disintermediate innovative eyeballs, engage extensible bandwidth, and drive ubiquitous partnerships",
                    "Exploit innovative e-tailers, transition synergistic niches, and evolve turn-key e-commerce",
                    "Engineer collaborative schemas, syndicate compelling bandwidth, and brand end-to-end users",
                    "Incentivize back-end vortals, utilize virtual models, and innovate efficient convergence"
                ],
                "preferredQualifications": [
                    "Leverage 24/7 users, productize ubiquitous experiences, and empower global synergies",
                    "Utilize sticky e-tailers, integrate world-class bandwidth, and seize web-enabled info-mediaries",
                    "Embrace enterprise communities, enable robust convergence, and re-intermediate sticky infrastructures"
                ],
                "description": [
                    "Hundred probably test build letter.",
                    "Reason operation house pick speech close.",
                    "Candidate usually raise far since phone. Model moment almost. Back eat wish."
                ],
                "dateAdded": "2021-05-19"
            },
            {
                "id": 86,
                "title": "Ember Programmer",
                "organization": "Et Vue Brute",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Fukuoka",
                    "London",
                    "Melbourne"
                ],
                "minimumQualifications": [
                    "Incubate 24/365 roi, grow web-enabled convergence, and engage front-end technologies",
                    "Facilitate integrated interfaces, monetize wireless users, and revolutionize cutting-edge infrastructures",
                    "Utilize back-end e-tailers, monetize end-to-end models, and cultivate compelling content",
                    "Target next-generation methodologies, reinvent dot-com convergence, and productize cross-media models"
                ],
                "preferredQualifications": [
                    "Utilize b2b functionalities, aggregate granular deliverables, and scale visionary e-markets",
                    "Utilize innovative e-markets, drive wireless interfaces, and innovate 24/7 action-items",
                    "Benchmark intuitive functionalities, e-enable sticky users, and repurpose distributed paradigms"
                ],
                "description": [
                    "Laugh concern book space next lose strong. Quality recognize meeting memory director. Message soon organization southern individual question.",
                    "Bring fly including decision anything. Money offer walk role pay.",
                    "Table senior story. City stay avoid glass city far create. Economy office material capital week. House full religious mind develop federal."
                ],
                "dateAdded": "2021-01-29"
            },
            {
                "id": 87,
                "title": "Software Specialist",
                "organization": "Et Vue Brute",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Rotterdam",
                    "Los Angeles"
                ],
                "minimumQualifications": [
                    "Extend leading-edge partnerships, matrix open-source functionalities, and re-contextualize virtual supply-chains",
                    "Optimize magnetic niches, facilitate impactful e-tailers, and transition end-to-end niches",
                    "Revolutionize killer vortals, orchestrate user-centric networks, and drive world-class synergies",
                    "Enable vertical markets, revolutionize next-generation info-mediaries, and synergize synergistic networks"
                ],
                "preferredQualifications": [
                    "Engineer customized portals, strategize ubiquitous networks, and enhance magnetic systems",
                    "Re-intermediate e-business e-commerce, mesh 24/7 e-business, and whiteboard clicks-and-mortar e-tailers",
                    "Drive synergistic e-markets, engage granular info-mediaries, and reinvent innovative info-mediaries"
                ],
                "description": [
                    "Executive section history start first outside music. Teacher education grow office.",
                    "Put past field party picture hair on. Item tonight learn walk.",
                    "Which fear here offer. Effort front something institution."
                ],
                "dateAdded": "2021-03-15"
            },
            {
                "id": 88,
                "title": "Vue Associate",
                "organization": "Vue and Me",
                "degree": "Associate",
                "jobType": "Part-time",
                "locations": [
                    "Tel Aviv"
                ],
                "minimumQualifications": [
                    "Visualize efficient convergence, target turn-key web services, and syndicate turn-key web services",
                    "Synthesize transparent web-readiness, reinvent viral relationships, and reinvent dynamic bandwidth",
                    "Architect visionary portals, harness proactive experiences, and harness world-class partnerships"
                ],
                "preferredQualifications": [
                    "Utilize bleeding-edge e-services, monetize strategic vortals, and embrace efficient communities",
                    "Envisioneer distributed paradigms, reinvent world-class deliverables, and transform cutting-edge markets",
                    "Innovate global systems, target interactive bandwidth, and target real-time infrastructures"
                ],
                "description": [
                    "Television seven finish this answer level begin everybody. Necessary community across popular speech.",
                    "Back market scientist fish pick. Per general up right provide plan heart.",
                    "Three human cut others. Lose term practice opportunity project. Modern speech hot east science. System such raise actually."
                ],
                "dateAdded": "2021-02-16"
            },
            {
                "id": 89,
                "title": "React Native Specialist",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Karlsruhe",
                    "Zürich"
                ],
                "minimumQualifications": [
                    "Envisioneer plug-and-play infrastructures, scale compelling methodologies, and orchestrate strategic applications",
                    "Synergize back-end info-mediaries, architect visionary content, and engage open-source content",
                    "Productize turn-key initiatives, e-enable innovative interfaces, and unleash intuitive technologies"
                ],
                "preferredQualifications": [
                    "Extend plug-and-play e-commerce, strategize dynamic ROI, and innovate ubiquitous relationships",
                    "Strategize visionary networks, re-contextualize 24/7 architectures, and leverage dot-com web services",
                    "Harness e-business technologies, morph viral e-tailers, and redefine visionary e-commerce"
                ],
                "description": [
                    "Nearly sometimes simple create doctor action meeting be. Gas after strong become list response affect.",
                    "Suggest party program name house owner. Or guy half no room. Add social door into section open prove. For fast product section.",
                    "Produce course light space with great. Major true heart that. Republican dinner leader different weight."
                ],
                "dateAdded": "2021-04-20"
            },
            {
                "id": 90,
                "title": "iOS Director",
                "organization": "Vue Can Do It",
                "degree": "Associate",
                "jobType": "Full-time",
                "locations": [
                    "Copenhagen"
                ],
                "minimumQualifications": [
                    "Maximize front-end roi, monetize bricks-and-clicks synergies, and evolve seamless bandwidth",
                    "Whiteboard mission-critical deliverables, transition proactive action-items, and enhance value-added models",
                    "Redefine seamless experiences, drive granular solutions, and re-intermediate clicks-and-mortar synergies",
                    "Brand world-class applications, harness efficient e-services, and transition innovative e-commerce"
                ],
                "preferredQualifications": [
                    "Facilitate back-end communities, iterate synergistic vortals, and re-contextualize global metrics",
                    "Orchestrate dot-com e-business, innovate value-added technologies, and generate proactive platforms",
                    "Syndicate plug-and-play e-commerce, deliver seamless web-readiness, and orchestrate interactive channels"
                ],
                "description": [
                    "Instead world man sort role authority. Store minute office offer front almost. Opportunity analysis who science town specific I.",
                    "Specific change hospital position heart. Officer identify service world least leave either.",
                    "Western water west later. Ability town necessary game network."
                ],
                "dateAdded": "2021-01-08"
            },
            {
                "id": 91,
                "title": "Meteor Lead",
                "organization": "Vue Can Do It",
                "degree": "Master's",
                "jobType": "Full-time",
                "locations": [
                    "Cologne",
                    "San Diego",
                    "Paris"
                ],
                "minimumQualifications": [
                    "Reinvent 24/7 e-business, visualize holistic solutions, and deliver open-source relationships",
                    "Brand cutting-edge models, enhance mission-critical supply-chains, and integrate revolutionary partnerships",
                    "Expedite revolutionary vortals, transition cutting-edge deliverables, and empower enterprise markets",
                    "Optimize frictionless experiences, facilitate sticky applications, and revolutionize proactive mindshare"
                ],
                "preferredQualifications": [
                    "Orchestrate magnetic users, unleash compelling infrastructures, and cultivate mission-critical solutions",
                    "Repurpose e-business e-business, seize one-to-one infrastructures, and maximize intuitive niches",
                    "Whiteboard dot-com communities, grow seamless web-readiness, and visualize compelling deliverables"
                ],
                "description": [
                    "Morning doctor level measure bring leg develop. Far much parent those environmental speak.",
                    "Floor society rule country. Executive growth court third meeting source. Sometimes wife least certain either audience team.",
                    "Six adult probably avoid. Glass question camera TV. Story expert person future."
                ],
                "dateAdded": "2021-05-08"
            },
            {
                "id": 92,
                "title": "Backbone Developer",
                "organization": "Vue and a Half Men",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Lisbon",
                    "Bangalore"
                ],
                "minimumQualifications": [
                    "Drive out-of-the-box methodologies, expedite collaborative infrastructures, and transition turn-key technologies",
                    "Innovate virtual synergies, scale wireless metrics, and facilitate wireless info-mediaries",
                    "Scale frictionless systems, streamline magnetic e-commerce, and generate extensible infrastructures"
                ],
                "preferredQualifications": [
                    "Aggregate cross-media vortals, drive leading-edge ROI, and deploy cutting-edge niches",
                    "Enhance sticky e-services, orchestrate end-to-end bandwidth, and deploy bricks-and-clicks experiences",
                    "Harness dot-com interfaces, productize B2B bandwidth, and mesh intuitive interfaces"
                ],
                "description": [
                    "Trouble a officer rule must material.",
                    "Receive range mind pressure behind that. Bill two from stay fire. Thousand executive argue last score region.",
                    "Hot model tax relationship American. Type consumer reveal thank a draw me go. Action firm film easy."
                ],
                "dateAdded": "2021-05-05"
            },
            {
                "id": 93,
                "title": "Backend Ninja",
                "organization": "Point of Vue",
                "degree": "Bachelor's",
                "jobType": "Intern",
                "locations": [
                    "Vancouver",
                    "Tokyo",
                    "Washington DC"
                ],
                "minimumQualifications": [
                    "Expedite extensible methodologies, orchestrate best-of-breed content, and empower innovative relationships",
                    "Disintermediate bricks-and-clicks web services, productize best-of-breed architectures, and generate distributed content",
                    "Enable sticky channels, drive leading-edge web-readiness, and target seamless e-tailers",
                    "Iterate collaborative e-tailers, synthesize seamless metrics, and enhance killer networks"
                ],
                "preferredQualifications": [
                    "Synergize b2c deliverables, syndicate virtual markets, and scale efficient channels",
                    "Productize best-of-breed networks, redefine frictionless metrics, and benchmark proactive e-services",
                    "Generate extensible applications, transform customized supply-chains, and matrix back-end initiatives",
                    "Embrace viral communities, iterate extensible e-commerce, and exploit killer web services"
                ],
                "description": [
                    "Knowledge product lead my already some. Provide speak area direction reach yeah result.",
                    "But room kind less play song. Us dog note effort different. Thank of improve. Young old young general.",
                    "Most statement herself face any yes space. Officer into form conference kind. Art push new make consider house recently."
                ],
                "dateAdded": "2021-01-25"
            },
            {
                "id": 94,
                "title": "UI Designer",
                "organization": "Point of Vue",
                "degree": "Bachelor's",
                "jobType": "Temporary",
                "locations": [
                    "Busan"
                ],
                "minimumQualifications": [
                    "Redefine front-end networks, drive one-to-one architectures, and productize rich supply-chains",
                    "Leverage back-end web-readiness, deliver interactive web-readiness, and optimize proactive platforms",
                    "Utilize bricks-and-clicks action-items, integrate 24/7 niches, and utilize end-to-end e-tailers"
                ],
                "preferredQualifications": [
                    "Harness seamless channels, transform 24/365 markets, and extend distributed infrastructures",
                    "Re-intermediate out-of-the-box e-markets, generate 24/365 applications, and monetize innovative e-tailers",
                    "Incentivize real-time eyeballs, envisioneer robust schemas, and transition wireless systems",
                    "Aggregate b2b bandwidth, utilize front-end functionalities, and repurpose strategic web services"
                ],
                "description": [
                    "Can region back scene send quality produce himself. Always high activity response.",
                    "Investment under contain establish who real. Store election even girl marriage tax month. Child do site once goal own above.",
                    "Ball anyone seek response business modern. Finally kid feeling across unit reflect court. Already degree skill."
                ],
                "dateAdded": "2021-01-28"
            },
            {
                "id": 95,
                "title": "Kotlin Engineer",
                "organization": "Et Vue Brute",
                "degree": "Pursuing Degree",
                "jobType": "Intern",
                "locations": [
                    "Shanghai",
                    "Madrid"
                ],
                "minimumQualifications": [
                    "Seize dynamic relationships, cultivate granular methodologies, and seize robust synergies",
                    "Engage distributed methodologies, morph killer schemas, and target value-added relationships",
                    "Empower innovative relationships, generate cross-media infrastructures, and enhance plug-and-play applications"
                ],
                "preferredQualifications": [
                    "Enhance web-enabled content, mesh revolutionary users, and empower revolutionary technologies",
                    "Revolutionize distributed mindshare, embrace one-to-one info-mediaries, and optimize bleeding-edge models",
                    "Cultivate end-to-end web services, optimize distributed convergence, and empower web-enabled action-items",
                    "Synthesize world-class e-markets, transition one-to-one markets, and re-contextualize dot-com channels"
                ],
                "description": [
                    "Them small main budget hot kitchen. Just leave say record. Stay we anyone better system century enjoy.",
                    "Matter free billion fund will. White discuss without me positive us. Structure tonight wrong policy open citizen movement.",
                    "Treat recently commercial mention citizen. Social front between ever."
                ],
                "dateAdded": "2021-02-22"
            },
            {
                "id": 96,
                "title": "React Associate",
                "organization": "VueTube",
                "degree": "Master's",
                "jobType": "Temporary",
                "locations": [
                    "Santa Ana-Anaheim",
                    "Singapore",
                    "Mexico City",
                    "Edmonton"
                ],
                "minimumQualifications": [
                    "Incubate integrated networks, incentivize innovative e-services, and synthesize 24/365 info-mediaries",
                    "Generate e-business infrastructures, target viral mindshare, and re-intermediate killer metrics",
                    "E-enable rich functionalities, harness turn-key experiences, and engage robust applications"
                ],
                "preferredQualifications": [
                    "Benchmark frictionless e-business, optimize wireless schemas, and engage intuitive niches",
                    "Enable clicks-and-mortar systems, enable back-end experiences, and integrate frictionless e-commerce",
                    "Optimize visionary functionalities, integrate virtual deliverables, and monetize transparent applications",
                    "Revolutionize open-source niches, iterate virtual paradigms, and engineer synergistic e-commerce"
                ],
                "description": [
                    "Expect stop painting he almost car. Sign look act address.",
                    "Guy begin election. Knowledge black they appear because house. Assume traditional hand green.",
                    "Point important doctor relationship bag. Also trip nice fact."
                ],
                "dateAdded": "2021-01-08"
            },
            {
                "id": 97,
                "title": "Mobile Specialist",
                "organization": "Vue and a Half Men",
                "degree": "Ph.D.",
                "jobType": "Temporary",
                "locations": [
                    "Bilbao",
                    "Prague"
                ],
                "minimumQualifications": [
                    "Iterate 24/365 e-commerce, expedite strategic markets, and visualize vertical web services",
                    "Re-contextualize clicks-and-mortar niches, mesh ubiquitous solutions, and unleash sticky metrics",
                    "Brand enterprise web-readiness, integrate cross-platform channels, and repurpose back-end solutions",
                    "Envisioneer transparent mindshare, seize granular eyeballs, and embrace wireless ROI"
                ],
                "preferredQualifications": [
                    "Engage extensible applications, grow granular solutions, and leverage efficient web-readiness",
                    "Utilize granular supply-chains, engage magnetic paradigms, and envisioneer robust content",
                    "Benchmark end-to-end web-readiness, harness dynamic mindshare, and deploy customized methodologies",
                    "Architect global niches, expedite sticky functionalities, and deploy dynamic eyeballs"
                ],
                "description": [
                    "West eye again the. Life value drop really management thus true design. Crime choose little during.",
                    "Movement participant service. Source clear fight TV short bit least.",
                    "Do list large mother over however mother main. Born from avoid summer situation. Enter pay follow analysis song trial."
                ],
                "dateAdded": "2021-04-30"
            },
            {
                "id": 98,
                "title": "React Native Specialist",
                "organization": "Point of Vue",
                "degree": "Ph.D.",
                "jobType": "Intern",
                "locations": [
                    "Brisbane"
                ],
                "minimumQualifications": [
                    "Synergize real-time convergence, morph e-business networks, and streamline ubiquitous eyeballs",
                    "Empower revolutionary platforms, syndicate value-added web services, and repurpose collaborative experiences",
                    "Incubate bricks-and-clicks initiatives, re-contextualize B2B e-commerce, and brand turn-key niches"
                ],
                "preferredQualifications": [
                    "Empower open-source bandwidth, matrix back-end supply-chains, and grow global e-commerce",
                    "Synthesize open-source web services, re-intermediate wireless relationships, and iterate strategic architectures",
                    "Integrate robust mindshare, syndicate interactive info-mediaries, and incentivize dynamic models",
                    "Reinvent intuitive convergence, deliver rich vortals, and re-contextualize real-time applications"
                ],
                "description": [
                    "Term turn whose community. Might maintain put remember five have base. Force gun return draw suffer certain discuss.",
                    "Executive matter money. Its along position policy yourself so. Style place north cold place success.",
                    "Election statement rate eight radio water each price."
                ],
                "dateAdded": "2021-01-14"
            },
            {
                "id": 99,
                "title": "iOS Lead",
                "organization": "Vue Can Do It",
                "degree": "Ph.D.",
                "jobType": "Full-time",
                "locations": [
                    "Oslo"
                ],
                "minimumQualifications": [
                    "Iterate end-to-end platforms, optimize cross-media convergence, and streamline B2B functionalities",
                    "Empower bricks-and-clicks content, cultivate virtual convergence, and utilize scalable relationships",
                    "Strategize virtual paradigms, matrix front-end e-business, and grow user-centric deliverables"
                ],
                "preferredQualifications": [
                    "Enable enterprise channels, implement cross-platform info-mediaries, and strategize killer systems",
                    "Innovate e-business paradigms, engineer strategic supply-chains, and matrix open-source platforms",
                    "Reinvent out-of-the-box communities, morph customized action-items, and facilitate seamless initiatives"
                ],
                "description": [
                    "Deal however of first. Expert fact night where.",
                    "Size nearly only part although us. Group none home type. Heart figure within contain.",
                    "Central financial present despite. Senior thing house appear ask property. Follow watch race north operation."
                ],
                "dateAdded": "2021-01-26"
            },
            {
                "id": 100,
                "title": "Software Associate",
                "organization": "Point of Vue",
                "degree": "Pursuing Degree",
                "jobType": "Temporary",
                "locations": [
                    "Vancouver",
                    "Cincinnati",
                    "Bangkok",
                    "São Paulo"
                ],
                "minimumQualifications": [
                    "E-enable strategic architectures, expedite 24/365 solutions, and seize visionary web-readiness",
                    "Whiteboard user-centric portals, incubate killer solutions, and expedite customized content",
                    "Monetize revolutionary paradigms, empower efficient models, and engage holistic web-readiness",
                    "Redefine distributed niches, deliver cutting-edge e-business, and disintermediate rich solutions"
                ],
                "preferredQualifications": [
                    "Leverage killer solutions, benchmark holistic communities, and engineer value-added synergies",
                    "Strategize rich convergence, maximize robust relationships, and cultivate scalable deliverables",
                    "Benchmark out-of-the-box eyeballs, matrix e-business e-commerce, and maximize turn-key experiences"
                ],
                "description": [
                    "Try outside offer. Religious politics same wide.",
                    "Rock positive recognize establish my national.",
                    "Answer financial account eat court reveal finally. Pay their capital. This federal defense parent gun."
                ],
                "dateAdded": "2021-01-26"
            }
        ]
    }

