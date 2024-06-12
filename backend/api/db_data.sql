--
-- PostgreSQL database dump
--

-- Dumped from database version 14.12 (Debian 14.12-1.pgdg120+1)
-- Dumped by pg_dump version 14.12 (Debian 14.12-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: yarik
--

INSERT INTO public."user" VALUES (1, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764');


--
-- Data for Name: certificate; Type: TABLE DATA; Schema: public; Owner: yarik
--

INSERT INTO public.certificate VALUES (6, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1430', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 23:11:00', 186.2570, '2024-05-28 17:41:58.300626', '2024-05-29 12:24:29.324815', '2024-05-29 14:37:58.735905', '70aae0da6a867305aba1dd1c5b55ae3c5091bc3cf05ea2e827011f053ec53f16', NULL);
INSERT INTO public.certificate VALUES (3, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1425', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:21:00', 170.8900, '2024-05-28 15:51:41.662067', '2024-05-29 12:24:29.132962', '2024-05-28 11:51:42.0946', 'f7f36d5bf7834dc367e021951bfa913a9aee160de28e7da7789cad102958f785', NULL);
INSERT INTO public.certificate VALUES (7, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1424', 'Satyam Steel', '2024-05-01 00:00:00', '2024-05-28 21:17:00', 5461.8310, '2024-05-28 15:47:06.87463', '2024-05-29 12:24:29.37467', '2024-05-28 11:47:24.7203', 'a15a5ccba9f90ce59e26575944f8cee10344ddc567937c6b2991023e2951df6c', NULL);
INSERT INTO public.certificate VALUES (9, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1433', 'Satyam Steel', '2024-03-31 19:02:00', '2024-04-30 05:56:00', 5795.8530, '2024-05-29 18:57:29.416193', '2024-05-29 14:57:29.500857', '2024-05-29 14:57:36.547399', '9bc8f2a912754347691de7a79621744bd0d30dc3c274398f91940243552a9d1f', NULL);
INSERT INTO public.certificate VALUES (2, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1423', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:08:00', 167.6990, '2024-05-28 15:38:41.441447', '2024-05-29 12:24:29.091538', '2024-05-28 11:38:48.8629', 'bf8f94eaf512df7f8cc5295f60c1b840b1c95584a090c75c1128082c7a52d687', NULL);
INSERT INTO public.certificate VALUES (1, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1422', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:04:00', 167.6990, '2024-05-28 15:34:50.56942', '2024-05-29 12:24:29.046454', '2024-05-28 11:35:00.6719', '8cbfc67bc3acb402832c04c5c5e8d393d97670eb2f2182f6c3beab28fcb9e671', NULL);
INSERT INTO public.certificate VALUES (10, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1434', 'Satyam Steel', '2024-01-01 00:00:00', '2024-05-30 00:45:00', 29464.1680, '2024-05-29 19:15:18.685267', '2024-05-29 15:15:18.743274', '2024-05-29 15:15:24.42103', '56781969fb882323dbcd89776f3a0b263aa6b7a8f03803737a2bcc516e4f0f31', NULL);
INSERT INTO public.certificate VALUES (11, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1396', 'Satyam Steel', '2024-05-27 00:00:00', '2024-05-27 20:33:00', 167.0340, '2024-05-28 17:46:56.437199', '2024-05-29 17:18:50.784972', NULL, NULL, NULL);
INSERT INTO public.certificate VALUES (8, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1431', 'Satyam Steel', '2024-05-27 00:00:00', '2024-05-29 23:52:00', 591.8810, '2024-05-29 18:22:28.642403', '2024-05-29 14:22:28.699788', '2024-05-29 14:22:36.7147', '54c753bc7c119a034e99012f53dd7e3ae53cf8cac21f8a0d7eb1fed2ab7d0ef1', NULL);
INSERT INTO public.certificate VALUES (4, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1428', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:34:00', 173.1370, '2024-05-28 16:04:25.375444', '2024-05-29 12:24:29.174255', '2024-05-28 16:04:36', '6d013a2940eff42ef8a702293a1d08e56eedd72c2a82e22711f23cc3a58c09d2', NULL);
INSERT INTO public.certificate VALUES (12, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1440', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 02:16:00', 17.5720, '2024-05-30 20:46:19.885728', '2024-05-30 16:46:20.018274', '2024-05-30 16:46:24.732094', '5b726973032dae676c21156a72a962a3a806db6b8c9c2f4d65358aa606c590a1', NULL);
INSERT INTO public.certificate VALUES (13, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1441', 'Satyam Steel', '2024-05-01 00:00:00', '2024-05-31 02:31:00', 5901.1540, '2024-05-30 21:01:18.362498', '2024-05-30 17:01:18.385774', '2024-05-30 17:01:24.605698', '5f3dba534fd2c4c9ef6982143feb8818c9a1fe736913fbd93075ae41e9d9fc9d', NULL);
INSERT INTO public.certificate VALUES (14, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1218', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 19:06:00', 157.8180, '2024-05-31 13:36:52.020067', '2024-05-31 09:36:52.401178', '2024-05-31 09:37:00.708803', '5a9e8d08a5295f8e3d82fd15c3f996da609234cf559cf5c6063dae3cdfad7718', NULL);
INSERT INTO public.certificate VALUES (15, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1219', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 20:07:00', 167.0390, '2024-05-31 14:37:33.676573', '2024-05-31 10:37:33.839608', '2024-05-31 10:38:02.367685', 'd140d54ec946f28281902209aab8969b1915baa64a9cbc3ab6507932af78d48c', NULL);
INSERT INTO public.certificate VALUES (5, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1429', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 23:06:00', 186.2570, '2024-05-28 17:36:27.281567', '2024-05-29 12:24:29.216408', '2024-05-28 13:36:35.9393', 'ea21850796db7d108b3ad4fdc3b04ad24daf9fe7b076dadc14c17f955c758f83', NULL);
INSERT INTO public.certificate VALUES (16, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1220', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 21:21:00', 177.8700, '2024-05-31 15:51:56.184957', '2024-05-31 15:51:56.427455', '2024-05-31 15:52:00.594428', '8af7266bd72baf6050c0167aaa044701fe5a774580b4784a6c2053a34404823b', NULL);
INSERT INTO public.certificate VALUES (17, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1457', 'Satyam Steel', '2024-06-03 00:00:00', '2024-06-03 22:42:00', 185.4590, '2024-06-03 17:12:18.407856', '2024-06-03 19:36:12.955094', '2024-06-03 19:36:13.142118', '357934311251debf1858d126977dee400130b8880fa0563eec965dd74dfeb69f', NULL);
INSERT INTO public.certificate VALUES (18, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1456', 'Satyam Steel', '2024-06-03 00:00:00', '2024-06-03 22:41:00', 185.4590, '2024-06-03 17:11:26.486261', '2024-06-03 19:50:38.048922', '2024-06-03 19:50:38.128411', '66346a626b6bd3e2d2b69241d55388face4ecdf4a027a8023b8e27cc39b68b69', NULL);
INSERT INTO public.certificate VALUES (19, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1455', 'Satyam Steel', '2024-05-10 00:00:00', '2024-05-22 00:00:00', 2412.0890, '2024-06-03 11:15:31.621173', '2024-06-03 21:05:10.13462', '2024-06-03 21:05:10.548392', '4590f25c97c362feb809ee962430a66f324e31d15a51bac7f1cb9d6f71f5dd47', NULL);
INSERT INTO public.certificate VALUES (27, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1505', 'Satyam Steel', '2024-06-10 00:00:00', '2024-06-12 22:10:00', 557.9830, '2024-06-12 16:40:08.51454', '2024-06-12 17:40:37.930795', '2024-06-12 16:40:14.238465', '42aced7ae0a3f4d91a7992c6f09a07d96f8526bfa9120c89608e54ad32597281', 'certificate_address');
INSERT INTO public.certificate VALUES (20, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1460', 'Satyam Steel', '2024-06-10 00:00:00', '2024-06-10 20:28:00', 162.4000, '2024-06-10 14:58:36.586856', '2024-06-10 14:58:36.689709', '2024-06-10 14:58:37.599812', NULL, NULL);
INSERT INTO public.certificate VALUES (21, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1465', 'Satyam Steel', '2024-06-11 00:00:00', '2024-06-11 03:05:00', 25.8190, '2024-06-10 21:35:09.937793', '2024-06-10 21:35:09.9936', '2024-06-10 21:35:24.936099', 'f6a9aae8fa8a270dd5052cdb8154463c658748f7b53dc260267fc0f326e43827', NULL);
INSERT INTO public.certificate VALUES (22, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1466', 'Satyam Steel', '2024-06-11 00:00:00', '2024-06-11 03:06:00', 25.8190, '2024-06-10 21:36:33.3512', '2024-06-10 21:36:33.383889', '2024-06-10 21:36:33.916101', NULL, NULL);
INSERT INTO public.certificate VALUES (23, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1498', 'Satyam Steel', '2024-06-01 00:00:00', '2024-06-12 00:17:00', 2171.6470, '2024-06-11 18:47:12.950876', '2024-06-11 18:47:24.799421', '2024-06-11 18:47:24.692935', 'b97e9c650e904ba42be5f8a1084a512646d5d792378d4811194936c6e5b05b46', '');
INSERT INTO public.certificate VALUES (24, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1502', 'Satyam Steel', '2024-06-01 00:00:00', '2024-06-12 21:32:00', 2345.5560, '2024-06-12 16:02:29.830773', '2024-06-12 16:02:37.349215', '2024-06-12 16:02:36.493405', 'fa204000fd1855fee963de862fea294679e2abd02b28e5b226bb9d4154628495', 'certificate_address');
INSERT INTO public.certificate VALUES (25, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1503', 'Satyam Steel', '2024-06-12 00:00:00', '2024-06-12 21:43:00', 178.4170, '2024-06-12 16:13:18.088515', '2024-06-12 16:13:25.20295', '2024-06-12 16:13:24.651978', '1e1e974396f67de3a030c711eb2a7fb6dba96e31383189d773062ed79fdb1e60', 'certificate_address');
INSERT INTO public.certificate VALUES (26, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1504', 'Satyam Steel', '2024-01-01 00:00:00', '2024-06-12 21:56:00', 32195.2840, '2024-06-12 16:26:20.412943', '2024-06-12 16:26:25.218617', '2024-06-12 16:26:24.289011', 'a11d56e43cf827c3c5fd8a478c46cac6c97c531904b35cf3504e15d79765f0df', 'certificate_address');


--
-- Data for Name: certificateverificationattempt; Type: TABLE DATA; Schema: public; Owner: yarik
--

INSERT INTO public.certificateverificationattempt VALUES (1, 'cert-ca-1429', 186.2570, '2024-05-29 12:24:42.573817', true);
INSERT INTO public.certificateverificationattempt VALUES (2, 'cert-ca-1430', 186.2570, '2024-05-29 12:25:18.145641', true);
INSERT INTO public.certificateverificationattempt VALUES (3, 'cert-ca-1429', 186.2570, '2024-05-29 12:25:25.399221', true);
INSERT INTO public.certificateverificationattempt VALUES (4, 'cert-ca-1422', 167.6990, '2024-05-29 12:25:44.130958', true);
INSERT INTO public.certificateverificationattempt VALUES (5, 'cert-ca-1424', 5461.8310, '2024-05-29 12:26:03.026526', true);
INSERT INTO public.certificateverificationattempt VALUES (6, 'cert-ca-1425', 5461.8310, '2024-05-29 12:26:21.93587', false);
INSERT INTO public.certificateverificationattempt VALUES (7, 'cert-ca-1429', 186.2570, '2024-05-29 12:35:26.652598', true);
INSERT INTO public.certificateverificationattempt VALUES (8, 'cert-ca-1430', 186.2570, '2024-05-29 13:24:22.82067', true);
INSERT INTO public.certificateverificationattempt VALUES (9, 'cert-ca-1429', 186.2570, '2024-05-29 13:24:42.042112', true);
INSERT INTO public.certificateverificationattempt VALUES (10, 'cert-ca-1430', 186.2570, '2024-05-29 13:31:06.554952', true);
INSERT INTO public.certificateverificationattempt VALUES (11, 'cert-ca-1429', 186.2570, '2024-05-29 13:31:11.730244', true);
INSERT INTO public.certificateverificationattempt VALUES (12, 'cert-ca-1424', 5461.8310, '2024-05-29 13:31:46.207775', true);
INSERT INTO public.certificateverificationattempt VALUES (13, 'cert-ca-1430', 186.2570, '2024-05-29 13:33:18.876078', true);
INSERT INTO public.certificateverificationattempt VALUES (14, 'cert-ca-1429', 186.2570, '2024-05-29 13:33:37.272857', true);
INSERT INTO public.certificateverificationattempt VALUES (15, 'cert-ca-1424', 5461.8310, '2024-05-29 13:33:59.900319', true);
INSERT INTO public.certificateverificationattempt VALUES (16, 'cert-ca-1425', 5461.8310, '2024-05-29 13:34:09.418701', false);
INSERT INTO public.certificateverificationattempt VALUES (17, 'cert-ca-1425', 170.8900, '2024-05-29 13:34:32.910615', true);
INSERT INTO public.certificateverificationattempt VALUES (18, 'cert-ca-1430', 186.2570, '2024-05-29 13:48:54.774543', true);
INSERT INTO public.certificateverificationattempt VALUES (19, 'cert-ca-1429', 186.2570, '2024-05-29 13:49:21.696878', true);
INSERT INTO public.certificateverificationattempt VALUES (20, 'cert-ca-1424', 186.2570, '2024-05-29 13:49:33.279483', false);
INSERT INTO public.certificateverificationattempt VALUES (21, 'cert-ca-1424', 5461.8310, '2024-05-29 13:49:51.124185', true);
INSERT INTO public.certificateverificationattempt VALUES (22, 'cert-ca-1431', 591.8810, '2024-05-29 14:27:09.277696', true);
INSERT INTO public.certificateverificationattempt VALUES (23, 'cert-ca-1433', 5795.8530, '2024-05-29 15:00:48.557992', true);
INSERT INTO public.certificateverificationattempt VALUES (24, 'cert-ca-1434', 29464.1680, '2024-05-29 15:16:33.774918', true);
INSERT INTO public.certificateverificationattempt VALUES (26, 'cert-ca-1433', 5795.8530, '2024-05-29 15:22:14.794555', true);
INSERT INTO public.certificateverificationattempt VALUES (27, 'cert-ca-1434', 29464.1680, '2024-05-29 15:34:42.142691', true);
INSERT INTO public.certificateverificationattempt VALUES (29, 'cert-ca-1434', 29464.1600, '2024-05-29 15:35:20.569966', false);
INSERT INTO public.certificateverificationattempt VALUES (32, 'cert-ca-1434', 29464.1680, '2024-05-29 15:36:17.00543', true);
INSERT INTO public.certificateverificationattempt VALUES (35, 'cert-ca-1396', 167.0340, '2024-05-29 17:19:47.557668', false);
INSERT INTO public.certificateverificationattempt VALUES (36, 'cert-ca-1434', 29464.1680, '2024-05-30 09:45:19.104788', true);
INSERT INTO public.certificateverificationattempt VALUES (37, 'cert-ca-1396', 167.0340, '2024-05-30 09:45:32.845563', false);
INSERT INTO public.certificateverificationattempt VALUES (38, 'cert-ca-1440', 17.5720, '2024-05-30 16:47:28.166767', true);
INSERT INTO public.certificateverificationattempt VALUES (39, 'cert-ca-1441', 5901.1540, '2024-05-30 17:02:31.462899', true);
INSERT INTO public.certificateverificationattempt VALUES (40, 'cert-ca-1440', 5901.1540, '2024-05-30 17:02:47.715891', false);
INSERT INTO public.certificateverificationattempt VALUES (41, 'cert-ca-1218', 157.8180, '2024-05-31 09:38:17.403034', true);
INSERT INTO public.certificateverificationattempt VALUES (42, 'cert-ca-1422', 167.6990, '2024-05-31 10:12:06.091243', true);
INSERT INTO public.certificateverificationattempt VALUES (43, 'cert-ca-1423', 167.6990, '2024-05-31 10:12:50.772842', true);
INSERT INTO public.certificateverificationattempt VALUES (44, 'cert-ca-1425', 170.8900, '2024-05-31 10:13:01.061113', true);
INSERT INTO public.certificateverificationattempt VALUES (45, 'cert-ca-1428', 173.1370, '2024-05-31 10:13:11.676099', true);
INSERT INTO public.certificateverificationattempt VALUES (46, 'cert-ca-1429', 186.2570, '2024-05-31 10:13:22.760056', true);
INSERT INTO public.certificateverificationattempt VALUES (47, 'cert-ca-1424', 5461.8310, '2024-05-31 10:13:30.779123', true);
INSERT INTO public.certificateverificationattempt VALUES (48, 'cert-ca-1431', 591.8810, '2024-05-31 10:14:01.147593', true);
INSERT INTO public.certificateverificationattempt VALUES (49, 'cert-ca-1430', 186.2570, '2024-05-31 15:20:28.007686', true);
INSERT INTO public.certificateverificationattempt VALUES (50, 'cert-ca-1430', 186.2500, '2024-05-31 15:20:38.286918', false);
INSERT INTO public.certificateverificationattempt VALUES (51, 'cert-ca-1396', 167.0340, '2024-05-31 15:21:03.949536', false);
INSERT INTO public.certificateverificationattempt VALUES (52, 'cert-ca-1220', 177.8700, '2024-05-31 16:43:37.241532', true);
INSERT INTO public.certificateverificationattempt VALUES (53, 'cert-ca-1220', 177.8700, '2024-05-31 17:45:15.98782', true);
INSERT INTO public.certificateverificationattempt VALUES (54, 'cert-ca-1220', 177.8700, '2024-05-31 17:45:34.574058', true);
INSERT INTO public.certificateverificationattempt VALUES (55, 'cert-ca-1220', 177.8000, '2024-05-31 17:47:36.025374', false);
INSERT INTO public.certificateverificationattempt VALUES (56, 'cert-ca-1220', 177.8700, '2024-05-31 17:47:38.094368', true);
INSERT INTO public.certificateverificationattempt VALUES (57, 'cert-ca-1220', 177.8700, '2024-05-31 17:49:26.762115', true);
INSERT INTO public.certificateverificationattempt VALUES (58, 'cert-ca-1220', 77.8700, '2024-05-31 17:49:37.816876', false);
INSERT INTO public.certificateverificationattempt VALUES (59, 'cert-ca-1220', 177.8700, '2024-05-31 17:49:42.698887', true);
INSERT INTO public.certificateverificationattempt VALUES (60, 'cert-ca-1424', 186.2570, '2024-05-31 18:13:04.897765', false);
INSERT INTO public.certificateverificationattempt VALUES (61, 'cert-ca-1434', 29464.1680, '2024-05-31 18:13:41.734393', true);
INSERT INTO public.certificateverificationattempt VALUES (63, 'cert-ca-1434', 29464.1670, '2024-05-31 20:45:54.44296', false);
INSERT INTO public.certificateverificationattempt VALUES (64, 'cert-ca-1434', 29464.1670, '2024-05-31 20:45:58.405407', false);
INSERT INTO public.certificateverificationattempt VALUES (65, 'cert-ca-1434', 29464.1680, '2024-05-31 20:46:01.233357', true);
INSERT INTO public.certificateverificationattempt VALUES (66, 'cert-ca-1455', 2412.0890, '2024-06-05 21:04:38.139229', true);
INSERT INTO public.certificateverificationattempt VALUES (67, 'cert-ca-1455', 2412.0890, '2024-06-05 21:05:53.727372', true);
INSERT INTO public.certificateverificationattempt VALUES (68, 'cert-ca-1455', 2412.0880, '2024-06-05 21:05:58.625702', false);
INSERT INTO public.certificateverificationattempt VALUES (69, 'cert-ca-1455', 2412.0890, '2024-06-05 21:07:13.832001', true);
INSERT INTO public.certificateverificationattempt VALUES (70, 'cert-ca-1455', 2412.0880, '2024-06-05 21:07:17.093575', false);
INSERT INTO public.certificateverificationattempt VALUES (71, 'cert-ca-1455', 2412.0890, '2024-06-05 21:09:37.190387', true);
INSERT INTO public.certificateverificationattempt VALUES (72, 'cert-ca-1455', 2412.0880, '2024-06-05 21:09:40.600812', false);
INSERT INTO public.certificateverificationattempt VALUES (73, 'cert-ca-1455', 2412.0890, '2024-06-05 21:10:25.36466', true);
INSERT INTO public.certificateverificationattempt VALUES (74, 'cert-ca-1455', 2412.0880, '2024-06-05 21:10:29.464966', false);
INSERT INTO public.certificateverificationattempt VALUES (75, 'cert-ca-1455', 2412.0890, '2024-06-05 21:11:48.649746', true);
INSERT INTO public.certificateverificationattempt VALUES (76, 'cert-ca-1455', 2412.0880, '2024-06-05 21:11:52.91917', false);
INSERT INTO public.certificateverificationattempt VALUES (77, 'cert-ca-1455', 2412.0890, '2024-06-05 21:24:11.955027', true);
INSERT INTO public.certificateverificationattempt VALUES (78, 'cert-ca-1455', 2412.0880, '2024-06-05 21:24:16.505759', false);
INSERT INTO public.certificateverificationattempt VALUES (79, 'cert-ca-1455', 2412.0890, '2024-06-06 13:55:45.539159', true);
INSERT INTO public.certificateverificationattempt VALUES (80, 'cert-ca-1455', 2412.0880, '2024-06-06 13:55:49.565649', false);
INSERT INTO public.certificateverificationattempt VALUES (81, 'cert-ca-1455', 2412.0890, '2024-06-06 13:55:52.883295', true);
INSERT INTO public.certificateverificationattempt VALUES (82, 'cert-ca-1455', 2412.0890, '2024-06-06 19:46:57.816657', true);
INSERT INTO public.certificateverificationattempt VALUES (83, 'cert-ca-1455', 2412.0891, '2024-06-06 19:47:01.865032', false);
INSERT INTO public.certificateverificationattempt VALUES (84, 'cert-ca-1455', 2412.0890, '2024-06-06 20:05:03.367048', true);
INSERT INTO public.certificateverificationattempt VALUES (85, 'cert-ca-1455', 2412.0891, '2024-06-06 20:05:05.821371', false);
INSERT INTO public.certificateverificationattempt VALUES (86, 'cert-ca-1455', 2412.0890, '2024-06-07 16:16:20.506764', true);
INSERT INTO public.certificateverificationattempt VALUES (87, 'cert-ca-1455', 2412.0891, '2024-06-07 16:16:24.977051', false);
INSERT INTO public.certificateverificationattempt VALUES (88, 'cert-ca-1455', 2412.0890, '2024-06-07 18:27:49.226842', true);
INSERT INTO public.certificateverificationattempt VALUES (89, 'cert-ca-1455', 2412.0890, '2024-06-07 18:28:13.129775', true);
INSERT INTO public.certificateverificationattempt VALUES (90, 'cert-ca-1455', 2412.0891, '2024-06-07 18:28:15.708627', false);
INSERT INTO public.certificateverificationattempt VALUES (91, 'cert-ca-1455', 2412.0890, '2024-06-07 18:38:11.364986', true);
INSERT INTO public.certificateverificationattempt VALUES (92, 'cert-ca-1455', 2412.0891, '2024-06-07 18:38:13.948048', false);
INSERT INTO public.certificateverificationattempt VALUES (93, 'cert-ca-1455', 2412.0890, '2024-06-07 18:40:02.919869', true);
INSERT INTO public.certificateverificationattempt VALUES (94, 'cert-ca-1455', 2412.0891, '2024-06-07 18:40:05.820263', false);
INSERT INTO public.certificateverificationattempt VALUES (95, 'cert-ca-1455', 2412.0890, '2024-06-07 19:54:30.116751', true);
INSERT INTO public.certificateverificationattempt VALUES (96, 'cert-ca-1455', 2412.0891, '2024-06-07 19:54:32.431214', false);
INSERT INTO public.certificateverificationattempt VALUES (128, 'cert-ca-1455', 2412.0890, '2024-06-07 20:03:19.51471', true);
INSERT INTO public.certificateverificationattempt VALUES (129, 'cert-ca-1455', 2412.0890, '2024-06-07 20:08:34.8514', true);
INSERT INTO public.certificateverificationattempt VALUES (130, 'cert-ca-1455', 2412.0890, '2024-06-09 17:51:21.639046', true);
INSERT INTO public.certificateverificationattempt VALUES (131, 'cert-ca-1455', 2412.0890, '2024-06-09 18:09:19.670637', true);
INSERT INTO public.certificateverificationattempt VALUES (132, 'cert-ca-1455', 2412.0891, '2024-06-09 18:09:22.620086', false);
INSERT INTO public.certificateverificationattempt VALUES (133, 'cert-ca-1455', 2412.0890, '2024-06-09 18:09:25.469924', true);
INSERT INTO public.certificateverificationattempt VALUES (134, 'cert-ca-1455', 2412.0890, '2024-06-09 18:28:28.376745', true);
INSERT INTO public.certificateverificationattempt VALUES (135, 'cert-ca-1455', 2412.0891, '2024-06-09 18:28:39.410531', false);
INSERT INTO public.certificateverificationattempt VALUES (136, 'cert-ca-1455', 2412.0890, '2024-06-09 18:28:42.685566', true);
INSERT INTO public.certificateverificationattempt VALUES (137, 'cert-ca-1455', 2412.0890, '2024-06-09 18:37:19.443507', true);
INSERT INTO public.certificateverificationattempt VALUES (138, 'cert-ca-1455', 2412.0891, '2024-06-09 18:37:22.275864', false);
INSERT INTO public.certificateverificationattempt VALUES (139, 'cert-ca-1455', 2412.0890, '2024-06-10 14:00:31.698452', true);
INSERT INTO public.certificateverificationattempt VALUES (140, 'cert-ca-1455', 2412.0891, '2024-06-10 14:00:34.7471', false);
INSERT INTO public.certificateverificationattempt VALUES (141, 'cert-ca-1460', 162.4000, '2024-06-10 15:01:59.580016', true);
INSERT INTO public.certificateverificationattempt VALUES (142, 'cert-ca-1455', 2412.0890, '2024-06-11 17:28:40.317306', true);
INSERT INTO public.certificateverificationattempt VALUES (143, 'cert-ca-1502', 178.4170, '2024-06-12 16:13:55.273422', false);
INSERT INTO public.certificateverificationattempt VALUES (144, 'cert-ca-1503', 178.4170, '2024-06-12 16:14:00.359794', true);
INSERT INTO public.certificateverificationattempt VALUES (145, 'cert-ca-1504', 32195.2840, '2024-06-12 16:26:59.785765', true);
INSERT INTO public.certificateverificationattempt VALUES (146, 'cert-ca-1505', 557.9830, '2024-06-12 17:42:03.976642', true);


--
-- Name: certificate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.certificate_id_seq', 27, true);


--
-- Name: certificateverificationattempt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.certificateverificationattempt_id_seq', 146, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

