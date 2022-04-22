--
-- PostgreSQL database dump
--

-- Dumped from database version 10.20
-- Dumped by pg_dump version 10.20

-- Started on 2022-04-22 01:13:37

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 205 (class 1259 OID 16545)
-- Name: sm_app comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sm_app comments" (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public."sm_app comments" OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16543)
-- Name: sm_app comments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."sm_app comments" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."sm_app comments_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 203 (class 1259 OID 16528)
-- Name: sm_app likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sm_app likes" (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public."sm_app likes" OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16526)
-- Name: sm_app likes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."sm_app likes" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."sm_app likes_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 201 (class 1259 OID 16512)
-- Name: sm_app posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sm_app posts" (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    used_id integer NOT NULL
);


ALTER TABLE public."sm_app posts" OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16451)
-- Name: sm_app users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sm_app users" (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    nationality character varying NOT NULL
);


ALTER TABLE public."sm_app users" OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16449)
-- Name: sm_app user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."sm_app users" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."sm_app user_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 200 (class 1259 OID 16510)
-- Name: sm_app_post_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."sm_app posts" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.sm_app_post_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2834 (class 0 OID 16545)
-- Dependencies: 205
-- Data for Name: sm_app comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."sm_app comments" (id, text, user_id, post_id) FROM stdin;
1	One Life	2	3
2	Race	6	8
3	Wow	9	1
4	Like for Like	5	2
5	War Man	4	5
6	Would you like	8	4
7	My post	3	6
8	My favorite game	7	7
\.


--
-- TOC entry 2832 (class 0 OID 16528)
-- Dependencies: 203
-- Data for Name: sm_app likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."sm_app likes" (id, user_id, post_id) FROM stdin;
1	2	4
4	8	5
6	4	8
7	9	2
2	3	3
8	7	1
9	5	7
10	6	6
\.


--
-- TOC entry 2830 (class 0 OID 16512)
-- Dependencies: 201
-- Data for Name: sm_app posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."sm_app posts" (id, title, description, used_id) FROM stdin;
1	Grov	S23	3
2	Hi man	L321	4
3	Hello	S23	5
4	Dark	Z2233	6
5	Orks	9998DA	2
6	Party	99DA99	7
7	Salt	99RA9	9
8	Often	DS9223	8
\.


--
-- TOC entry 2828 (class 0 OID 16451)
-- Dependencies: 199
-- Data for Name: sm_app users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."sm_app users" (id, name, age, gender, nationality) FROM stdin;
2	Alex	25	M	BEL
3	Oleg	26	M	BEL
4	Olya	25	W	UKR
5	Alex	27	M	RUS
6	Alla	22	W	RUS
7	Nika	25	W	BEL
8	Ylya	24	W	KZ
9	Max	25	M	BEL
\.


--
-- TOC entry 2841 (class 0 OID 0)
-- Dependencies: 204
-- Name: sm_app comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sm_app comments_id_seq"', 8, true);


--
-- TOC entry 2842 (class 0 OID 0)
-- Dependencies: 202
-- Name: sm_app likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sm_app likes_id_seq"', 10, true);


--
-- TOC entry 2843 (class 0 OID 0)
-- Dependencies: 198
-- Name: sm_app user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sm_app user_id_seq"', 9, true);


--
-- TOC entry 2844 (class 0 OID 0)
-- Dependencies: 200
-- Name: sm_app_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sm_app_post_id_seq', 8, true);


--
-- TOC entry 2700 (class 2606 OID 16552)
-- Name: sm_app comments sm_app_comments_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app comments"
    ADD CONSTRAINT sm_app_comments_pk PRIMARY KEY (id);


--
-- TOC entry 2698 (class 2606 OID 16532)
-- Name: sm_app likes sm_app_likes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app likes"
    ADD CONSTRAINT sm_app_likes_pk PRIMARY KEY (id);


--
-- TOC entry 2696 (class 2606 OID 16519)
-- Name: sm_app posts sm_app_post_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app posts"
    ADD CONSTRAINT sm_app_post_pk PRIMARY KEY (id);


--
-- TOC entry 2694 (class 2606 OID 16458)
-- Name: sm_app users sm_app_users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app users"
    ADD CONSTRAINT sm_app_users_pk PRIMARY KEY (id);


--
-- TOC entry 2704 (class 2606 OID 16553)
-- Name: sm_app comments sm_app_comments_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app comments"
    ADD CONSTRAINT sm_app_comments_fk FOREIGN KEY (user_id) REFERENCES public."sm_app users"(id);


--
-- TOC entry 2705 (class 2606 OID 16558)
-- Name: sm_app comments sm_app_comments_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app comments"
    ADD CONSTRAINT sm_app_comments_fk_1 FOREIGN KEY (post_id) REFERENCES public."sm_app posts"(id);


--
-- TOC entry 2702 (class 2606 OID 16533)
-- Name: sm_app likes sm_app_likes_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app likes"
    ADD CONSTRAINT sm_app_likes_fk FOREIGN KEY (user_id) REFERENCES public."sm_app users"(id);


--
-- TOC entry 2703 (class 2606 OID 16538)
-- Name: sm_app likes sm_app_likes_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app likes"
    ADD CONSTRAINT sm_app_likes_fk_1 FOREIGN KEY (post_id) REFERENCES public."sm_app posts"(id);


--
-- TOC entry 2701 (class 2606 OID 16520)
-- Name: sm_app posts sm_app_post_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sm_app posts"
    ADD CONSTRAINT sm_app_post_fk FOREIGN KEY (used_id) REFERENCES public."sm_app users"(id);


-- Completed on 2022-04-22 01:13:37

--
-- PostgreSQL database dump complete
--

