import os

# ── YOUR ANTHROPIC API KEY ─────────────────────────────────────────────────
# Go to console.anthropic.com → API Keys → Create Key
# Paste your key below replacing the text inside the quotes
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your_key_here")

# ── EDGAR IDENTITY ─────────────────────────────────────────────────────────
# SEC requires a contact email — use your university email
EDGAR_IDENTITY = "Research Project yourname@university.edu"

# ── RUN MODE ───────────────────────────────────────────────────────────────
# Set TEST_MODE = True to run only 5 companies first (takes ~2 mins)
# Set TEST_MODE = False to run all 74 companies (takes ~25 mins)
TEST_MODE = False

# ── TICKER LIST ────────────────────────────────────────────────────────────
TICKERS_FULL = [
    {"ticker": "SKYW",   "name": "SkyWest Inc",                "sector": "Aviation"},
    {"ticker": "MESA",   "name": "Mesa Air Group",              "sector": "Aviation"},
    {"ticker": "BLDE",   "name": "Blade Air Mobility",          "sector": "Aviation"},
    {"ticker": "ACHR",   "name": "Archer Aviation",             "sector": "Aviation - eVTOL"},
    {"ticker": "JOBY",   "name": "Joby Aviation",               "sector": "Aviation - eVTOL"},
    {"ticker": "LOVE",   "name": "The Lovesac Company",         "sector": "Retail - Furniture"},
    {"ticker": "PRPL",   "name": "Purple Innovation",           "sector": "Retail - Consumer"},
    {"ticker": "TLYS",   "name": "Tilly's Inc",                 "sector": "Retail - Apparel"},
    {"ticker": "CATO",   "name": "The Cato Corporation",        "sector": "Retail - Apparel"},
    {"ticker": "DXLG",   "name": "Destination XL Group",        "sector": "Retail - Apparel"},
    {"ticker": "JILL",   "name": "J.Jill Inc",                  "sector": "Retail - Apparel"},
    {"ticker": "IMKTA",  "name": "Ingles Markets",              "sector": "Retail - Grocery"},
    {"ticker": "BYON",   "name": "Beyond Inc",                  "sector": "Retail - E-commerce"},
    {"ticker": "LESL",   "name": "Leslie's Inc",                "sector": "Retail - Pool Supplies"},
    {"ticker": "GOED",   "name": "1847 Goedeker Inc",           "sector": "Retail - Appliances"},
    {"ticker": "SNFCA",  "name": "Security National Financial", "sector": "Insurance"},
    {"ticker": "NODK",   "name": "NI Holdings Inc",             "sector": "Insurance - P&C"},
    {"ticker": "FNHC",   "name": "Federated National Holding",  "sector": "Insurance - P&C"},
    {"ticker": "DGICA",  "name": "Donegal Group Inc",           "sector": "Insurance - P&C"},
    {"ticker": "HGBL",   "name": "Heritage Global Inc",         "sector": "Insurance / Financial"},
    {"ticker": "KMPR",   "name": "Kemper Corporation",          "sector": "Insurance"},
    {"ticker": "TELL",   "name": "Tellurian Inc",               "sector": "Energy - LNG"},
    {"ticker": "EGY", "name": "VAALCO Energy",               "sector": "Energy - Oil & Gas"},
    {"ticker": "AMPY",   "name": "Amplify Energy Corp",         "sector": "Energy - Oil & Gas"},
    {"ticker": "NINE",   "name": "Nine Energy Service",         "sector": "Energy - Oilfield Services"},
    {"ticker": "HTLD",   "name": "Heartland Express",           "sector": "Transportation - Trucking"},
    {"ticker": "MRTN",   "name": "Marten Transport",            "sector": "Transportation - Trucking"},
    {"ticker": "PTSI",   "name": "PAM Transport Services",      "sector": "Transportation - Trucking"},
    {"ticker": "RLGT",   "name": "Radiant Logistics",           "sector": "Transportation - 3PL"},
    {"ticker": "ECHO",   "name": "Echo Global Logistics",       "sector": "Transportation - 3PL"},
    {"ticker": "FWRD",   "name": "Forward Air Corp",            "sector": "Transportation - Air Freight"},
    {"ticker": "ARCB",   "name": "ArcBest Corporation",         "sector": "Transportation - Freight"},
    {"ticker": "ASTE",   "name": "Astec Industries",            "sector": "Industrials - Mfg"},
    {"ticker": "GNSS",   "name": "Genasys Inc",                 "sector": "Industrials - Defense Tech"},
    {"ticker": "PESI",   "name": "Perma-Pipe Industries",       "sector": "Industrials - Piping"},
    {"ticker": "LIQT",   "name": "LiqTech International",       "sector": "Industrials - Filtration"},
    {"ticker": "HLIO",   "name": "Helios Technologies",         "sector": "Industrials - Hydraulics"},
    {"ticker": "ZEUS",   "name": "Olympic Steel",               "sector": "Industrials - Metals"},
    {"ticker": "IIIN",   "name": "Insteel Industries",          "sector": "Industrials - Steel"},
    {"ticker": "CODA",   "name": "Coda Octopus Group",          "sector": "Industrials - Marine Tech"},
    {"ticker": "FTCI",   "name": "FTC Solar Inc",               "sector": "Industrials - Solar"},
    {"ticker": "HIHO",   "name": "Highway Holdings",            "sector": "Industrials - Mfg"},
    {"ticker": "NXRT",   "name": "NexPoint Residential Trust",  "sector": "Real Estate - Multifamily REIT"},
    {"ticker": "GOOD",   "name": "Gladstone Commercial Corp",   "sector": "Real Estate - Net Lease REIT"},
    {"ticker": "CLPR",   "name": "Clipper Realty",              "sector": "Real Estate - Residential"},
    {"ticker": "ELME",   "name": "Elme Communities",            "sector": "Real Estate - Multifamily REIT"},
    {"ticker": "HFFG",   "name": "HF Foods Group",              "sector": "Consumer - Food Distribution"},
    {"ticker": "MAMA",   "name": "Mama's Creations",            "sector": "Consumer - Food Mfg"},
    {"ticker": "COCO",   "name": "The Vita Coco Company",       "sector": "Consumer - Beverage"},
    {"ticker": "KRUS",   "name": "Kura Sushi USA",              "sector": "Restaurant / Consumer"},
    {"ticker": "WEYS",   "name": "Weyco Group",                 "sector": "Consumer - Footwear"},
    {"ticker": "SNBR",   "name": "Sleep Number Corp",           "sector": "Consumer - Mattresses"},
    {"ticker": "RMCF",   "name": "Rocky Mountain High Brands",  "sector": "Consumer - Beverage"},
    {"ticker": "GTN",    "name": "Gray Television",             "sector": "Media - Broadcasting"},
    {"ticker": "EMMS",   "name": "Emmis Communications",        "sector": "Media - Radio"},
    {"ticker": "SALM",   "name": "Salem Communications",        "sector": "Media - Radio/Publishing"},
    {"ticker": "CLFD",   "name": "Clearfield Inc",              "sector": "Technology - Fiber"},
    {"ticker": "SURG",   "name": "SurgePays Inc",               "sector": "Telecom / Industrials"},
    {"ticker": "MFAC",   "name": "Medallion Financial Corp",    "sector": "Financial Services"},
    {"ticker": "AMTB",   "name": "Amerant Bancorp",             "sector": "Banking"},
    {"ticker": "KCAP",   "name": "Portman Ridge Finance",       "sector": "Financial Services - BDC"},
    {"ticker": "TPVG",   "name": "TriplePoint Venture Growth",  "sector": "Financial - Venture Lending"},
    {"ticker": "AGYS",   "name": "Agilysys Inc",                "sector": "Technology / Hospitality"},
    {"ticker": "TASK",   "name": "TaskUs Inc",                  "sector": "Technology - BPO"},
    {"ticker": "MNDO",   "name": "MIND C.T.I Ltd",              "sector": "Technology - Telecom"},
    {"ticker": "PGNY",   "name": "Progyny Inc",                 "sector": "Healthcare Benefits"},
]

TICKERS_TEST = [
    {"ticker": "HTLD",   "name": "Heartland Express",    "sector": "Transportation - Trucking"},
    {"ticker": "CATO",   "name": "The Cato Corporation", "sector": "Retail - Apparel"},
    {"ticker": "NODK",   "name": "NI Holdings Inc",      "sector": "Insurance - P&C"},
    {"ticker": "EGY", "name": "VAALCO Energy",        "sector": "Energy - Oil & Gas"},
    {"ticker": "GNSS",   "name": "Genasys Inc",          "sector": "Industrials - Defense Tech"},
]

TICKERS = TICKERS_TEST if TEST_MODE else TICKERS_FULL