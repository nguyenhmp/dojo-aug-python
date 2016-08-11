CREATE DATABASE  IF NOT EXISTS `thewall` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `thewall`;
-- MySQL dump 10.13  Distrib 5.6.13, for osx10.6 (i386)
--
-- Host: 127.0.0.1    Database: thewall
-- ------------------------------------------------------
-- Server version	5.5.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Adam','Jacobs','adamj@gmail.com','$2b$12$Rv9MkkwkAzrVvwolkGC71.FhS1QhY4BnZBxkeYYph82Q4tXXxtjC.','2016-08-09 16:27:36',NULL),(2,'Allison','Johnson','aj26@gmail.com','$2b$12$irqghPzUzmsMqOMFyqKaaufGNgrcBmQLf3ZlsPbE/0Vj.Mq12fBoy','2016-08-09 16:34:11',NULL),(3,'Allison','Johnson','aj26@gmail.com','$2b$12$3TJrpq96.te0tqog..RDDOiQTmLh6OoiUMpa3bh2aQNF6WNKH0T0y','2016-08-09 18:06:41',NULL),(4,'James','Smith','jsmith@gmail.com','$2b$12$UoyAzFhuPSGHuJl49oKfkegeZm3s5k7c2vxqU4u2ODJRQ8TqoChlO','2016-08-09 18:07:47',NULL),(5,'paul','bluth','funkedelic@user.net','$2b$12$WxvQ/34kZcRnuUQEVLBPg.pj9gzusfpxXggQfJI3qH8Ux5dF1/8gK','2016-08-09 18:18:50',NULL),(6,'New','Person','newperson@new.com','$2b$12$JSAyy0NAbIHrK0tGAdd83.l3NB2x3wytSzLh7xGalkxV8wHXNN/Y2','2016-08-10 08:32:58',NULL),(7,'second','newperson','secondnew@new.com','$2b$12$PwmHt3oy9TOkEcT1P/HeuOs07umJER3Bk/PAYyfeWaY6vKXxD9WwK','2016-08-10 08:34:27',NULL),(8,'Jon','Snow','jonsnow@got.com','$2b$12$B19flg4UcSlacm/EHE2kue2cPfY3BsPQ2WcOVNlhWRVh00U3TM8gi','2016-08-10 08:40:05',NULL),(9,'Ned','Stark','nedstark@gmail.com','$2b$12$iIEA1UJx1Ylw3789IRkTEOvJlwT2rGeC3mUvtufJ08O7e7/ATyt3a','2016-08-10 13:05:27',NULL),(10,'Tyrion ','Lannister','tyrion@gmail.com','$2b$12$PyFigI5CBfbIGNCt2Tjfi.YghGetjo/7VH.AFb/Mkii4jsPMb.nSG','2016-08-10 13:06:09',NULL),(11,'Green','Dragon','gdragon@gmail.com','$2b$12$AZEc.DZlX7qIyoD09R3WyeD8q2s9tguvdqsoC.HgT8mFSj2VYvzTS','2016-08-10 13:06:42',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-10 14:04:43
