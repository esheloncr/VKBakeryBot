--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

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

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id integer NOT NULL,
    section character varying(255),
    title character varying(255) NOT NULL,
    description character varying,
    photo character varying
);


ALTER TABLE public.product OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- Name: section; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.section (
    id integer NOT NULL,
    title character varying(255)
);


ALTER TABLE public.section OWNER TO postgres;

--
-- Name: section_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.section_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.section_id_seq OWNER TO postgres;

--
-- Name: section_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.section_id_seq OWNED BY public.section.id;


--
-- Name: product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Name: section id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.section ALTER COLUMN id SET DEFAULT nextval('public.section_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
f2b2d8a0ad6e
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (id, section, title, description, photo) FROM stdin;
1	Выпечка	Круассан	Булочка в форме полумесяца (рогалика) из слоёного теста	https://www.povarenok.ru/data/cache/2019may/23/04/2543052_25331-710x550x.jpg
2	Выпечка	Хачапури по Аджарски	Блюдо грузинской кухни, пирожок с начинкой из сыра и яйца.	https://www.maggi.ru/data/images/recept/img640x500/recept_14545_el5k.jpg
3	Выпечка	Пончик	Круглое или кольцеобразное, жаренное во фритюре хлебобулочное изделие, с начинкой или без неё	https://images.unian.net/photos/2019_03/thumb_files/400_0_1553353520-4665.jpg?0.9301246680090183
4	Торты	Торт идеал мужской	Идеальный вариант к сердцу любого мужчины!	https://static.1000.menu/img/content-v2/cb/28/38768/tort-ideal-mujskoi_1568143869_11_max.jpg
5	Торты	Двухъярусный торт	Двухъярусный торт с одинаковыми начинками в ярусах	https://cdn.lmbd.ru/e93847d3-35b1-4dda-89ed-31946a721205/
6	Торты	Торт Kit Kat	Такой торт- мечта для сладкоежек. Бисквит и конфеты в одном десерте, что может быть лучше!	https://www.patee.ru/r/x6/01/00/b1/960m.jpg
7	Печенье	Серпантин	Печенье вкусное, рассыпчатое, нежное и очень нарядное.	https://img3.zakaz.ua/upload.version_1.0.384e38ad45a654fac8f7f108cd203f99.350x350.jpeg
8	Печенье	Ромашка	Красивое и очень аппетитное печенье к чаю	https://static.1000.menu/img/content/24809/pesochnoe-pechene-romashka_1515673948_2_max.jpg
9	Печенье	Брауни	Печенье на основе шоколада, насыщенный шоколадный аромат и вкус.	https://www.marybakery.ru/wp-content/uploads/2019/12/CE0B95F8-0884-4973-9135-FB36171FE0A1.jpeg
10	Хлеб	Белый хлеб	Пушистый, ароматный, нежный и необыкновенно вкусный хлеб	https://hozoboz.com/wp-content/webpc-passthru.php?src=https://hozoboz.com/wp-content/uploads/2014/02/Beliy-hleb-v-hlebopechke-360x270.jpg&nocache=1
11	Хлеб	Итальянский хлеб	Итальянский хлеб из дрожжевого теста	https://eda.ru/img/eda/c620x415i/s1.eda.ru/StaticContent/Photos/120214123706/120214123940/p_O.jpg
12	Хлеб	Быстрый	Вкусный белый дрожжевой хлеб из пшеничной муки.	https://img.iamcook.ru/old/upl/recipes/middle/u4142-10b7c9c0972f7a6486ec930a56c01777.jpg
13	Мучное	Тыквенные лепешки	Лепешки с сочной начинкой из тыквы	https://domreceptu.ru/wp-content/uploads/2018/11/drojjevue_tukvennue_lepeshki_1.jpg
14	Мучное	Пирог с капустой	Дрожжевой пирог с капустой	https://domreceptu.ru/wp-content/uploads/2018/10/drojovoe_pirog_s_kapustoy_1.jpg
15	Мучное	Беляши с мясом	Восточное блюдо, воздушное тесто, сочная начинка	https://domreceptu.ru/wp-content/uploads/2018/09/belyashu_s_myasom_1.jpg
\.


--
-- Data for Name: section; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.section (id, title) FROM stdin;
1	Выпечка
2	Торты
3	Печенье
4	Хлеб
5	Мучное
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 15, true);


--
-- Name: section_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.section_id_seq', 5, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: section section_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.section
    ADD CONSTRAINT section_pkey PRIMARY KEY (id);


--
-- Name: section section_title_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.section
    ADD CONSTRAINT section_title_key UNIQUE (title);


--
-- Name: product product_section_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_section_fkey FOREIGN KEY (section) REFERENCES public.section(title) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

