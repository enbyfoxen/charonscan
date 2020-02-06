--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-1)

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
-- Name: dscan_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dscan_data (
    scan_id uuid NOT NULL,
    scan_data json NOT NULL,
    creation_time timestamp without time zone,
    typelist json,
    grouplist json,
    categorylist json,
    location text
);


ALTER TABLE public.dscan_data OWNER TO postgres;

--
-- Name: localscan_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.localscan_data (
    scan_id uuid NOT NULL,
    scan_data json NOT NULL,
    creation_time timestamp without time zone NOT NULL
);


ALTER TABLE public.localscan_data OWNER TO postgres;

--
-- Name: dscan_data dscan_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dscan_data
    ADD CONSTRAINT dscan_data_pkey PRIMARY KEY (scan_id);


--
-- Name: localscan_data localscan_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.localscan_data
    ADD CONSTRAINT localscan_data_pkey PRIMARY KEY (scan_id);


--
-- PostgreSQL database dump complete
--

