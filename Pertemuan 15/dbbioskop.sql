-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2024 at 08:33 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbbioskop`
--

-- --------------------------------------------------------

--
-- Table structure for table `bioskop`
--

CREATE TABLE `bioskop` (
  `id` int(1) NOT NULL,
  `no_kursi` int(2) NOT NULL,
  `hari` enum('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu') NOT NULL,
  `film` enum('The Shawshank Redemption','Pulp Fiction','Star Wars: Episode V - The Empire Strikes Back','Fight Club','Inception','The Dark Knight','The Matrix','Goodfellas','The Silence of the Lambs','Pengabdi Setan','The Lord of the Rings: The Return of the King','Suster Kramas','Warkop DKI Reborn','Sumpah Pocong','Sang Kyai','Parasite','Agak lain','The Raid','Gundala','Titanic','The Godfather','Dilan 1990','Jatuh Cinta seperti di Film-Film','Naga Bonar','Habibie dan Ainun','Schindlers List','Mission Imposible','Bullet Rain','Youtubers','Yowes Ben','The Lord of the Rings: The Return of the King','Kereta Berdarah','Munkar','Pemukiman Setan','Pasutri gaje') NOT NULL,
  `harga` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bioskop`
--

INSERT INTO `bioskop` (`id`, `no_kursi`, `hari`, `film`, `harga`) VALUES
(1, 1, 'Senin', 'Pulp Fiction', 25000);

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `id` int(10) NOT NULL,
  `no` int(10) NOT NULL,
  `hari` enum('Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu') NOT NULL,
  `film` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id`, `no`, `hari`, `film`) VALUES
(1, 1, 'Senin', 'Kungfu Panda'),
(2, 2, 'Senin', 'The Medium'),
(3, 3, 'Senin', 'Agak Lain'),
(4, 4, 'Senin', 'Sayap Sayap Patah'),
(5, 5, 'Senin', 'Habibie dan Ainun'),
(6, 6, 'Senin', 'Pengabdi Setan'),
(7, 7, 'Selasa', 'Sijjin'),
(8, 8, 'Selasa', 'Youtubers'),
(9, 9, 'Selasa', 'Home Alone');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bioskop`
--
ALTER TABLE `bioskop`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `no_kursi` (`no_kursi`);

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `no` (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bioskop`
--
ALTER TABLE `bioskop`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
