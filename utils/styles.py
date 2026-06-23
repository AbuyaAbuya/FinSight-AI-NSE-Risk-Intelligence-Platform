def load_css():

    return """
    <style>

    /* =====================================================
       SIDEBAR
    ===================================================== */
    /* Hide sidebar collapse arrow */
[data-testid="collapsedControl"]{
    display:none !important;
}

    section[data-testid="stSidebar"]{
        background:#0B132B;
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    [data-testid="stSidebarNav"]{
        padding-top:10px;
    }

    [data-testid="stSidebarNav"] a{
        background:#16213E;
        border:1px solid #243B55;
        border-radius:12px;
        padding:12px 15px;
        margin-bottom:8px;
        text-decoration:none;
        font-weight:600;
        transition:all .3s ease;
        display:block;
    }

    [data-testid="stSidebarNav"] a:hover{
        background:#1E3A5F;
        border-color:#3B82F6;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"]{
        background:linear-gradient(
            90deg,
            #2563EB,
            #3B82F6
        ) !important;

        color:white !important;
        border:none !important;
        font-weight:700 !important;

        box-shadow:
        0px 4px 12px rgba(
            59,
            130,
            246,
            0.4
        );
    }

    /* =====================================================
       MAIN PAGE LAYOUT
    ===================================================== */

    .main{
        background:#F8FAFC;
    }

    .main .block-container{
        max-width:95%;
        padding-top:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    /* =====================================================
       METRIC CARDS
    ===================================================== */

    div[data-testid="metric-container"]{
        background:white;
        border-radius:12px;
        border:1px solid #E5E7EB;
        padding:15px;

        box-shadow:
        0px 2px 8px rgba(
            0,
            0,
            0,
            0.05
        );
    }

    /* =====================================================
       HEADINGS
    ===================================================== */

    h1{
        color:#0F172A;
    }

    h2{
        color:#1E293B;
    }

    h3{
        color:#1E293B;
    }

    </style>
    """