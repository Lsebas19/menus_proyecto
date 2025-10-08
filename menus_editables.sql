-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-09-2025 a las 15:30:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `menus_editables`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` varchar(4) NOT NULL,
  `nit_empresa` varchar(11) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresas`
--

CREATE TABLE `empresas` (
  `nit_empresa` varchar(11) NOT NULL,
  `numero_identidad` varchar(15) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `correo` varchar(30) DEFAULT NULL,
  `ciudad` varchar(30) DEFAULT NULL,
  `codigo_qr` varchar(128) DEFAULT NULL,
  `link` varchar(128) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `logo` varchar(30) DEFAULT NULL,
  `pais` varchar(30) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `menus`
--

CREATE TABLE `menus` (
  `id_menu` varchar(4) NOT NULL,
  `nit_empresa` varchar(11) DEFAULT NULL,
  `fecha_Creacion` datetime DEFAULT NULL,
  `estado` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_productos` varchar(4) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` varchar(230) DEFAULT NULL,
  `presentacion` varchar(150) DEFAULT NULL,
  `imagen` varchar(30) DEFAULT NULL,
  `precio` int(6) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `nit_empresa` varchar(10) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_categorias`
--

CREATE TABLE `productos_categorias` (
  `id_tabla` varchar(4) NOT NULL,
  `productos` varchar(4) DEFAULT NULL,
  `categorias` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seleccionados`
--

CREATE TABLE `seleccionados` (
  `id_seleccionado` varchar(4) NOT NULL,
  `menu` varchar(4) DEFAULT NULL,
  `id_categoria` varchar(4) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `numero_identidad` varchar(15) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `correo` varchar(30) DEFAULT NULL,
  `contrasena` varchar(128) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `rol` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`numero_identidad`, `nombre`, `correo`, `contrasena`, `fecha_creacion`, `estado`, `rol`) VALUES
('1234567891', 'Sebatian Loaiza', 'juansebas190gmail.com', '1ae69ab2d28724430a0d45e62349755826329d6ad6b1f1da7ccf8ed78119cd3d2e8ec0c276daac0eb241d034189fc408d86e073f456f8dab85213a185ee8858e', '2025-09-08 18:25:00', 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`),
  ADD KEY `nit_empresa` (`nit_empresa`);

--
-- Indices de la tabla `empresas`
--
ALTER TABLE `empresas`
  ADD PRIMARY KEY (`nit_empresa`),
  ADD KEY `fk_usuario` (`numero_identidad`);

--
-- Indices de la tabla `menus`
--
ALTER TABLE `menus`
  ADD PRIMARY KEY (`id_menu`),
  ADD KEY `nit_empresa` (`nit_empresa`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_productos`),
  ADD KEY `nit_empresa` (`nit_empresa`);

--
-- Indices de la tabla `productos_categorias`
--
ALTER TABLE `productos_categorias`
  ADD PRIMARY KEY (`id_tabla`),
  ADD KEY `productos` (`productos`),
  ADD KEY `categorias` (`categorias`);

--
-- Indices de la tabla `seleccionados`
--
ALTER TABLE `seleccionados`
  ADD PRIMARY KEY (`id_seleccionado`),
  ADD KEY `menu` (`menu`),
  ADD KEY `fk_categoria_seleccionada` (`id_categoria`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`numero_identidad`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD CONSTRAINT `categorias_ibfk_1` FOREIGN KEY (`nit_empresa`) REFERENCES `empresas` (`nit_empresa`);

--
-- Filtros para la tabla `empresas`
--
ALTER TABLE `empresas`
  ADD CONSTRAINT `fk_documento` FOREIGN KEY (`numero_identidad`) REFERENCES `usuarios` (`numero_identidad`),
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`numero_identidad`) REFERENCES `usuarios` (`numero_identidad`);

--
-- Filtros para la tabla `menus`
--
ALTER TABLE `menus`
  ADD CONSTRAINT `menus_ibfk_1` FOREIGN KEY (`nit_empresa`) REFERENCES `empresas` (`nit_empresa`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`nit_empresa`) REFERENCES `empresas` (`nit_empresa`);

--
-- Filtros para la tabla `productos_categorias`
--
ALTER TABLE `productos_categorias`
  ADD CONSTRAINT `productos_categorias_ibfk_1` FOREIGN KEY (`productos`) REFERENCES `productos` (`id_productos`),
  ADD CONSTRAINT `productos_categorias_ibfk_2` FOREIGN KEY (`categorias`) REFERENCES `categorias` (`id_categoria`);

--
-- Filtros para la tabla `seleccionados`
--
ALTER TABLE `seleccionados`
  ADD CONSTRAINT `fk_categoria_seleccionada` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`),
  ADD CONSTRAINT `seleccionados_ibfk_1` FOREIGN KEY (`menu`) REFERENCES `menus` (`id_menu`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
