PGDMP  2    5                }            repositorio_ternurin    17.4    17.4 :    O           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            P           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            Q           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            R           1262    16388    repositorio_ternurin    DATABASE     z   CREATE DATABASE repositorio_ternurin WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-ES';
 $   DROP DATABASE repositorio_ternurin;
                     postgres    false            �            1259    16419 	   Contenido    TABLE     i  CREATE TABLE public."Contenido" (
    "ContenidoID" integer NOT NULL,
    "Titulo" character varying(100) NOT NULL,
    "Descripcion" text,
    "TipoContenido" character varying(50) NOT NULL,
    "Materia" text,
    "Vistas" integer DEFAULT 0,
    "Estado" character varying(20) NOT NULL,
    "Formato" character varying(50) NOT NULL,
    "FechaSubida" timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    "UsuarioID" integer NOT NULL,
    "Autor" text,
    CONSTRAINT "Contenido_Estado_check" CHECK ((("Estado")::text = ANY ((ARRAY['Publicado'::character varying, 'Borrador'::character varying])::text[])))
);
    DROP TABLE public."Contenido";
       public         heap r       postgres    false            �            1259    16418    Contenido_ContenidoID_seq    SEQUENCE     �   CREATE SEQUENCE public."Contenido_ContenidoID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."Contenido_ContenidoID_seq";
       public               postgres    false    222            S           0    0    Contenido_ContenidoID_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."Contenido_ContenidoID_seq" OWNED BY public."Contenido"."ContenidoID";
          public               postgres    false    221            �            1259    16491 
   Documentos    TABLE       CREATE TABLE public."Documentos" (
    "ContenidoID" integer NOT NULL,
    "Tamaño" integer NOT NULL,
    "Paginas" integer NOT NULL,
    CONSTRAINT "Documentos_Paginas_check" CHECK (("Paginas" > 0)),
    CONSTRAINT "Documentos_Tamaño_check" CHECK (("Tamaño" > 0))
);
     DROP TABLE public."Documentos";
       public         heap r       postgres    false            �            1259    16402    Estudiantes    TABLE     M  CREATE TABLE public."Estudiantes" (
    "EstudianteID" integer NOT NULL,
    "UsuarioID" integer NOT NULL,
    "Matricula" character varying(10) NOT NULL,
    "Semestre" integer NOT NULL,
    "Carrera" character varying(100) NOT NULL,
    CONSTRAINT "Estudiantes_Semestre_check" CHECK ((("Semestre" >= 1) AND ("Semestre" <= 12)))
);
 !   DROP TABLE public."Estudiantes";
       public         heap r       postgres    false            �            1259    16401    Estudiantes_EstudianteID_seq    SEQUENCE     �   CREATE SEQUENCE public."Estudiantes_EstudianteID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public."Estudiantes_EstudianteID_seq";
       public               postgres    false    220            T           0    0    Estudiantes_EstudianteID_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public."Estudiantes_EstudianteID_seq" OWNED BY public."Estudiantes"."EstudianteID";
          public               postgres    false    219            �            1259    16435    Libros    TABLE     �   CREATE TABLE public."Libros" (
    "ContenidoID" integer NOT NULL,
    isbn character varying(20) NOT NULL,
    "Editorial" character varying(100) NOT NULL,
    "AñoPublicacion" integer NOT NULL,
    "Edicion" integer NOT NULL
);
    DROP TABLE public."Libros";
       public         heap r       postgres    false            �            1259    16479    Podcasts    TABLE     n  CREATE TABLE public."Podcasts" (
    "ContenidoID" integer NOT NULL,
    "Duracion" integer NOT NULL,
    "Locutor" character varying(100) NOT NULL,
    "Tema" character varying(255) NOT NULL,
    "Episodios" integer NOT NULL,
    CONSTRAINT "Podcasts_Duracion_check" CHECK (("Duracion" > 0)),
    CONSTRAINT "Podcasts_Episodios_check" CHECK (("Episodios" >= 1))
);
    DROP TABLE public."Podcasts";
       public         heap r       postgres    false            �            1259    16447    Revistas    TABLE     �   CREATE TABLE public."Revistas" (
    "ContenidoID" integer NOT NULL,
    "Volumen" integer NOT NULL,
    "Numero" integer NOT NULL
);
    DROP TABLE public."Revistas";
       public         heap r       postgres    false            �            1259    16457    Tesis    TABLE     �   CREATE TABLE public."Tesis" (
    "ContenidoID" integer NOT NULL,
    "Asesor" character varying(100) NOT NULL,
    "AñoDefensa" integer NOT NULL
);
    DROP TABLE public."Tesis";
       public         heap r       postgres    false            �            1259    16390    Usuario    TABLE     �  CREATE TABLE public."Usuario" (
    "UsuarioID" integer NOT NULL,
    "Nombre" character varying(50) NOT NULL,
    "A_Paterno" character varying(50) NOT NULL,
    "A_Materno" character varying(50) NOT NULL,
    "Email" character varying(100) NOT NULL,
    "Contraseña" text NOT NULL,
    "Rol" character varying(18) NOT NULL,
    CONSTRAINT "Usuario_Rol_check" CHECK ((("Rol")::text = ANY ((ARRAY['admin'::character varying, 'usuario'::character varying])::text[])))
);
    DROP TABLE public."Usuario";
       public         heap r       postgres    false            �            1259    16389    Usuario_UsuarioID_seq    SEQUENCE     �   CREATE SEQUENCE public."Usuario_UsuarioID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public."Usuario_UsuarioID_seq";
       public               postgres    false    218            U           0    0    Usuario_UsuarioID_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public."Usuario_UsuarioID_seq" OWNED BY public."Usuario"."UsuarioID";
          public               postgres    false    217            �            1259    16467    Videos    TABLE     7  CREATE TABLE public."Videos" (
    "ContenidoID" integer NOT NULL,
    "Duracion" integer NOT NULL,
    "Tamaño" integer NOT NULL,
    "Resolucion" character varying(20) NOT NULL,
    CONSTRAINT "Videos_Duracion_check" CHECK (("Duracion" > 0)),
    CONSTRAINT "Videos_Tamaño_check" CHECK (("Tamaño" > 0))
);
    DROP TABLE public."Videos";
       public         heap r       postgres    false            �            1259    16506    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap r       postgres    false                       2604    16422    Contenido ContenidoID    DEFAULT     �   ALTER TABLE ONLY public."Contenido" ALTER COLUMN "ContenidoID" SET DEFAULT nextval('public."Contenido_ContenidoID_seq"'::regclass);
 H   ALTER TABLE public."Contenido" ALTER COLUMN "ContenidoID" DROP DEFAULT;
       public               postgres    false    222    221    222            ~           2604    16405    Estudiantes EstudianteID    DEFAULT     �   ALTER TABLE ONLY public."Estudiantes" ALTER COLUMN "EstudianteID" SET DEFAULT nextval('public."Estudiantes_EstudianteID_seq"'::regclass);
 K   ALTER TABLE public."Estudiantes" ALTER COLUMN "EstudianteID" DROP DEFAULT;
       public               postgres    false    220    219    220            }           2604    16393    Usuario UsuarioID    DEFAULT     |   ALTER TABLE ONLY public."Usuario" ALTER COLUMN "UsuarioID" SET DEFAULT nextval('public."Usuario_UsuarioID_seq"'::regclass);
 D   ALTER TABLE public."Usuario" ALTER COLUMN "UsuarioID" DROP DEFAULT;
       public               postgres    false    217    218    218            E          0    16419 	   Contenido 
   TABLE DATA           �   COPY public."Contenido" ("ContenidoID", "Titulo", "Descripcion", "TipoContenido", "Materia", "Vistas", "Estado", "Formato", "FechaSubida", "UsuarioID", "Autor") FROM stdin;
    public               postgres    false    222   jM       K          0    16491 
   Documentos 
   TABLE DATA           K   COPY public."Documentos" ("ContenidoID", "Tamaño", "Paginas") FROM stdin;
    public               postgres    false    228   �^       C          0    16402    Estudiantes 
   TABLE DATA           h   COPY public."Estudiantes" ("EstudianteID", "UsuarioID", "Matricula", "Semestre", "Carrera") FROM stdin;
    public               postgres    false    220   �^       F          0    16435    Libros 
   TABLE DATA           b   COPY public."Libros" ("ContenidoID", isbn, "Editorial", "AñoPublicacion", "Edicion") FROM stdin;
    public               postgres    false    223   m_       J          0    16479    Podcasts 
   TABLE DATA           _   COPY public."Podcasts" ("ContenidoID", "Duracion", "Locutor", "Tema", "Episodios") FROM stdin;
    public               postgres    false    227   P`       G          0    16447    Revistas 
   TABLE DATA           H   COPY public."Revistas" ("ContenidoID", "Volumen", "Numero") FROM stdin;
    public               postgres    false    224   `a       H          0    16457    Tesis 
   TABLE DATA           I   COPY public."Tesis" ("ContenidoID", "Asesor", "AñoDefensa") FROM stdin;
    public               postgres    false    225   �a       A          0    16390    Usuario 
   TABLE DATA           s   COPY public."Usuario" ("UsuarioID", "Nombre", "A_Paterno", "A_Materno", "Email", "Contraseña", "Rol") FROM stdin;
    public               postgres    false    218   �a       I          0    16467    Videos 
   TABLE DATA           V   COPY public."Videos" ("ContenidoID", "Duracion", "Tamaño", "Resolucion") FROM stdin;
    public               postgres    false    226   e       L          0    16506    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public               postgres    false    229   Se       V           0    0    Contenido_ContenidoID_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Contenido_ContenidoID_seq"', 30, true);
          public               postgres    false    221            W           0    0    Estudiantes_EstudianteID_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public."Estudiantes_EstudianteID_seq"', 6, true);
          public               postgres    false    219            X           0    0    Usuario_UsuarioID_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."Usuario_UsuarioID_seq"', 14, true);
          public               postgres    false    217            �           2606    16429    Contenido Contenido_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."Contenido"
    ADD CONSTRAINT "Contenido_pkey" PRIMARY KEY ("ContenidoID");
 F   ALTER TABLE ONLY public."Contenido" DROP CONSTRAINT "Contenido_pkey";
       public                 postgres    false    222            �           2606    16497    Documentos Documentos_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public."Documentos"
    ADD CONSTRAINT "Documentos_pkey" PRIMARY KEY ("ContenidoID");
 H   ALTER TABLE ONLY public."Documentos" DROP CONSTRAINT "Documentos_pkey";
       public                 postgres    false    228            �           2606    16412 %   Estudiantes Estudiantes_Matricula_key 
   CONSTRAINT     k   ALTER TABLE ONLY public."Estudiantes"
    ADD CONSTRAINT "Estudiantes_Matricula_key" UNIQUE ("Matricula");
 S   ALTER TABLE ONLY public."Estudiantes" DROP CONSTRAINT "Estudiantes_Matricula_key";
       public                 postgres    false    220            �           2606    16410 %   Estudiantes Estudiantes_UsuarioID_key 
   CONSTRAINT     k   ALTER TABLE ONLY public."Estudiantes"
    ADD CONSTRAINT "Estudiantes_UsuarioID_key" UNIQUE ("UsuarioID");
 S   ALTER TABLE ONLY public."Estudiantes" DROP CONSTRAINT "Estudiantes_UsuarioID_key";
       public                 postgres    false    220            �           2606    16408    Estudiantes Estudiantes_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."Estudiantes"
    ADD CONSTRAINT "Estudiantes_pkey" PRIMARY KEY ("EstudianteID");
 J   ALTER TABLE ONLY public."Estudiantes" DROP CONSTRAINT "Estudiantes_pkey";
       public                 postgres    false    220            �           2606    16441    Libros Libros_isbn_key 
   CONSTRAINT     U   ALTER TABLE ONLY public."Libros"
    ADD CONSTRAINT "Libros_isbn_key" UNIQUE (isbn);
 D   ALTER TABLE ONLY public."Libros" DROP CONSTRAINT "Libros_isbn_key";
       public                 postgres    false    223            �           2606    16439    Libros Libros_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."Libros"
    ADD CONSTRAINT "Libros_pkey" PRIMARY KEY ("ContenidoID");
 @   ALTER TABLE ONLY public."Libros" DROP CONSTRAINT "Libros_pkey";
       public                 postgres    false    223            �           2606    16485    Podcasts Podcasts_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public."Podcasts"
    ADD CONSTRAINT "Podcasts_pkey" PRIMARY KEY ("ContenidoID");
 D   ALTER TABLE ONLY public."Podcasts" DROP CONSTRAINT "Podcasts_pkey";
       public                 postgres    false    227            �           2606    16451    Revistas Revistas_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public."Revistas"
    ADD CONSTRAINT "Revistas_pkey" PRIMARY KEY ("ContenidoID");
 D   ALTER TABLE ONLY public."Revistas" DROP CONSTRAINT "Revistas_pkey";
       public                 postgres    false    224            �           2606    16461    Tesis Tesis_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Tesis"
    ADD CONSTRAINT "Tesis_pkey" PRIMARY KEY ("ContenidoID");
 >   ALTER TABLE ONLY public."Tesis" DROP CONSTRAINT "Tesis_pkey";
       public                 postgres    false    225            �           2606    16400    Usuario Usuario_Email_key 
   CONSTRAINT     [   ALTER TABLE ONLY public."Usuario"
    ADD CONSTRAINT "Usuario_Email_key" UNIQUE ("Email");
 G   ALTER TABLE ONLY public."Usuario" DROP CONSTRAINT "Usuario_Email_key";
       public                 postgres    false    218            �           2606    16398    Usuario Usuario_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."Usuario"
    ADD CONSTRAINT "Usuario_pkey" PRIMARY KEY ("UsuarioID");
 B   ALTER TABLE ONLY public."Usuario" DROP CONSTRAINT "Usuario_pkey";
       public                 postgres    false    218            �           2606    16473    Videos Videos_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."Videos"
    ADD CONSTRAINT "Videos_pkey" PRIMARY KEY ("ContenidoID");
 @   ALTER TABLE ONLY public."Videos" DROP CONSTRAINT "Videos_pkey";
       public                 postgres    false    226            �           2606    16510 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public                 postgres    false    229            �           2606    16430     Contenido fk_Contenido_UsuarioID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Contenido"
    ADD CONSTRAINT "fk_Contenido_UsuarioID" FOREIGN KEY ("UsuarioID") REFERENCES public."Usuario"("UsuarioID") ON DELETE SET NULL;
 N   ALTER TABLE ONLY public."Contenido" DROP CONSTRAINT "fk_Contenido_UsuarioID";
       public               postgres    false    4750    218    222            �           2606    16498 $   Documentos fk_Documentos_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Documentos"
    ADD CONSTRAINT "fk_Documentos_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 R   ALTER TABLE ONLY public."Documentos" DROP CONSTRAINT "fk_Documentos_ContenidoID";
       public               postgres    false    222    4758    228            �           2606    16413 $   Estudiantes fk_Estudiantes_UsuarioID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Estudiantes"
    ADD CONSTRAINT "fk_Estudiantes_UsuarioID" FOREIGN KEY ("UsuarioID") REFERENCES public."Usuario"("UsuarioID") ON DELETE CASCADE;
 R   ALTER TABLE ONLY public."Estudiantes" DROP CONSTRAINT "fk_Estudiantes_UsuarioID";
       public               postgres    false    220    4750    218            �           2606    16442    Libros fk_Libros_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Libros"
    ADD CONSTRAINT "fk_Libros_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Libros" DROP CONSTRAINT "fk_Libros_ContenidoID";
       public               postgres    false    4758    223    222            �           2606    16486     Podcasts fk_Podcasts_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Podcasts"
    ADD CONSTRAINT "fk_Podcasts_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 N   ALTER TABLE ONLY public."Podcasts" DROP CONSTRAINT "fk_Podcasts_ContenidoID";
       public               postgres    false    227    4758    222            �           2606    16452     Revistas fk_Revistas_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Revistas"
    ADD CONSTRAINT "fk_Revistas_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 N   ALTER TABLE ONLY public."Revistas" DROP CONSTRAINT "fk_Revistas_ContenidoID";
       public               postgres    false    4758    224    222            �           2606    16462    Tesis fk_Tesis_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Tesis"
    ADD CONSTRAINT "fk_Tesis_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 H   ALTER TABLE ONLY public."Tesis" DROP CONSTRAINT "fk_Tesis_ContenidoID";
       public               postgres    false    4758    225    222            �           2606    16474    Videos fk_Videos_ContenidoID    FK CONSTRAINT     �   ALTER TABLE ONLY public."Videos"
    ADD CONSTRAINT "fk_Videos_ContenidoID" FOREIGN KEY ("ContenidoID") REFERENCES public."Contenido"("ContenidoID") ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Videos" DROP CONSTRAINT "fk_Videos_ContenidoID";
       public               postgres    false    222    226    4758            E      x��Z�nǖ^�OQwg4/�$͟�0d���!)�%;w�M��D����TuӦV�o0��0�;Zf�E�]0@ �M�3�0�9UM6%9N8���:����)v�y�R=Wy��8�����)�r1ͯ����&Q67�)����デB9Q�"��҈��y������-���B�TϬ��fz�c�Wor�M�B&F���XiS#b��e�r)��\�y���l)7?mn����\!�>�J��t�i�c�z�c�L�t��"�xksS����T6V�Xo>�-a��e���i	��
