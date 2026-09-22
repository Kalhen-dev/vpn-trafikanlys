# Loggblad — Fas 4


Fyra scenarion × tre omgångar 
Paketfångst görs **en gång per scenario** — inte i varje omgång.

---

## Referensvärden

| Uppgift                   | Värde                           |
| ------------------------- | ------------------------------- |
| Egen publik IP (utan VPN) | maskerad                        |
| srv01 publik IP           | maskerad                        |
| Abonnemangets hastighet   | 300/300 telia                   |
| Ping-mål                  | 1.1.1.1                         |
| Nedladdningsfil           | ash-speed.hetzner.com/100MB.bin |

---

## Omgång 1

**Datum:** 2026-09-17
**Starttid:** 16:33
**Anmärkning om tillfället:** Gjord torsdag 

| Scenario       | Klockslag | Publik IP       | Ping medel | Min  | Max  | Förlust % | Tid s | MB/s  | Anmärkning                                                       |
| -------------- | --------- | --------------- | ---------- | ---- | ---- | --------- | ----- | ----- | ---------------------------------------------------------------- |
| `01-utan-vpn`  | 16;33     | maskerad        | 4ms        | 4ms  | 7ms  | 0         | 9,87  | 10,13 |                                                                  |
| `02-wireguard` | 16:44     | maskerad        | 7ms        | 6ms  | 10ms | 0         | 7,95  | 12.58 |                                                                  |
| `03-nordvpn`   | 16:58     | 187.15.110.177  | 5ms        | 5ms  | 12ms | 0         | 4.39  | 22.89 |                                                                  |
| `04-protonvpn` | 17:09     | 185.184.195.135 | 27ms       | 26ms | 45ms | 46%       | ~     | ~     | tog 6 minuter att mäta, samt server NL. Nedladning misslyckad 2x |

### Paketfångst — görs endast i omgång 1

| Scenario       | Filnamn                    | Klockslag   | Anmärkning |
| -------------- | -------------------------- | ----------- | ---------- |
| `01-utan-vpn`  | `01-utan-vpn-omg1.pcapng`  | 16:38-16:39 |            |
| `02-wireguard` | `02-wireguard-omg1.pcapng` | 16:48:16:49 |            |
| `03-nordvpn`   | `03-nordvpn-omg1.pcapng`   | 17:04-17:05 |            |
| `04-protonvpn` | `04-protonvpn-omg1.pcapng` | 17:47-17:48 |            |

### Traceroute — görs endast i omgång 1

| Scenario       | Antal hopp | Anmärkning om vägen                 |
| -------------- | ---------- | ----------------------------------- |
| `01-utan-vpn`  | 11         | Via stockholm till cloudflares nät. |
| `02-wireguard` | 12         |                                     |
| `03-nordvpn`   | 9          | via stockholm till cloudflare       |
| `04-protonvpn` | 13         | Request timed out                   |

---

## Omgång 2

**Datum:** 2026-09-18
**Starttid:** 12:04
**Anmärkning om tillfället:** 

| Scenario       | Klockslag | Publik IP     | Ping medel | Min  | Max   | Förlust % | Tid s | MB/s  | Anmärkning                                                                                                        |
| -------------- | --------- | ------------- | ---------- | ---- | ----- | --------- | ----- | ----- | ----------------------------------------------------------------------------------------------------------------- |
| `01-utan-vpn`  | 12:04     | maskerad      | 4ms        | 4ms  | 12ms  | 0         | 9,47  | 10,56 |                                                                                                                   |
| `02-wireguard` | 12:36     | maskerad      | 7ms        | 6ms  | 12ms  | 0         | 8,72  | 11,46 |                                                                                                                   |
| `03-nordvpn`   | 12:40     | 187.15.109.25 | 4ms        | 4ms  | 5ms   | 0         | 4,19  | 23,83 | Blev uppringd på discord så fick packetloss så blev att göra om ping mättningen                                   |
| `04-protonvpn` | 12:45     | 205.147.17.29 | 29ms       | 13ms | 113ms | 0         | 5,15  | 19.41 | Ingen packet loss denna dag på ping. Nedladning gav information denna omgång. Server blev norge så inte förvånat. |

