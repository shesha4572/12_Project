-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: Project
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AC`
--

DROP TABLE IF EXISTS `AC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AC` (
  `Product_ID` varchar(15) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Model` varchar(100) DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Price` decimal(10,0) NOT NULL,
  `Pieces` int NOT NULL,
  `Colour` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AC`
--

LOCK TABLES `AC` WRITE;
/*!40000 ALTER TABLE `AC` DISABLE KEYS */;
INSERT INTO `AC` VALUES ('AC0001','Whirpool','Whirlpool 1 Ton 5 Star Split Inverter AC - White','(1.0T MAGICOOL PRO 5S COPR INV/N, Copper Condenser)',29999,23,'White'),('AC0002','Voltas','Voltas 1.2 Ton 3 Star Split Inverter AC','(153V DZV (R32), Copper Condenser)',29999,5,'White'),('AC0003','Onida','Onida 1 Ton 3 Star Split Inverter AC','(IR123RHO, Copper Condenser)',24999,50,'White'),('AC0004','Panasonic','Panasonic 1.5 Ton 3 Star Split AC with PM 2.5 Filter','(CS/CU-YN18WKYM, Alloy Condenser)',28999,43,'White'),('AC0005','Godrej','Godrej 1 Ton 3 Star Split AC','(AC 1T GSC 12NTC3-WTA, Copper Condenser)',26499,6,'White'),('AC0006','Blue Star','Blue Star 1.2 Ton 3 Star Split Inverter AC','(IC315AATU, Copper Condenser)',31999,46,'White'),('AC0007','Samsung','Samsung 1.5 Ton 3 Star Split Triple Inverter Dura Series AC','(AR18TV3HMWKNNA/AR18TV3HMWKXNA, Alloy Condenser)',32990,12,'White'),('AC0008','Carrier','Carrier 1.2 Ton 5 Star Split Inverter AC with PM 2.5 Filter','(14K 5 STAR ESTER NEO-i INVERTER R32 SPLIT AC, Copper Condenser)',34499,36,'White'),('AC0009','Whirpool','Whirlpool 1.5 Ton 5 Star Split Inverter AC','(1.5T Magicool Pro 5S COPR INV, Copper Condenser)',34999,23,'White'),('AC0010','Voltas','Voltas 1.5 Ton 3 Star Split Inverter AC','(183 VCZJ (R 32), Copper Condenser)',34999,65,'White'),('AC0011','Carrier','Carrier 1.5 Ton 3 Star Split Inverter AC with PM 2.5 Filter','(18K 3 Star Ester Neo Inverter R32 IDU (I011) / 18K 3Star Inverter R32 ODU (I011), Copper Condenser)\n',35999,13,'White'),('AC0012','Samsung','Samsung 1.5 Ton 5 Star Split Triple Inverter Dura Series AC','(AR18TV5HLTUNNA/AR18TV5HLTUXNA, Alloy Condenser)',36990,32,'White'),('AC0013','LG','LG 1.5 Ton 3 Star Split Dual Inverter AC','(KS-Q18YNXA, Copper Condenser)',37999,15,'White'),('AC0014','Voltas','Voltas 1.5 Ton 5 Star Split Inverter AC','(185V JZJ (R32), Copper Condenser)',38999,1,'White'),('AC0015','LG','LG 1.5 Ton 5 Star Split Dual Inverter AC','(LS-Q18YNZA, Copper Condenser)',42999,7,'White'),('AC0016','Carrier','Carrier 1.5 Ton 5 Star Split Inverter AC with PM 2.5 Filter','(18K 5 Star Ester Neo Hybridjet Inverter R32 (I015) / 18K 5 Star Hybridjet Inverter R32 ODU (I015), Copper Condenser)',42999,6,'White'),('AC0017','Whirpool','Whirlpool 1.5 Ton 3 Star Split AC','(1.5T Magicool Elite Pro 3S COPR, Copper Condenser)',44000,3,'Grey'),('AC0018','Samsung','Samsung 1 Ton 3 Star Split Triple Inverter Dura Series AC','(AR12TV3HMWKNNA/AR12TV3HMWKXNA, Alloy Condenser)',47990,6,'White'),('AC0019','Samsung','Samsung 1.5 Ton 3 Star Split Triple Inverter AC','(AR18TV3JFMCNNA/AR18TV3JFMCXNA, Copper Condenser)',54990,9,'Blue'),('AC0020','Hitachi','Hitachi 1.5 Ton 5 Star Split Inverter AC','(RSOG/ESOG/CSOG518HDEA, Copper Condenser)',60090,10,'Gold');
/*!40000 ALTER TABLE `AC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FRIDGES`
--

DROP TABLE IF EXISTS `FRIDGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FRIDGES` (
  `Product_ID` varchar(15) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Model` varchar(100) NOT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Price` decimal(10,2) NOT NULL,
  `Pieces` int DEFAULT NULL,
  `Colour` varchar(10) NOT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FRIDGES`
--

LOCK TABLES `FRIDGES` WRITE;
/*!40000 ALTER TABLE `FRIDGES` DISABLE KEYS */;
INSERT INTO `FRIDGES` VALUES ('F001','Whilrpool','Whirlpool 215 L Direct Cool Single Door 3 Star (2019) Refrigerator','(Argyle Black, 230 VITAMAGIC PRM 3S ARGYLE BLACK-E)',14990.00,17,'Black'),('F002','Haier','Haier 195 L Direct Cool Single Door 3 Star (2020) Refrigerator','(Red Ornate, HRD-1953CPRO-E)',14999.00,33,'Red'),('F003','Whirpool','Whirlpool 190 L Direct Cool Single Door 3 Star (2020) Refrigerator','(Solid blue, WDE 205 CLS 3S BLUE)',11990.00,80,'Blue'),('F004','Samsung','Samsung 192 L Direct Cool Single Door 2 Star (2020) Refrigerator ','(Elective Silver, RR19T241BSE/NL)',11990.00,78,'Silver'),('F005','Samsung','Samsung 192 L Direct Cool Single Door 3 Star (2020) Refrigerator','(Star Flower Red, RR20T172YR2/HL)',13990.00,91,'Red'),('F006','Whirpool','Whirlpool 292 L Frost Free Double Door 3 Star (2019) Refrigerator','(Alpha Steel, IF 305 ELT ALPHA STEEL(3S))',24990.00,54,'Steel'),('F007','Godrej','Godrej 330 L Frost Free Double Door 2 Star (2019) Refrigerator','(Sleek Steel, RF GF 3302 PTH SLK STL)',24990.00,44,'Steel'),('F008','LG','LG 260 L Frost Free Double Door 3 Star (2020) Refrigerator','(Shiny Steel, GL-I292RPZL)',24690.00,56,'Steel'),('F009','Samsung','Samsung 253 L Frost Free Double Door 2 Star (2020) Convertible Refrigerator','(Saffron Red, RT28T3922R8/HL)',24490.00,51,'Red'),('F010','Samsung','Samsung 253 L Frost Free Double Door 3 Star (2019) Refrigerator','(Pebble Blue, RT28R3023UT/HL)',24190.00,23,'Blue'),('F011','LG','LG 260 L Frost Free Double Door 3 Star Convertible Refrigerator','(Shiny Steel, GL-T292RPZY)',26400.00,26,'Steel'),('F012','Samsung','Samsung 324 L Frost Free Double Door 2 Star (2020) Convertible Refrigerator','(Elegant Inox, RT34M5538S8/HL)',29690.00,48,'Inox'),('F013','LG','LG 308 L Frost Free Double Door 2 Star (2020) Refrigerator','(Shiny Steel, GL-C322KPZY)',29990.00,2,'Steel'),('F014','LG','LG 308 L Frost Free Double Door 2 Star (2020) Refrigerator','(Shiny Steel, GL-C322RPZU)',29999.00,48,'Steel'),('F015','Samsung','Samsung 476 L Frost Free Double Door 3 Star (2019) Refrigerator','(Refined Inox, RT49K6758S9)',58890.00,3,'Inox'),('F016','LG','LG 687 L Frost Free Side by Side Refrigerator','(Shiny Gold, GC-B247SVUV)',72990.00,6,'Inox'),('F017','Samsung','Samsung 700 L Frost Free Side by Side (2019) Refrigerator','(Ez Clean Steel, RS72R5011SL/TL)',85240.00,4,'Steel'),('F018','LG','LG 675 L Frost Free Side by Side Refrigerator','(Linen White, GC-C247UGLW)',99990.00,0,'White'),('F019','Bosch','Bosch 636 L Frost Free Side by Side (0) Refrigerator','(Glass Black, KAD92SB30)',149990.00,1,'Black'),('F020','Samsung','Samsung 810 L Frost Free Side by Side Refrigerator','Inverter Technology Star (2019) Convertible Refrigerator  (Black Caviar, RF28N9780SG/TL)',259990.00,2,'Black');
/*!40000 ALTER TABLE `FRIDGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `K_APPS`
--

DROP TABLE IF EXISTS `K_APPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `K_APPS` (
  `Product_ID` varchar(10) NOT NULL,
  `Type` varchar(15) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Name` varchar(200) DEFAULT NULL,
  `Price` double(10,2) NOT NULL,
  `Pieces` int DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `K_APPS`
--

LOCK TABLES `K_APPS` WRITE;
/*!40000 ALTER TABLE `K_APPS` DISABLE KEYS */;
INSERT INTO `K_APPS` VALUES ('KAD01','Dishwasher','BPL','D812S27A Free Standing 12 Place Settings Dishwasher',22499.00,7),('KAD02','Dishwasher','Bosch','SMS24AW00I Free Standing 12 Place Settings Dishwasher',31790.00,5),('KAD03','Dishwasher','Bosch','SMS66GW01I Free Standing 12 Place Settings Dishwasher',35999.00,2),('KAD04','Dishwasher','Bosch','SMS66GI01I Free Standing 12 Place Settings Dishwasher',39999.00,3),('KAD05','Dishwasher','Kaff','DW SPECTRA 60 Free Standing 14 Place Settings Dishwasher',54990.00,6),('KAF01','Food Processor','Prestige','CleanHome Fruit and Vegetable Cleaner 250 W Food Processor  (White and Blue)',3760.00,54),('KAF02','Food Processor','Philips','HR7627/00 650 W Food Processor  (White)',4299.00,99),('KAF03','Food Processor','Crompton','OMNIA 700 W Food Processor  (White and black)',5149.00,65),('KAF04','Food Processor','Philips','hl 1660 700 W Food Processor  (White)',7799.00,55),('KAF05','Food Processor','Morphy','Icon DLX 1000 W Food Processor  (Black)',10995.00,51),('KAM01','Mixer','Bajaj','GX1 500 W Mixer Grinder',1949.00,14),('KAM02','Mixer','Philips','HL7555 600 W Mixer Grinder  (white and Blue, 3 Jars)',3149.00,75),('KAM03','Mixer','Bosch','Radiance MGM4341RIN 600 Juicer Mixer Grinder  (Red, 4 Jars)',4499.00,14),('KAM04','Mixer','Butterfly','SPECTRA 750 W Juicer Mixer Grinder  (Red, 4 Jars)',4950.00,64),('KAM05','Mixer','Philips','Avance Collection HL7707 750 W Mixer Grinder  (Black, 4 Jars)',7999.00,58),('KAO01','Microwave Oven','Bajaj','17 L Solo Microwave Oven  (1701MT, White)',3999.00,99),('KAO02','Microwave Oven','Samsung','23 L Solo Microwave Oven  (MS23F301TAK/TL, Black)',5750.00,24),('KAO03','Microwave Oven','Onida','23 L Air Fryer Convection Microwave Oven  (MO23CJS11BN, Black)',8299.00,75),('KAO04','Microwave Oven','Samsung','21 L Convection Microwave Oven  (CE73JD-B/XTL, Full Black)',8999.00,50),('KAO05','Microwave Oven','LG','32 L Convection Microwave Oven  (MC3286BRUM, Black)',17999.00,60);
/*!40000 ALTER TABLE `K_APPS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TV`
--

DROP TABLE IF EXISTS `TV`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TV` (
  `Product_ID` varchar(10) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Size` int NOT NULL,
  `Price` double(10,2) NOT NULL,
  `Pieces` int DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TV`
--

LOCK TABLES `TV` WRITE;
/*!40000 ALTER TABLE `TV` DISABLE KEYS */;
INSERT INTO `TV` VALUES ('TV001','Vu','Vu Premium',32,11999.00,61,'80 cm (32) HD Ready LED Smart Android TV  (32US)'),('TV002','MI','Mi 4A PRO',32,12499.00,89,'80 cm (32) HD Ready LED Smart Android TV'),('TV003','Samsung','Samsung Series 4',32,13999.00,86,'80cm (32 inch) HD Ready LED Smart TV  (UA32N4305ARXXL)'),('TV004','Motorola','Motorola TV',32,13999.00,34,'80.5cm (32 inch) HD Ready LED Smart Android TV with Wireless Gamepad  (32SAFHDM)'),('TV005','LG','LG All-in-One',32,14999.00,97,'80cm (32 inch) HD Ready LED Smart TV  (32LM560BPTC)'),('TV006','Sony','Sony Bravia W622G',32,23999.00,66,'80cm (32 inch) HD Ready LED Smart TV  (KLV-32W622G)'),('TV007','MI','MI 4X',43,24999.00,57,'108 cm (43) Ultra HD (4K) LED Smart Android TV'),('TV008','Vu','Vu Premium',43,25999.00,12,'108cm (43 inch) Ultra HD (4K) LED Smart Android TV  (43PM)'),('TV009','LG','LG All-in-One',43,28999.00,43,'108cm (43 inch) Full HD LED Smart TV  (43LM5600PTC)'),('TV010','Motorola','Motorola TV',43,29999.00,2,'109cm (43 inch) Ultra HD (4K) LED Smart Android TV with Wireless Gamepad  (43SAUHDM)'),('TV011','LG','LG TV',43,36499.00,19,'108cm (43 inch) Ultra HD (4K) LED Smart TV  (43UM7290PTF)'),('TV012','Motorola','Motorola TV',55,39999.00,47,'139cm (55 inch) Ultra HD (4K) LED Smart Android TV with Wireless Gamepad  (55SAUHDM)'),('TV013','Samsung','Samsung Super 6',55,49999.00,31,'138cm (55 inch) Ultra HD (4K) LED Smart TV  (UA55NU6100KXXL / UA55NU6100KLXL)'),('TV014','Sony','Sony Bravia X8500F',43,49999.00,46,'108cm (43 inch) Ultra HD (4K) LED Smart Android TV  (KD-43X8500F)'),('TV015','Motorola','Motorola TV',65,64999.00,6,'164cm (65 inch) Ultra HD (4K) LED Smart Android TV with Wireless Gamepad  (65SAUHDM)'),('TV016','Samsung','Samsung The Frame',55,82999.00,3,'138cm (55 inch) Ultra HD (4K) QLED Smart TV  (QA55LS03RAKXXL)'),('TV017','Samsung','Samsung TV',65,89999.00,5,'163cm (65 inch) Ultra HD (4K) LED Smart TV  (UA65NU7090KXXL)'),('TV018','Motorola','Motorola TV',75,119999.00,6,'189cm (75 inch) Ultra HD (4K) LED Smart Android TV with Wireless Gamepad  (75SAUHDM)'),('TV019','Sony','Sony Bravia X8000G',65,123499.00,3,'163.9cm (65 inch) Ultra HD (4K) LED Smart Android TV  (KD-65X8000G)'),('TV020','LG','LG C9',55,165999.00,6,'138cm (55 inch) Ultra HD (4K) OLED Smart TV  (OLED55C9PTA)');
/*!40000 ALTER TABLE `TV` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WSH_MCH`
--

DROP TABLE IF EXISTS `WSH_MCH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WSH_MCH` (
  `Product_ID` varchar(10) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Model` varchar(100) DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL,
  `Price` double(10,2) NOT NULL,
  `Type` varchar(30) DEFAULT NULL,
  `Pieces` int DEFAULT NULL,
  `Colour` varchar(10) NOT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WSH_MCH`
--

LOCK TABLES `WSH_MCH` WRITE;
/*!40000 ALTER TABLE `WSH_MCH` DISABLE KEYS */;
INSERT INTO `WSH_MCH` VALUES ('WS001','LG','LG 6 kg With Collar Scrubber Semi Automatic Top Load','(P6001RG)',9699.00,'Semi Automatic',71,'White'),('WS002','Whirpool','Whirlpool 7 kg 5 Star,Turbo Scrub Technology','(SUPERB ATOM 70S GREY DAZZLE (5YR))',9299.00,'Semi Automatic',43,'Grey'),('WS003','Samsung','Samsung 6.5 kg 5 Star Semi Automatic Top Load','(WT667QPNDPGXTL)',9499.00,'Semi Automatic',19,'White'),('WS004','Haier','Haier 7 kg Semi Automatic Top Load','(HTW70-186S)',9499.00,'Semi Automatic',22,'Black'),('WS005','Whirpool','Whirlpool 7.5 kg 5 Star, Supersoak Technology Semi Automatic Top Load','(Ace 7.5 Sup Soak (Coral Red) (5 yr))',9890.00,'Semi Automatic',33,'Red'),('WS006','Panasonic','Panasonic 6.2 kg Fully Automatic Top Load','(NA-F62B3HRB)',12990.00,'Fully Automatic Top Load',1,'Grey'),('WS007','Onida','Onida 7 kg with One Touch Operations Fully Automatic Top Load','(T70CGN)',12999.00,'Fully Automatic Top Load',62,'Grey'),('WS008','Samsung','Samsung 6.2 kg with Monsoon Feature Fully Automatic Top Load','(WA62M4100HY/TL 01)',13100.00,'Fully Automatic Top Load',43,'Grey'),('WS009','Whirpool','Whirlpool 7 kg 5 Star, Hard Water wash Fully Automatic Top Load','(WM ROYAL PLUS 7.0 GREY 5YMW)',14990.00,'Fully Automatic Top Load',21,'Grey'),('WS010','Godrej','Godrej 7 kg Fully Automatic Top Load','(WT EON 700 A Gp Gr)',14999.00,'Fully Automatic Top Load',39,'Grey'),('WS011','Samsung','Samsung 7.5 kg Fully Automatic Top Load','(WA75T4560BM/TL)',29400.00,'Fully Automatic Top Load',38,'Purple'),('WS012','Whirpool','Whirlpool 12 kg Inbuilt Heater Fully Automatic Top Load with In-built Heater','(360 ULTIMATE CARE 12.0 GRAPHITE 10 YMW)',28999.00,'Fully Automatic Top Load',25,'Grey'),('WS013','Bosch','Bosch 9.5 kg Inverter Fully Automatic Top Load','(WOA956X0IN)',29999.00,'Fully Automatic Top Load',40,'Silver'),('WS014','Bosch','Bosch 12 kg Fully Automatic Top Load','(WOA126X0IN)',35999.00,'Fully Automatic Top Load',34,'Grey'),('WS015','LG','LG 12 kg Fully Automatic Top Load with In-built Heater','(THD12STB)',42999.00,'Fully Automatic Top Load',35,'Black'),('WS016','Samsung','Samsung 8 kg Inverter with Ecobubble and In-built Heater',' (WW80J4243MW/TL)',32100.00,'Fully Automatic Front Load',3,'White'),('WS017','Whirpool','Whirlpool 9 kg Fully Automatic Front Load','(Supreme Care 9014)',34999.00,'Fully Automatic Front Load',4,'White'),('WS018','LG','LG 8 kg Inverter Fully Automatic Front Load with In-built Heater','(FHT1208SWL)',38999.00,'Fully Automatic Front Load',8,'Silver'),('WS019','Samsung','Samsung 9 kg Inverter Fully Automatic Front Load with In-built Heater','(WW90K6410QX/TL)',53990.00,'Fully Automatic Front Load',0,'Grey'),('WS020','Bosch','Bosch 9 kg Fully Automatic Front Load with In-built Heater','(WAW28790IN)',64199.00,'Fully Automatic Front Load',3,'White');
/*!40000 ALTER TABLE `WSH_MCH` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-10 17:10:55
