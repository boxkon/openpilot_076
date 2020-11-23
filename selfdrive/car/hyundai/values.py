from cereal import car
from selfdrive.car import dbc_dict
from common.params import Params
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  STEER_MAX = 409   # 409 is the max, 255 is stock
  STEER_DELTA_UP = 5
  STEER_DELTA_DOWN = 10
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1


class CAR:
  # genesis
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_G90 = "GENESIS G90 2017"
  GENESIS_G90_L = "GENESIS G90 LIMOUSINE"

  AVANTE = "HYUNDAI AVANTE"
  SONATA = "HYUNDAI SONATA"
  SONATA_HEV = "HYUNDAI SONATA Hybrid"
  SONATA_TURBO = "HYUNDAI SONATA Turbo"
  GRANDEUR = "HYUNDAI GRANDEUR"
  GRANDEUR_HEV = "HYUNDAI GRANDEUR Hybrid"
  GENESIS = "GENESIS"
  SANTAFE = "HYUNDAI SANTAFE"
  KONA = "HYUNDAI KONA"
  KONA_HEV = "HYUNDAI KONA Hybrid"
  KONA_EV = "HYUNDAI KONA ELECTRIC"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID"
  IONIQ_EV = "HYUNDAI IONIQ ELECTRIC"
  K5 = "KIA K5"
  K5_HEV = "KIA K5 Hybrid"
  K7 = "KIA K7"
  K7_HEV = "KIA K7 Hybrid"
  STINGER = "KIA STINGER"
  SORENTO = "KIA SORENTO"
  NIRO_HEV = "KIA NIRO Hybrid"
  NIRO_EV = "KIA NIRO ELECTRIC"
  NEXO = "HYUNDAI NEXO"
  MOHAVE = "KIA MOHAVE"
  I30 = "HYUNDAI I30"
  SELTOS = "KIA SELTOS"
  PALISADE = "HYUNDAI PALISADE"


class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4


params = Params()
fingerprint_issued_fix = params.get("FingerprintIssuedFix", encoding='utf8') == "1"

if fingerprint_issued_fix:
  FINGERPRINTS = {
    CAR.AVANTE: [{}],
    CAR.SONATA: [{}],
    CAR.SONATA_HEV: [{}],
    CAR.SONATA_TURBO: [{}],
    CAR.GRANDEUR: [{}],
    CAR.GRANDEUR_HEV: [{}],
    CAR.GENESIS: [{}],
    CAR.SANTAFE: [{}],
    CAR.KONA: [{}],
    CAR.KONA_HEV: [{}],
    CAR.KONA_EV: [{}],
    CAR.IONIQ_HEV: [{}],
    CAR.IONIQ_EV: [{}],
    CAR.K5: [{}],
    CAR.K5_HEV: [{}],
    CAR.K7: [{}],
    CAR.K7_HEV: [{}],
    CAR.STINGER: [{}],
    CAR.NIRO_HEV: [{}],
    CAR.NIRO_EV: [{}],
    CAR.NEXO: [{}],
    CAR.MOHAVE: [{}],
    CAR.I30: [{}],
    CAR.SELTOS: [{}],
    CAR.PALISADE: [{}],
    CAR.SORENTO: [{}],
  }
else:
  FINGERPRINTS = {
    CAR.GENESIS_G70: [{}],
    CAR.GENESIS_G80: [{}],
    CAR.GENESIS_G90: [{67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2003: 8, 2004: 8, 2005: 8, 2008: 8, 2011: 8, 2012: 8, 2013: 8}],
    CAR.GENESIS_G90_L: [{67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 3, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1434: 2, 1456: 4, 1470: 8}],
    CAR.AVANTE: [{}],
    CAR.SONATA: [{}],
    CAR.SONATA_HEV: [{}],
    CAR.SONATA_TURBO: [{}],
    CAR.GRANDEUR: [{}],
    CAR.GRANDEUR_HEV: [{}],
    CAR.GENESIS: [{67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1268: 8, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1437: 8, 1456: 4},
                  {67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4},
                  {67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4}],
    CAR.SANTAFE: [{}],
    CAR.KONA: [{}],
    CAR.KONA_HEV: [{}],
    CAR.KONA_EV: [{}],
    CAR.IONIQ_HEV: [{}],
    CAR.IONIQ_EV: [{}],
    CAR.K5: [{}],
    CAR.K5_HEV: [{}],
    CAR.K7: [{}],
    CAR.K7_HEV: [{}],
    CAR.STINGER: [{}],
    CAR.NIRO_HEV: [{}],
    CAR.NIRO_EV: [{}],
    CAR.NEXO: [{}],
    CAR.MOHAVE: [{}],
    CAR.I30: [{}],
    CAR.SELTOS: [{}],
    CAR.PALISADE: [{}],
    CAR.SORENTO: [{}],
  }


ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

CHECKSUM = {
  "crc8": [CAR.SANTAFE, CAR.SONATA, CAR.PALISADE],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  "use_cluster_gears": [CAR.KONA, CAR.GRANDEUR, CAR.K7, CAR.MOHAVE, CAR.I30, CAR.AVANTE],     # Use Cluster for Gear Selection, rather than Transmission
  "use_tcu_gears": [CAR.K5, CAR.SONATA, CAR.SONATA_TURBO],                                    # Use TCU Message for Gear Selection
  "use_elect_gears": [CAR.K5_HEV, CAR.SONATA_HEV, CAR.GRANDEUR_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV, CAR.NIRO_HEV, CAR.KONA_HEV, CAR.KONA_EV, CAR.NIRO_EV, CAR.NEXO], # Use TCU Message for Gear Selection
}

EV_HYBRID = [CAR.K5_HEV, CAR.SONATA_HEV, CAR.GRANDEUR_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV, CAR.NIRO_HEV, CAR.KONA_HEV, CAR.KONA_EV, CAR.NIRO_EV, CAR.NEXO]

DBC = {
  CAR.AVANTE: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTAFE: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.K5: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.K7: dbc_dict('hyundai_kia_generic', None),
  CAR.K7_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NEXO: dbc_dict('hyundai_kia_generic', None),
  CAR.MOHAVE: dbc_dict('hyundai_kia_generic', None),
  CAR.I30: dbc_dict('hyundai_kia_generic', None),
  CAR.SELTOS: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 100
