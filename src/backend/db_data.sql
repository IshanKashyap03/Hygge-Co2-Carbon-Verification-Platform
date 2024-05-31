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

INSERT INTO public.certificate VALUES (6, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1430', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 23:11:00', 186.257, '2024-05-28 17:41:58.300626', '2024-05-29 12:24:29.324815', '2024-05-29 14:37:58.735905', 'COMPLETED', '70aae0da6a867305aba1dd1c5b55ae3c5091bc3cf05ea2e827011f053ec53f16', NULL);
INSERT INTO public.certificate VALUES (3, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1425', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:21:00', 170.89, '2024-05-28 15:51:41.662067', '2024-05-29 12:24:29.132962', '2024-05-28 11:51:42.0946', 'COMPLETED', 'f7f36d5bf7834dc367e021951bfa913a9aee160de28e7da7789cad102958f785', NULL);
INSERT INTO public.certificate VALUES (7, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1424', 'Satyam Steel', '2024-05-01 00:00:00', '2024-05-28 21:17:00', 5461.831, '2024-05-28 15:47:06.87463', '2024-05-29 12:24:29.37467', '2024-05-28 11:47:24.7203', 'COMPLETED', 'a15a5ccba9f90ce59e26575944f8cee10344ddc567937c6b2991023e2951df6c', NULL);
INSERT INTO public.certificate VALUES (9, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1433', 'Satyam Steel', '2024-03-31 19:02:00', '2024-04-30 05:56:00', 5795.853, '2024-05-29 18:57:29.416193', '2024-05-29 14:57:29.500857', '2024-05-29 14:57:36.547399', 'COMPLETED', '9bc8f2a912754347691de7a79621744bd0d30dc3c274398f91940243552a9d1f', NULL);
INSERT INTO public.certificate VALUES (2, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1423', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:08:00', 167.699, '2024-05-28 15:38:41.441447', '2024-05-29 12:24:29.091538', '2024-05-28 11:38:48.8629', 'COMPLETED', 'bf8f94eaf512df7f8cc5295f60c1b840b1c95584a090c75c1128082c7a52d687', NULL);
INSERT INTO public.certificate VALUES (1, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1422', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:04:00', 167.699, '2024-05-28 15:34:50.56942', '2024-05-29 12:24:29.046454', '2024-05-28 11:35:00.6719', 'COMPLETED', '8cbfc67bc3acb402832c04c5c5e8d393d97670eb2f2182f6c3beab28fcb9e671', NULL);
INSERT INTO public.certificate VALUES (10, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1434', 'Satyam Steel', '2024-01-01 00:00:00', '2024-05-30 00:45:00', 29464.168, '2024-05-29 19:15:18.685267', '2024-05-29 15:15:18.743274', '2024-05-29 15:15:24.42103', 'COMPLETED', '56781969fb882323dbcd89776f3a0b263aa6b7a8f03803737a2bcc516e4f0f31', NULL);
INSERT INTO public.certificate VALUES (11, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1396', 'Satyam Steel', '2024-05-27 00:00:00', '2024-05-27 20:33:00', 167.034, '2024-05-28 17:46:56.437199', '2024-05-29 17:18:50.784972', NULL, 'FAILED', NULL, NULL);
INSERT INTO public.certificate VALUES (8, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1431', 'Satyam Steel', '2024-05-27 00:00:00', '2024-05-29 23:52:00', 591.881, '2024-05-29 18:22:28.642403', '2024-05-29 14:22:28.699788', '2024-05-29 14:22:36.7147', 'COMPLETED', '54c753bc7c119a034e99012f53dd7e3ae53cf8cac21f8a0d7eb1fed2ab7d0ef1', NULL);
INSERT INTO public.certificate VALUES (4, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1428', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 21:34:00', 173.137, '2024-05-28 16:04:25.375444', '2024-05-29 12:24:29.174255', '2024-05-28 16:04:36', 'COMPLETED', '6d013a2940eff42ef8a702293a1d08e56eedd72c2a82e22711f23cc3a58c09d2', NULL);
INSERT INTO public.certificate VALUES (12, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1440', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 02:16:00', 17.572, '2024-05-30 20:46:19.885728', '2024-05-30 16:46:20.018274', '2024-05-30 16:46:24.732094', 'COMPLETED', '5b726973032dae676c21156a72a962a3a806db6b8c9c2f4d65358aa606c590a1', NULL);
INSERT INTO public.certificate VALUES (13, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1441', 'Satyam Steel', '2024-05-01 00:00:00', '2024-05-31 02:31:00', 5901.154, '2024-05-30 21:01:18.362498', '2024-05-30 17:01:18.385774', '2024-05-30 17:01:24.605698', 'COMPLETED', '5f3dba534fd2c4c9ef6982143feb8818c9a1fe736913fbd93075ae41e9d9fc9d', NULL);
INSERT INTO public.certificate VALUES (14, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1218', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 19:06:00', 157.818, '2024-05-31 13:36:52.020067', '2024-05-31 09:36:52.401178', '2024-05-31 09:37:00.708803', 'COMPLETED', '5a9e8d08a5295f8e3d82fd15c3f996da609234cf559cf5c6063dae3cdfad7718', NULL);
INSERT INTO public.certificate VALUES (15, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1219', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 20:07:00', 167.039, '2024-05-31 14:37:33.676573', '2024-05-31 10:37:33.839608', '2024-05-31 10:38:02.367685', 'COMPLETED', 'd140d54ec946f28281902209aab8969b1915baa64a9cbc3ab6507932af78d48c', NULL);
INSERT INTO public.certificate VALUES (5, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1429', 'Satyam Steel', '2024-05-28 00:00:00', '2024-05-28 23:06:00', 186.257, '2024-05-28 17:36:27.281567', '2024-05-29 12:24:29.216408', '2024-05-28 13:36:35.9393', 'COMPLETED', 'ea21850796db7d108b3ad4fdc3b04ad24daf9fe7b076dadc14c17f955c758f83', NULL);
INSERT INTO public.certificate VALUES (16, '64522a0a-c8f1-40f8-a2e5-9aed2dc23764', 'cert-ca-1220', 'Satyam Steel', '2024-05-31 00:00:00', '2024-05-31 21:21:00', 177.87, '2024-05-31 15:51:56.184957', '2024-05-31 15:51:56.427455', '2024-05-31 15:52:00.594428', 'COMPLETED', '8af7266bd72baf6050c0167aaa044701fe5a774580b4784a6c2053a34404823b', NULL);


--
-- Data for Name: certificateverificationattempt; Type: TABLE DATA; Schema: public; Owner: yarik
--

INSERT INTO public.certificateverificationattempt VALUES (1, 'cert-ca-1429', 186.257, '2024-05-29 12:24:42.573817', true);
INSERT INTO public.certificateverificationattempt VALUES (2, 'cert-ca-1430', 186.257, '2024-05-29 12:25:18.145641', true);
INSERT INTO public.certificateverificationattempt VALUES (3, 'cert-ca-1429', 186.257, '2024-05-29 12:25:25.399221', true);
INSERT INTO public.certificateverificationattempt VALUES (4, 'cert-ca-1422', 167.699, '2024-05-29 12:25:44.130958', true);
INSERT INTO public.certificateverificationattempt VALUES (5, 'cert-ca-1424', 5461.831, '2024-05-29 12:26:03.026526', true);
INSERT INTO public.certificateverificationattempt VALUES (6, 'cert-ca-1425', 5461.831, '2024-05-29 12:26:21.93587', false);
INSERT INTO public.certificateverificationattempt VALUES (7, 'cert-ca-1429', 186.257, '2024-05-29 12:35:26.652598', true);
INSERT INTO public.certificateverificationattempt VALUES (8, 'cert-ca-1430', 186.257, '2024-05-29 13:24:22.82067', true);
INSERT INTO public.certificateverificationattempt VALUES (9, 'cert-ca-1429', 186.257, '2024-05-29 13:24:42.042112', true);
INSERT INTO public.certificateverificationattempt VALUES (10, 'cert-ca-1430', 186.257, '2024-05-29 13:31:06.554952', true);
INSERT INTO public.certificateverificationattempt VALUES (11, 'cert-ca-1429', 186.257, '2024-05-29 13:31:11.730244', true);
INSERT INTO public.certificateverificationattempt VALUES (12, 'cert-ca-1424', 5461.831, '2024-05-29 13:31:46.207775', true);
INSERT INTO public.certificateverificationattempt VALUES (13, 'cert-ca-1430', 186.257, '2024-05-29 13:33:18.876078', true);
INSERT INTO public.certificateverificationattempt VALUES (14, 'cert-ca-1429', 186.257, '2024-05-29 13:33:37.272857', true);
INSERT INTO public.certificateverificationattempt VALUES (15, 'cert-ca-1424', 5461.831, '2024-05-29 13:33:59.900319', true);
INSERT INTO public.certificateverificationattempt VALUES (16, 'cert-ca-1425', 5461.831, '2024-05-29 13:34:09.418701', false);
INSERT INTO public.certificateverificationattempt VALUES (17, 'cert-ca-1425', 170.89, '2024-05-29 13:34:32.910615', true);
INSERT INTO public.certificateverificationattempt VALUES (18, 'cert-ca-1430', 186.257, '2024-05-29 13:48:54.774543', true);
INSERT INTO public.certificateverificationattempt VALUES (19, 'cert-ca-1429', 186.257, '2024-05-29 13:49:21.696878', true);
INSERT INTO public.certificateverificationattempt VALUES (20, 'cert-ca-1424', 186.257, '2024-05-29 13:49:33.279483', false);
INSERT INTO public.certificateverificationattempt VALUES (21, 'cert-ca-1424', 5461.831, '2024-05-29 13:49:51.124185', true);
INSERT INTO public.certificateverificationattempt VALUES (22, 'cert-ca-1431', 591.881, '2024-05-29 14:27:09.277696', true);
INSERT INTO public.certificateverificationattempt VALUES (23, 'cert-ca-1433', 5795.853, '2024-05-29 15:00:48.557992', true);
INSERT INTO public.certificateverificationattempt VALUES (24, 'cert-ca-1434', 29464.168, '2024-05-29 15:16:33.774918', true);
INSERT INTO public.certificateverificationattempt VALUES (26, 'cert-ca-1433', 5795.853, '2024-05-29 15:22:14.794555', true);
INSERT INTO public.certificateverificationattempt VALUES (27, 'cert-ca-1434', 29464.168, '2024-05-29 15:34:42.142691', true);
INSERT INTO public.certificateverificationattempt VALUES (29, 'cert-ca-1434', 29464.16, '2024-05-29 15:35:20.569966', false);
INSERT INTO public.certificateverificationattempt VALUES (32, 'cert-ca-1434', 29464.168, '2024-05-29 15:36:17.00543', true);
INSERT INTO public.certificateverificationattempt VALUES (35, 'cert-ca-1396', 167.034, '2024-05-29 17:19:47.557668', false);
INSERT INTO public.certificateverificationattempt VALUES (36, 'cert-ca-1434', 29464.168, '2024-05-30 09:45:19.104788', true);
INSERT INTO public.certificateverificationattempt VALUES (37, 'cert-ca-1396', 167.034, '2024-05-30 09:45:32.845563', false);
INSERT INTO public.certificateverificationattempt VALUES (38, 'cert-ca-1440', 17.572, '2024-05-30 16:47:28.166767', true);
INSERT INTO public.certificateverificationattempt VALUES (39, 'cert-ca-1441', 5901.154, '2024-05-30 17:02:31.462899', true);
INSERT INTO public.certificateverificationattempt VALUES (40, 'cert-ca-1440', 5901.154, '2024-05-30 17:02:47.715891', false);
INSERT INTO public.certificateverificationattempt VALUES (41, 'cert-ca-1218', 157.818, '2024-05-31 09:38:17.403034', true);
INSERT INTO public.certificateverificationattempt VALUES (42, 'cert-ca-1422', 167.699, '2024-05-31 10:12:06.091243', true);
INSERT INTO public.certificateverificationattempt VALUES (43, 'cert-ca-1423', 167.699, '2024-05-31 10:12:50.772842', true);
INSERT INTO public.certificateverificationattempt VALUES (44, 'cert-ca-1425', 170.89, '2024-05-31 10:13:01.061113', true);
INSERT INTO public.certificateverificationattempt VALUES (45, 'cert-ca-1428', 173.137, '2024-05-31 10:13:11.676099', true);
INSERT INTO public.certificateverificationattempt VALUES (46, 'cert-ca-1429', 186.257, '2024-05-31 10:13:22.760056', true);
INSERT INTO public.certificateverificationattempt VALUES (47, 'cert-ca-1424', 5461.831, '2024-05-31 10:13:30.779123', true);
INSERT INTO public.certificateverificationattempt VALUES (48, 'cert-ca-1431', 591.881, '2024-05-31 10:14:01.147593', true);
INSERT INTO public.certificateverificationattempt VALUES (49, 'cert-ca-1430', 186.257, '2024-05-31 15:20:28.007686', true);
INSERT INTO public.certificateverificationattempt VALUES (50, 'cert-ca-1430', 186.25, '2024-05-31 15:20:38.286918', false);
INSERT INTO public.certificateverificationattempt VALUES (51, 'cert-ca-1396', 167.034, '2024-05-31 15:21:03.949536', false);
INSERT INTO public.certificateverificationattempt VALUES (52, 'cert-ca-1220', 177.87, '2024-05-31 16:43:37.241532', true);
INSERT INTO public.certificateverificationattempt VALUES (53, 'cert-ca-1220', 177.87, '2024-05-31 17:45:15.98782', true);
INSERT INTO public.certificateverificationattempt VALUES (54, 'cert-ca-1220', 177.87, '2024-05-31 17:45:34.574058', true);
INSERT INTO public.certificateverificationattempt VALUES (55, 'cert-ca-1220', 177.8, '2024-05-31 17:47:36.025374', false);
INSERT INTO public.certificateverificationattempt VALUES (56, 'cert-ca-1220', 177.87, '2024-05-31 17:47:38.094368', true);
INSERT INTO public.certificateverificationattempt VALUES (57, 'cert-ca-1220', 177.87, '2024-05-31 17:49:26.762115', true);
INSERT INTO public.certificateverificationattempt VALUES (58, 'cert-ca-1220', 77.87, '2024-05-31 17:49:37.816876', false);
INSERT INTO public.certificateverificationattempt VALUES (59, 'cert-ca-1220', 177.87, '2024-05-31 17:49:42.698887', true);
INSERT INTO public.certificateverificationattempt VALUES (60, 'cert-ca-1424', 186.257, '2024-05-31 18:13:04.897765', false);
INSERT INTO public.certificateverificationattempt VALUES (61, 'cert-ca-1434', 29464.168, '2024-05-31 18:13:41.734393', true);


--
-- Name: certificate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.certificate_id_seq', 16, true);


--
-- Name: certificateverificationattempt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.certificateverificationattempt_id_seq', 62, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yarik
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