---

## Omgång 3

**Datum:** 2026-09-19
**Starttid:** 15:10
**Anmärkning om tillfället:** 

| Scenario       | Klockslag | Publik IP       | Ping medel | Min | Max | Förlust % | Tid s | MB/s  | Anmärkning                             |
| -------------- | --------- | --------------- | ---------- | --- | --- | --------- | ----- | ----- | -------------------------------------- |
| `01-utan-vpn`  | 15:10     | maskerad        | 4          | 4   | 7   | 0         | 6,92  | 14,43 |                                        |
| `02-wireguard` | 15:12     | maskerad        | 6          | 6   | 18  | 0         | 7,33  | 13,64 |                                        |
| `03-nordvpn`   | 15:17     | 187.15.111.108  | 4          | 4   | 9   | 0         | 6,09  | 16,40 |                                        |
| `04-protonvpn` | 15:23     | 195.242.214.214 | 114        | 114 | 117 | 2%        | 18,71 | 5,34  | 2% förlust, fick idag kanada som land. |

---

# Sammanställning


## Latens — medelvärden över fem omgångar

| Scenario       | Omg 1 | Omg 2 | Omg 3  | Medel   | Förlust   |
| -------------- | ----- | ----- | ------ | ------- | --------- |
| `01-utan-vpn`  | 4 ms  | 4 ms  | 4 ms   | 4,00 ms | 0% alla   |
| `02-wireguard` | 7 ms  | 7 ms  | 6 ms   | 6,67 ms | 0% alla   |
| `03-nordvpn`   | 5 ms  | 4 ms  | 4 ms   | 4,33 ms | 0% alla   |
| `04-protonvpn` | 27 ms | 29 ms | 114 ms | 56,7 ms | 46%/0%/2% |

## Throughput — MB/s över fem omgångar

| Scenario       | Omg 1      | Omg 2 | Omg 3 | Medel | Spridning |
| -------------- | ---------- | ----- | ----- | ----- | --------- |
| `01-utan-vpn`  | 10,13      | 10,56 | 14,43 | 11,71 |           |
| `02-wireguard` | 12,58      | 11,46 | 13,64 | 12,56 |           |
| `03-nordvpn`   | 22,89      | 23,83 | 16,40 | 21,04 |           |
| `04-protonvpn` | misslyckad | 19,41 | 5,34  | 12,38 |           |

## Overhead jämfört med baslinjen

Räknas ut från medelvärdena ovan.

| Scenario       | Latens +ms | Latens +% | Throughput −MB/s | Throughput −% |
| -------------- | ---------- | --------- | ---------------- | ------------- |
| `02-wireguard` | +2,67 ms   | +67%      | +0,85 MB/s       | +7%           |
| `03-nordvpn`   | +0,33 ms   | +8%       | +9,33 MB/s       | +80%          |
| `04-protonvpn` | +52,7 ms   | +1317%    | +0,67 MB/s       | +6%           |

---

# Analys av paketfångsterna

Fylls i när fångsterna analyserats i Wireshark.

| Mätvärde | 01 utan VPN | 02 WireGuard | 03 NordVPN | 04 ProtonVPN |
|---|---|---|---|---|
| Antal DNS-frågor |  |  |  |  |
| Unika domäner |  |  |  |  |
| Unika destinations-IP |  |  |  |  |
| TLS SNI synligt |  |  |  |  |
| Okrypterade HTTP-anrop |  |  |  |  |
| Totalt antal paket |  |  |  |  |
| Dominerande protokoll |  |  |  |  |

## Domäner som exponerades utan VPN

Lista de mest talande. Särskilt bakgrundstrafik du inte själv initierade.

| Domän | Vad den avslöjar |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

---

# Avvikelser och observationer

Skriv ner allt som inte gick som planerat. Det blir diskussionsdelen i rapporten.

| Datum | Omgång | Scenario | Vad som hände | Åtgärd |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

*Gymnasiearbete 2026 · Carl-Henrik Catry*
