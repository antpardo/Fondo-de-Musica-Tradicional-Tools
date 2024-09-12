# Fondo de Musica Tradicional Tools

This set of tools is designed for the management and the uploading of large amounts of data about informants and pieces of music to the platform of the Fondo de Música Tradicional (FMT). The aim is to improve the quality of the data uploaded to this platform and to reduce the upload time.

With the first version of these tools, developed by Pablo López Rocamora (PhD student, University of Murcia) and Antonio Pardo-Cayuela (University of Murcia), between September 2021 and March 2022, it was possible to collect, organise, format and upload to the FMT data from some 1,500 informants and 23,000 pieces collected by the Joaquín Díaz Foundation. These tools are currently being updated to do the same with some 1,000 informants and 9,300 pieces collected by the researcher Fermín Pardo Pardo, which are located in the Municipal Archive of the City Council of Requena (Valencia, Spain). This task is being carried out by Albert López López (Conservatorio de Molina de Segura, Murcia, Spain) and Antonio Pardo-Cayuela (Universidad de Murcia).

The toolkit consists of the following elements

- A database in SQLite format with three tables: (a) "team_data", which contains the usernames, passwords and other specific data of FMT staff; (b) "informants", which collects the data of traditional music performers according to the model used in FMT; and (c) "pieces", which contains the data of musical pieces, also according to the model defined in FMT. The definition of the database can be found in the file FMT_database.txt.

- The files (a) addinformantFMT.py, (b) addpieceFMT.py, (c) updatepieceFMT.py and checkinformant.py, that adds informants, adds pieces, updates the information of the pieces from the local database to the online FMT platform, respectively. A new tool have been recently added: the file ckeckinformant.py, which checks whether the informants selected from the table "informants" have been added to FMT already, in order to avoid duplicates.
 
## About the FMT

The Fondo de Música Tradicional (FMT) of the Institution Milá y Fontanals of Research in Humanities (IMF-CSIC) in Barcelona is a comprehensive collection comprising a physical archive and an open-access digital platform. The physical archive contains over 25,000 melodies gathered between 1944 and 1960 from all regions of Spain. This was accomplished through "folkloric missions" and contests organized by the former Instituto Español de Musicología of the CSIC in Barcelona. The archive includes documentation on researchers, musical recordings in various formats, films, and historical audiovisual devices.

Since 2013, the digitized and cataloged materials are accessible on the FMT digital platform (https://musicatradicional.eu/es/home, ISSN 2564-8500). Created by Emilio Ros-Fabregas, this platform is considered the most significant digital repository of oral tradition music in the Hispanic world. By April 2023, it included over 48,000 pieces from 9,300 informants in 3,900 locations.

This musicological project makes an invaluable Spanish traditional music collection available to researchers and the public, enabling comparative studies. The collection identifies individuals who contributed to the repertory, allowing descendants to reconnect with their family's musical history. The website is a resource for researchers, music teachers, organizations promoting traditional music revival, and individuals exploring their cultural heritage. It also incorporates audio and video files, contributing to understanding the relationship between oral traditions in Spain and the Americas.

The FMT received support from the Fundación General CSIC in the 2015-2016 biennium for digitization and equipment renewal. Research on Fondo de Música Tradicional CSIC-IMF was part of the R+D Project "Hispanic Polyphony and Music of Oral Tradition in the Age of Digital Humanities" (HAR2016-75371-P, Spanish Ministry of Science and Innovation, 2016-2020). The website encourages user participation through a Facebook page, facilitating the sharing of personal experiences related to the music repertoire in the Fondo de Música Tradicional.

At present, the development of the FMT is an objetive of the R+D Proyect entitled "Desarrollo digital del Fondo de Música Tradicional IMF-CSIC" (TED2021-130843B-I00)  ("Convocatoria 2021 de proyectos estratégicos orientados a la transición ecológica y a la transición digital en el marco del plan de recuperación, transformación y resiliencia"), a grant funded by the Spanish Ministerio de Ciencia e Innovación (MCIN)/AEI/10.13039/501100011033/ and the European Union NextGenerationEU/PRTR. Period: 1/12/2022 to 30/11/2024. PI: Emilio Ros-Fábregas.

Research Team: 
- María Gembero-Ustárroz (IMF-CSIC)
- Ascensión Mazuela-Anguita (Universidad de Granada)
- Antonio Pardo-Cayuela (Universidad de Murcia)
- Andrea Puentes-Blanco (IMF-CSIC) 
- Emilio Ros-Fábregas (IMF-CSIC). 

Work Team: 
- María del Mar Miranda-López (contratada posdoctoral Margarita Salas, Universitat de Girona / IMF-CSIC)
- Miguel López-Fernández (Conservatorio Superior de Música "Manuel Castillo" de Sevilla)
- Antoni Llofriu-Prohens (doctorando, Universitat de Barcelona)
- Pablo López-Rocamora (doctorando, Universidad de Murcia)
- Juan Francisco Perez Fuentes (Conservatorio Profesional de Música "Ángel Barrios" de Granada). 


