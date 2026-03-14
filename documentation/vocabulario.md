# Vocabulario

## Clases

| Término  | IRI      | Descripción |
|:-------- |:--------:|:--------:|
| Hospital | `schema:Hospital` | Centro sanitario destinado a la prestación de servicios asistenciales |
| HospitalType | `hosp:HospitalType` | Categoría utilizada para clasificar un hospital según su tipología |
| FunctionalDependency | `hosp:FunctionalDependency` | Tipo de dependencia funcional de un hospital dentro del sistema sanitario |
| ConcertAgreement | `hosp:ConcertAgreement` | Tipo de concierto sanitario asociado a un hospital |
| Municipality | `hosp:Municipality` | Entidad administrativa correspondiente a un municipio |
| AutonomousCommunity | `hosp:AutonomousCommunity` | Entidad administrativa correspondiente a una comunidad autónoma |
| Country | `schema:Country` | Entidad administrativa correspondiente a un país |
| PostalAddress | `schema:PostalAddress` | Dirección postal asociada a una entidad o lugar |
| AdministrativeArea | `schema:AdministrativeArea` | Área administrativa utilizada para representar divisiones territoriales |
| MedicalOrganization | `schema:MedicalOrganization` | Organización médica en el contexto de `schema.org` |
| Organization | `schema:Organization` | Organización o entidad institucional en el contexto de `schema.org` |
| CivicStructure | `schema:CivicStructure` | Infraestructura cívica en el contexto de `schema.org` |
| Place | `schema:Place` | Lugar físico en el contexto de `schema.org` |

## Object properties

| Término  | IRI      | Dominio | Rango | Descripción |
|:-------- |:--------:|:--------:|:--------:|:--------:|
| hasHospitalType | `hosp:hasHospitalType` | `schema:Hospital` | `hosp:HospitalType` | Relaciona un hospital con su tipología |
| hasFunctionalDependency | `hosp:hasFunctionalDependency` | `schema:Hospital` | `hosp:FunctionalDependency` | Relaciona un hospital con su dependencia funcional |
| hasConcertAgreement | `hosp:hasConcertAgreement` | `schema:Hospital` | `hosp:ConcertAgreement` | Relaciona un hospital con el tipo de concierto sanitario asociado |
| containedInRegion | `hosp:containedInRegion` | `hosp:Municipality` | `hosp:AutonomousCommunity` | Indica la comunidad autónoma en la que se sitúa un municipio |
| containedInCountry | `hosp:containedInCountry` | `hosp:AutonomousCommunity` | `schema:Country` | Indica el país en el que se sitúa una comunidad autónoma |
| address | `schema:address` | `schema:Hospital` | `schema:PostalAddress` | Relaciona un hospital con su dirección postal |
| addressLocality | `schema:addressLocality` | `schema:PostalAddress` | `hosp:Municipality` | Relaciona una dirección postal con un municipio |
| addressRegion | `schema:addressRegion` | `schema:PostalAddress` | `hosp:AutonomousCommunity` | Relaciona una dirección postal con una comunidad autónoma |
| addressCountry | `schema:addressCountry` | `schema:PostalAddress` | `schema:Country` | Relaciona una dirección postal con un país |

## Datatype properties

| Término  | IRI      | Dominio | Rango | Descripción |
|:-------- |:--------:|:--------:|:--------:|:--------:|
| name | `schema:name` | `schema:Hospital` | `xsd:string` | Nombre de un hospital |
| telephone | `schema:telephone` | `schema:Hospital` | `xsd:string` | Números de teléfono de contacto de un hospital |
| ccnCode | `hosp:ccnCode` | `schema:Hospital` | `xsd:int` | Código CCN de un hospital |
| cnhCode | `hosp:cnhCode` | `schema:Hospital` | `xsd:int` | Código CNH de un hospital |
| numberOfBeds | `hosp:numberOfBeds` | `schema:Hospital` | `xsd:int` | Número de camas instaladas en un hospital |
| teachingAccreditation | `hosp:teachingAccreditation` | `schema:Hospital` | `xsd:boolean` | Indica si un hospital dispone de acreditación docente |
| streetAddress | `schema:streetAddress` | `schema:PostalAddress` | `xsd:string` | Dirección postal de un hospital |
| postalCode | `schema:postalCode` | `schema:PostalAddress` | `xsd:string` | Código postal de la dirección asociada a un hospital |