'^˷
+e^R����m���@b�@&�Y�J� ƉD��q��+���������E��h!!5�4Ṇ7���Bm��BZmx?)���	��V���I,%~��k�u��T�d�h�M�7�r�ֆ	9)ݷ���'ʑX�J|V����9����k�G_{M�[+�L�XZ�6�`�T:�7��D�ͭLq|8Oڂ�JKDN�%�-���E	s���8!�ܗ���i<5��g�G�Q'<��u"э&���o������6ޜ5����O3C��Z,o>��zh2�H&���p0t&C,�y�B�P�Q�p���k��Pq�p��A�iqmq���˥d�#n��'`&��J�Eii�L�q�M�R[�2�c�!w�W�:�q����C���'�&S1R��~���@#�mH��A�r��k���A;D^aM�n�T+�8�-���3R-1���Ng=��:�h8���_s�o xhYR\Z�>M�J��Fd�K�9C�s&e�T/�t �-%�t�����DP�z�,͡���ع�>5�a]�y���27��!�`� P䛟@�[e'2� aH�%=&�Z�^���)���43�ִ��9�`S��&"e�s`�w��T?�-�����W(a �ci5�I���U_�i��mB�<�������9��67��Ċ/{w$��Io4����Q�?��݃<�꽸h�K�_>�e�Gr��-�S�����nԸ� ю9P�"X�A�lLw�67��[jA�'�b���Z	�.u*I!J<���"M	�� L����	y��rϑ*9�-A�(3a�3�!��J��sh�/f�R"�Bu¿f*	'"NM�7#�Z��<x��^!Qx3���@�h
!C重���s�pc���!��eN5�j3�7WnWU��Bl~NM�Rm��
Ѐ󏁀 �����UAq�����C�[�K��꡹S�ݺX�}"�J�K2�\v�����\��^7i�! s�j^�J���'2��bdGC�Ad�&�A{����['�v�YK�yI6mv{ 3D�8��sq.������5��q)�A1��,U׷���kQ,�)����f,Zɴ���xo���չ��Zx�̌y'��!�, �5�abT�e�������P�J(ڐP�щ�R�$�E�Mx��\�����@�s$6у+��H`�U�-  u\��:M�B�K�6%��;E?X���ݡ�U�*�P�E�IA�H��	¡߱��?z4�+:��{o컫�J�(�L� 5�� C9,vK�h���)��2�=�G��b��OZT;_w��;5CD�n>!��Ư�p��G����ᩎa�P��Iu����I5пb 2��J���ea�vss��2󌝀ŕB]��0A��P�-�'�K���G^Q-��y��*�;�\Y�^�2��r�~cW��t�sۤ�D}̀а��#W� ��c��EH��Ǹ$�ORl>��L}�e1-��s�pѕyd�5+z�-~ �5W<��a��K��g�ܔ�� 9�)��&�J� ٌ݈�B9��%�π�x�4��Q�K��q�@�D\@ �ѵ8-7?��Ӥ��=H�[$ �H�s*���)u�X-a<�)Q�t}�씄�jv��iNlB��l�:��3GR��z8�-�f��1b�U�HF��������"�qƞA�����G�;�ro�W9��*�.��4�JB4�|���s+�7[i~�Ῠ��i��A�}�����=�e*���J4�q���`f,.!fF-�N�8.��#��ڒ6��rg^@)�:}�b{��:��_�W:J�أ��m�{␄�I���q\zn��]��"5��t�$� �����z���Ỗ�Z�~�a4�=&��ɡ�b�iJ���R�o���~7�׋��v���a���K�����]�'8���y_�{tx�#{v���.�����k�'�$H/�H���I��H1�)?G�u5��\�ae�n>RφR��TιP��B��a&�m~LPރ�f2����ԷKԓ�*ܮ������M����v~>$��I�~<�s?��-N%�����3]��^��j����HJm�DY�m�a'NA���So�x�� k���S�J4���B�}qq����ZO���g!g��Dm��}�
�Z�z��a�#�Nt^~h�gh.�^� ��X|s!���}"U-	��]Ozu�.�s�vk��K'���d.]Is%'�j�|�p��"��Yr�mWՀ�yR�Q@� ���@ò�x��X< >.0q*^�@Lϯ��~��
$yXm�◄"�t2u�>o�9�l@�͹FIfw�[��8��(�!"�rf�$U}����A !d'Q��:�������7>��m��Q0�Q��������������@��<~v��N���U[��y������	}D�H2���ho���P��7��^HP#���4�M��\��4>=��2�Ǔ~o�A#�y��=B:���ͨӸ8����\�oΧ/.�_#�ICE#*�����=J�b��=�67�NS��C�O^�n� 0�RZ��]R!=��H�:�)�qpk'�qK�'��R/}�s��5g(�#8����rR���E�ܚ�k�v۴�IM:Q{4�������P�s�f�m�8j�P��*jq��3UP+����\)��n!�ϡ7�[�[��nF�|z{ݓ�t(t�ZH��u{�aj�=�xUe�f5��������MԳ��p߇�v���N�zGYt�ဒ�:����) ��eo��3�{B4��-�wh�Rdo�2�J�My��%�Vs�5�˘P�f�
���=җߕ�}�e���/D(+x6C�<Lb�:�����jOq��4����.1�ihd`�f�kl3`U�TC9�(��!��u�#���k�yLI9T|q�DH�/�*�%�A����	����Wt�u'Ѩ�w�1t�+�
7�~�r7$6+U���Z��M>��8�k*� ����Z�©�5�0��&B�tZ2�
�"G���m`����f�牵�X"�?���n$q�����v4F�w��2Q�&t��y�/���bG��e�N�l�R��+0Jhw@ff�m��yM|dS��n�]d\1�C�"��k��ϠO��XtO��N��/.�J��=n�������/8������(�c�Lm|�9(y��	��q��Chy�b;�(��`�iuK���s�p�|��܊�'5@�u��J+,�sh[�P��:�πqz���1�Eh��1��8�B�ߊ��@��g�3�(o���(��v&\�M�u����}��D����{�a��'&6U�є��a������?�.Vγ�[��
�!h��FJr��)������n�P��s��g���'o��uq[��c��=�Q5�~��w���˝�\��C�D�B��SI��9��>Q�Q>�rR� ��.��sr:�8���:nW��~�Ow��P��T��}���E=��A7�3����t����\@t�A��%5^i�&��m��0/��ؾ���:�-_�鼤1L��8��3"�m>�����"�`YyFc|O�ŧ��y*瞫X���w��;�N��v4�8|�!�N6{�]�nэ���� �y�=\W�a?� �����E:��RMY9�w�a��(I[T
�����{�����ѨKQ2E�����Ѱ5���d�O��=�Nk��K�Ua�:������v�Y���.x{������*��+*4,�C'��;�]A�����>�h��1�.@�ъҍ4"�m�'�����|��OTQ���4���   a_}�%'�Kv�-X̀~�"�W̆ma��Zm����U��`�ۿ��i���۪mӌt�ݻ��M��e�v��j�HU��?�]фˉ�5a��/��a�A���{�bM"�ݸ�w�XHql)�^���!8�5��D�P�R�x��%M�6����� >�@�C��>g(��x�Z/�CW6��r�1��� ?�kY��s ��MH��_:ȯ7?��������ۄ�8���g>��N<C��0��oK��u�X���J�4��X�s�|�n6����f      K      x������ � �      C   �   x���A� ������/PX��1qaR�sC�ېP0@c<���b6��ɼ�BwtpJ�@��q�?Ru��3�+��c�֬�;�!?��bzD����)���R��j�y��y~.�����T��ZY#�
lZV \��
�6C�@�ژ�?n;��Ϫo      F   �   x�M�AN�0E��S� L4�ǎ��D��Dt�ƴ�D9-K��z1l���
�ޣg�d��������4��x0�P!��� wQ^����v:}%�!/�J��/䦻�ByP��(�h4�W=zc(KNQ`��g�i�Q�?X�O!��}�W����z7ri[��La�;dk�6l_r<>���<�}�����\#���k��x��$�B�      J      x�U�=NAFk�)|D~��\��R��DC��8+����3J:��P ��c$$�O���-�n��n$s��t�pBǸ�=��� wchE��!)nBb/�!amI���Y5�,"����&��霤%h$&�)���FI^5��q'��"��l�wX��?�Jb������R
�\X��dH�2�*I;���A�F�S���ꖰ��F�8���=��M��Hf�}�G|�}��;�l���đC�q��S=����+f�����oy&sv      G      x�3�4�4����� �[      H   =   x�34��4202�241M�-8]��\�KR����3R��3K�@j�b���� v��      A   0  x�}T�vE]�����9]�.�0~���:���*�D҄��=�Xp<������>�vp���O�7o�.�~r?��8l���i��'��|�����͘6Btě����kr+zqgO�՚f������~�fْ{\=�³yE;�6�?�wc��aC-����B�����Ԗ*�o�^#�I��猪�{�T{T\�j�"-a�c$i%�|����H�U�J�C{�$q��{�Pl3�Z{��jn���aw�y5�dwo�ĝ����sڎ�vr��k��ݬ/77�kM��a�����_��C�"r�D�d�l�ra��= q��:�R��l��r"��s����b��q��z�� Ķ��D_%�[{w��yw~8�l��k��x������Y.bgl�bȽAP#(�H��f?R�ޛ�xΊ�#�(Q����|���Sh�2bc��C�-dL��<�\�$����ܣl;w;ʹ��;�f���=��4-��^p\�k~�!���^��Z�8���5!+�b�T)��+0ǖ��d�g!����ކ����ѧ 1�Se
y�A�5�^�CJ��J�d�EEȂ�ҹ஄�j9}���<�vN{M��������2�#Ne��r��Dm���Ԍ}� �YW|�JH&Ũ"Z�js=��}���uGe�.)�"��9���ԀL����K*Ü0$h�yf���Ewaw:&�D�Ϛ���&g}Xn�~����yٟ>�)�d]_}�� C{�V*Us�3c�J�2��t�Z��n.؇ԣ�!�v�@��U���QB��7��@��$U;d,{�'��ߜ��� ���      I   3   x�32�4�4�472(�22�44�s�9M�lNK8ے��66�4��c���� �]�      L      x�36L5I16�0�0K����� (��     