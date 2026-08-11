import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ===========================
   GLOBAL
=========================== */

html,
body,
[data-testid="stAppViewContainer"]{

    background:#0f172a !important;
    color:white;

}

.stApp{

    background:transparent !important;

}


/* ===========================
   SIDEBAR
=========================== */

section[data-testid="stSidebar"]{

    background:#111827 !important;

    border-right:1px solid rgba(255,255,255,.08);

    box-shadow:8px 0px 18px rgba(0,0,0,.25);

}

section[data-testid="stSidebar"] *{

    color:white !important;

}


/* ===========================
   METRIC CARDS
=========================== */

div[data-testid="stMetric"]{

    background:#1e293b;

    border:1px solid rgba(255,255,255,.08);

    border-radius:18px;

    padding:18px;

    box-shadow:0px 8px 20px rgba(0,0,0,.20);

    transition:0.25s ease;

}

div[data-testid="stMetric"]:hover{

    transform:translateY(-3px);

    border:1px solid #3b82f6;

    box-shadow:0px 10px 25px rgba(59,130,246,.20);

}


/* ===========================
   BUTTONS
=========================== */

.stButton>button{

    background:#2563eb;

    color:white;

    border:none;

    border-radius:12px;

    padding:10px 22px;

    font-weight:600;

    transition:.25s;

}

.stButton>button:hover{

    background:#1d4ed8;

}


/* ===========================
   FILE UPLOADER
=========================== */

section[data-testid="stFileUploader"]{

    background:#1e293b;

    border:1px dashed #3b82f6;

    border-radius:16px;

    padding:15px;

}


/* ===========================
   DATAFRAME
=========================== */

div[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}


/* ===========================
   EXPANDERS
=========================== */

details{

    background:#1e293b;

    border-radius:12px;

    padding:8px;

}


/* ===========================
   TABS
=========================== */

button[data-baseweb="tab"]{

    background:#1e293b;

    color:white;

    border-radius:10px;

    margin-right:5px;

}

button[data-baseweb="tab"][aria-selected="true"]{

    background:#2563eb;

}


/* ===========================
   INPUTS
=========================== */

input,
textarea{

    border-radius:10px !important;

}


/* ===========================
   TITLES
=========================== */

h1{

    font-size:42px;

    font-weight:800;

}

h2{

    font-weight:700;

}

h3{

    font-weight:700;

}


/* ===========================
   HR
=========================== */

hr{

    border:1px solid rgba(255,255,255,.08);

}


/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#111827;

}

::-webkit-scrollbar-thumb{

    background:#374151;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#4b5563;

}

</style>
""",
        unsafe_allow_html=True,
    )